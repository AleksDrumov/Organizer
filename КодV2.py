import os
import time
import random
import datetime
from tkcalendar import *
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

text_dicrectory = ""
text_file = ""
data_and_time = datetime.datetime.today()
data_and_time = str(data_and_time)
data_and_time = data_and_time.split(".")
data_and_time = data_and_time[0]
tema = 2
tema_var = ""
root = ""
def tema_var_def():
    global tema, root
    tema = tema_var.get()
    root.destroy()
    osnova()

def osnova():
    global tema_var, tema, root
    if tema == 1:
        tema_full = "white"
        text_tema = "black"
        bg_frame = "#f53333"
        menu_theme = "white"
    else:
        tema_full = "#1e1e1e"
        text_tema = "white"
        bg_frame = "#941616"
        menu_theme = "#323233"
    root = Tk()
    root['bg'] = tema_full
    root.title('Menu')
    root.geometry('540x660+500+100')
    menutext = Label(root,text='Главное меню',relief=RAISED,bd=10,font=('Arial',20,'bold'),bg=tema_full,fg=text_tema)
    menutext.pack()
    frame = Frame(root,bg=bg_frame)
    frame.place(relx=0.02,rely=0.1,relwidth=0.95,relheight=0.05)
    calender_lbl = Label(root,text="Функции календаря",font="Arial 18",bg=tema_full,fg=text_tema)
    calender_lbl.place(relx=0.28,rely=0.15)
    discover_date_btn = Button(root, text="Узнать что сегодня запланировано",command=discover_date,bg=tema_full,fg=text_tema)
    discover_date_btn.place(relx=0.3,rely=0.2)
    discover_calendar_btn = Button(root,text="Показать каледарь",command=discover_calendar,bg=tema_full,fg=text_tema)
    discover_calendar_btn.place(relx=0.38,rely=0.3)
    file_lbl = Label(root,text="Функции файлов",font="Arial 18",bg=tema_full,fg=text_tema)
    file_lbl.place(relx=0.31,rely=0.35)
    num_file_btn = Button(root,text="Прономеровать строки в файле",command=num_file_func,bg=tema_full,fg=text_tema)
    num_file_btn.place(relx=0.315,rely=0.4)
    del_str_num_btn = Button(root,text="Удалить строку по номеру",command=del_str_num,bg=tema_full,fg=text_tema)
    del_str_num_btn.place(relx=0.34,rely=0.5)
    miscellaneous_lbl = Label(root,text="Разное",font="Arial 18",bg=tema_full,fg=text_tema)
    miscellaneous_lbl.place(relx=0.41,rely=0.55)
    seach_word_btn = Button(root,text="Найти слово в файле", command = seach_word,bg=tema_full,fg=text_tema)
    seach_word_btn.place(relx=0.37,rely=0.6)   
    tema_var = IntVar()                                                
    tema_bla = Radiobutton(root,text="Белая тема",variable=tema_var,value=1,command=tema_var_def,bg=tema_full,fg=text_tema)
    tema_bla.place(relx=0.4,rely=0.7)
    tema_whi = Radiobutton(root,text="Чёрная тема",variable=tema_var,value=2,command=tema_var_def,bg=tema_full,fg=text_tema)
    tema_whi.place(relx=0.4,rely=0.75)
    main_menu = Menu(bg=menu_theme,fg=text_tema)
    file_menu = Menu(bg=menu_theme,fg=text_tema)
    file_menu.add_command(label="Новый файл",command=do_new_file)
    file_menu.add_command(label="Операции над файлом",command=file_view)
    main_menu.add_cascade(label="Файл", menu=file_menu)
    main_menu.add_cascade(label="Выход",command=root.destroy)
    main_menu.add_cascade(label=data_and_time)
    root.config(menu=main_menu)
    root.mainloop()


def do_new_file():
    global tema_var, tema
    if tema == 1:
        tema_full = "white"
        text_tema = "black"
    else:
        tema_full = "#1e1e1e"
        text_tema = "white"
    filedo = Tk()
    filedo["bg"] = tema_full
    file_label = Label(filedo,text="Введите название файла:",bg=tema_full,fg=text_tema)
    file_label.pack()
    file_string = StringVar()
    file_entry = Entry(filedo,textvariable=file_string,bg=tema_full,fg=text_tema)
    file_entry.pack()
    def file_user_but():
        global text_file
        text_file = '\\' + str(file_entry.get()) + ".txt" 
        prosto_tak = Tk()
        mb.showinfo(title="INFO",message="Укажите директорию создания файлов")
        directory_new_file = fd.askdirectory()
        directory_new_file = directory_new_file + text_file
        prosto_tak.destroy()
        print(directory_new_file)
        f = open(directory_new_file,"x")
        
    file_btn = Button(filedo,text="Создать",command=file_user_but,bg=tema_full,fg=text_tema)
    file_btn.pack()

    def file_robot_but():
        number = random.randint(0,1000000)
        number = str(number)
        number_file_name = '\\' + number + ".txt"
        directory_new_file = fd.askdirectory()
        directory_new_file = directory_new_file + number_file_name
        f = open(directory_new_file,"x")
        print(directory_new_file)
    file_btn2 = Button(filedo,text="рандом имя",command=file_robot_but,bg=tema_full,fg=text_tema)
    file_btn2.pack()
    file_btn_close = Button(filedo,text="закрыть",command=filedo.destroy,bg=tema_full,fg=text_tema)
    file_btn_close.pack()
    
    filedo.mainloop()

