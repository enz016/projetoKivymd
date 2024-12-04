from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Usuário e/ou senha não deve estar vazio![/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Logado com sucesso![/color]'
            else: 
                info.text = '[color=#FF0000]Usuário e/ou senha inválido![/color]'
class SigninApp(App):
    def build(self):
        return SigninWindow()
    
if __name__ == "__main__":
    sa = SigninApp()
    sa.run()
