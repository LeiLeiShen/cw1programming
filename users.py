#先把抽象类写好
from CW1_Program.courses import Course
import json
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
        with open('course.json','r') as filename:
            course=json.load(filename)
        print("all the available courses:",end='\n')
        for i in course:
            print(f"course name: {i['course_name']}, course_id: {i['course_id']}")

    def enroll_course(self):
        #加入课程
        course_id=input("please type in the course id OF the course that you want to enroll: ")
        with open("course.json","r") as filename:
            course=json.load(filename)
        '''
         你这里的读文件最好也一块集成到工具类里去
        '''
        #查找课程
        for i in course:
            if i['course_id']==course_id:
                if self.user_id not in i['student_list']:
                    i['student_list'].append(self.user_id)
                    self.enrolled_course.append(course_id)
                    #这里没定义save的函数
                    save_course(course)
                    #这里的函数到时候再定义一个工具类，去工具类里面写
                    users = load_users()
                    for j in users:
                        if j['user_id']==self.user_id:
                            j['enrolled_course']=self.enrolled_course
                            break
                    save_user(users)
                    # 这里也没定义save
                    print('your had successfully enrolled')
                    return
                else:
                    print('your had already enrolled')
                    return
        print('the class does not exist')

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
