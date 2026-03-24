import random
import string

words = {
"datos": ["entero", "float", "boole", "string"],
"conceptos": ["programa","variable","funcion","bucle","cadena"]
}  

guessed = []
attempts = 6
abc = string.ascii_letters
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()


for elem in words:                                                                       
    print("-", elem)

print()
# Verifica que el usuario ingrese la categoria
seleccion = input("Elegi una categoria: ").lower()
while True:                                                                 
    if seleccion in words.keys():
        break     
    else:
        print("Entrada no valida ")
        seleccion = input("Elegi una categoria(Escribe el nombre): ").lower()

coleccion = random.sample(words[seleccion],len(words[seleccion]))

print()
for word in coleccion:
    attempts = 6
    progress = ""
    guessed = []
    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        print()
        if len(letter) > 1 or not(letter in abc):
            print("Entrada no valida")
            continue
        print()
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            puntaje -= 1
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0
print()
print(f'Puntos obtenidos: {puntaje}')