# Task: Create 2 functions ,
#   the first one takes text as input,replaces each letter
#       with another letter, and outputs the “encoded” message.
#   the second one decode the message to the original text  

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


def coder(msg:str, shift, De_or_En):
    out_msg = ''
    if De_or_En == 1:
        shift = -shift
    for _ in msg:
        if _ == " ":
            out_msg += " "
        else:
            x = Letters.index(_)
            x += shift
            out_msg += Letters[x]
    return "Result >>> " + out_msg


print("Welcom To My Code Generator Game")

while True:     
    try:
        org_msg = input("Enter your message here....\n>>").lower()
        code  = int(input("Use What ?\n\t1-Decode\n\t2-Encode\n>>"))
        shift = int(input("Enetr Shift Amount\n>>"))
        if code ==1 and shift in range(10) :
            print(coder(org_msg, shift, code))
        elif code == 2 and shift in range(10):
            print(coder(org_msg, shift, code))
        else :
            print("Please Enter 1 for Decoding or 2 for Encoding with shift amount between [1 : 9] ")
    except Exception:
        print(Exception)
        
        
    finally:
        again = input("-----------------------------------------------\nDo you want to try it again ? y / n\n>>").lower()
        if again[0] == 'n':
            break
        print("------------------ New Start ------------------")
