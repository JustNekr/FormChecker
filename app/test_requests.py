import requests

tests = [{"data": {"field_name_1": "fgdgdg@gthy.ru",
                   "field_name_2": "75653596666",
                   "field_name_3": "2002.12.22"},
          "accepted_answer": {'field_name_1': 'email',
                              'field_name_2': 'phone',
                              'field_name_3': 'date'}
          },
         {"data": {"publication_date": "2002.12.22",
                   "disclaimer": 'some text'},
          "accepted_answer": {'name': 'Book form'}
          },
         {"data": {"order_date": "12.06.1987",
                   "client_email": "client@mail.com",
                   "order_text": 'some text',
                   "unavailable field": "23568"},
          "accepted_answer": {"name": "Order form"}
          },
         {"data": {"order_date": "12.06.1987",
                   "client_email": "client@mail.com",
                   "order_text": 'some text',
                   "publication_date": "2002.12.22"},
          "accepted_answer": {"name": "Order form"}
          },
         ]


def url_from_dict(input_dict, url='http://127.0.0.1:80/get_form'):
    str_from_dict = ''
    for key, value in input_dict.items():
        str_from_dict += f'{key}={value}&'
    return f'{url}?{str_from_dict}'[:-1]


def run_test():
    tests_result = []
    for test in tests:
        test_result = False
        response = requests.post(url_from_dict(test["data"]))
        if response.json() == test["accepted_answer"]:
            test_result = True
        answer = test
        answer.update({"result": test_result})
        tests_result.append(answer)
    return tests_result
