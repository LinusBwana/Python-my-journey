# magic methods - Dunder methods (double underscore) __init__ , __str__, __eq__
#                 They are automatically called by many of the python's build it operations
#                 They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}" # returns the string representations of the object

    def __eq__(self, other): #checks whether the two books have the same author and title
        return self.title == self.title and self.author == self.author

    def __lt__(self, other): #comparison.lower than
        return self.num_pages == self.num_pages

    def __add__(self, other): #addition
        return f"{self.num_pages + self.num_pages}pages"

    def __contains__(self, keyword): #check for searched keyword
        return keyword in f"{self.title}".lower() or keyword in self.author

    def __getitem__(self, key):
        if key == 'title'.capitalize():
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'nom_pages':
            return  self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("Utengano", "J. R. R", 310)
book2 = Book("The Sun Goes Down", "Wa Thiongo", 650)
book3 = Book("The River Between", "Wala bin Wala", 150)
book4 = Book("Utengano", "J. R. R", 980)

print(book3)
print(book1 == book4)
print(book1 < book4)
print(book1 + book4)
print(f"river".lower() in book3)
print(book1['title'.capitalize()]) #gets the title of the book1
print(book3['author'])
print(book3['video'])

