from flask import Flask, render_template, request, send_file
from PIL import Image
from rembg import remove
import time
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handleRequest():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No se enviaron archivos', 400
        else:
            archivos = request.files.getlist('file')
            for archivo in archivos:
                input_img = Image.open(archivo.stream)
                output_img = remove(input_img, post_process_mask=True)
                
                # Guardar la imagen en un búfer de memoria
                img_io = io.BytesIO()
                output_img.save(img_io, format='PNG')
                img_io.seek(0)
    
                # Enviar el archivo al cliente
                return send_file(img_io, mimetype='image/png', as_attachment=True, 
                             download_name=f"_{time.strftime('%d')}_"
                                                f"{time.strftime('%m')}_"
                                                f"{time.strftime('%j')}_"
                                                f"{time.strftime('%H')}_"
                                                f"{time.strftime('%M')}_"
                                                f"{time.strftime('%S')}_nobackground.png"),200
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
