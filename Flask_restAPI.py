from flask import Flask
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

x = datetime.datetime.now()

cred = credentials.Certificate("/home/naira/Database/demo/demodb-4250a-firebase-adminsdk-fioqo-70e77e012f.json")

default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://demodb-4250a-default-rtdb.firebaseio.com/'

})

# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/Customer')
def get_customers():
    customer = db.reference("/Customer")
    data = customer.get()
    customer_data = []
    for key in data:
        customer_data.append(data[key])

    # Returning an api for showing in  reactjs
    return customer_data


@app.route('/Contact')
def get_contact():
    customer_id = 5
    contact = db.reference("/Contact")
    data = contact.order_by_child('Customer ID').equal_to(customer_id).get()
    contact_data = []
    for key in data:
        contact_data.append(data[key])

    return contact_data


# Running app
if __name__ == '__main__':
    app.run(debug=True)
