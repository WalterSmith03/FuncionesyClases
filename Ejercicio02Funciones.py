import os
os.system('cls' if os.name == 'nt' else 'clear')

def letras_unicas(palabra):
    return sorted(set(palabra.lower()))

print(letras_unicas("PANZER"))
print("")
print(letras_unicas("SISTEMAS"))
print("")
print(letras_unicas("ACORAZADO"))
print("")
