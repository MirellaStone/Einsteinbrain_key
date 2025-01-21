import random

print ("Hola! Soy Safetkey, tu generador de contraseñas seguras, actualmente hay hackers que deambulan por cualquier site web, así que vamos a luchar💪")

def llave (long):

    digitos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password = ""

    for i in range ( long ):
        password += random.choice(digitos)

    return password
