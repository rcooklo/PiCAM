from flask import Flask, render_template, redirect, request
import os
process1 = ''
app = Flask(__name__)

@app.route('/startvideo/')
def startvideo():
  import os, time

  cmd1 = "/home/pi/python/mjpeg_server.py &"
  os.system(cmd1)
  time.sleep(5)
  return redirect("/index/")

@app.route('/stopvideo/')
def stopvideo():
  import os

  os.system('sudo killall -9 mjpeg_server.py') 
  return redirect("/index/")

@app.route('/')
def start():
  import socket

  startvideo()
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  #print(s.getsockname()[0])
  hostIP = (s.getsockname()[0])
  #print(hostIP)
  s.close()
  return render_template('index.html', hostIP=hostIP, hostName=os.uname()[1])

@app.route('/index/')
def index():
  import socket
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  #print(s.getsockname()[0])
  hostIP = (s.getsockname()[0])
  #print(hostIP)
  s.close()
  return render_template('index.html', hostIP=hostIP, hostName=os.uname()[1])

@app.route('/timelapse/', methods =["GET", "POST"])
def timelapse():
  import os
  if request.method == "POST":
    # getting input with name = minutes in HTML form
    theminutes = request.form.get("minutes")
    # getting input with name = interval in HTML form
    theinterval = request.form.get("interval")
    #return "Your data is "+theminutes + theinterval
    cmd1 = "python3 /home/pi/timelapse/timelapse3.py " + theminutes + " " + theinterval
    print(cmd1)
    os.system(cmd1)
    return redirect("/index/")
  return render_template('timelapse.html')

@app.route('/video1')
def video1():
  return render_template('webframe1.html')

@app.route('/left/')
def left():
  os.system("/home/pi/python/flask/left.sh")
  #print("Do Left")
  return redirect("/index/")

@app.route('/right/')
def right():
  os.system("/home/pi/python/flask/right.sh")
  return redirect("/index/")

@app.route('/shutdownquestion/')
def shutdownquestion():
  return render_template('shutdownquestion.html')

@app.route('/shutdownno/')
def shutdownno():
  return redirect("/index/")

@app.route('/shutdown/')
def shutdown():
  os.system("/usr/bin/sdc &")
  os.system("sudo cp /usr/bin/sd /usr/bin/sdc")
  return redirect("/index/")

@app.route('/reboot/')
def reboot():
  os.system("/usr/bin/sdc -r &")
  os.system("sudo cp /usr/bin/sd /usr/bin/sdc")
  return redirect("/index/")

@app.route('/up/')
def up():
  os.system("/home/pi/python/flask/up.sh")
  return redirect("/index/")

@app.route('/down/')
def down():
  os.system("/home/pi/python/flask/down.sh")
  return redirect("/index/")

@app.route('/neutral/')
def neutral():
  os.system("/home/pi/python/flask/neutral.sh")
  return redirect("/index/")

if __name__ == '__main__':
  from waitress import serve
  serve(app, host='0.0.0.0', port=5000)
#if __name__ == '__main__':
#  app.run(host='0.0.0.0', port=5000)

