import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

DATA_FILE = "library_data.json"

class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        b = Book(data['book_id'], data['title'], data['author'], data['total_copies'])
        b.available_copies = data['available_copies']
        return b


class IssueRecord:
    def __init__(self, user, book_id, issue_date=None, return_date=None):
        self.user = user
        self.book_id = book_id
        self.issue_date = issue_date or datetime.now().strftime("%Y-%m-%d")
        self.return_date = return_date

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return IssueRecord(data['user'], data['book_id'], data['issue_date'], data['return_date'])


class Library:
    def __init__(self):
        self.books = {}
        self.issues = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                self.books = {k: Book.from_dict(v) for k, v in data.get('books', {}).items()}
                self.issues = [IssueRecord.from_dict(i) for i in data.get('issues', [])]

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump({
                'books': {k: v.to_dict() for k, v in self.books.items()},
                'issues': [i.to_dict() for i in self.issues]
            }, f, indent=4)

    def add_book(self, book_id, title, author, copies):
        if book_id in self.books:
            self.books[book_id].total_copies += copies
            self.books[book_id].available_copies += copies
        else:
            self.books[book_id] = Book(book_id, title, author, copies)
        self.save_data()

    def search_book(self, keyword):
        return [b for b in self.books.values() if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]

    def issue_book(self, user, book_id):
        if book_id not in self.books:
            return "Book not found"
        book = self.books[book_id]
        if book.available_copies > 0:
            book.available_copies -= 1
            self.issues.append(IssueRecord(user, book_id))
            self.save_data()
            return "Book issued"
        return "No copies available"

    def return_book(self, user, book_id):
        for record in self.issues:
            if record.user == user and record.book_id == book_id and record.return_date is None:
                record.return_date = datetime.now().strftime("%Y-%m-%d")
                self.books[book_id].available_copies += 1
                self.save_data()
                return "Book returned"
        return "Record not found"


class LibraryGUI:
    def __init__(self, root):
        self.lib = Library()
        self.root = root
        self.root.title("Library Management System")

        tk.Button(root, text="Add Book", width=20, command=self.add_book).pack(pady=5)
        tk.Button(root, text="View Books", width=20, command=self.view_books).pack(pady=5)
        tk.Button(root, text="Search Book", width=20, command=self.search_book).pack(pady=5)
        tk.Button(root, text="Issue Book", width=20, command=self.issue_book).pack(pady=5)
        tk.Button(root, text="Return Book", width=20, command=self.return_book).pack(pady=5)
        tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=5)

    def add_book(self):
        book_id = simpledialog.askstring("Input", "Book ID:")
        title = simpledialog.askstring("Input", "Title:")
        author = simpledialog.askstring("Input", "Author:")
        copies = simpledialog.askinteger("Input", "Copies:")
        if book_id and title and author and copies:
            self.lib.add_book(book_id, title, author, copies)
            messagebox.showinfo("Success", "Book added")

    def view_books(self):
        text = "\n".join([f"{b.book_id} | {b.title} | {b.author} | {b.available_copies}/{b.total_copies}" for b in self.lib.books.values()])
        messagebox.showinfo("Books", text if text else "No books available")

    def search_book(self):
        keyword = simpledialog.askstring("Search", "Enter keyword:")
        results = self.lib.search_book(keyword) if keyword else []
        text = "\n".join([f"{b.title} by {b.author}" for b in results])
        messagebox.showinfo("Results", text if text else "No results")

    def issue_book(self):
        user = simpledialog.askstring("Input", "User name:")
        book_id = simpledialog.askstring("Input", "Book ID:")
        if user and book_id:
            result = self.lib.issue_book(user, book_id)
            messagebox.showinfo("Info", result)

    def return_book(self):
        user = simpledialog.askstring("Input", "User name:")
        book_id = simpledialog.askstring("Input", "Book ID:")
        if user and book_id:
            result = self.lib.return_book(user, book_id)
            messagebox.showinfo("Info", result)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.geometry("300x300")
    root.mainloop()