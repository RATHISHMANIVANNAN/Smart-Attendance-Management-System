import mysql.connector
import sys
import datetime
from video_frame import *
from face_trainer import *
from face_recog import *
connection=mysql.connector.connect(host="127.0.0.1",user="root",passwd="IoT",database="dbms")
if connection.is_connected():
       print("Connection Successfull")
else:
       print("Connection is not successful.")
       sys.exit()
cursor = connection.cursor()
def students_add():
       s_id = int(input("Assign a register number : "))
       f_name = input("Enter the  First name of student : ")
       m_name = input("Enter the  middle  name of student : ")
       l_name = input("Enter the  First name of student : ")
       dob = input("Enter the date of birth of student : ")
       age = int(input("Enter the age : "))
       gender = input("Enter the  gender of student : ")
       EMAIL_ID = input("Enter the  EmailID of student : ")
       dept = input("Enter the  dept of student : ")
       query="INSERT INTO students VALUES 
       (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       cursor.execute(query,(s_id,dob,age,f_name,m_name,l_name,gender,EMAIL_ID,dept))
       connection.commit()
def student_cn_add():
    s_id = int(input("Enter  register number : "))
    mobile_number = input("Enter the Phone number of student:")
    query="INSERT INTO student_cn VALUES (%s,%s)"
    cursor.execute(query,(s_id,mobile_number))
    connection.commit()
def students_update():
    s_id = input("Enter the Student_id: ")
    query = "SELECT * FROM students WHERE s_id = %s"
    cursor.execute(query, (s_id,))
    student = cursor.fetchone()
    if not student:
        print("Course not found.")
        return
    f_name = input("Enter the  First name of student : ")
    m_name = input("Enter the  middle  name of student : ")
    l_name = input("Enter the  First name of student : ")
    dob = input("Enter the date of birth of student : ")
    age = int(input("Enter the age : "))
    gender = input("Enter the  gender of student : ")
    EMAIL_ID = input("Enter the  EmailID of student : ")
    dept = input("Enter the  dept of student : ")
    update_query = "UPDATE students SET f_name = %s, 
    m_name = %s,l_name = %s, dob=%s, age=%s,
   gender=%s, EMAIL_ID=%s, dept=%s WHERE s_id = %s"
    cursor.execute(update_query,(f_name,m_name,l_name,dob,age,gender,EMAIL_ID,dept,s_id))
         connection.commit()
    print("Course details updated successfully.")
def faculty_update():
    f_id = input("Enter the faculty_id: ") query = "SELECT * 
   FROM faculty WHERE f_id = %s"
    cursor.execute(query, (f_id,))
    faculty = cursor.fetchone()
    if not faculty:
        print("Faculty not found.")
        return
    f_name = input("Faculty first name : ")
    m_name = input("Faculty middle name : ")
    l_name = input("Faculty last name : ")
    dob = input("Enter the date of birth of faculty : ")
    age = int(input("Enter the age : "))
    gender = input("Enter the gender of faculty : ")
    email_id = input("Enter the EmailID of faculty : ")
    dept = input("Enter the dept of faculty : ")
    update_query = "UPDATE faculty SET f_name = %s,
    m_name = %s, l_name = %s, dob = %s, age = %s, gender = 
    %s, EMAIL_ID = %s, dept = %s WHERE f_id = %s"
    cursor.execute(update_query, (f_name, m_name, l_name, 
    dob, age, gender, email_id, dept,f_id))
    connection.commit()
    print("Faculty details updated successfully.")      
def faculty_cn_add():
    f_id = int(input("Enter register number : "))
    mobile_number =input("Enter the Phone number of faculty:”) 
    query="INSERT INTO faculty_cn VALUES (%s,%s)"
    cursor.execute(query,(f_id,mobile_number))
    connection.commit()
def faculty_cn_update():
    f_id = input("Enter the faculty_id: ")
    query = "SELECT * FROM faculty_cn WHERE f_id = %s"
    cursor.execute(query, (f_id,))
    faculty = cursor.fetchone()
    if not faculty:
        print("Course not found.")
        return
    mobile_number = input("Faculty Mobile number : ")  
    update_query = "UPDATE faculty_cn SET faculty_cn=%s 
    WHERE f_id = %s"
    cursor.execute(update_query, (mobile_number,f_id))
    connection.commit()
def student_cn_update():
    s_id = input("Enter the student_id: ")
    query = "SELECT * FROM student_cn WHERE s_id = %s"
    cursor.execute(query, (s_id,))
    faculty = cursor.fetchone()
    if not faculty:
        print("Course not found.")
        return
    mobile_number = input("Student Mobile number : ")  
    update_query = "UPDATE student_cn SET student_cn=%s WHERE s_id = %s"
    cursor.execute(update_query, (mobile_number,s_id))
    connection.commit()
def student_cn_delete(s_id):
       query = "DELETE FROM student_cn where s_id=%s"
       cursor.execute(query,(s_id,))
       connection.commit()      
def faculty_cn_delete(f_id):
       query = "DELETE FROM faculty_cn where f_id=%s"
       cursor.execute(query,(f_id,))
       connection.commit()     
def student_delete(s_id):
       query = "DELETE FROM students where s_id=%s"
       cursor.execute(query,(s_id,))
       connection.commit()
def faculty_add():
       f_id = int(input("Assign a register number : "))
       f_name = input("Faculty first name : ")
       m_name = input("Faculty middle name : ")
       l_name = input("Faculty last name : ")
       dob = input("Enter the date of birth of faculty : ")
       age = int(input("Enter the age : "))
       gender = input("Enter the  gender of faculty : ")
       EMAIL_ID = input("Enter the  EmailID of faculty : ")
       dept = input("Enter the  dept of faculty : ")
       query="INSERT INTO faculty VALUES 
       (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       cursor.execute(query,(f_id,f_name,m_name,l_name,age,dob,EMAIL_ID,gender,dept))
       connection.commit()
def faculty_delete(f_id):
       query = "DELETE FROM faculty where f_id=%s"
       cursor.execute(query,(f_id,))
       connection.commit()
def attendance_add(f_id,s_id):
    if s_id:
        markings = "yes"
    else:
        markings = "no"
    date = datetime.date.today()
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    query="INSERT INTO attendance VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(query,(f_id,s_id,markings,date,time))
    connection.commit()  
def attendance_update(f_id,s_id):
       markings=input("Enter attendance:")
       query="update attendance set markings=%s where f_id=%s and s_id=%s"
       cursor.execute(query,(markings,f_id,s_id))
       print("Record updated successfully.")
       connection.commit()
def calculate_attendance_percentage(f_id, s_id):
    query = "SELECT markings " \
            "FROM attendance " \
            "WHERE f_id=%s AND s_id=%s"
    cursor.execute(query, (f_id, s_id))
    total_attendance = cursor.fetchall()
    if not total_attendance:
        print("No attendance records found for your registered 
        courses.")
    else:
        print("\nAttendance Percentage for Registered Courses:")
        y = "yes"
        query_present = "SELECT markings " \
                        "FROM attendance " \
                        "WHERE f_id=%s AND s_id=%s AND 
                        markings=%s"
        cursor.execute(query_present, (f_id, s_id, y))
        present_attendance = cursor.fetchall()
        total_attendance_count = len(total_attendance)
        present_attendance_count = len(present_attendance)             
        if total_attendance_count > 0:
            attendance_percentage = (present_attendance_count / 
            total_attendance_count) * 100
        else:
            attendance_percentage = 0       
        print(f"Total Attendance: {total_attendance_count}")
        print(f"Present Classes: {present_attendance_count}")
        print(f"Attendance Percentage: 
        {attendance_percentage:.2f}%")
def add_student():
    roll_number=input("ENTER STUDENTS ROLL_NUMBER:
    ")  
    capture_and_save_images(roll_number)
    train()
    students_add()
    student_cn_add()
    print("Student details added successfully!!")
def take_attendance(f_id):
    presentees=detect_faces(delay_time=30)
    for i in presentees:
        attendance_add(f_id,i)
    print("Attendance Taken!")   
ch1=input("FACULTY DETAILS(1) ,STUDENT DETAILS(2),ATTENDANCE(3)")
ch2=0
if ch1=="1":
    ch2=input("ADD FACULTY(1),REMOVE FACULTY 
    DETAILS(2),UPDATE FACULTY DETAILS(3)")
    if ch2=='1':
        faculty_add()
        faculty_cn_add()
    elif ch2=='2':
        de=input("enter Faculty id:")
        faculty_delete(de)
        faculty_cn_delete(de)
    elif ch2=='3':
        faculty_update()
        faculty_cn_update()
    else:
        print("incorrect choice")
elif ch1=='2':
    ch2=input("ADD STUDENT(1),REMOVE STUDENT 
    DETAILS(2),UPDATE STUDENT DETAILS(3)")
    if ch2=='1':
        students_add()
        student_cn_add()
    elif ch2=='2':
        de=input("enter Student id:")
        student_delete(de)
        student_cn_delete(de)
    elif ch2=='3':
        students_update()
        student_cn_update()
    else:
        print("incorrect choice")
elif ch1=='3':
    ch2=input("TAKE ATTENDANCE(1),
               UPDATE_ATTENDANCE(2),
               CHECK_ATTENDANCE(3)")
    if ch2=='1':
        dee=input("ENTER faculty Id:")
        take_attendance(dee)
    elif ch2=='2':
        f_id=input("faculty id:")
        s_id=input("student id:")
        attendance_update(f_id,s_id)
    elif ch2=='3':
        f_id=input("faculty id:")
        s_id=input("student id:")
        calculate_attendance_percentage(f_id,s_id)
    else:
        print("incorrect choice")
cursor.close()
connection.close()
