from flask import Flask, jsonify, request
from flask_restful import Api, Resource 

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if functionName == "add" or functionName == "subtract" or functionName == "multiply":
        if "x" not in postedData or "y" not in postedData:
            return 301 # Missing Parameter 
        else:
            return 200 
    elif functionName == "division":
        if "x" not in postedData or "y" not in postedData:
            return 301 
        elif postedData["y"] == 0:
            return 302 
        else:
            return 200 

class Add(Resource):
    def post(self):
        # if I am here, then the resource Add was requested here POST 
        #Step1: Get posted data 
        postedData = request.get_json() 
        
        #step 1-b: Verify validity of posted data 
        status_code = checkPostedData(postedData, "add")
        if status_code != 200:
            retJson = {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
            
        # If we are here then status code is 200 
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x + y 
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        # if I am here, then the resource Subtract was requested here POST 
        #Step1: Get posted data 
        postedData = request.get_json() 
        
        #step 1-b: Verify validity of posted data 
        status_code = checkPostedData(postedData, "subtract")
        if status_code != 200:
            retJson = {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
            
        # If we are here then status code is 200 
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x - y 
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        # if I am here, then the resource Multiply was requested here POST 
        #Step1: Get posted data 
        postedData = request.get_json() 
        
        #step 1-b: Verify validity of posted data 
        status_code = checkPostedData(postedData, "multiply")
        if status_code != 200:
            retJson = {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
            
        # If we are here then status code is 200 
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x * y 
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        # if I am here, then the resource Divide was requested here POST 
        #Step1: Get posted data 
        postedData = request.get_json() 
        
        #step 1-b: Verify validity of posted data 
        status_code = checkPostedData(postedData, "division")
        if status_code != 200:
            retJson = {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
            
        # If we are here then status code is 200 
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x / y 
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")

if __name__ == "__main__":
    app.run(host='0.0.0.0')