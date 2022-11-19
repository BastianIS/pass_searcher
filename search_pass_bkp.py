from datetime import datetime
inicio = datetime.now()
lista = "abc" #defghijklmnñopqrstuvwxyz"
clave = "bca"
contador_global = 0
#contador_for = 0
print(f"{inicio}\n--------------------\n")

#def proc(contador_for, contador_global, auxiliar):
def proc(contador_for, auxiliar):
    global contador_global
    print(f"\n*contador_for: {contador_for} / contador_global: {contador_global} / auxiliar: {auxiliar}*\n")
    if (contador_for != -1):
        contador_for += 1
        for x in auxiliar:
            for y in lista:
                contador_global += 1
                z = x + y
                print(f"{str(contador_global)} |{z}|")
                if(z == clave):
                    contador_for = -1
                    print("\n----------------------\n----Fin por z == clave\n--------------------\n")
                    return
                if(contador_global == 1000):
                    print("\n----------------------\n----Fin por contador_global == 1000\n--------------------\n")
                    return
        print(f"contador_global == len(lista) * len(auxiliar) = {contador_global} == {len(lista) * len(auxiliar)}")
        if(contador_global == len(lista) * len(auxiliar)):
            for a in lista:
                auxiliar = auxiliar + a
                print(f"\n*2*contador_for: {contador_for} / contador_global: {contador_global} / auxiliar: {auxiliar}*\n")
                #proc(contador_for, contador_global, auxiliar)
                proc(contador_for, auxiliar)
    else:
        print("\n----------------------\n----Fin por contador_for == -1\n--------------------\n")
        return

#proc(0, 0, None)
proc(0, "")

final = datetime.now()
print(f"{final}\n--------------------\n")
tarda = final - inicio

print(f"Tarda: {tarda}")