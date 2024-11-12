# main.py

import json

from CW1_Program.users import Student, Teacher, Admin


def load_users():
    with open('users.json', 'r') as file:
        users_data = json.load(file)
    return users_data


def login():
    users_data = load_users()
    username = input("please enter your username: ")
    password = input("please enter your password: ")

    for user in users_data:
        if user['username'] == username and user['password'] == password:
            role = user['role']
            if role == 'student':
                return Student(user['user_id'], username, password)
            elif role == 'teacher':
                return Teacher(user['user_id'], username, password)
            elif role == 'admin':
                return Admin(user['user_id'], username, password)
    print("wrong id or password！")
    return None
