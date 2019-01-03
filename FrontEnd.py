from flask import Flask, jsonify, render_template
import getNewspaper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/my-link/')
def my_link():
    print ('I got clicked!')

    return getNewspaper.construction_nom_fichier('lyon')


@app.route('/api')
def my_microservice():
    return jsonify({'Hello': 'World!'})

if __name__ == '__main__':
    app.run(debug=True)
