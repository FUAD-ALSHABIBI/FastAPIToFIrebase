import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("path of Certificate from FastAPI")
firebase_admin.initialize_app(cred)
db = firestore.client()


def setData(data):
    doc_ref = db.collection('fuad').document()
    doc_ref.set(data)

def getAll():
    collections = db.collection('fuad').stream()
    for doc in collections:
        print(f"{doc.id} => {doc.to_dict()}")
         # MHVEWnqdyBXnCy16tfDd => {'fruit': 'banana'} \s eXLMzZjggpQlYfpy7AF6 => {'fruit': 'apple'}
         

def getData(id):
    doc_ref = db.collection("fuad").document(id)
    doc = doc_ref.get()
    print(doc.to_dict()) 
    # {'fruit': 'banana'}

def delete(id):
    doc_ref = db.collection("fuad").document(id)
    doc_ref.delete()


# delete('MHVEWnqdyBXnCy16tfDd')
# data = {
#     'id' : "1234",
#     'fruit' : 'apple'
# }







