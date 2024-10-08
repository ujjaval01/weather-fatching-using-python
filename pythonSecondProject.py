import time
import random
import string
import validators
import re
import csv

def is_valid_email(email):
    return validators.email(email)

def is_valid_pass(password):
 if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'[0-9]', password) and
    re.search(r'[@$!%*?&]', password)):
    return True
 return False

def generate_captcha():
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(5))
    return captcha

def registration():
    while True:
        email = input("Enter your email: ")
        if not is_valid_email(email):
            print("Enter a valid email, ends with '@gmail.com'")
            continue
        while True:
            password = input("Enter your password: ")
            if not is_valid_pass(password):
                print("Invalid password.\nEnter Again, It must be at least 8 characters long, include an uppercase letter, a lowercase letter, a digit, and a special character.")
                continue
            confirm_password = input("Confirm your password: ")
            if password == confirm_password:
                security_question = input("Enter security question: ")
                security_answer = input("Enter security answer: ")
                try:
                    with open("info.csv", 'a', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([email, password, security_question, security_answer])
                        print("Data written to csv successfully.")
                except Exception as e:
                    print("The error is- ", str(e))
                print("Registration successful")
                break  
            else:
                print("Passwords do not match")
        break
            

def login():
    attempts = 3
    while attempts > 0:
        email = input("Enter your email: ")
        password = input("Enter your Password: ")
            
        with open("info.csv", "r") as file:
            for line in file:
                data = line.strip().strip(",")
                # if len(data) !=4:
                #     print(f"skipped: {line}")
                #     continue
                eml, pwd, security_question,security_answer = data
            
                if email == eml and password == pwd:
                    pfun()
                    break
            else:
                print("Invalid email or password. Try again.")
                attempts -= 1
  
def exit_program():
    print("Exiting...")

def pfun():
        captcha = generate_captcha()
        print(f"CAPTCHA: {captcha}")
        entered_captcha = input("Enter the CAPTCHA: ")
        if entered_captcha == captcha:
            print("Login successful")
            return True
        else:
            print("Incorrect CAPTCHA. Try again.")
            attempts -= 1
            if attempts > 1:
                print(f"You have {attempts} remaining attempts. Try again.")
            elif attempts == 1:
                print(f"You have {attempts} remaining attempt. Try again.")
            else:
                print("You have exceeded the maximum number of attempts. Please try again after 30 minutes.")
                time.sleep(30 * 60) 
                return False
        return False

while True:
    print("1. Registration")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            registration()
        case 2:
            print
            login()
            
        case 3:
            exit_program()
            break
        case _:
            print("Invalid choice")
