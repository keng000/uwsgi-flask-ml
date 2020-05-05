
# uWSGI Preforking mode woun't response

## To Reproduce

```
$ docker build -t myapp .
$ docker run -itd --rm -p8000:8000 myapp
$ curl localhost:8000/estimate # -> this would be end with a connection timeout
```

## Solution

You should run uWSGI+Flask with lazy-apps Mode.

```
$ docker run -itd --rm -p8000:8000 myapp --lazy-apps
$ curl localhost:8000/estimate # -> OK
```
