#先把抽象类写好
from CW1_Program.courses import Course


class Users():
    def __init__(self,user_id,user_name,user_password,role):
        self.user_name=user_name
        self.user_id=user_id
        self.user_password=user_password
        self.role=role

    def display(self):
        print(f"User ID: {self.user_id}")
        print(f"Username: {self.user_name}")
        print(f"Role: {self.role}")

class Student(Users):
    def __init__(self,user_id,user_name,user_password):
        super().__init__(user_id,user_name,user_password,role='student')
        self.enrolled_course = []

    def view_available_course(self):
        #查看可选课程
        pass

    def enroll_course(self):
        #加入课程
        pass

    def view_enrolled_course(self):
        #查看已经加入的课程
        pass

class Teacher(Users):
    def __init__(self,user_id,user_name,user_password):
        super().__init__(user_id,user_name,user_password,role='teacher')
        self.course_teach = []

    def create_course(self):
        #创建课程
        course_id = input('Enter course ID: ')
        course_name = input('Enter course name: ')
        new_course = Course(course_id,course_name,self.user_id)
        #还没有写save这个函数
        save_course(new_course)
        self.course_teach.append(course_id)
        #之后考虑要在初始化的时候就把teach这个列表写好
        print(f'the course {course_name} ,id: {course_id }has been created')
        pass

    def view_students(self):
        #查看学生
        pass

    def enroll_students(self):
        #注册学生
        pass

    def view_course_teach(self):
        #查看教授的课程
        pass

    def manage_student(self):
        #管理学生
        pass

    def manage_course(self):
        #管理课程
        pass

class Admin(Users):
    def __init__(self,user_id,user_name,user_password):
        super().__init__(user_id,user_name,user_password,role='admin')

    def create_course_admin(self):
        #创建课程，管理员权限
        pass

    def manage_course_admin(self):
        #管理课程，管理员权限
        pass
