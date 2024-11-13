#先把抽象类写好
from CW1_Program.courses import Course
from CW1_Program.utils import *
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
        #这里在之后可以加一个key来判断能选的课
        course=load_course()
        print("all the available courses:",end='\n')
        for i in course:
            print(f"course name: {i['course_name']}, course_id: {i['course_id']}")

    def enroll_course(self):
        #加入课程
        course = load_course()
        course_id=input("please type in the course id OF the course that you want to enroll: ")

        #查找课程
        for i in course:
            if i['course_id']==course_id:
                if self.user_id not in i['student_list']:
                    i['student_list'].append(self.user_id)
                    self.enrolled_course.append(course_id)
                    save_course(course)

                    users = load_user()
                    for j in users:
                        if j['user_id']==self.user_id:
                            j['enrolled_course']=self.enrolled_course
                            break
                    save_user(users)

                    print('your had successfully enrolled')
                    return
                else:
                    print('your had already enrolled')
                    return
        print('the class does not exist')

    def view_enrolled_course(self):
        #查看已经加入的课程
        if not self.enrolled_course:
            print("您尚未报名任何课程。")
        else:
            print("您已报名的课程：")
        for course_id in self.enrolled_course:
            print(f"课程 ID: {course_id}")



class Teacher(Users):
    def __init__(self,user_id,user_name,user_password):
        super().__init__(user_id,user_name,user_password,role='teacher')
        self.course_teach = []

    def create_course(self):
        #创建课程
        course_id = input('Enter course ID: ')
        course_name = input('Enter course name: ')
        new_course = Course(course_id,course_name,self.user_id)

        course=load_course()
        course.append(new_course)
        save_course(course)
        self.course_teach.append(course_id)
        #之后考虑要在初始化的时候就把teach这个列表写好
        user_data=load_user()
        for user in user_data:
            if user['user_id']==self.user_id:
                user['course_teach']=self.course_teach
        print(f'the course {course_name} ,id: {course_id }has been created')


    def view_students(self):
        #查看学生
        pass

    def view_course_teach(self):
        #查看教授的课程
        if not self.course_teach:
            print("you are not teaching any class")
        else:
            print("the class you teach are list followed")
            for i in self.course_teach:
                print(f'course_id:{i}')

    def manage_student_of_course(self):
        #管理学生 增/删
        course_id = input('Enter course ID: ')
        if course_id in self.course_teach:
            course_data=load_course()
            for course in course_data:
                if course['course_id']==course_id:
                    print("the student in this course are followed")
                    print(course['student_list'])
                    manage=input('what you wanna do?(add/remove)')
                    #增
                    if manage=='add':
                        student_id=input('enter student ID: ')
                        if student_id not in course['student_list']:
                            course[student_id].append(student_id)
                            print(f'you had added the student {student_id} to the course {course_id}')
                        else:
                            print(f'student {student_id} is already enrolled in this course')
                    #删
                    elif manage=='remove':
                        student_id=input('enter student ID: ')
                        if student_id in course['student_list']:
                            course[student_id].remove(student_id)
                            print(f'you had removed the student {student_id} from coursee {course_id}')
                        else:
                            print(f'student {student_id} is not enrolled in this course{course_id}')
                    else:
                        print('wrong input')


    def manage_course(self):
        #管理课程 改id或者名字
        course_id=input('Enter course ID: ')
        if course_id in self.course_teach:
            course_data=load_course()
            for course in course_data:
                if course['course_id']==course_id:
                    print(f'the course {course["course_id"]} ,name: {course["course_name"]}, \
                    teacher: {course["teacher_id"]}')
                    print('1.change the id of course')
                    print('2.change the name of course')
                    manage=input('what you wanna do (1/2)')
                    if manage=='1':
                        new_id=input('enter new course ID: ')
                        course['course_id']=new_id
                        print(f'the id of course {course["course_name"]} has benn changed to {course["course_id"]}')
                    elif manage=='2':
                        new_name=input('enter new course name:')
                        course['course_name']=new_name
                        print(f'the name of course {course["course_id"]} has benn changed to {course["course_name"]}')
                    else:
                        print("wrong input")

                    save_course(course_data)
                    return
        else:
            print(f"the course {course_id} does not exist or you dont have permission to manage this course")
class Admin(Users):
    def __init__(self,user_id,user_name,user_password):
        super().__init__(user_id,user_name,user_password,role='admin')

    def create_course_admin(self):
        #创建课程，管理员权限
        pass

    def manage_course_admin(self):
        #管理课程，管理员权限
        pass
