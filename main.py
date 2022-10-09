import googlemaps
from pprint import pprint
from flask import Flask,request, render_template,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/home', methods =["GET","POST"])
def geocodeapi():
        f = open("Key.txt", 'r')
        api_key = f.readline()
        api_client = googlemaps.Client(api_key)

        if request.method == "POST":
                address = request.form.get("origin")
                #address = "state bank of india, wadegaon, akola, 444502"
                print(address)
                type(address)
                response = api_client.geocode("akola")
                return response
                return response[0]["address_components"][0]["long_name"]

        else:
                return render_template("index.html")

@app.route('/check', methods =["GET","POST"])
def distancematrix():
        f = open("Key.txt", 'r')
        api_key = f.readline()
        api_client = googlemaps.Client(api_key)
        if request.form.get('send') == 'send':
                origin = str(request.form.get('test1'))
                destination = str(request.form.get('test2'))
                response = api_client.distance_matrix(origin,destination)
        return response

if __name__ == "__main__":
        app.run(debug=True)

