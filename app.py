from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os

app = Flask(__name__)
app.secret_key = os.urandom(24)

db_url="postgres://gdhsgcrpexxhrv:b0aba3843a99ad38f3ceacec1e8358abbe06895dbb972acb8b0cc516a776c45b@ec2-54-204-23-228.compute-1.amazonaws.com:5432/datafrifoj0nkf"
db = dataset.connect(db_url)
@app.route('/')
@app.route('/home')
def homepage():
	return render_template('home.html')
# TODO: route to /register
@app.route('/signin', methods=['POST', 'GET'])
def template_test():
	return render_template('signin.html')



@app.route('/signup', methods=['POST', 'GET'])
def template_test1():
	return render_template('signup.html')

# @app.route("/newAccount" , methods=['POST'])
# def newAccount():
# 	account =db ['account']
# 	potential_username= request.form['username']
# 	potential_password= request.form['password']
# 	username_exists = account.find_one(username=potential_username)
# 	if username_exists:
# 		return render_template("ss.html")
# 	else:
# 		account.insert(dict(username=potential_username, password=potential_password))
# 		return render_template("home.html")





# TODO: set up database
# db = dataset.connect("<database>")
# hello maysam!db = dataset.connect(db_url)


if __name__ == "__main__":
    app.run(port=3000)











