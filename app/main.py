from flask import Flask, render_template, request, redirect, url_for
from models import db, User
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///racer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return 'Login successful!'
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return 'Username already exists', 400
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/users')
def users():
    users = User.query.order_by(User.username).all()
    return render_template('users.html', users=users)

@app.route('/healthz')
def healthz():
    return 'OK', 200

@app.route('/cars')
@app.route('/cars')
def cars():
    car_list = [
        {
            "name": "Mercedes W11",
            "type": "F1",
            "year": 2020,
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercedes_W11_Williams_FW42_Silverstone_2019_01.jpg"
        },
        {
            "name": "Red Bull RB16B",
            "type": "F1",
            "year": 2021,
            "image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/2021_British_Grand_Prix_%2825219345947%29.jpg"
        },
        {
            "name": "Ferrari SF1000",
            "type": "F1",
            "year": 2020,
            "image": "https://upload.wikimedia.org/wikipedia/commons/5/5e/2020_Ferrari_SF1000_front_left_%28cropped%29.jpg"
        },
        {
            "name": "McLaren MCL35M",
            "type": "F1",
            "year": 2021,
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/d9/McLaren_MCL35M_2021_British_GP_%283%29.jpg"
        },
        {
            "name": "Alpine A521",
            "type": "F1",
            "year": 2021,
            "image": "https://upload.wikimedia.org/wikipedia/commons/f/f1/2021_Alpine_A521_Side.jpg"
        }
    ]
    return render_template('cars.html', cars=car_list)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use PORT from env or default 8080
    app.run(host='0.0.0.0', port=port)
