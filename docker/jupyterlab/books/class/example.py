import time
from base import Auto_Client

class Example(Auto_Client):
    def __init__(self, url='https://www.google.com/', domain='https://www.google.com'):
        super().__init__(url, domain)
    
    def execGoogleSearch(self):
        self.sendkey_by_elmName('q', 'selenium')
        self.submit()
        time.sleep(1)
        self.SaveScreenShot('/content/', 'result.png')