from flask import Flask,render_template,request         


app = Flask(__name__)

@app.route("/login" , methods=['GET' , 'POST'])
def login():
    errors = {}
    if request.method == "POST":
        uName = request.form["uName"]
        print("User =", uName)
        print("Password =", request.form["uPass"])
        if not uName[0].isalpha():
            errors["uName"] = ["Username should start with alphabet"]
    return render_template('client/login.html')

@app.route("/")    
def home():
    return render_template('client/index.html')

@app.route("/register" , methods= ['GET' , 'POST'])
def register():
    return render_template('client/register.html')
 
# run the server 
app.run(host="0.0.0.0", port=5500 , debug=True)