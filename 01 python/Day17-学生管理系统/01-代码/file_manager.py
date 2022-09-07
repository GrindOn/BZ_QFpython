base_dir = './files/'


def read_file(file_name):
    try:
        with open(base_dir + file_name, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('文件未找到')


def write_json(file_name, data):
    with open(base_dir + file_name, 'w', encoding='utf8') as file:
        import json
        json.dump(data, file)


def read_json(file_name, default_data):
    try:
        with open(base_dir + file_name, 'r', encoding='utf8') as file:
            import json
            return json.load(file)
    except FileNotFoundError:
        # print('文件未找到')
        return default_data
