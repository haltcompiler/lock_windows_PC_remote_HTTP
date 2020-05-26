from flask import Flask
import ctypes
app = Flask(__name__)

@app.route('/')
def hello_world():
	ctypes.windll.user32.LockWorkStation()
	return '<h1>Locked!</h1>'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)
