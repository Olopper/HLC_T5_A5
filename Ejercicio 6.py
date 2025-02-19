class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []  

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo} de {libro.autor}")

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"{libro.titulo} - {libro.autor}")


biblio = Biblioteca()
biblio.agregar_libro(Libro("1984", "George Orwell"))
biblio.agregar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
biblio.mostrar_libros()
