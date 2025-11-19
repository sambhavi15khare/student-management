students = {}
logged_user = ''
logged = False
quiz_scores = {}

def register():
    global students
    
    print("--- Registration ---")
    
    username = input("Enter username: ")
    
    if username in students:
        print("Username already taken!")
        main()
        return
    
    password = input("Enter password: ")
    
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
    
    quiz_scores[username] = []
    
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

def quiz():
    global logged_user, logged, quiz_scores
    
    print("--- Quiz Module ---")
    
    if logged == False:
        print("Please login first!")
        main()
        return
    
    print("Welcome to Quiz!")
    print("Select subject:")
    print("1. Python Programming")
    print("2. Data Structures")
    print("3. Database Management")
    
    subject = input("Enter choice: ")
    
    score = 0
    total = 5
    
    if subject == '1':
        print("--- Python Programming Quiz ---")
        
        print("Q1. What is the output of print(2**3)?")
        print("a) 5")
        print("b) 6")
        print("c) 8")
        print("d) 9")
        ans1 = input("Your answer: ")
        if ans1 == 'c' or ans1 == 'C':
            score = score + 1
        
        print("Q2. Which keyword is used to create a function?")
        print("a) func")
        print("b) def")
        print("c) function")
        print("d) define")
        ans2 = input("Your answer: ")
        if ans2 == 'b' or ans2 == 'B':
            score = score + 1
        
        print("Q3. What is the correct file extension for Python?")
        print("a) .python")
        print("b) .pt")
        print("c) .py")
        print("d) .p")
        ans3 = input("Your answer: ")
        if ans3 == 'c' or ans3 == 'C':
            score = score + 1
        
        print("Q4. Which of these is a mutable data type?")
        print("a) tuple")
        print("b) string")
        print("c) list")
        print("d) int")
        ans4 = input("Your answer: ")
        if ans4 == 'c' or ans4 == 'C':
            score = score + 1
        
        print("Q5. What does len() function do?")
        print("a) Returns length")
        print("b) Returns type")
        print("c) Returns value")
        print("d) Returns index")
        ans5 = input("Your answer: ")
        if ans5 == 'a' or ans5 == 'A':
            score = score + 1
    
    elif subject == '2':
        print("--- Data Structures Quiz ---")
        
        print("Q1. Which data structure uses LIFO?")
        print("a) Queue")
        print("b) Stack")
        print("c) Array")
        print("d) Tree")
        ans1 = input("Your answer: ")
        if ans1 == 'b' or ans1 == 'B':
            score = score + 1
        
        print("Q2. Time complexity of binary search?")
        print("a) O(n)")
        print("b) O(log n)")
        print("c) O(n^2)")
        print("d) O(1)")
        ans2 = input("Your answer: ")
        if ans2 == 'b' or ans2 == 'B':
            score = score + 1
        
        print("Q3. Which uses FIFO principle?")
        print("a) Stack")
        print("b) Tree")
        print("c) Queue")
        print("d) Graph")
        ans3 = input("Your answer: ")
        if ans3 == 'c' or ans3 == 'C':
            score = score + 1
        
        print("Q4. What is a linked list node?")
        print("a) Data only")
        print("b) Pointer only")
        print("c) Data and pointer")
        print("d) Array")
        ans4 = input("Your answer: ")
        if ans4 == 'c' or ans4 == 'C':
            score = score + 1
        
        print("Q5. Root node in tree has?")
        print("a) No parent")
        print("b) No child")
        print("c) Two parents")
        print("d) One child")
        ans5 = input("Your answer: ")
        if ans5 == 'a' or ans5 == 'A':
            score = score + 1
    
    elif subject == '3':
        print("--- Database Management Quiz ---")
        
        print("Q1. SQL stands for?")
        print("a) Structured Query Language")
        print("b) Simple Query Language")
        print("c) Standard Query Language")
        print("d) System Query Language")
        ans1 = input("Your answer: ")
        if ans1 == 'a' or ans1 == 'A':
            score = score + 1
        
        print("Q2. Which command is used to retrieve data?")
        print("a) GET")
        print("b) SELECT")
        print("c) RETRIEVE")
        print("d) FETCH")
        ans2 = input("Your answer: ")
        if ans2 == 'b' or ans2 == 'B':
            score = score + 1
        
        print("Q3. Primary key is?")
        print("a) Duplicate allowed")
        print("b) NULL allowed")
        print("c) Unique identifier")
        print("d) Optional")
        ans3 = input("Your answer: ")
        if ans3 == 'c' or ans3 == 'C':
            score = score + 1
        
        print("Q4. DELETE command is used to?")
        print("a) Delete database")
        print("b) Delete table")
        print("c) Delete records")
        print("d) Delete column")
        ans4 = input("Your answer: ")
        if ans4 == 'c' or ans4 == 'C':
            score = score + 1
        
        print("Q5. Foreign key is used for?")
        print("a) Primary identification")
        print("b) Relationship between tables")
        print("c) Indexing")
        print("d) Sorting")
        ans5 = input("Your answer: ")
        if ans5 == 'b' or ans5 == 'B':
            score = score + 1
    
    else:
        print("Invalid subject!")
        main()
        return
    
    print("--- Quiz Complete ---")
    print("Your score:", score, "/", total)
    percentage = (score / total) * 100
    print("Percentage:", percentage, "%")
    
    if percentage >= 80:
        print("Grade: Excellent")
    elif percentage >= 60:
        print("Grade: Good")
    elif percentage >= 40:
        print("Grade: Average")
    else:
        print("Grade: Need Improvement")
    
    quiz_scores[logged_user].append({'subject': subject, 'score': score, 'total': total})
    
    main()

def view_quiz_history():
    global logged_user, logged, quiz_scores
    
    print("--- Quiz History ---")
    
    if logged == False:
        print("Please login first!")
        main()
        return
    
    if logged_user not in quiz_scores or len(quiz_scores[logged_user]) == 0:
        print("No quiz attempted yet!")
        main()
        return
    
    print("Your quiz history:")
    subject_names = {
        '1': 'Python Programming',
        '2': 'Data Structures',
        '3': 'Database Management'
    }
    
    for i in range(len(quiz_scores[logged_user])):
        quiz = quiz_scores[logged_user][i]
        sub_name = subject_names.get(quiz['subject'], 'Unknown')
        print(str(i+1) + ". Subject:", sub_name, "- Score:", quiz['score'], "/", quiz['total'])
    
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
        5. Take Quiz
        6. View Quiz History
        7. Logout
        8. Main Menu
        9. Exit
            select option 1/2/3/4/5/6/7/8/9: ''')
    
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
        view_quiz_history()
    elif response == '7':
        logout()
    elif response == '8':
        main()
    elif response == '9':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()

main()
