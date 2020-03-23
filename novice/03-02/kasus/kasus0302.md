## Membuat Aplikasi untuk mengupload File dengan Flask

membuat file html sbb

```
<!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Upload>
</form>
```
jalankan file, muncul di localhost seperti gambar

![img](https://github.com/speedey58/GAMBAR/blob/master/DeepinScreenshot_dde-desktop_20200323220319.png)

membuat direktori penyimpanan file uploads

![img](https://github.com/speedey58/GAMBAR/blob/master/DeepinScreenshot_select-area_20200323223218.png)

menentukan directory penyimpanan file yang akan di upload, serta ekstensi apa aja yang acceptable untuk diupload.
```
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
```
file python menjalankan upload file di flask
```
import os
from flask import Flask, request, redirect, url_for,send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
    app.run(debug=True)
```
