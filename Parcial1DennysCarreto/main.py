from DoublyLinkedList import DoublyLinkedList


polinomioA = DoublyLinkedList()
polinomioB = DoublyLinkedList()

polinomioA.insertar_inicio(10)
polinomioA.insertar_inicio(18)
polinomioA.insertar_inicio(3)

polinomioB.insertar_inicio(25)
polinomioB.insertar_inicio(0)
polinomioB.insertar_inicio(4)
polinomioB.insertar_inicio(-17)

while True:
    print('Menu de navegacion')
    print('1 Ingresar componentes a un polinomio')
    print('2 Adicion y sustraccion')
    print('3 Evaluar polinomios')
    print('4 Visualizar polinomios')
    print('5 Salir')
    opcion = int(input('Eliga una ocpion: '))
    if opcion == 1:
        print('Ingrese el coeficiente: ')
        dato = int(input())
        print('En que polinomio desea insertar el nuevo componente?')
        print('Polinomio A')
        print('Polinimio B')
        print('Elija(a|A / b|B): ')
        poli = input()
        if poli == 'a' or poli == 'A':
            # Ingresar el dato al inicio de la lista A
            polinomioA.insertar_inicio(dato)
            print('Polinomio A Actualizado ')
            polinomioA.printList()
        elif poli == 'b' or poli == 'B':
            # Ingresar el dato al inicio de la lista B
            polinomioB.insertar_inicio(dato)
            print('Polinomio B Actualizado ')
            polinomioB.printList()

    elif opcion == 2:
        print('**** Operaciones ****')
        print('1 Suma')
        print('2 Resta')
        opera = int(input('Eliga una ocpion: '))
        if opera == 1:
            # Sumar los polinomios
            ListaC = DoublyLinkedList()
            print('Adicion y Sustraccion')
            current_a = polinomioA.tail
            current_b = polinomioB.tail
            cont = 0
            while cont >= 0:
                if current_a.prev != polinomioA.tail:
                    if current_b.prev != polinomioB.tail:
                        new = current_a.dato + current_b.dato
                        cont -= 1
                        current_a = current_a.prev
                        current_b = current_b.prev
                        ListaC.insertar_inicio(new)
                    if current_b.prev == polinomioB.tail:
                        new = current_a
                        cont -= 1
                        current_a = current_a.prev
                        ListaC.insertar_inicio(new)
                if current_b is not None:
                    new = current_b
                    cont -= 1
                    current_b = current_b.prev
                    ListaC.insertar_inicio(new)
            ListaC.printList()
        elif opera == 2:
            # Restar los polinomios
            pass

    elif opcion == 3:
        resultado = 0
        print('Ingrese el valor de X para evaluar: ')
        valorX = int(input())
        print('Polinomio a evaluar? (a|A / b|B): ')
        poli = input()
        if poli == 'a' or poli == 'A':
            # Evaluar valor x en polinomio A
            polinomioA.recorrerOperar(valorX)
        elif poli == 'b' or poli == 'B':
            # # Evaluar valor x en polinomio B
            pass

    elif opcion == 4:
        if polinomioA.is_empy() and polinomioB.is_empy():
            print('Polinomios vacios')
        else:
            # Mostar estado de los polinomios
            print('Polinomio A ')
            polinomioA.printList()
            print('Polinomio B ')
            polinomioB.printList()

    elif opcion == 5:
        print("¡Hasta luego!")
        break

    else:

        print("Opción inválida. Por favor, seleccione una opción válida.")