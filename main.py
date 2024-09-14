from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return {"message": sum([1, 2])}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
