from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from plyer import notification


# notification.notify(
#     title = 'testing',
#     message = 'message',
#     app_icon = None,
#     timeout = 10,
# )

DB_N = 'messy_db.sqlite'

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'messy'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_N}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.drop_all()

with app.app_context():
    db.create_all()


@app.route("/")
def home ():
#     notification.notify(
#     title = 'Get',
#     message = 'home',
#     app_icon = None,
#     timeout = 10,
# )
    return "<h1>Hi</h1>"


@app.route('/')
def basic():
    return "hi"
	# return render_template("base.html")


@app.route('/', subdomain ='sub1')
def sub1h():
	return "subdomain 1 home"

@app.route('/', subdomain ='sub2')
def sub2h():
	return "subdomain 2 home"

@app.route('/pg1/', subdomain ='sub2')
def sub2p1():
	return "subdomain 2 page 1 " 

@app.route('/pg1/', subdomain ='sub1')
def sub1p1():
	return "subdomain 1 page 1 " 

if __name__ == "__main__":
	website_url = 'messy-flask.com:5000'
	app.config['SERVER_NAME'] = website_url
	app.run(debug=True)


# https://develie.hashnode.dev/custom-alerts-in-flask-using-sweetalert2
# https://code.tutsplus.com/tutorials/creating-pretty-popup-messages-using-sweetalert2--cms-30662
# https://sweetalert2.github.io/
# pyscript
