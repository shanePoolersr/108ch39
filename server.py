from flask import Flask, request, abort
from config import me, db
import json

app = Flask("server")

@app.get("/")
def home():
    return "Hello World"

@app.get("/test")
def test():
    return "This is a test page"

#get /about to show your name

@app.get("/about")
def about_me():
    return "Shane Pooler"




##############################################################
################### API - Products ###########################
#####################  JSON #################################
################################################################

@app.get("/api/about")
def about_data():
    return json.dumps(me)
#get /api/about/developer
# return full name

@app.get("/api/about/developer")
def developer_name():
    full_name = me["name"] + "" + me["last_name"]
    # python string formatting, f string
    return json.dumps(full_name)
    

@app.get("/api/categories")
def categories():
    all_cats = ["shoes", "pants","accessories"]
    return json.dumps(all_cats)

def fix_id(record):
    record["_id"] =str(record["_id"])
    return record

@app.get("/api/products")
def get_products():
    products = []
    
    return json.dumps(products)


@app.post("/api/products")
def save_product():
    product = request.get_json()
    
    db.products.insert_one(product)

    print(product)
    return json.dumps(fix_id(product))


#start the server
app.run(debug=True)



