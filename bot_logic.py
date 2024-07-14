import random

def gen_pass(pass_length):
    #elementos de la contraseña
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        #se eligen los caracteres que estaran en la contraseña y los pasa a "password"
        password += random.choice(elements)

    return password
