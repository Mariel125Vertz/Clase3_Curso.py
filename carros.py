class Book:
    def __init__(self, modelo, año): #init constructor de la clase
        self.modelo = modelo 
        self.año = año
        self.available = True

    def tramite(self):
        if self.available:
            self.available = False
            print(f"El carro {self.modelo} esta en tramite de compra")
        else:
            print(f"El carro {self.modelo} no está disponible")
    
    def return_car(self):
        self.available = True
        print(f"El carro {self.modelo} ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.tramite()
            self.borrowed_books.append(book)
        else:
            print(f"El carro {book.modelo} no está disponible")

    def return_car(self, book):
        if book in self.borrowed_books:
            book.return_car()
            self.borrowed_books.remove(book)
        else:
            print(f"El carro {book.tmodelo} no está en la lista de ventas")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El carro {book.modelo} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El cliente {user.name} ha sido registrado")

    def show_available_books(self):
        print("Los carros que estan disponibles:")
        for book in self.books:
            if book.available:
                print(f"El carro {book.modelo} del año {book.año}")

# Crear carros
book1 = Book("BMW", "1950")
book2 = Book("FERRARI", "1589")
            
# Crear clientes
user1 = User("Mariel", "001")

# Crear biblioteca
library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.register_user(user1)

# Mostrar carros  disponibles
library1.show_available_books()

# Préstamo
user1.borrow_book(book1)

# Mostrar carror disponibles
library1.show_available_books()

# cancelar compra
user1.return_car(book1)

# mostrar  carros disponibles
library1.show_available_books()

