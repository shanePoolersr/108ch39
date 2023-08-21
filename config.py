import pymongo
import certifi


me = { 
    "name": "Shane",
    "last_name":"Pooler",
    "age": 52,
    "hobbies": ["weight lifting"],
    "address": {
        "street": "marline",
        "city": "el cajon",
        "zip": 92021
    }
}
# database config
con_str ="mongodb+srv://shanep:XxLl2024@cluster0.oyytphk.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("server")
