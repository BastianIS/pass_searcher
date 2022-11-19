from datetime import datetime
tiempo_inicio = datetime.now()
lista = "abcde" #fghijklmnñopqrstuvwxyz"
clave = input("Clave: ")
cadena = None
auxiliar = ""
encontrado = False
contador_global = 0
largo_caracteres = len(lista)

#global lista, clave, cadena, auxiliar, encontrado, contador_global, largo_caracteres
if(auxiliar == clave):
    print("ENCONTRADO 0")
    encontrado = True
    
if(not encontrado):
    for x in lista:
        #auxiliar = cadena + x
        auxiliar = x
        contador_global += 1
        print(f"Intento #{contador_global}: {auxiliar}")
        if(auxiliar == clave):
            print("ENCONTRADO 1")
            encontrado = True
            break
    largo_caracteres -= 1

if(not encontrado):
    for x in lista:
        for y in lista:
            auxiliar = x + y
            contador_global += 1
            print(f"Intento #{contador_global}: {auxiliar}")
            if(auxiliar == clave):
                print("ENCONTRADO 2.1")
                encontrado = True
                break
        if(encontrado):
            print("ENCONTRADO 2.2")
            break
    largo_caracteres -= 1

if(not encontrado):
    for x in lista:
        for y in lista:
            for z in lista:
                auxiliar = x + y + z
                contador_global += 1
                print(f"Intento #{contador_global}: {auxiliar}")
                if(auxiliar == clave):
                    print("ENCONTRADO 3.1")
                    encontrado = True
                    break
            if(encontrado):
                print("ENCONTRADO 3.2")
                break
        if(encontrado):
            print("ENCONTRADO 3.3")
            break
    largo_caracteres -= 1

tiempo_final = datetime.now()
tarda = tiempo_final - tiempo_inicio
print(f"\nClave: {clave}")
print(f"Auxiliar: {auxiliar}")
print(f"Tardó: {tarda}")
print(f"Intentos: {contador_global}")
print(f"Caracteres restantes: {largo_caracteres}")