def file_view():
    global tema_var, tema
    if tema == 1:
        tema_full = "white"
        text_tema = "black"
    else:
        tema_full = "#1e1e1e"
        text_tema = "white"
    def insert_text():
        file_name = fd.askopenfilename()
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    
    def delete_file():
        file_name = fd.askopenfilename()
        os.remove(file_name)
    def extract_text():
        file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
 
 
    view = Tk()
    view['bg'] = tema_full
    view["bg"] = tema_full
    text = Text(view,width=50, height=25,bg=tema_full,fg=text_tema)
    text.pack()
    b1 = Button(view,text="Открыть", command=insert_text,bg=tema_full,fg=text_tema)
    b1.pack()
    b2 = Button(view,text="Сохранить", command=extract_text,bg=tema_full,fg=text_tema)
    b2.pack()
    b3 = Button(view,text="Удалить", command=delete_file,bg=tema_full,fg=text_tema)
    b3.pack()
    view.mainloop()

def discover_date():
    global tema_var, tema
    if tema == 1:
        tema_full = "white"
        text_tema = "black"
    else:
        tema_full = "#1e1e1e"
        text_tema = "white"
    okno = mb.showinfo(title='info',message="дата в файле должны быть записана в формате:дд.мм.гггг\nдругими способомами разпознать не возможно")
    file_name = fd.askopenfilename()
    answer = mb.askyesno(
        title="Вопрос:", 
        message="Ваш документ органайзер?")
    if answer:
        with open(file_name,"r") as f:
            lines = f.readlines()
        date = datetime.datetime.today()
        date_day = date.day
        date_month = date.month
        date_year = date.year
        if date_day > 9:
            data = str(date_day) + "." + str(date_month) + "." + str(date_year)
            if date_month > 9:
                data = str(date_day) + "." + str(date_month) + "." + str(date_year)
            else:
                data = str(date_day) + "." + "0" + str(date_month) + "." + str(date_year)
            
        else:
            data ="0" + str(date_day) + "." + str(date_month) + "." + str(date_year)
            if date_month > 9:
                data = "0" + str(date_day) + "." + str(date_month) + "." + str(date_year)
            else:
                data = "0" + str(date_day) + "." + "0" + str(date_month) + "." + str(date_year)
        n = 0
        discover_file = Tk()
        discover_file["bg"] = tema_full
        for line in lines:
            n = n + 1
            find = line.find(data)
            if find == 0:
                discover_lbl = Label(discover_file,text=line,bg=tema_full,fg=text_tema)
                discover_lbl.pack()
seach_file = ""
file_name = ""
lines = ""
f = ""
def seach_word():
    global tema_var, tema, seach_file, file_name, f, lines
    if tema == 1:
        tema_full = "white"
        text_tema = "black"
    else:
        tema_full = "#1e1e1e"
        text_tema = "white"
    if seach_file == "":
        file_name = fd.askopenfilename()
        f = open(file_name,"r") 
        lines = f.readlines()
    else:
        seach_file.destroy()
    n = 0
    seach_file = Tk()
    seach_file['bg'] = tema_full
    seach_lbl = Label(seach_file,text="Найти слово",bg=tema_full,fg=text_tema)
    seach_lbl.pack()
    seach_string = StringVar()
    seach_entry = Entry(seach_file,textvariable=seach_string,bg=tema_full,fg=text_tema)
    seach_entry.pack()
    
    def find_word():
        n = 0
        for line in lines:
            n = n + 1
            what_find = seach_entry.get()
            find = line.find(what_find)
            if find > -1:
                find_text = "\n" + "Ввод: " + what_find
                word_lbl = Label(seach_file,text=find_text,bg=tema_full,fg=text_tema)
                word_lbl.pack()
                n_text = "Номер строки: " + str(n)
                line_text = "Строка: " + line 
                result_lbl = Label(seach_file,text=line_text,bg=tema_full,fg=text_tema)
                result_lbl.pack()
                number_lbl = Label(seach_file,text=n_text,bg=tema_full,fg=text_tema)
                number_lbl.pack()
            else:
                pass
                               

    seach_btn = Button(seach_file,text="Найти",command=find_word,bg=tema_full,fg=text_tema)
    seach_btn.pack()
    delete_btn = Button(seach_file,text="Очистить",command=seach_word,bg=tema_full,fg=text_tema)
    delete_btn.pack()


