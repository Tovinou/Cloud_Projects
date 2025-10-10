class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_book(self, book):
        if book in self.items:
            self.items[book] += 1
        else:
            self.items[book] = 1
    
    def remove_book(self, book):
        if book in self.items:
            if self.items[book] > 1:
                self.items[book] -= 1
            else:
                del self.items[book]
    
    def get_total_quantity(self):
        return sum(self.items.values())
    
    def get_total_price(self):
        total = 0
        for book, quantity in self.items.items():
            total += book.price * quantity
        return total
    
    def get_discount_percentage(self):
        total_quantity = self.get_total_quantity()
        if total_quantity >= 4:
            return 10
        return 0
    
    def get_final_price(self):
        total = self.get_total_price()
        discount = self.get_discount_percentage()
        return total * (100 - discount) // 100
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clear(self):
        self.items.clear()
    
    def get_quantity(self, book):
        return self.items.get(book, 0)