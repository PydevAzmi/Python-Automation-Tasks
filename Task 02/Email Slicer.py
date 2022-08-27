# Build an email slicer :
# create a function that takes an email as input 
# and retrieve the username and domain of the email


def email_slicer(email):
    email = email.split("@")
    return email[0],email[1]

user_name, domain_name = email_slicer(input("Entet Your Email \n>>"))
print(f"User Name : {user_name}\nDomain Name : {domain_name}")
