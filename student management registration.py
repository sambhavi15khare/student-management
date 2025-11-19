#student management system

students = {}
logged_user = ''
logged = False

def register():
    global students
    
    print("--- Registration ---")
    
    username = input("Enter username: ")
    
    # check if username already exists
    if username in students:
        print("Username already taken!")
        main()
        return
    
    password = input("Enter password: ")
    
    # get student details
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    dob = input("Date of Birth: ")
    gender = input("Gender: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    pincode = input("Pincode: ")
    enrollment = input("Enrollment Number: ")
    course = input("Course: ")
    branch = input("Branch: ")
    semester = input("Semester: ")
    
    # save student data
    students[username] = {
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'dob': dob,
        'gender': gender,
        'address': address,
        'city': city,
        'state': state,
        'pincode': pincode,
        'enrollment': enrollment,
        'course': course,
        'branch': branch,
        'semester': semester
    }
    
    print("Registration successful!")
    main()

def login():
    global logged_user, logged, students
    
    print("--- Login ---")
    
    if logged == True:
        print("Already logged in!")
        main()
        return
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # check username and password
    if username in students:
        if students[username]['password'] == password:
            logged_user = username
            logged = True
            print("Login successful!")
        else:
            print("Wrong password!")
    else:
        print("Username not found!")
    
    main()

def show_profile():
    global logged_user, logged, students
    
    print("--- Profile ---")
    
    if logged == False:
        print("Please login first!")
        main()
        return
    
    # get current user data
    data = students[logged_user]
    
    print("Username:", logged_user)
    print("Name:", data['first_name'], data['last_name'])
    print("Email:", data['email'])
    print("Phone:", data['phone'])
    print("DOB:", data['dob'])
    print("Gender:", data['gender'])
    print("Address:", data['address'])
    print("City:", data['city'])
    print("State:", data['state'])
    print("Pincode:", data['pincode'])
    print("Enrollment:", data['enrollment'])
    print("Course:", data['course'])
    print("Branch:", data['branch'])
    print("Semester:", data['semester'])
    
    main()

def update_profile():
    global logged_user, logged, students
    
    print("--- Update Profile ---")
    
    if logged == False:
        print("Please login first!")
        main()
        return
    
    print("What do you want to update?")
    print("1. Phone")
    print("2. Email")
    print("3. Address")
    print("4. City")
    print("5. Semester")
    print("6. Password")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        new_phone = input("Enter new phone: ")
        students[logged_user]['phone'] = new_phone
        print("Phone updated!")
    elif choice == '2':
        new_email = input("Enter new email: ")
        students[logged_user]['email'] = new_email
        print("Email updated!")
    elif choice == '3':
        new_address = input("Enter new address: ")
        students[logged_user]['address'] = new_address
        print("Address updated!")
    elif choice == '4':
        new_city = input("Enter new city: ")
        students[logged_user]['city'] = new_city
        print("City updated!")
    elif choice == '5':
        new_sem = input("Enter new semester: ")
        students[logged_user]['semester'] = new_sem
        print("Semester updated!")
    elif choice == '6':
        new_pass = input("Enter new password: ")
        students[logged_user]['password'] = new_pass
        print("Password updated!")
    else:
        print("Invalid choice!")
    
    main()

def logout():
    global logged_user, logged
    
    print("--- Logout ---")
    
    if logged == False:
        print("Not logged in!")
    else:
        logged_user = ''
        logged = False
        print("Logged out successfully!")
    
    main()

def terminate():
    print("Thank you!")
    exit()

def main():
    print("Welcome in LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit
            select option 1/2/3/4/5/6/7: ''')
    
    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        main()
    elif response == '7':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()

main()
