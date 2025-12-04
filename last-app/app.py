from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body>
            <h1>Hello, DevOps!</h1>
            <p>Ласкаво просимо до веб-застосунку</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)