from flask import Flask,jsonify,render_template,request,make_response

app1 = Flask(__name__)

orders = {
    "order1" :
    {
        "name":"pizza",
        "toppings":"cheese",
        "crust":"Thin crust"
    }
}



@app1.route("/orders")
def get_order():
    response =  make_response(jsonify(orders),200)
    return response

@app1.route("/orders/<orderid>")
def get_order1(orderid):
    if orderid in orders:
        return make_response(orders[orderid],200)
    else:
        return jsonify({"Message":"No Order ID found"})    
    
@app1.route("/orders/<orderid>/<items>")
def get_items(orderid,items):
    items = orders[orderid].get(items)
    if items:
        return make_response(jsonify(items),200)
    else:
        return make_response(jsonify({"Message":"Not items found"}),400)

'''
We are creating a post method to create post method which will create an order 
'''
@app1.route("/orders/<orderid>",methods=["POST"])
def post_order_creation(orderid):
    json = request.get_json()
    if orderid in orders:
        return make_response(jsonify({"Message":"Order ID already exists"}),400)
    else:
        orders.update({orderid : json})
        return make_response(jsonify({"Message":"Order ID Added"}),200)            

'''
We are creating a put method to update the data
'''

@app1.route("/orders/<orderid>",methods=["PUT"])
def put_order_creation(orderid):
    json = request.get_json()
    if orderid in orders:
        orders[orderid] = json
        return make_response(jsonify({"Message":"Order ID Updated"}),200)
    orders[orderid] = json
    return make_response(jsonify({"Message":"New Order id Created"}),201)            

'''
We are creating a patch method where it take only few items in teh order and it will update..
where as in put methold we need to pass the entire josn
'''

@app1.route("/orders/<orderid>",methods=["PATCH"])
def patch_order_creation(orderid):
    req = request.get_json()
    if orderid in orders:
        for k,v in req.items():
            orders[orderid][k] =v
        response =  make_response(jsonify({"Message":"Order ID Updated"}),200)   
        return response
    orders[orderid] = req    
    return make_response(jsonify({"Message":"patch Order id Created"}),201)            

'''
Now we are going to delete the order id
'''

@app1.route("/orders/<orderid>",methods=["DELETE"])
def delete_order_id(orderid):
    if orderid in orders:
        del orders[orderid]
        response =  make_response(jsonify({"Message":"Order ID Deleted"}),204)   
        return response
    return make_response(jsonify({"Message":"Order id did not exits"}),201)            



if __name__ == "__main__":
    app1.run(debug=True)