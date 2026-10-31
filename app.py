from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/")
def home():
    name ="Preeti "
    last_nm="Jaiswal"
    course ="flask"
    city ='pune'
    age=23
    return render_template("index.html", name = name,last_nm=last_nm, 
                           course=course, city=city, age=age)

if __name__ =="__main__":
    app.run(debug=True)
    
