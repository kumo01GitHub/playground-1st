from flask import Flask
from flask_cors import CORS

from hoge import controllers as hoge
from stores import controllers as stores


app = Flask(__name__)
CORS(app)

app.register_blueprint(hoge.app)
app.register_blueprint(stores.app)

app.run(port=5000)
