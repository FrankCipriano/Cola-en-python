#importamos la libreria
from collections import deque

#creamos la cola
cola = deque(["Frank","Yess","Chejo","Mary","Susy"])

#comprobamos el tipo de dato
print(type(cola))

#revisamos el contenido de la cola
print("\n\n",cola)

#Desencolar
cola.popleft()
print(cola)

#Encolar
cola.append("Yuli")
print(cola)