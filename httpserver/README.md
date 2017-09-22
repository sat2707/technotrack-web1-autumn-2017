## Что это такое

Это простейший `tcp`-сервер, писаный вкривь и вкось за пять минут.  
Запускается с помощью `python server/run.py`  
После этого вы можете зайти браузером на [localhost:8000](http://localhost:8000/) и увидеть, что ничего не работает  
Кроме того, вы можете присоединиться к серверу с помощью `telnet` и увидеть, что что-то таки работает:

```
msk-wire-i_stycenko-i:~ ilastycenko$ telnet localhost 8000
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
TEST
WRITE YOU RESPONSE HERE
Connection closed by foreign host.
msk-wire-i_stycenko-i:~ ilastycenko$
```
С помощью `telnet` удобно будет отлаживать программку

## Ваша задача

* Превратить его в простейший `http`-сервер
* Прописать в коде комментарии в тех строчках, которые заканчиваются на `#`

## Что эта штука должна уметь?

### Обработка пути `/`
Зайдя браузером на [http://localhost:8000/](http://localhost:8000/), вы должны увидеть простейшую текстовую страничку с содержимым:
```
Hello mister!
You are: (содержимое заголовка User-Agent)
```
 (код http-ответа - `200 OK`)

### Обработка пути `/media/`
Зайдя браузером на [http://localhost:8000/media/](http://localhost:8000/media/), вы должны увидеть список файлов в директории `files`  
(код http-ответа - `200 OK`)

### Обработка отдельного файла
Заходя браузером в [http://localhost:8000/media/test1.txt](http://localhost:8000/media/test1.txt), [http://localhost:8000/media/test2.txt](http://localhost:8000/media/test2.txt) или любые подобные ссылки, вы должны увидеть содержимое соответствующих файлов (код http-ответа - `200 OK`). Если такого файла нет - страничку "`File not found`"  
(код http-ответа - `404 Not found`)

### Обработка пути `/test/`
Заходя браузером в [http://localhost:8000/test/](http://localhost:8000/test/), вы должны просто увидеть весь `http`-запрос, который прислал браузер

### Все остальные `URL`
"`Page not found`"  
(код http-ответа - `404 Not found`)

## Как показать результат
Регистрируетесь на `github`, форкаете этот репозиторий, выкладываете код, создаете `pull-request` в `master` моего репозитория

## Что можно а что нельзя
Списывать нельзя. Спрашивать и советоваться в `telegram` - запросто
