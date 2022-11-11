import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  
  "Code": "",
  "Course": "行動電子商務",
  "Leacture": "康贊清",
  "Time" : "三7、8、9",
  "Room": "主顧303"
}

collection_ref = db.collection("111")
collection_ref.add(doc)
