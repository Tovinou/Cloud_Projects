from models.book import Book

class Inventory:
    def __init__(self):
        self.books = {}  # book -> stock
        self.reserved = {}  # (book, cart_id) -> quantity
    
    def add_book(self, book, quantity):
        self.books[book] = quantity
    
    def find_book(self, title):
        for book in self.books.keys():
            if book.title == title:
                return book
        raise ValueError(f"Book '{title}' not found in inventory")
    
    def get_available_stock(self, book):
        total_reserved = 0
        for (reserved_book, _), quantity in self.reserved.items():
            if reserved_book == book:
                total_reserved += quantity
        return self.books.get(book, 0) - total_reserved
    
    def reserve_book(self, book, cart):
        total_stock = self.books.get(book, 0)
        if total_stock <= 0:
            return False, "Out of stock"

        current_in_cart = cart.get_quantity(book)
        if current_in_cart >= total_stock:
            return False, (
                f"Only {total_stock} copy available" if total_stock == 1 else f"Only {total_stock} copies available"
            )
        
        # Simulate reservation
        cart_id = id(cart)
        key = (book, cart_id)
        self.reserved[key] = self.reserved.get(key, 0) + 1
        return True, "Book added to cart"
    
    def release_reservation(self, book, cart):
        cart_id = id(cart)
        key = (book, cart_id)
        if key in self.reserved:
            if self.reserved[key] > 1:
                self.reserved[key] -= 1
            else:
                del self.reserved[key]