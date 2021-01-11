from flask import Blueprint, jsonify
from hoge import dtos, daos

app = Blueprint('hoge', __name__)

# GET /hoge
@app.route('/hoge')
def get_hoge():
    hoge0 = dtos.HogeDTO(0, "trump")
    hoges = daos.HogeDAO.get_all()
    hoge1 = dtos.HogeDTO(hoges[0].get_id(), hoges[0].get_value())
    return jsonify(
        {
            'value': hoge1.get_value()
        })
