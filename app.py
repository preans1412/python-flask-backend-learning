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
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

# multiple dynamic parameter

@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"

if __name__ =="__main__":
    app.run(debug=True)
    # if i change anythong then it will take automatic, we donot need to start /run the app again and again
    
    
# interview questions
'''
why need flask
why need venv
__name__?- special python var - if we have to directly excute it then we have to store in __main__
why debugger mode needed?
what is routing
@app.route why use?
multiple route how to handle?
'''


'''
-- Static Route vs Dynamic Route
-- What are Dynamic Routes in Flask?
-- Create Your First Dynamic Route
-- URL Parameters in Flask
-- Multiple Dynamic Parameters
-- Pass Parameters from URL to Python Function
-- Real-World Dynamic Route Examples
-- User Profile URLs
-- Product & Order URLs
-- Common Dynamic Routing Mistakes
'''

