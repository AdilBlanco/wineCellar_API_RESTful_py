import bottle
import pymongo
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
from bottle import request, response, route

url = "mongodb://Localhost:27017"
connection = pymongo.MongoClient(url)
db = connection.winedb
wines = db.wines



# GET wines list
@route('/wines', method='GET')
def findAll():
    items = wines.find()
    result = []
    
    for item in items:
        result.append({
            '_id' : str( item['_id']), 
            'name': item['name'], 
            'year': item['year'],
            'grapes' : item['grapes'],
            'country': item['country'],
            'region' : item['region'],
            'description': item['description'],
            'picture': item['picture']
            })
    return dumps(result)

# GET wine by id    
@route('/wines/:id', method='GET')
def findById(id):
    item = wines.find_one({'_id': ObjectId(id)})
    return dumps(item)
    
# POST a wine at the list
@route('/wines', method='POST')
def addOneToList():
    data = request.body.read()
    item = json.loads(data)
    print item
    wines.insert_one(item)       
    
# DELETE wine from the list
@route('/wines/:id', method='DELETE')
def removeById(id):
    wines.remove({'_id': ObjectId(id)})
    return "item deleted"
    


bottle.debug(True)
bottle.run(host = 'localhost', port = 8080, reloader = True)