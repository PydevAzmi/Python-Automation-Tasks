# Random Password Generator :
# create a function that generates a random password, 
# the password must be +7 letters,
# should contain numbers upper case letter ,
# small letter and _ only
import random
import string
def random_password_generator(length):
    characters =[list(string.digits),
                 list(string.ascii_lowercase),
                 list(string.ascii_uppercase),
                 ["!", "@", "#", "$", "%", "&", "*", "(", ")"],
                 ["_","_"]]
    if length > 7 :
        password = []
        for i in range(length):
            char_type = random.randint(0, len(characters)-1)
            char_index = random.randint(0, len(characters[char_type])-1)
            password.append(random.choice(characters[char_type][char_index]))
            # for preventing recurrent 
            characters[char_type].pop(char_index)
            # for only one select of "_"
            if char_type == 3 :
                characters.pop(-1)
        random.shuffle(password)
        return "".join(password)


length = int(input("Enter password length: "))   
print(f"Your Password :{random_password_generator(length)}")

