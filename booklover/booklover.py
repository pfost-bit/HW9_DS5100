import pandas as pd

class BookLover: 
    # Constructor 
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name 
        self.email = email 
        self.fav_genre = fav_genre 
        self.num_books = num_books 
        self.book_list = book_list 
    
    # Add Book Method 
    def add_book(self, book_name, book_rating):
        """
        A method to add a book, takes as an input, a new book and its associated rating. 
        If the book is already in the list, throws an error.
        Args: 
            book_name: str
            book_rating: int
        """
        if book_name in self.book_list["book_name"].values: 
            raise ValueError(f"{book_name}: already in list") 
        else: 
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]}) 
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1 
    
    # Has Read Method
    def has_read(self, book_name): 
        """
        A method to determine if a book has already been read. 
        Returns True if read, false otherwise.
        Args: 
            book_name: str
        """
        return book_name in self.book_list["book_name"].values

    # Number of Books Read Method
    def num_books_read(self): 
        """
        A method to return the number of books read.
        Returns:
            num_books: int
        """
        return self.num_books
    
    # Favorite Books Method
    def fav_books(self): 
        """
        A method to return the user's favorite books, which are books with a rating greater than 3.
        Returns:
            fav_books: DataFrame
        """
        return self.book_list[self.book_list.book_rating > 3]

if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    print(test_object.book_list)
    print(test_object.has_read("War of the Worlds"))
    print(test_object.num_books_read())
    test_object.add_book("Fever Pitch", 3)
    test_object.add_book("Crime and Punishment", 5)
    test_object.add_book("The Great Gatsby",2)
    print(test_object.num_books_read())
    print(test_object.fav_books())