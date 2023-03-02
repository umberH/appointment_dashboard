import pyodbc
import firebase_admin
from firebase_admin import credentials, db
#import * as firebase from 'firebase/app'
import json
import datetime
from google.protobuf import timestamp_pb2

# Set up Firebase credentials
cred = credentials.Certificate("C://Users//dumb_//Github//appointments//smartcookieappointments-firebase-adminsdk-ayamd-b9a8b27906.json")


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartcookieappointments-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Set up Access database connection
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C://Users//dumb_//Github//appointments//ContactsDat.mdb;'


)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

res = cursor.execute("SELECT * FROM tCustomer WHERE 1=0")
columnList = [tuple[0] for tuple in res.description]

print(columnList)
newColumnList = []
for column in columnList:
    
    column = column.title()
    column = column.replace(" ", "")
    column = column[0].lower()+column[1:]
    newColumnList.append(column)

print(newColumnList)

# Retrieve data from Access database
param1 = 'NSW'

query = "SELECT * FROM tCustomer WHERE state=?"
cursor.execute(query,param1)   # tCOntact, tCustomer
rows = cursor.fetchall()
print(len(rows))

#print(datetime.datetime(*rows[14][14][:6]))


# Map data to Firebase database structure
customers = {}
for row in rows:

    key = str(row[0])
  #  python_datetime = datetime.datetime(row[14])
    value = {
         newColumnList[1]: row[1],
         newColumnList[2]: row[2],
         newColumnList[3]: row[3],
         newColumnList[4]: row[4],
         newColumnList[5]: row[5],
         newColumnList[6]: row[6],
         newColumnList[7]: row[7],
         newColumnList[8]: row[8],
         newColumnList[9]: row[9],

         newColumnList[10]: row[10],
         newColumnList[11]: row[11],
         newColumnList[12]: row[12],
         newColumnList[13]: row[13],

        #  # Convert Python datetime object to JSON datetime string
        #  #columnList[14]: row[14],
        #  #columnList[14]: firebase.firestore.Timestamp.fromDate(row[14]),
         newColumnList[15]: row[15],
         newColumnList[16]: row[16],
         newColumnList[17]: row[17],
         newColumnList[18]: row[18],
        #  columnList[19]: row[19],
         newColumnList[20]: row[20],
         newColumnList[21]: row[21],
         newColumnList[22]: row[22],

        

     }
    customers[key] = value
# for keys,values in customers.items():
#     print(keys)
#     print(values)
    #ref.set(customers[keys])


# # # Import data into Firebase Realtime Database
ref = db.reference('tCustomer')
ref.set(customers)


res = cursor.execute("SELECT * FROM tContact WHERE 1=0")
columnList = [tuple[0] for tuple in res.description]

print(columnList)
newColumnList = []
for column in columnList:
    
    column = column.title()
    column = column.replace(" ", "")
    column = column[0].lower()+column[1:]
    newColumnList.append(column)

print(newColumnList)
# Retrieve data from Access database
param = '10000'

query = "SELECT * FROM tContact where 'Contact Id'>=?"
cursor.execute(query,param)   # tCOntact, tCustomer
rows = cursor.fetchall()
print(len(rows))

#print(datetime.datetime(*rows[14][14][:6]))


#customer_ref = db.collection('tCustomer').document('key')
# Map data to Firebase database structure
contacts = {}

for row in rows:
#dates = [datetime(*x[2]) for x in rows]
    key = (row[0])
    # print(row[6])
    # print(row[8])
    
    value = {

         columnList[1]: row[1],
         columnList[2]: json.dumps(datetime.datetime(1998, 10, 5, 18, 00) if row[2] is None else row[2].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),default=str),
         columnList[3]: row[3],
         columnList[4]: json.dumps(datetime.datetime(1998, 10, 5, 18, 00) if row[4] is None else row[4].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),default=str),
         columnList[5]: row[5],
         columnList[6]+"Time": json.dumps(datetime.datetime(1998, 10, 5, 18, 00) if row[6] is None or row[8] is None else datetime.datetime.combine(row[6].date(),row[8].time()).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),default=str),
         columnList[7]: row[7],
         #columnList[8]: row[8],
        
     }
     # Add the Timestamp to Firestore
#data = {'timestamp': timestamp}
    contacts[key] = value
print(contacts)
#print(dates)
# for keys,values in customers.items():
#     print(keys)
#     print(values)
    #ref.set(customers[keys])


# # # Import data into Firebase Realtime Database

ref = db.reference('tContact')
ref.set(contacts)

# Close Access database connection
cursor.close()
conn.close()
