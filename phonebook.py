from tkinter import *
from tkinter.ttk import *
import pandas as pd
import subprocess
import os


big_data = pd.read_csv("big_data.csv")


phones = big_data["phone"].values.tolist()
fio = big_data["fio"].values.tolist()
sex = big_data["sex"].values.tolist()
born = big_data["born_date"].values.tolist()
message_p = big_data["message"].values.tolist()


class Application():
    def __init__(self):
        self.window = Tk()
        self.window.title("Телефонный справочник")
        self.window.iconphoto(False, PhotoImage(file="icon.png"))
        self.window.geometry("900x400")
        self.window.resizable(False, False)
        self.create_widgets()
        self.create_label()
        self.create_menu()
        self.window.mainloop()

    def create_widgets(self):
        self.entry_data = Treeview(self.window, columns = ["Имя", "Номер телефона"], show = "headings")
        
        self.entry_data.heading("Имя", text = "Имя")
        self.entry_data.heading("Номер телефона", text = "Номер телефона")
        self.entry_data.place(x = 10, y = 10)

        for i in range(len(phones)):
            self.entry_data.insert("", END, values = [fio[i], phones[i]])

        self.entry_name = Text(self.window, width = 40, height = 2, wrap = WORD)
        self.entry_name.place(x=500, y=5)

        self.phone_loc = StringVar()
        self.entry_phone = Entry(self.window, textvariable=self.phone_loc)
        self.entry_phone.place(x=500, y=75)

        self.sex_loc = StringVar()
        self.entry_sex = Entry(self.window, textvariable=self.sex_loc)
        self.entry_sex.place(x=500, y=110)

        self.born_loc = StringVar()
        self.entry_born = Entry(self.window, textvariable=self.born_loc)
        self.entry_born.place(x=500, y=150)

        self.enrty_message = Text(self.window, width = 50, height = 5, wrap = WORD)
        self.enrty_message.place(x = 450, y = 250)


        self.entry_data.bind('<<TreeviewSelect>>', lambda event:self.select(self.phone_loc, self.born_loc, self.sex_loc))
        
    def create_label(self):
        self.lb_name = Label(self.window, text = "Имя:")
        self.lb_name.place(x = 450, y = 5)

        self.lb_phone = Label(self.window, text = "Телефон:")
        self.lb_phone.place(x = 423, y = 75)

        self.lb_sex = Label(self.window, text = "Пол:")
        self.lb_sex.place(x = 450, y = 110)

        self.lb_born1 = Label(self.window, text = "Дата")
        self.lb_born1.place(x = 430, y = 140)

        self.lb_born2 = Label(self.window, text = "рождения:")
        self.lb_born2.place(x = 415, y = 160)

        self.lb_message = Label(self.window, text = "Комментарий:")
        self.lb_message.place(x = 460, y = 230)

    def create_menu(self):
        self.instr_menu = Menu(self.window)

        self.instr_menu.add_command(label = "Инструкция", command = lambda: self.open_instr())

        self.window.config(menu = self.instr_menu)
    
    def open_instr(self):
        os.system("libreoffice --writer Instruction.docx")

    def select(self, phone_loc, born_loc, sex_loc):
        for row in self.entry_data.selection():
            self.entry_name.delete(0.0, END)
            self.entry_name.insert(0.0, self.entry_data.item(row)['values'][0])
            phone_loc.set(self.entry_data.item(row)['values'][1])
        
            index = phones.index(self.entry_data.item(row)['values'][1])

            born_loc.set(born[index])

            sex_loc.set(sex[index])

            self.enrty_message.delete(0.0, END)
            self.enrty_message.insert(0.0, message_p[index])   


new_win = Application()