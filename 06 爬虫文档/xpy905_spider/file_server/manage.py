#!/usr/bin/python3
# coding: utf-8
from __future__ import absolute_import

from flask import request, jsonify
from werkzeug.datastructures import FileStorage

from file_server import app


@app.route('/upload/', methods=['POST'])
def upload():
    file1: FileStorage = request.files.get('img')
    print(type(file1))
    print(file1.content_type, file1.filename)

    # 保存文件到static
    file1.save(f'static/{file1.filename}')
    return jsonify({'status': 'ok',
                    'path': f'/s/{file1.filename}'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)