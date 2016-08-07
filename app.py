import bottle
import pymongo
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
from bottle import request, response

url = "mongodb://Localhost:27017"
connection = pymongo.MongoClient(url)
db = connection.winedb
wines = db.wines

@bottle.get('/wines')
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
            

bottle.debug(True)
bottle.run(host = 'localhost', port = 8080, reloader = True)