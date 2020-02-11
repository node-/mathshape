from flask import Flask, send_from_directory
import pymesh

app = Flask(__name__,
            static_url_path='', 
            static_folder='build',
            template_folder='web/templates')


@app.route('/')
def index():
    return send_from_directory('build', 'index.html')

@app.route("/model")
def model():
    return pymesh.generate_regular_tetrahedron();

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

