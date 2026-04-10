from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video')
def video():
  return render_template('webframe.html')

@app.route('/video1')
def video1():
  return render_template('webframe1.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return 'Click.'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
