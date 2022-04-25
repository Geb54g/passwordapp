from user import User

class Credential(User):
    """
    this generates new  credential
    """

    account= [] # Empty account

    def __init__(self,username,user_password,credential_name,password):
        super().__init__(username,user_password)
        

      
        self.credential_name = credential_name
        self.password = password
    def save_account(self):

        '''
        save_account  objects into account
        '''

        Credential.accounts.append(self)
    def delete_account(self):

        '''
        delete_account deletes a saved credential from the account
        '''

        Credential.accounts.remove(self) 
    @classmethod
    def display_accounts(cls):
        for account in cls.accounts:
            return cls.accounts

    @classmethod
    def find_by_number(cls,number):
        
        for account in cls.accounts:
            if account.accountusername == number:
                return account