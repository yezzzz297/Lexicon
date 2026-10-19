from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

from pymongo.errors import OperationFailure

validator = {"$jsonSchema": {
    "bsonType": "object",
    "required": ["email"],
    "properties": {
        "email": {"bsonType": "string"},
        "source": {"enum": ["web", "store"]}
    }
}}

if "newsletter_signups" in db.list_collection_names():
    db.command("collMod", "newsletter_signups", validator=validator)
else:
    db.create_collection("newsletter_signups", validator=validator)

db.newsletter_signups.insert_one({"email": "student@example.com", "source": "web"})
print("Valid signup saved.")

try:
    db.newsletter_signups.insert_one({"email": "student@example.com", "source": "phone"})
except OperationFailure as error:
    if error.code == 121:
        print("Invalid signup rejected by validation.")
    else:
        raise

client.close()
