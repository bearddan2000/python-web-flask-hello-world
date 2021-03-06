from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    txt = "Hello world from {me:s} app"
    return txt.format(me = 'hello_world')

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
