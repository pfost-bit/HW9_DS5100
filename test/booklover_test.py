import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        """ 
        add a book and test if it is in `book_list`. 
        """
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #create test object
        test_object.add_book("War of the Worlds", 4) #add a book
        print(test_object.book_list) #show its in the list
        
        self.assertIn("War of the Worlds", test_object.book_list.book_name.values) #Test it is in the list

    def test_2_add_book(self):
        """
        add the same book twice. Test if it's in `book_list` only once.
        """
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #create test object
        test_object.add_book("War of the Worlds", 4) # add a book
        
        self.assertEqual(len(test_object.book_list), 1) #test that it was added
        
        # Check if adding the same book raises ValueError
        with self.assertRaises(ValueError):
            test_object.add_book("War of the Worlds",4)
            
        print(test_object.book_list) # show the book_list is only length 1
            
    def test_3_has_read(self): 
        """ 
        pass a book in the list and test if the answer is `True`.
        """
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #create test object
        test_object.add_book("War of the Worlds", 4)  # add a book
        
        self.assertTrue(test_object.has_read("War of the Worlds")) #test that has_read evaluates to true
        
    def test_4_has_read(self): 
        """
        pass a book NOT in the list and use `assert False` to test the answer is `True`
        """
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #create test object
        test_object.add_book("War of the Worlds", 4)  # add a book

        self.assertFalse(test_object.has_read("Crime and Punishment")) #test that has_read evaluates to false
        
        
    def test_5_num_books_read(self): 
        """
        add some books to the list, and test num_books matches expected.
        """
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #create test object
        test_object.add_book("War of the Worlds", 4)  # add a bunch of books
        test_object.add_book("Crime and Punishment",5)
        test_object.add_book("Fever Pitch", 3)
        test_object.add_book("The Great Gatsby", 2)
        
        self.assertEqual(len(test_object.book_list), test_object.num_books) # test to see if the the expected value (len of the book_list) == num_books
        
        
        

    def test_6_fav_books(self):
        """
        add some books with ratings to the list, making sure some of them have rating > 3. 
        The test should check that the returned books have rating  > 3
        """

        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #create test object
        test_object.add_book("War of the Worlds", 4)  # add a bunch of books
        test_object.add_book("Crime and Punishment",5)
        test_object.add_book("Fever Pitch", 3)
        test_object.add_book("The Great Gatsby", 2)
        
        fav_list = test_object.fav_books() # create a pd.Dataframe of the fav books
        
        print(fav_list) # print them 
        
        self.assertTrue((fav_list["book_rating"] > 3).all()) #using the .all() function check to see if the book_rating is >3 for all books in fav list
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
