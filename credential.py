from credential import credential

class Credential:
    """
    this generates new  credential
    """

    account= [] # Empty account

    def __init__(self,account_name,account_password):

      
        self.account_name = account_name
        self.account_password = account_password
    def save_account(self):

        '''
        save_account  objects into account
        '''

        Credential.account.append(self)
    def delete_account(self):

        '''
        delete_account deletes a saved credential from the account
        '''

        credential.account.remove(self) 
