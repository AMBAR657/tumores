from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Lista de nombres de imágenes en la carpeta 'static/img'
    image_names = ["", "", "imagen_3.png", "imagen_4.png", "imagen_5.png"]

    # Ruta a la carpeta de imágenes (static/img)
    image_folder = 'static/img'

    # Renderizar la plantilla HTML con los datos
    return render_template('index.html', title="API de Tumores", image_names=image_names, image_folder=image_folder)

if __name__ == '__main__':
    app.run(debug=True)
