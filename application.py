from flask import Flask

application = Flask(__name__)

@application.route('/')
def hellow_world():
    return 'hello, world, again!'