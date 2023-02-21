import my_module
from flask import Flask
from flask_restful import Api, Resource
import configparser



app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        new = my_module.uid_generate()
        return new

def read_config():
    config = configparser.ConfigParser()
    config.read("Net_settings.ini")
    return config
config = read_config()
host = config["Net_settings"]["host"]
port = config["Net_settings"]["port"]
api.add_resource(Main, "/api/main")
api.init_app(app)

if __name__ == '__main__':
    print(f"Ссылка для проверки : {host}:{port}/api/main")
    app.run(debug=True, port=port, host=host)

