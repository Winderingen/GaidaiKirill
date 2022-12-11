import requests
import json
def JsoN():
    tab = name.get()
    res = requests.get('https://api.github.com/users/rust')
    _d_ = json.loads(res.text)
    e1 = dict.fromkeys(['company'], _d_['company'])
    e2 = dict.fromkeys(['created_at'], _d_['created_at'])
    e3 = dict.fromkeys(['email'], _d_['email'])
    e4 = dict.fromkeys(['id'], _d_['id'])
    e5 = dict.fromkeys(['name'], _d_['name'])
    e6 = dict.fromkeys(['url'], _d_['url'])
    jSON = e1,e2,e3,e4,e5,e6
    if tab == 'rust':
        with open('C:\\Users\\dirpu\\Desktop\\demichev_project\\vivod.json', 'w') as file:
            json.dump(jSON,file)        
    else:
        print(':(')
import tkinter as tk 
window = tk.Tk()
window.geometry('540x480')
window.title("Мой первый интерфейс:)") 
name = tk.Entry(window)
name.grid(padx=200, pady=15)
btn = tk.Button(window, text="project", command=JsoN)
btn.grid(padx=140, pady=15)
window.mainloop()
JsoN()