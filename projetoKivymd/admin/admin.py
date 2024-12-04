from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from pymongo import MongoClient

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # stb = {
        #     'TH0' : {0:'St0',1:'Sample1',2:'Sample2',3:'Sample4'},
        #     'TH1' : {0:'Stm0',1:'Sample1',2:'Sample2',3:'Sample4'},
        #     'TH2' : {0:'Stmp0',1:'Sample1.0',2:'Sample2.0',3:'Sample4.0'},
        #     'TH3' : {0:'Stmpl0',1:'Sample1',2:'Sample2',3:'Sample4'},
        #     'TH4' : {0:'Stmple0',1:'Sample1',2:'Sample2',3:'Sample4'},
        # }
    client = MongoClient()
    db = client.silverpos
    users = db.users

    for user in users.find():
         print(user['first_name'])
    
class AdminApp(App):
    def build(self):

        return AdminWindow()

if __name__ =='__main__':
    AdminApp().run()
