# Start copying user functions from blablo here
class User:
    def __init__(self,url,get,post):
        self.url    =   url
        self.get    =   get
        self.post   =   post
        self.response    =   {'output':str(url)+str(get)+str(post),'status':200}

    def run(self):
       
        return self.response