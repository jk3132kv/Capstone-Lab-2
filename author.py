class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        books_list = ', '.join(self.books) or 'No books'
        return f"{self.name} has published: {books_list}"

def main():
    author1 = Author("John Smith")
    author2 = Author("Jane Doe")

    author1.publish("Book1")
    author1.publish("Book2")
    author2.publish("Book3")
    author2.publish("Book4")

    print(author1)
    print(author2)

if __name__ == "__main__":
    main()
