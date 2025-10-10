# features/store.py
from decimal import Decimal
from collections import defaultdict

class Book:
    def __init__(self, title, price, stock=0):
        self.title = title
        self.price = Decimal(price)
        self.stock = int(stock)

class User:
    def __init__(self, username, email=None, password=None):
        self.username = username
        self.email = email or f"{username}@example.com"
        self.password = password

class Store:
    def __init__(self):
        self.catalog = {}
        self.sent_emails = []

    def add_book(self, book: Book):
        self.catalog[book.title] = book

    def get_book(self, title):
        return self.catalog.get(title)

    def send_email(self, to, subject, body):
        self.sent_emails.append({'to': to, 'subject': subject, 'body': body})

class Cart:
    def __init__(self, store: Store):
        self.store = store
        # items: title -> quantity
        self.items = defaultdict(int)
        self.messages = []

    def add_book_by_title(self, title, qty=1):
        book = self.store.get_book(title)
        if not book:
            self.messages.append(f"Book '{title}' not found")
            return
        # If qty negative -> handle as invalid (ignore)
        if qty <= 0:
            self.messages.append(f"Invalid quantity {qty} for '{title}'")
            return
        # enforce stock
        allowed = min(qty, max(0, book.stock - self.items[title]))
        if allowed < qty:
            self.messages.append(f"Stock limit for '{title}': only {book.stock} available. Added {allowed}.")
        # add allowed quantity
        self.items[title] += allowed

    def remove_book_by_title(self, title):
        if title in self.items:
            del self.items[title]

    def total_items(self):
        return sum(self.items.values())

    def quantity_of(self, title):
        return self.items.get(title, 0)

    def total(self):
        total = Decimal('0.00')
        for title, qty in self.items.items():
            book = self.store.get_book(title)
            if book:
                total += book.price * qty
        return total.quantize(Decimal('0.00'))

    def empty(self):
        self.items = defaultdict(int)

    def checkout(self, user: User = None):
        # Apply stock limits: ensure no item exceeds stock, adjust and inform
        for title in list(self.items.keys()):
            book = self.store.get_book(title)
            if not book:
                continue
            if self.items[title] > book.stock:
                self.messages.append(f"Stock limit for '{title}': only {book.stock} added.")
                self.items[title] = book.stock

        # Compute total and discount: >3 books -> 10% discount
        total_books = self.total_items()
        total_amount = self.total()
        if total_books > 3:
            discount = (total_amount * Decimal('0.10')).quantize(Decimal('0.00'))
            total_amount = (total_amount - discount).quantize(Decimal('0.00'))
        # Negative quantities were prevented when adding; still guard
        if total_amount < Decimal('0.00'):
            total_amount = Decimal('0.00')

        # Simulate sending receipt email if user provided
        receipt = {
            'user': getattr(user, 'username', None),
            'total': total_amount,
            'items': dict(self.items)
        }
        if user:
            subject = f"Receipt for {user.username}"
            body = f"Thank you {user.username}. Your order: {receipt['items']} Total: {total_amount}"
            # Add each title to the body for tests that assert it
            self.store.send_email(user.email, subject, body)

        # Optionally clear cart after checkout
        # self.empty()
        return receipt
