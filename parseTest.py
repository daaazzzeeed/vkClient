import json

jsonText = '{"count": 283496, "items": [{"id": 507872, "date": 1513074594, "out": 0,"user_id": 143772776, "read_state": 1,"title": "", "body": "какой то текст"}]}'


def parse_some_json(json_string):
    parsed_string = json.loads(json_string)
    substring = str(parsed_string['items']).replace('[', '')
    substring = substring.replace(']', '')
    substring = substring.replace("'", '"')
    json_dict = json.loads(substring)
    print(json_dict['body'])





parse_some_json(jsonText)