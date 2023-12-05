from flask import Flask, render_template, url_for,redirect,request,jsonify
from dotenv import load_dotenv
import queries
import json

from threading import Timer


app = Flask(__name__)

load_dotenv()

@app.route("/", methods=['POST', 'GET'] )
def index():    
    if request.method == "GET":
        first_name = queries.ttt()  
        # print(first_name)
    return render_template('index.html' , first_name=first_name) 




# @app.route("/add", methods=['POST', 'GET'])
# def add():
       
#     if request.method == "POST":
#             # first_name = first_name + 1
#         first_name = request.form
        
#         queries.update_DB(first_name['status'], '1')
#         return redirect('/')



# @app.route("/create", methods=["POST"])
# def create():
#     data = request.get_json()
#     print(data['id'])
#     queries.update_DB(data['id'], 1)
#     queries.test()
#     return jsonify(data), 201





# @app.route('/api/getCounter')
# def update(): # Data to be written
#     counter = queries.test()  
#     counterDict = {
#         "Id": counter[0][0],
#         "TomKurwQty": counter[0][1]
        
#          }
    

#     # Serializing json
#     json_object = json.dumps(counterDict, indent=4)
#     return json_object


def main():
    app.run(debug=True)
    load_dotenv('.env')

   

    # with app.app_context():
    #     app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()







