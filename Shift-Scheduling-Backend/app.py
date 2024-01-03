from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/shift'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    preferences = db.relationship('Preference', backref='user', lazy=True)

    def to_dict(self):
        return {
            'userId': self.userId,
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'preferences': [preference.to_dict() for preference in self.preferences]
        }

class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), nullable=False)
    day = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'day': self.day,
            'time': self.time
        }

# GET method for all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# GET method for a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'message': 'User not found'}), 404

# POST method to add a new user
@app.route('/users', methods=['POST'])
def add_new_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# GET method for all preferences
@app.route('/preferences', methods=['GET'])
def get_all_preferences():
    preferences = Preference.query.all()
    return jsonify([preference.to_dict() for preference in preferences])

# GET method for preferences of a specific user by ID
@app.route('/preferences/<int:user_id>', methods=['GET'])
def get_preferences_by_user_id(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify([preference.to_dict() for preference in user.preferences])
    else:
        return jsonify({'message': 'User not found'}), 404

# POST method to add a new preference for a user
@app.route('/preferences', methods=['POST'])
def add_new_preference():
    data = request.get_json()
    user = User.query.get(data['userId'])
    if user:
        new_preference = Preference(userId=user.userId, day=data['day'], time=data['time'])
        db.session.add(new_preference)
        db.session.commit()
        return jsonify(new_preference.to_dict()), 201
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
