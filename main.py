from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

client = httpx.AsyncClient(timeout=15)
pHeaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36'}

@app.api_route("/", methods=["GET", "POST"])
async def post_proxy(request: Request):
  r = request.query_params.get('r')
  url = ''.join(str(request.url).split('?r=')[1:]) if r else ''
  res = None

  try:
    if request.method == "GET":
      if url: res = await client.get(url, headers=pHeaders) # GET request
      else: return 'Hello : <Post Proxy 1.0>' # home page

    if request.method == "POST":
      item = None
      try: item = await request.json()
      except: return Response('Error 01 Invalid JSON body (post)', status_code=400, media_type='text/plain')

      headers = item.get('headers', pHeaders)
      data = item.get('data', None)
      method = item.get('method', None)
      url = item.get('url', url)

      if data or method == 'POST':
        if type(data).__name__ == 'dict': # POST request
          res = await client.post(url, headers=headers, data=data)
        else:
          res = await client.post(url, headers=headers, content=data)
      else: res = await client.get(url, headers=headers) # GET request

  except httpx.TimeoutException: return Response('Error 03 Upstream timeout', status_code=504, media_type='text/plain')
  except (httpx.UnsupportedProtocol, httpx.InvalidURL): return Response('Error 04 Invalid URL', status_code=400, media_type='text/plain')
  except httpx.RequestError: return Response('Error 05 Upstream request failed', status_code=502, media_type='text/plain')

  if res and res.is_success:
    try: return res.json()
    except:
      ctype = res.headers.get('Content-Type', '')
      if 'text/html' in ctype or 'text/plain' in ctype: return Response(res.text, media_type=ctype)
      else: return Response(res.content, media_type=ctype or 'application/octet-stream')
  else: return Response(f'Error 02 / code {res.status_code}', status_code=res.status_code, media_type='text/plain')