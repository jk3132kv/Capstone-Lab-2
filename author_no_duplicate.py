class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if title in self.books:
            print(f"Error: {title} has already been published by {self.name}")
        else:
            self.books.append(title)

    def __str__(self):
        books_list = ', '.join(self.books)
        return f"{self.name} has published: {books_list}"

def main():
    author1 = Author("John Smith")
    author2 = Author("Jane Doe")

    author1.publish("Book1")
    author1.publish("Book2")
    author1.publish("Book1") # this will be rejected as the book already exists in the list
    author2.publish("Book3")
    author2.publish("Book4")

    print(author1)
    print(author2)

if __name__ == "__main__":
    main()
