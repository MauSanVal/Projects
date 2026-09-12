from parser_poly import parse_polynomial
from dominio import dominio
from raices import raices_complejas
from derivadas import derivada
from extremos import maximos_minimos
from crecimiento import crecimiento_decrecimiento
from concavidad import concavidad
from grafica import graficar
from integral import integral_definida
import sympy as sp


def menu():
    print("\n=== ANALIZADOR DE POLINOMIOS ===")
    print("1. Dominio")
    print("2. Raíces")
    print("3. Derivada")
    print("4. Máximos y mínimos")
    print("5. Crecimiento y decrecimiento")
    print("6. Concavidad")
    print("7. Graficar")
    print("8. Integral definida")
    print("0. Salir")

if __name__ == "__main__":
 
    print("Introduce el polinomio:")
    entrada = input()

    poly = parse_polynomial(entrada)

    while True:

        menu()
        op = input("Opción: ")

        if op == "1":
            print(dominio())

        elif op == "2":
            sp.pprint(raices_complejas(poly))

        elif op == "3":
            sp.pprint(derivada(poly))

        elif op == "4":
            sp.pprint(maximos_minimos(poly))

        elif op == "5":
            sp.pprint(crecimiento_decrecimiento(poly))

        elif op == "6":
            sp.pprint(concavidad(poly))

        elif op == "7":
            graficar(poly)

        elif op == "8":
            sp.pprint(integral_definida(poly))

        elif op == "0":
            break

        else:
            print("Opción inválida")

