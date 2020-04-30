from threading import Thread
from flask import Flask, request
from flask_restful import Api

from app.modules.tankzao.tankzao import tankzao

app = Flask(__name__)
api = Api(app)

api.add_resource(tankzao, '/naoh-etoh')


def create_app():
    global app
    threads_classses = [tankzao]
    
    threads = [Thread(target=thread().run) for thread in threads_classses]
    for thread in threads:
        thread.start()

    return app

def create_app_local():
    global app
    threads_classses = [tankzao]
    
    threads = [Thread(target=thread().run) for thread in threads_classses]
    for thread in threads:
        thread.start()
    
    app.run()
