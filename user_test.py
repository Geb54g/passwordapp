import unittest
from user import user
import pyperclip

class Testuser(unittest.TestCase):

    def setUp(self):

        """Set up method to run before each test cases.
        """

        self.new_user = user("Gabriel","Ndolo","geb888")

    def test_init(self):

        """_sutest_init test case to test if the object is initialized properlymmary_
        """
        self.assertEqual(self.new_user.first_name,"Gabriel")
        self.assertEqual(self.new_user.last_name,"Ndolo")
        self.assertEqual(self.new_password,"geb888")
    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(user.user_list),1)
