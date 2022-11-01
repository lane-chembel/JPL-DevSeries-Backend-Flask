from flask import Flask, render_template, url_for, json, jsonify, Response
from flask_cors import CORS

from DataClass import DataClass


app = Flask(__name__)
CORS(app)

my_data = DataClass()

@app.route("/getSomeData")
def getSomeData():
    r = my_data.globalData
    return Response(json.dumps(r), mimetype='application/json')

@app.route("/getSomeDataFromFile")
def getSomeDataFromFile():
    r = my_data.getJsonFromFile('./data/hello.json')
    return Response(json.dumps(r), mimetype='application/json')

@app.route("/getEmployees")
def getEmployees():
    emp = my_data.getJsonFromFile('./data/employees.json')
    return jsonify(emp)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
