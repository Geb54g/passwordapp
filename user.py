from user import user

class User:
    """
    this generates new  users.
    """

    user_list = [] # Empty user list

    def __init__(self,first_name,last_name,number,password):

      
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.password = password
    def save_user(self):

        '''
        save_user  objects into user_list
        '''

        User.user_list.append(self)