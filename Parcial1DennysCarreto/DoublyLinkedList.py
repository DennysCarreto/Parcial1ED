from Node import Nodo


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empy(self):
        return self.head is None and self.tail is None

    # INSERTAR
    def insertar_inicio(self, dato):
        newNode = Nodo(dato)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            self.head.next = self.head
            self.head.prev = self.tail
            self.size += 1
        else:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode
            self.size += 1
    # Insertar en una posicion / insertar en un indice
    def insertar_indice(self, indice, dato):
        newNode = Nodo(dato)
        if indice < 0:
            print("El indice no puede ser negativo.")
            return
        if indice == 0:
            self.insertar_inicio(dato)
            return

        contador = 0
        actual = self.head
        while contador < indice - 1:
            actual = actual.next
            contador += 1

            if actual == self.head:
                print("El indice esta fuera de rango")
                return

        siguiente_nodo = actual.next
        actual.next = newNode
        newNode.prev = actual
        newNode.next = siguiente_nodo
        siguiente_nodo.prev = newNode


    # IMPRIMIR LISTA
    def printList(self):
        if not self.head:
            return
        actual = self.head
        while actual:
            print(actual.dato, end ='->')
            actual = actual.next
            if actual == self.head:
                break
        print()

    # ELIMINAR
    def eliminar(self, dato):
        if not self.head:
            return
        actual = self.head
        while actual.dato != dato:
            actual = actual.next
            if actual == self.head:
                return
        if actual == self.head:
            self.head = actual.next
            self.tail.next = self.head
            self.head = actual.next
            self.tail.next = self.head
            self.head.prev = self.tail

        elif actual == self.tail:
            self.tail = actual.prev
            self.tail.next = self.head
            self.head.prev = self.tail

        else:
            actual.prev.next = actual.next
            actual.next.prev = actual.prev
        self.size -= 1

    def recorrerOperar(self, x):
        if not self.head:
            print("La lista está vacía")
            return
        total = 0
        nodo_actual = self.head
        posicion = 1
        while True:
            resultado = nodo_actual.dato * (pow(x,posicion))
            total += resultado
            print(f"Dato en posición {posicion}: {nodo_actual.dato}, resultado: {resultado}")
            nodo_actual = nodo_actual.next
            posicion += 1
            if nodo_actual == self.head:
                break
        print("Resultado: ", total)

    # ACTUALIZAR
    def actualizar(self, dato_viejo, dato_nuevo):
        if not self.head:
            return

        actual = self.head
        while actual.dato != dato_viejo:
            actual = actual.next
            if actual == self.head:
                return

        actual.dato = dato_nuevo

    # BUSCAR
    def buscar(self, dato):
        if not self.head:
            return None

        actual = self.head
        while actual.dato != dato:
            actual = actual.next
            if actual == self.head:
                return None

        return actual.dato