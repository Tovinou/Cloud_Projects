class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
    
    def __hash__(self):
        return hash((self.title, self.author))
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"