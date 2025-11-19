logged_user = ''
logged = False
students = {}

def register():
    global students
    print("STUDENT REGISTRATION")
    
    username = input("Enter Username: ")
    
    if username in students:
        print("Username already exists!")
        return
    
    password = input("Enter Password: ")
    full_name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    date_of_birth = input("Date of Birth: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    enrollment_number = input("Enrollment Number: ")
    course = input("Course: ")
    semester = input("Semester: ")
    
    students[username] = {
        'password': password,
        'full_name': full_name,
        'email': email,
        'phone': phone,
        'date_of_birth': date_of_birth,
        'address': address,
        'city': city,
        'state': state,
        'enrollment_number': enrollment_number,
        'course': course,
        'semester': semester
    }
    
    print("Registration successful!")

def login():
    global logged_user, logged
    print("STUDENT LOGIN")
    
    if logged == True:
        print("You are already logged in")
        return
    
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username in students and students[username]['password'] == password:
        logged_user = username
        logged = True
        print("Login successful!")
    else:
        print("Invalid username or password")

def show_profile():
    global logged_user, logged
    print("STUDENT PROFILE")
    
    if logged == False:
        print("Please login first")
        return
    
    student = students[logged_user]
    print("Username:", logged_user)
    print("Full Name:", student['full_name'])
    print("Email:", student['email'])
    print("Phone Number:", student['phone'])
    print("Date of Birth:", student['date_of_birth'])
    print("Address:", student['address'])
    print("City:", student['city'])
    print("State:", student['state'])
    print("Enrollment Number:", student['enrollment_number'])
    print("Course:", student['course'])
    print("Semester:", student['semester'])

def update_profile():
    global logged_user, logged
    print("UPDATE PROFILE")
    
    if logged == False:
        print("Please login first")
        return
    
    print("What do you want to update?")
    print("1. Full Name")
    print("2. Email")
    print("3. Phone Number")
    print("4. Date of Birth")
    print("5. Address")
    print("6. City")
    print("7. State")
    print("8. Course")
    print("9. Semester")
    print("10. Password")
    
    choice = input("Select option: ")
    
    student = students[logged_user]
    
    if choice == '1':
        new_value = input("Enter new Full Name: ")
        student['full_name'] = new_value
        print("Full Name updated")
    elif choice == '2':
        new_value = input("Enter new Email: ")
        student['email'] = new_value
        print("Email updated")
    elif choice == '3':
        new_value = input("Enter new Phone Number: ")
        student['phone'] = new_value
        print("Phone Number updated")
    elif choice == '4':
        new_value = input("Enter new Date of Birth: ")
        student['date_of_birth'] = new_value
        print("Date of Birth updated")
    elif choice == '5':
        new_value = input("Enter new Address: ")
        student['address'] = new_value
        print("Address updated")
    elif choice == '6':
        new_value = input("Enter new City: ")
        student['city'] = new_value
        print("City updated")
    elif choice == '7':
        new_value = input("Enter new State: ")
        student['state'] = new_value
        print("State updated")
    elif choice == '8':
        new_value = input("Enter new Course: ")
        student['course'] = new_value
        print("Course updated")
    elif choice == '9':
        new_value = input("Enter new Semester: ")
        student['semester'] = new_value
        print("Semester updated")
    elif choice == '10':
        old_password = input("Enter old password: ")
        if old_password == student['password']:
            new_password = input("Enter new password: ")
            student['password'] = new_password
            print("Password updated")
        else:
            print("Incorrect old password")
    else:
        print("Invalid choice")

def quiz():
    print("QUIZ SECTION")
    
    if logged == False:
        print("Please login first")
        return
    
    print("Select Subject:")
    print("1. Python")
    print("2. DSA")
    print("3. DBMS")
    
    subject = input("Enter choice (1/2/3): ")
    
    if subject == '1':
        file_name = "questions1.txt"
        subject_name = "Python"
    elif subject == '2':
        file_name = "questions2.txt"
        subject_name = "DSA"
    elif subject == '3':
        file_name = "questions3.txt"
        subject_name = "DBMS"
    else:
        print("Invalid choice")
        return
    
    print("Starting", subject_name, "Quiz...")
    
    score = 0
    total = 0
    
    file = open(file_name, "r")
    
    while True:
        question = file.readline()
        if not question:
            break
        
        print(question.strip())
        
        option_a = file.readline()
        print(option_a.strip())
        
        option_b = file.readline()
        print(option_b.strip())
        
        option_c = file.readline()
        print(option_c.strip())
        
        option_d = file.readline()
        print(option_d.strip())
        
        correct = file.readline().strip()
        
        ans = input("Your answer (a/b/c/d): ")
        
        if ans == correct:
            score = score + 1
            print("Correct!")
        else:
            print("Wrong! Correct answer is:", correct)
        
        total = total + 1
        print("")
    
    file.close()
    
    print("Quiz Completed!")
    print("Your score:", score, "out of", total)
    
    result_file = open("results.txt", "a")
    result_file.write(logged_user + " scored " + str(score) + " out of " + str(total) + " in " + subject_name)
    result_file.write("\n")
    result_file.close()

def logout():
    global logged_user, logged
    print("LOGOUT")
    
    if logged == False:
        print("You are not logged in")
    else:
        print("Logged out successfully")
        logged_user = ''
        logged = False

def terminate():
    print("Thank you for using LNCT Student System")
    exit()

def main():
    print("Welcome in LNCT")
    response = input('''Choose option:
1. Registration
2. Login
3. Profile
4. Update profile
5. Quiz
6. Logout
7. Main Menu
8. Exit
select option 1/2/3/4/5/6/7/8: ''')
    
    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        quiz()
    elif response == '6':
        logout()
    elif response == '7':
        main()
    elif response == '8':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()

main()
