from flask import Flask

app = Flask(__name__) # flask app obj store 

@app.route("/")
def home():
    return "hello world"

@app.route("/about")
def about():
    return "welcome to about page"

@app.route("/contact")
def contact():
    return "welcome to contact page"

@app.route("/users")
def users():
    return "welcome to users page"

# dynamic route
'''
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}" '''


# multiple dynamic parameter
# var name mismatch then 404 not found - name and course shoild be in paramter
@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"


# integer url converter 
@app.route("/product/<int:id>")
def product(id):
    return f"Product User Id: {id}"

# float url converter 
@app.route("/price/<float:amount>")
def price(amount):
    return f"price amount is {amount}"

# string url converter 
@app.route("/product-nm/<string:name>")
def productname(name):
    return f"product name is {name}"


# path url converter 
@app.route("/files/<path:file_path>")
def files(file_path):
    return f"my file path {file_path}"


# uuid url converter - unique user id 
from uuid import UUID
@app.route("/students/<uuid:user_id>")
def students(user_id):
    return str(user_id)


if __name__ =="__main__":
    app.run(debug=True)
    # if i change anythong then it will take automatic, we donot need to start /run the app again and again
    