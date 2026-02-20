import os

# Solicita al usuario si desea apagar el sistema
shutdown = input("Shutdown? (Si / No: ) ")

# Si la respuesta es "no", el programa termina sin hacer nada
if shutdown == "no":
    exit
else:
    # Si la respuesta no es "no" (asumimos que es "si"), apaga el sistema
    os.system("Shutdown /s /f /t 1")