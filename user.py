
class User:
    """
    this generates new  users.
    """

    userslist = [] # Empty user list

    def __init__(self,username,user_password):

      
        self.username = username
        self.user_password = user_password
    def save_user(self):

        '''
        save_user  objects into user_list
        '''

        User.userslist.append(self)
    def delete_user(self):

        '''
        delete_user  deletes a saved user from the user_list
        '''

        User.userslist.remove(self) 

    @classmethod
    def display_users(cls):
        '''
        this gives back the user list
        '''
        return cls.userslist
    @classmethod
    def find_by_number(cls,number):
        '''.username is returned if it matches the isalnum
        '''

        for user in cls.userslist:
            if user.password == number:
                return user
    @classmethod
    def user_exist(cls,number):
        for user in cls.userslist:
            if user.username == number:
                return True
                return false
        