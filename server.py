from flask import Flask, jsonify

app = Flask(__name__)

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
@app.route("/products", methods=["GET"])
def get_products():
    get_products = [
        {"id": 1, "name": "Cake", "price": 25},
        {"id": 2, "name": "Ice-cream", "price": 5},
        {"id": 3, "name": "Cookie", "price": 3},
        {"id": 4, "name": "Chocolate", "price": 10}
    ]
    return get_products

@app.route("/products/count", methods=['GET'])
def get_products_count():
    products = [
        {"id": 1, "name": "Cake", "price": 25},
        {"id": 2, "name": "Ice-cream", "price": 5},
        {"id": 3, "name": "Cookie", "price": 3},
        {"id": 4, "name": "Chocolate", "price": 10}
    ]
    return ({
        "success": True,
        "count": len(products)
    }), 200
    

if __name__ == "__main__":
    app.run(debug=True)