from tinydb import TinyDB

db = TinyDB('app/db.json')
db.truncate()
db.insert({"name": "User form",
           "user_email": "email",
           "user_phone": "phone",
           "user_birthdate": "date"})

db.insert({"name": "Order form",
           "order_date": "date",
           "client_email": "email",
           "order_text": 'text'})

db.insert({"name": "Book form",
           "publication_date": "date",
           "disclaimer": 'text'})





