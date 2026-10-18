# Post Proxy
[English](README.md) <br>
CORS 정책을 우회하는 간단한 방법

## 사용법
### 일반 GET 요청
`https://post-proxy.vercel.app/?r=` [URL] <br>
[URL]로 GET 요청을 시도합니다. 이때 제공되는 기본 요청 헤더는 다음과 같습니다.

|키|값|
|:-:|:-:|
|User-Agent|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36|

### GET / POST 요청
`https://post-proxy.vercel.app/` 또는 `https://post-proxy.vercel.app/?r=` [URL] 으로 다음  body를 포함하는 POST 요청

|항목|키 이름|값 타입|설명|
|:-:|:-:|:-:|:-:|
|요청 헤더|headers|json|값이 없으면 기본 헤더로 설정|
|POST Body|data|json|값이 있으면 POST 요청, 없으면 GET 요청으로 판단|
|요청 타입|method|string|필수가 아니며 요청을 명시하기 위함("GET" 또는 "POST")|
|URL|url|string|필수가 아니며 url을 명시하기 위함 (r 파라미터를 쓰지 않을 경우 필요)|

POST 요청의 body에 따라 GET 또는 POST 요청을 수행합니다.
