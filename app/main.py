from flask import Flask, render_template, request, redirect, url_for
from models import db, User

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
def cars():
    car_list = [
        {"name": "Ferrari F8 Tributo", "type": "Sports", "year": 2022, "image": "car.jpg"},
        {"name": "Lamborghini Huracan EVO", "type": "Sports", "year": 2021, "image": "car.jpg"},
        {"name": "Porsche 911 Turbo S", "type": "Sports", "year": 2023, "image": "car.jpg"},
        {"name": "Tesla Model S Plaid", "type": "Electric", "year": 2022, "image": "car.jpg"},
        {"name": "BMW M4 Competition", "type": "Coupe", "year": 2022, "image": "car.jpg"}
    ]
    return render_template('cars.html', cars=car_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
