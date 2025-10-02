from flask import Flask, jsonify, request
from http import HTTPStatus
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask framework!"


# http://127.0.0.1:5000/cohort-60
@app.route("/cohort-60", methods=["GET"])
def hello_world():
    print ("Cohort 60 endpoint accessed")
    return "Hello Cohort#60"


# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
    information = {"email": "grantreggie09@gmail.com", "phone": "619-483-7137"}
    return information


@app.route("/course", methods=["GET"])
def course_information():
    return {
        "title": "Intro Web API Flask",
        "duration": "4 sessions",
        "level": "Beginner"
    }

@app.route("/user", methods=["GET"])
def user():
    return{
        "favorite_technologies": [
            "Vue.js",
            "FastAPI"

        ],
        "is_active": "True",
        "name": "Reggie",
        "Role": "Mail Carrier",
    }

# ------------ Mini Challange ---------------
# - Create a /user endpoint
# - Return a dictionary with:
#.     name, role, is_active, and favorite_technologies
# - Test it by visiting server
student_names = ["Reggie", "Tim", "Zane", "Mike", "Jose", "Jake"]

@app.route("/students", methods=["GET"])
def get_students():
    print("Students endpoint accessed")
    return student_names


@app.route("/students", methods=["POST"])
def add_student():
    student_names.append("Leo")
    return student_names



# -------- Assignment #1 --------
# products = [
#    {"id": 1, "name": "Cake", "price": 25},
#    {"id": 2, "name": "Ice-cream", "price": 5},
#    {"id": 3, "name": "Cookie", "price": 3},
#    {"id": 4, "name": "Chocolate", "price": 10}
#]

products = [
  {"id": 1, "title": "Cake", "price": 25, "category": "Electronics", "image": "https://picsum.photos/seed/1/300/300"},
  {"id": 2, "title": "Ice-cream", "price": 5, "category": "Kitchen", "image": "https://picsum.photos/seed/2/300/300"},
  {"id": 3, "title": "Cookie", "price": 3, "category": "Electronics", "image": "https://picsum.photos/seed/3/300/300"},
  {"id": 4, "title": "Chocolate", "price": 10, "category": "Entertainment", "image": "https://picsum.photos/seed/4/300/300"}
]

@app.route("/api/products", methods=["GET"])
def get_products():
    return products

@app.route("/api/products/count", methods=['GET'])
def get_products_count():
    return ({
        "success": True,
        "count": len(products)
    }), 200


# --------------- Assingment #2 -----------

# products = [
#    {"id": 1, "name": "Cake", "price": 25},
#    {"id": 2, "name": "Ice-cream", "price": 5},
#    {"id": 3, "name": "Cookie", "price": 3},
#    {"id": 4, "name": "Chocolate", "price": 10}
#]

@app.route("/api/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    print(new_product)
    products.append(new_product)
    return jsonify(new_product), HTTPStatus.CREATED

@app.route("/api/products/<int:id>", methods=["GET"])
def get_products_by_id(id):
    for product in products:
        if product.get("id") == id:
            return jsonify(product), HTTPStatus.OK
        print(f"product: {product}")
    return jsonify({"message": "Product not found"}), HTTPStatus.NOT_FOUND

@app.route("/api/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    for index, product in enumerate(products):
        if product.get("id") == id:
            products.pop(index)
            return jsonify({"message": "Product deleted successfully"}), HTTPStatus.NO_CONTENT
    return jsonify({"message": "Product not found"}), HTTPStatus.NOT_FOUND
    

# Only run the server once
if __name__ == "__main__":
    app.run(debug=True)

# UPDATE /api/products/2
@app.route("/api/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    print(data)
    for product in products:
        if product["id"] == id:
            product["name"] = data.get("name")
            product["price"] = data.get("price")
            return jsonify({"message": "Product updated successfully"}), HTTPStatus.OK
    return jsonify({"message": "Product not found"}), HTTPStatus.NOT_FOUND


# --------- Session #4 ------------
# Query paramters
# A query parameter is added to the end of the URL to filter, sort of modify the response
# GET /api/products/search?name=xxxx
@app.route("/api/products/search", methods=["GET"])
def get_product_by_name():
    keyword = request.args.get("name").lower()
    matched = []
    for product in products:
        if product["name"].lower() == keyword.lower():
            matched.append(product)
    print(keyword)
    return jsonify({"results": matched}), HTTPStatus.OK
        







coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "FALL25", "discount": 25},
    {"_id": 3, "code": "VIP500", "discount": 50}

]

# READ all coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return jsonify(coupons), HTTPStatus.OK


# CREATE add a new coupon
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    print(new_coupon)
    coupons.append(new_coupon)
    return jsonify(new_coupon), HTTPStatus.CREATED



# Path parameter
# A path parameter is a dynamic segment of the URL to pinpoint a specific item or resource.
# http://127.0.0.1:5000/greet/reggie
@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    return f"hello {name}", HTTPStatus.OK



# GET a coupon 
@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify(coupon), HTTPStatus.OK
        print(f"coupon: {coupon}")
    return jsonify({"message": "Coupon not found"}), HTTPStatus.NOT_FOUND


# UPDATE - 



# DELETE - delete a coupon
@app.route("/api/coupons/<int:id>", methods=["DELETE"])
def delete_coupon(id):
    for index, coupon in enumerate(coupons):
        if coupon["_id"] == id:
            coupons.pop(index)
            return jsonify({"message": "Coupon deleted successfully"}), HTTPStatus.NO_CONTENT
    return "testing"

# -------- Final report -------------

@app.route("/api/coupons/<int:id>", methods=["PUT"])
def update_coupon(id):
    data = request.get_json()
    print(data)
    for coupon in coupons:
        if coupon["_id"] == id:
            coupon["code"] = data.get("code", coupon["code"])
            coupon["discount"] = data.get("discount", coupon["discount"])
            return jsonify({"message": "Coupon updated successfully", "coupon": coupon}), HTTPStatus.OK
    return jsonify({"message": "Coupon not found"}), HTTPStatus.NOT_FOUND

@app.route("/api/coupons/search", methods=["GET"])
def search_coupons():
    filtered_coupons = []
    for coupon in coupons:
        if coupon["discount"] < 30:
            filtered_coupons.append(coupon)
    return jsonify({"results": filtered_coupons, "count": len(filtered_coupons)}), HTTPStatus.OK
    

if __name__ == "__main__":
    app.run(debug=True)