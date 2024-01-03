# # insert_schedule_data.py
# from app import db, User, Schedule

# def insert_schedule_data(user_id, schedule_data):
#     user = User.query.get(user_id)
#     if not user:
#         print(f"User with ID {user_id} not found.")
#         return

#     # Clear existing schedule data for the user
#     if user.schedule:
#         db.session.delete(user.schedule)

#     for day, times in schedule_data.items():
#         for time in times:
#             schedule = Schedule(userId=user_id, day=day, time=time)
#             db.session.add(schedule)

#     db.session.commit()
#     print("Schedule data inserted successfully.")

# if __name__ == '__main__':
#     from app import app

#     with app.app_context():
#         # Example usage:
#         user_id_to_insert = 1  # Replace with the desired user ID
#         schedule_data_to_insert = {
#             'Friday': ['morning'],
#             'Monday': ['morning'],
#             'Saturday': ['morning', 'evening'],
#             'Sunday': ['evening'],
#             'Thursday': ['evening'],
#             'Tuesday': ['evening'],
#             'Wednesday': ['morning']
#         }

#         insert_schedule_data(user_id_to_insert, schedule_data_to_insert)
