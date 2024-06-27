import os
os.system('cls' if os.name == 'nt' else 'clear')

#IMPORTAR CLASS LIBRO
from ClasesEspeciales import Libro

libro1 = Libro("Stephen King", "it", 1032)
print(len(libro1))


  