from flask import abort, current_app, Response
from models.model_base import BaseModel
import json


def make_success(code=1, msg='ok', data=None):
    return make_response(code, msg, data)


def make_faild(code=0, msg='操作失败', data=None):
    return make_response(code, msg, data)


def make_error(code=-1, msg='异常错误', data=None):
    return make_response(code, msg, data)


def make_response(code, msg, data):
    if data is None:
        data = {}
    if isinstance(data, BaseModel):
        data = data.dict()
    if isinstance(code, int) is False or isinstance(msg, str) is False or isinstance(data, (dict, list)) is False:
        current_app.logger.error('响应格式错误')
        abort(500)

    result = {
        'code': code,
        'msg': msg,
        'data': data,
    }
    # return jsonify()
    return Response(json.dumps(result), mimetype='application/json')
