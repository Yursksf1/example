print('este es mi error')
import random
res = int(input('En que numero estoy pensando?'))
print('Numero pensado', res, "\n\n")

while True:
    ran = random.randint(1, 10)
    print('random', ran)
    if ran == res:
        break
print("Felicitaciones..Ganaste...se ha adivinado el numero ", res)
