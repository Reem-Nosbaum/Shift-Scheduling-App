from app import app, db
from app.models import User, Schedule
from flask import jsonify, request


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

