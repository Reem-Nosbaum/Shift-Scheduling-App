from app import app, db
from app.models import User, Schedule
from flask import jsonify, request, session,make_response
from dotenv import load_dotenv
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager

import os

load_dotenv()

app.secret_key = os.getenv('SECRET_KEY')

jwt = JWTManager(app) 

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        user = User.query.filter_by(username=data['username']).first()

        if user and user.password == data['password']:
            user_data = {
                'id': user.id,
                'username': user.username,
                'role': user.role,
            }
            access_token = create_access_token(identity=user_data)
            return jsonify(access_token=access_token), 200
        else:
            # Authentication failed
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Protected route for admin
@app.route('/admin', methods=['GET'])
@jwt_required()
def admin_route():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({'error': 'Unauthorized access'}), 403
    # Continue with serving the admin content
    return jsonify({'message': 'Welcome to the admin page!'})


# Protected route for user
@app.route('/user', methods=['GET'])
@jwt_required()
def user_route():
    current_user = get_jwt_identity()
    user_data = {
        'id': current_user['id'],
        'username': current_user['username'],
        'role': current_user['role'],
    }

    if current_user['role'] != 'user':
        return jsonify({'error': 'Unauthorized access'}), 403
    # Continue with serving the user content
    return jsonify({'message': 'Welcome to the user page!', 'user': user_data})

# GET route to retrieve user and schedule information
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_and_schedule(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        schedule = Schedule.query.filter_by(userId=user.id).first()

        user_data = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'role': user.role,
            'schedule': schedule.schedule if schedule else {}
        }

        return jsonify(user_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route("/logout", methods=['POST'])
def logout():
    if 'user_id' in session:
        session.pop('user_id')
        return make_response(jsonify({'task': 'logout', 'status': 'success'}), 200)
    return make_response(jsonify({'task': 'logout', 'status': 'failed'}), 401)



# POST route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()

        # Create a user
        new_user = User(username=data['username'], password=data['password'], role=data['role'])
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# POST route to create a new schedule
@app.route('/schedules', methods=['POST'])
def create_schedule():
    try:
        data = request.get_json()

        # Create a schedule
        user_id = data.get('userId')  
        user = User.query.get(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        new_schedule = Schedule(userId=user.id, schedule=data.get('schedule', {}))
        db.session.add(new_schedule)
        db.session.commit()

        return jsonify({'message': 'Schedule created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

