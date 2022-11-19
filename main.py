from flask import Flask,jsonify,render_template,request,make_response

app = Flask(__name__)

@app.route("/")
def go_demo():
    return jsonify({'Message':'Hello world'})

@app.route("/endpoint1")
def go_demo1():
    return jsonify({'Message':'End Point1'})

@app.route("/html")
def get_html():
    return render_template("index.html")    

@app.route("/qs")
def get_qs():
    if request.args:
        req = request.args
        return "\n".join(f'{k}=>{v}' for k,v in req.items())
    else:
        return jsonify({"Message" : "No Query Parameters Found"})


@app.route("/orders")
def get_order():
    response =  make_response(jsonify(orders),200)
    return response

@app.route("/order1")
def get_order():
    response =  make_response(jsonify(orders),200)
    return response    

orders = {
    "order1" :
    {
        "name":"pizza",
        "toppings":"cheese",
        "crust":"Thin crust"
    }
}


if __name__ == "__main__":
    app.run(debug=True)