# main.py

import json

from CW1_Program.users import Student, Teacher, Admin
from CW1_Program.utils import load_user



def login():

    username = input("please enter your username: ")
    password = input("please enter your password: ")

    users_data = load_user()
    for user in users_data:
        if user['user_name'] == username and user['user_password'] == password:
            role = user['role']
            if role == 'student':
                return Student(user['user_id'], username, password)
            elif role == 'teacher':
                return Teacher(user['user_id'], username, password)
            elif role == 'admin':
                return Admin(user['user_id'], username, password)
    print("wrong id or password！")
    return None


def student_menu(student):
    pass

def teacher_menu(teacher):
    pass

def main():
    pass
