Flask adalah salah satu framework di python selain juga django

## Instalasi flash di linux
Sebelum melakukan installasi, pengguna 
Flask sebaiknya menggunakan virtual 
environtment dalam proses pengembangan web. 
Virtual environtment adalah sebuah sistem 
untuk mengisolasi sebuah proyek Python agar 
tidak terjadi konflik dengan proyek Python 
lainnya.
ketikkan perintah berikut di terminal nntuk menginstall virtual enviroment

```
pip3 install virtualenv
```
selanjutnya membuat virtual enviroment dengan nama virenv sb
```
python3 -m venv virenv
```
untuk mengaktifkan virtual enviroment
```
source virenv/bin/activate
```
selanjutnya install Flask dengan mengetikkan perintah berikut di terminal
```
pip3 install Flask
```

## Membuat aplikasi sederhana dengan Flask

akan dibuat program "Hello World" di python sebagai berikut dengan nama __hellpo.py__
```
from flask import Flask

app = Flask(__name__)
@app.route("/")

def hello():
 return "Hello World!"
```
ketikkan di terminal untuk menjalankan program tsb
```
FLASK_APP=hello.py flask run
```
akan muncul sbb:
```
Running on http://localhost:5000/
```
buka __localhost__ dibrowser, muncul sbb

![img](https://github.com/speedey58/GAMBAR/blob/master/DeepinScreenshot_dde-desktop_20200323134225.png?raw=true)
