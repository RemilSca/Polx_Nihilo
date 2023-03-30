import pywebio
import pywebio_battery
from pywebio.input import input, FLOAT, input_group, NUMBER, PASSWORD, select, checkbox
from pywebio.output import put_text, put_row, put_code, put_buttons, clear, popup, remove, put_scope, put_image, toast, \
    put_column, put_table, put_grid, close_popup, use_scope, put_button
from pywebio import start_server, config
from pywebio.session import run_js
from pywebio_battery import get_cookie, set_cookie

def checklogin(u):
    l = get_cookie('login')
    p = get_cookie('passwd')
    if u.nick == l and u.passwd == p:
        return True
    else:
        return False

@config(theme="dark")
def cope():
    login = get_cookie('login')
    passwd = get_cookie('passwd')

    if login != None and passwd != None:
        u = mod.load(login)
        panel()
    else:
        loginf()

def register():
    info = input_group("Rejestracja", [
        input('Podaj Nick', name='name', required=True),
        input('Podaj Haslo', name='pswd', required=True, type=PASSWORD)
    ], cancelable=True)
    try:
        u = mod.User(info['name'], info['pswd'])

        if mod.save(u):
            popup('Nick w uzyciu!')
        else:
            clear()
            panel()
    except:
        pass

def loginf_vali(data):
    try:
        u = mod.load(data['name'])
    except:
        u = False

    if u == False:
        return ('name','Nie ma takiego konta!')
    elif u.passwd != data['pswd']:
        return ('pswd','Złe hasło!')

def loginf():
    info = input_group("Logowanie", [
        input('Podaj Nick', name='name', required=True),
        input('Podaj Haslo', name='pswd', required=True, type=PASSWORD)
    ],validate=loginf_vali)

    u = mod.load(info['name'])
    cuser = u
    set_cookie('login', info['name'])
    set_cookie('passwd', info['pswd'])
    run_js('window.location.reload()')

    clear()

if __name__ == '__main__':

    #<- losuje nowa postac na kolejny dzien i resetuje zgadywanie i resetuje streak jak ktos nie zgadl ,trzeba zrobic to zeby co dzien sie ta funkcja robila o jakies godzinie
    start_server(cope, port=8888, debug=True)


