from flask import Flask, render_template, url_for,redirect,request,jsonify
from dotenv import load_dotenv
# from util import json_response
# import mimetypes
import queries

from threading import Timer

# mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)

load_dotenv()

@app.route("/", methods=['POST', 'GET'] )
def index():
    
    if request.method == "GET":
        first_name = queries.test()  
        # print(first_name)
    return render_template('index.html' , first_name = first_name[0][0]) 








@app.route("/add", methods=['POST', 'GET'])
def add():
   
    if request.method == "POST":
            # first_name = first_name + 1
        first_name = request.form
        
        queries.update_DB(first_name['status'], '1')
        return redirect('/')

# @app.route("/api/<id>&<costam>", methods=['PUT', 'POST'])
# def wczytaj(id, costam):
#     if request.method == "PUT":
#         queries.update_DB(costam, id)
#     elif request.method == "POST":
#         queries.insert_DB(costam, id)
    
#     return redirect('/')



# @app.route('/update')    
# def update():
#     import time
#     while True:
#         first_name =  jsonify(first_name = queries.test())
      
#         print(first_name)
#         time.sleep(5)
   



# @app.route('/update', methods=['POST'])
# def add_income():
#     incomes.append(request.get_json())
#     return '', 204



import json

@app.route('/update')
def update(): # Data to be written
    first_name = queries.test()  
    dictionary = {
        "name": first_name[0][0]
       
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    return json_object



# @app.route("/api/<id>", methods=['GET'])
# def getztabeli(id):
#     dodo= []
#     dodo = queries.getbyid(id)
#     return render_template('index3.html', id=dodo)



def main():
    app.run(debug=True)
    load_dotenv('.env')
    update()    
   

    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()







