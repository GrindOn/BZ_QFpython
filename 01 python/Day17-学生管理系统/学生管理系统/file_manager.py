import json

base_dir = './files/'


def read_text(file_name):
    try:
        with open(base_dir + file_name, 'r', encoding='utf8') as file:
            msg = file.read()
            return msg
    except FileNotFoundError:
        print('读取文件失败，请检查路径')
        return ''


def read_json(json_name, non_data):
    try:
        with open(base_dir + json_name, 'r', encoding='utf8') as file:
            msg = file.read()
            return json.loads(msg)
    except FileNotFoundError:
        return non_data


def write_json(json_name, data):
    with open(base_dir + json_name, 'w', encoding='utf8') as file:
        json.dump(data, file)
