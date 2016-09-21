class Connection:

    def __init__(self):
        self.host = None
        self.credentials_user = None
        self.credentials_pass = None
        self.credentials_erase_on_connect = False

    def get_params(self):
        return {
            'host' : self.host,
        }

    def credentials(self):
        return {
            'username'         : self.credentials_user,
            'password'         : self.credentials_pass,
            'erase_on_connect' : self.credentials_erase_on_connect,
        }
