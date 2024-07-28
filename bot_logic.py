import random, requests

def gen_pass(pass_length):
    #elementos de la contraseña
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        #se eligen los caracteres que estaran en la contraseña y los pasa a "password"
        password += random.choice(elements)

    return password

def imagenes_de_perros():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
#funcion para solicitar imagenes de patos

def get_duck():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]

#link de los videos
videos = [
        "https://www.youtube.com/watch?v=QrAta9gqYNQ&t=25s",
        "https://www.youtube.com/watch?v=6_zxPQuK1PY",
        "https://www.youtube.com/watch?v=uBMW8QM_iSI"
]
#funcion  que elige 1 de los 3 videos
def videos_choice():
    return random.choice(videos)
