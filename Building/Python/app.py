from flask import Flask, render_template, request, redirect, send_file
from PIL import Image
from rembg import remove
import time
from io import BytesIO
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handleRequest():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No se enviaron archivos', 400
        else:
            archivos = request.files.getlist('file')
            print("archivos enviados")
            for archivo in archivos:
                print(archivo)
                input = Image.open(archivo.stream)
                output = remove(input, post_process_mask=True)
                img_io = BytesIO()
                output.save(img_io, 'PNG')
                img_io.seek(0)
                return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='_' + time.strftime('%d') + '_' + time.strftime('%m') + '_' + time.strftime('%j') + "_" + time.strftime('%H') + '_' + time.strftime('%M') + '_' + time.strftime('%S') + '_nobackground.png')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
