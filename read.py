import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

cond = input("請輸入您要查詢的課程關鍵字:")

collection_ref = db.collection("111")
docs = collection_ref.get()
for doc in docs:
    dict = doc.to_dict()
    if cond in dict["Course"]:
        print(dict["Leacture"]+"老師開的"+dict["Course"]+"課程，每周"+dict["Time"]+"於"+dict["Room"]+"上課")
        