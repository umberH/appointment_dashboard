import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# import firestore
import pandas_access as mdb
import json

# reading from microsoft access
# db_filename = '/home/naira/Database/demo/ContactsDat .mdb'
# df2 = mdb.read_table(db_filename, "tContact")
# df2.fillna('', inplace=True)
# # print(df2.iloc[4])
# d = df2.set_index('Contact ID').T.to_dict('list')


cred = credentials.Certificate("/home/naira/Database/demo/demodb-4250a-firebase-adminsdk-fioqo-70e77e012f.json")

default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://demodb-4250a-default-rtdb.firebaseio.com/'

})
#this is for creating ref to customer object in firebase real time data base
# ref = db.reference('/Customer')

#this is for creating ref to contact object in firebase real time data base
ref = db.reference("/Contact")

#sample has contact data
#sampleCustomer has customer data
#change the json file name on basis of data you want to upload
with open("sample.json", "r") as f:
    file_contents = json.load(f)

for value in file_contents:
    ref.push().set(value)
