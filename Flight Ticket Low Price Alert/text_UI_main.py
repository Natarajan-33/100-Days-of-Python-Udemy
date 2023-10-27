# import sheety
#
# print(
#     "Welcome to Natarajan's Filght Club.\nWe find the best flight deals and email you."
# )
# first_name = input("what is your first name?\n").title()
# # print(first_name)
# last_name = input("what is your last name?\n").title()
#
# email=None
# def get_email():
#   global email
#   email = input("what is your email?\n").lower()
#   if email=="exit" or email=="quit" :
#     exit()
#
#   reenter_email = input("Type your email again.\n").lower()
#   if reenter_email=="exit" or reenter_email=="quit":
#     exit()
#   elif email == reenter_email and email.strip()!="":
#     return True
#   else:
#     print("Email does not match. Please reenter both")
#     return get_email()
#
#
# is_correct_email = get_email()
# if is_correct_email:
#   sheety.post_new_row(first_name, last_name, email)
#   print("You're in the club!")


import sheety

print("Welcome to Natarajan's Flight Club.\n \
We find the best flight deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

print("OK. You're in the club!")

sheety.post_new_row(first_name, last_name, email1)

