# Post Proxy
[한국어](README-ko.md) <br>
A simple way to bypass the browser's CORS policy

## Usage
### Common GET Request
`https://post-proxy.vercel.app/?r=` [URL] <br>
Sends a GET request to [URL] with the following default request headers.

|    Key     |                                                     Value                                                      |
|:----------:|:--------------------------------------------------------------------------------------------------------------:|
| User-Agent |Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 |

### GET / POST Request
`https://post-proxy.vercel.app/` or `https://post-proxy.vercel.app/?r=` [URL] <br>
Send a POST request to either URL above with the following body.

|      item       | key name | type of value |                                   description                                    |
|:---------------:|:--------:|:-------------:|:--------------------------------------------------------------------------------:|
| Request Headers | headers  |     json      |                       Uses the default headers if omitted                        |
|    POST Body    |   data   |     json      |       If provided, a POST request is made; if empty, a GET request is made       |
| Type of request |  method  |    string     |        Optional. Explicitly specifies the request type ("GET" or "POST")         |
|       URL       |   url    |    string     | Optional. Explicitly specifies the URL (required if the r parameter is not used) |

Performs a GET or POST request depending on the POST body.