def num_file_func():
    global tema_var, tema
    if tema == 1:
        tema_full = "white"
        text_tema = "black"
    else:
        tema_full = "#1e1e1e"
        text_tema = "white"
    num_file_ask = fd.askopenfilename()
    num_file = Tk()
    num_file['bg'] = tema_full
    f = open(num_file_ask,'r')
    full_text = ""
    num_check = ""
    full_del_text = ""
    
    for num, line in enumerate(f,1):
        f = open(num_file_ask,'r')
        num_check = str(num) + '. '
        full_del_text = full_del_text + line.replace(num_check,"")
    f = open(num_file_ask,"r")
    lines = f.readlines()
    len_lines = len(lines) + 2
    for number in range(len_lines):
        number_str = str(number) + ". "
        x = full_del_text.replace(number_str,"")

    f = open(num_file_ask,'w')
    f.write(x)
    f = open(num_file_ask,'r')
    for num, line in enumerate(f,1):
        text = str(num)+ '. ' + line.strip() + '\n'
        full_text = full_text + text
    f = open(num_file_ask,'w')
    f.write(full_text)
    text_lbl = 'В файле сейчас:' + "\n" + full_text
    num_lbl = Label(num_file,text=text_lbl,bg=tema_full,fg=text_tema)
    num_lbl.pack()


entry_vvod = ""
full_str = ""
def del_str_num():
    global tema_var, tema
    if tema == 1:
        tema_full = "white"
        text_tema = "black"
    else:
        tema_full = "#1e1e1e"
        text_tema = "white"
    ask = fd.askopenfilename()
    f = open(ask,"r")
    del_str_num_file = Tk()
    del_str_num_file['bg'] = tema_full
    entrty_lbl = Label(del_str_num_file,text="Веедите номер строки:",bg=tema_full,fg=text_tema)
    entrty_lbl.pack()
    vvod = StringVar()
    entry_entry = Entry(del_str_num_file,textvariable=vvod,bg=tema_full,fg=text_tema)
    entry_entry.pack()
    def entry_btn_def():
        global entry_vvod, full_str
        f = open(ask,"r")
        lines_list = f.readlines()
        entry_vvod = entry_entry.get()
        num_str = int(entry_vvod) - 1
        lines_list.pop(num_str)
        for line in lines_list:
            full_str = full_str + line
        f = open(ask,"w")
        f.write(full_str)
        result = "В файле: \n" + full_str
        mb.showinfo(title="INFO",message="Готово")
        add_lbl = Label(del_str_num_file,text=result,bg=tema_full,fg=text_tema)
        add_lbl.pack()
    entry_btn = Button(del_str_num_file,text="Enter",command=entry_btn_def,bg=tema_full,fg=text_tema)
    entry_btn.pack()

chek_text = "0"
prosto = Tk()
doname_file_text = mb.showinfo(title="календар",message="Путь к календарю")
name_file_text = fd.askopenfilename()
prosto.destroy()
def discover_calendar():
    global tema_var, tema
    if tema == 1:
        tema_full = "white"
        text_tema = "black"
    else:
        tema_full = "#1e1e1e"
        text_tema = "white"
    discover_calendar_file = Tk()
    discover_calendar_file['bg'] = tema_full
    discover_calendar_file.title("КАЛЕНДАРЬ")
    date = datetime.datetime.today()
    cal = Calendar(discover_calendar_file, selectmode="day",year=date.year, month=date.month, day=date.day)
    cal.pack(pady=20)
    def grab_date():
        global name_file_text
        date_calen = cal.get_date()
        text_file = Tk()
        text_file["bg"] = tema_full
        text_lbl = Label(text_file,text="Введите заметки к дате",bg=tema_full,fg=text_tema)
        text_lbl.pack()
        text_string = StringVar()
        text_entry = Entry(text_file,textvariable=text_string,bg=tema_full,fg=text_tema)
        text_entry.pack()
        def file_text_def():
            global chek_text,name_file_text
            f = open(name_file_text,"r")
            read_chek = f.read()
            if read_chek == "":
                string_text = date_calen + " " + text_entry.get()
            else:
                string_text = "\n" + date_calen + " " + text_entry.get()
            f = open(name_file_text,"a")
            f.write(string_text)
            text_file.destroy()
        text_btn = Button(text_file,text="Ввод",command=file_text_def,bg=tema_full,fg=text_tema)
        text_btn.pack()




    my_button = Button(discover_calendar_file,text="Вписать дату",command=grab_date,bg=tema_full,fg=text_tema)
    my_button.pack(pady=20)

osnova()
