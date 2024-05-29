# Importar los módulos necesarios para la ejecución del programa.
from Genre import GENRE
from datetime import datetime
class Book:
    def __init__(self,id,titulo,autor,NºPaginas,realease_date,genres = None):
        self.id=id
        self.titulo=titulo
        self.autor=autor
        self.NºPaginas=NºPaginas
        self.realease_date=realease_date
        self.genres=[]

    def get_id(self):
        if isinstance(self.id, int):
            return self.id
        else:
            raise TypeError("El id del libro debe ser un número entero.")
        
    def get_titulo(self):
        if isinstance(self.titulo, str):
            return self.titulo
        else:
            raise TypeError("El titulo del libro debe ser una cadena de caracteres.")
        
    def get_autor(self):
        if isinstance(self.autor, str):
            return self.autor
        else:
            raise TypeError("El nombre del autor debe ser una cadena de caracteres número.")
        
    def get_NºPaginas(self):
        if isinstance(self.NºPaginas, int):
            return self.NºPaginas
        elif self.NºPaginas <= 1:
            return ValueError("El numero de paginas del libro tiene que ser positivo.")
        else:
            raise TypeError("El numero de paginas del libro debe ser un numero entero.")
        
    def get_realease_date(self):
        if isinstance(self.realease_date, datetime):
            return self.realease_date
        # No puede ser una fecha futura
        elif self.realease_date > datetime.today():

            raise ValueError("La fecha de publicación no puede ser en el futuro.")
        else:
            raise TypeError("La fecha de publicación debe ser de módulo datetime.")
        
    def get_genres(self):
      if isinstance(self.genres, list):
        for genre in self.genres:
            if not isinstance(genre, GENRE):
                raise TypeError("Los elementos de la lista de géneros deben ser instancias de GENRE.")
        return self.genres
      else:
        raise TypeError("El género del libro debe ser una lista.")
    def set_titulo(self,titulo):
        self.titulo=titulo
    def set_autor(self,autor):
        self.autor=autor
    def set_NºPaginas(self,NºPaginas):
        self.NºPaginas=NºPaginas
    def set_id(self,id):
        self.id=id

    def add_genre(self, genero):#genero es otro tipo de genres de tipo GENRE
        # Si no es de tipo Genere no se añade
        if not isinstance(genero, GENRE):
            raise TypeError("Genre debe ser de módulo GENRE.")
        # Si el género no esta ya en generes se añade
        if genero not in self.genres:
            self.genres.append(genero)
    def __eq__(self, other):
        return(isinstance(other,Book) and
                self.titulo == other.titulo and
                self.autor == other.autor and
                self.realease_date == other.realease_date)
    def __str__(self) -> str:
        return f"{self.titulo} de {self.autor} con {self.NºPaginas} paginas"
    
        
    """Constructor of the class.

        The constructor of the class Book is used to create a new book.

        Syntax
        ------
          book = Book(id, title, author, pages, publication_date, genres)

        Parameters
        ----------
          id : int
            The unique identifier of the book.
          title : str
            The title of the book.
          author : str
            The author of the book.
          pages : int
            The number of pages of the book.
          publication_date : date
            The publication date of the book.
          genres : list
            The genres of the book.

        Returns
        -------
          The new book.

        Example
        -------
          book = Book(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [Genre.FANTASY])
        """
    
    # Realizar la implementación de la clase Book.

def main():
    """Function main of the module.

    The function main of this module is used to test the Class Book.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Book.")
    print("=================================================================.")
    book = Book(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])

    if book.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_title() == "Harry Potter":
        print("Test PASS. The parameter title has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_author() == "J.K. Rowling":
        print("Test PASS. The parameter author has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_pages() == 345:
        print("Test PASS. The parameter pages has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_publication_date() == date.today():
        print("Test PASS. The parameter publication_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_genres() == [GENRE.FANTASY]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    book2 = Book(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])

    if str(book2) == "J.K. Rowling escribió Harry Potter con 345 páginas.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(book2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(book2))


    print("=================================================================.")
    print("Test Case 3: book add_genre")
    print("=================================================================.")
    book2.add_genre(GENRE.FICTION)
    genres = book2.get_genres()
    if genres == [GENRE.FANTASY, GENRE.FICTION]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    book3 = Book(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])
    if book2 == book3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")

# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
