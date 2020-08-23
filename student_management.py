student_list = []


class Student:
    def __init__(self, first_name, last_name, email, password, p_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = p_number

    def full_data(self):
        print(self.first_name, self.last_name, self.email, self.password, self.phone_number)


def add_student():
    running = True
    while running:
        try:
            name, surname, email, tel, password = input(
                'prompt like :name surname email phone password').rstrip().split()
            student = Student(name, surname, email, tel, password)
            student_list.append(student)
        except:
            print("It's invalid operation")
            continue
        user_prompt = "Would you like to add student? type \"exit\" to quit"
        if user_prompt == "quit":
            running = False


def delete_student():
    student_password = input("enter student password to delete the profile : ")
    for id, in enumerate(password):
        if student_password == Student.password:
            print(f'Student {id} has been deleted. ')
            del student_list[id]

def all_students_data():
    pass



user_number = input("Enter user number : ")

if user_number.isdigit():
    user_number = int(user_number)
    for Student in range(0, user_number):
        first_name = input("Enter your name : ")
        student_list.append(first_name)
        last_name = input("Enter your surname : ")
        student_list.append(last_name)
        p_number = input("Enter your phone number (add +994) : ")
        student_list.append(p_number)
        if len(p_number) == 9:
            z = str("+994") + p_number
        else:
            print("Either number is incorrect or you have added 0 before prefix (e.g 051)")
        # email check etmek ucun :
        email = input("Enter your e-mail : ")
        student_list.append(email)
        loop0 = True
    while loop0:
        try:
            if "@" in email:
                print(email)
                student_list.append(email)
                break
            elif "@" not in email:
                print("You should attach \"@\" to your e-mail")
                break
        except "@" not in email:
            pass
    loop = True
    while loop:
        try:
            password = int(input("Enter your password : "))
            if 1000 > int(password) > 99:
                loop = False
                print(password)
            else:
                print("Enter value between 99 and 1000")
        except ValueError:
            print("Only numbers, please")
            continue
        if password < 0:
            print("Sorry, no negative numbers")

else:
    print("you have not entered a number")

choices = """
1) Add students to the list
2) Delete students from the list
3) All students
4) Exit
"""

while True:
    choice = input(choices)
    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        all_students_data()
    elif choice == "quit":
        break
