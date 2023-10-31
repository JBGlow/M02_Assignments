""" 
###Program Author: ###
#John Bigelow

###Program Name: ###
#GPA Tester v1.0

###Program Description: ###
#Program asks for student last and first name, then GPA.
#Entering zzz or ZZZ as last name will end the program
#If GPA is greater or equal to 3.5, a message about making the Dean's List will be printed.
#If GPA is greater or equal to 3.2, a message about making honor roll will be printed.
#It's possible to get both messages, as they are not mutually exclusive.

###Variables: ###
student_lname: a string, which will contain the student's last name
student_fname: a string, which will contain the student's first name
student_GPA: a float, which will contain the student's GPA

"""


#Asks for student last name
student_lname = input("Input student last name: ")

#Ends program if ZZZ had been entered for student last name
if student_lname == 'ZZZ' or student_lname == 'zzz':
    print('Ending program process.')
    exit()

#Asks for student first name
student_fname = input("Input student first name: ")

#Asks for student GPA
student_GPA = float(input("Input student GPA: "))

#Dean's list prompt if GPA is 3.5 or greater
if student_GPA >= 3.5:
    print(str(student_fname + " " + student_lname + " has made the dean's list."))

#Dean's list prompt if GPA is 3.25 or greater
if student_GPA >= 3.25:
    print(str(student_fname + " " + student_lname + " has made the honor roll."))