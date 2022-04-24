import unittest
from user import user
import pyperclip

class Testuser(unittest.TestCase):

    def setUp(self):

        """Set up to run before each test cases.
        """

        self.new_user = user("Gabriel","Ndolo","geb888")

    def test_init(self):

        """_test_init  test if the object is initialized 
        """
        self.assertEqual(self.new_user.first_name,"Gabriel")
        self.assertEqual(self.new_user.last_name,"Ndolo")
        self.assertEqual(self.new_password,"geb888")
    def test_save_user(self):
        '''
        test_save_user test if the user  is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(user.user_list),1)
