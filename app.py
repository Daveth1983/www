from flask import Flask, render_template, url_for,redirect,request,jsonify
from dotenv import load_dotenv
# from util import json_response
# import mimetypes
import queries

# mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)

load_dotenv()

@app.route("/", methods=['POST', 'GET'] )
def index():
    return render_template('index.html')


@app.route("/add", methods=['POST'])
def add():
    if request.method == "POST":
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





# @app.route("/api/<id>", methods=['GET'])
# def getztabeli(id):
#     dodo= []
#     dodo = queries.getbyid(id)
#     return render_template('index3.html', id=dodo)

def main():
    app.run(debug=True)
    load_dotenv('.env')
 

    # with app.app_context():
    #     app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()







