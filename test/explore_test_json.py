import json


def check_json_file(json_file):
    with open(json_file) as data_file:
        data_string = data_file.read()
        try:
            data = json.loads(data_string)
            print('Success!')
        except ValueError:
            print('Failed:')
            print(repr(data_string))


json_file = 'yummly_sample.json'

check_json_file(json_file)
