from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)
#print(app)

@app.route('/')
def index():    
    return '<h1>Hello World!</h1>\n'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/ua')
def ua():    
    user_agent = request.headers.get('User-Agent')    
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/rd')
def rd():
    return redirect('http://www.google.com')

@app.route('/hc')
def hc():
    return 'OKOKOK'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
