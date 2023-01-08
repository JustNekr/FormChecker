import re
from tinydb import Query


def type_validation(input_text):
    patterns_dict = {
        'date': [r'^\d\d\.\d\d\.\d{4}$', r'^\d{4}\.\d\d\.\d\d$'],
        'phone': [r'^7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}$'],
        'email': [r'^\S+@\w+.\w{2,4}$'],
    }
    for name, patterns in patterns_dict.items():
        for pattern in patterns:
            if re.fullmatch(pattern, input_text):
                return name
    return 'text'


def type_form(d):
    result = {}
    for k, v in d.items():
        result[k] = type_validation(v)
    return result


def match_dicts(db_dict, post_dict):
    for key in db_dict:
        if key == 'name':
            continue
        elif key in post_dict and db_dict[key] == post_dict[key]:
            continue
        else:
            return None
    return {"name": db_dict['name']}


def form_checker(my_db, post_dict):
    for k, v in post_dict.items():
        result = None
        db_item = my_db.search(Query().fragment({k: v}))
        for db_dict in db_item:
            result = match_dicts(db_dict, post_dict)
        if result:
            return result
        else:
            return None
