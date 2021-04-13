import time
import os
import random
import datetime
from tkinter import *
def f1():
    otvet1 = input('Выбирай: \n1. имя файла пишите вы. \n2. Я сделаю всё за тебя, братуха \n')
    if otvet1 == "1":
        name_new_file = input("какое имя? ")
        name_new_file_txt = name_new_file + ".txt"
        f = open(name_new_file_txt,"x")
    else:
        number = random.randint(0,1000000)
        number = str(number)
        number_file_name = number + ".txt"
        f = open(number_file_name,"x")
    osnova()
def f2():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('какой файл?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    if otvet1 in os.listdir("D:\Органайзер"):
        f = open(otvet1,"r")
        print(f.read())
        time.sleep(10)
    else:
        print('Такого файла нет...')
        print('Миша всё фигня, давай по новой!')
        f2()
    osnova()
def f3():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('какой файл?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    if otvet1 in os.listdir("D:\Органайзер"):
        while True:
            otvet4 = input("что вы хотите добавить(напишите закончить чтобы закончить)?\n")
            if otvet4 == 'закончить':
                break
            f = open(otvet1,"a")
            f.write("\n"+otvet4)
    else:
        print('Такого файла нет...')
        print('Миша всё фигня, давай по новой!')
        f3()
    osnova()
def f4():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('какой файл?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    if otvet1 in os.listdir("D:\Органайзер"): 
        otvet2 = input("На что перезаписавыть/записывать? — ")
        f = open(otvet1, "w")
        f.write(otvet2)
    else:
        print('Такого файла нет...')
        print('Миша всё фигня, давай по новой!')
        f4()
    osnova()
def f5():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('какой файл?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    if otvet1 in os.listdir("D:\Органайзер"):
        otvet2 = input("1. УДАЛИТЬ СОДЕРЖИМОЕ ФАЙЛА; 2.Вернуться к функциям")
        if otvet2 == "1":
            f = open(otvet1, "w")
            f.write("")
        else:
            osnova()
    else:
        print('Такого файла нет...')
        print('Миша всё фигня, давай по новой!')
        f5()
    osnova()
def f6():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('какой файл?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    if otvet1 in os.listdir("D:\Органайзер"):
        otvet2 = input("1. УДАЛИТЬ ФАЙЛ;2.Вернуться к функциям")
        if otvet2 == '1':
            os.remove(otvet1)
        else:
            osnova()
    else:
        print('Такого файла нет...')
        print('Миша всё фигня, давай по новой!')
        f6()
    osnova()
def f7():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('какой файл?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    if otvet1 in os.listdir("D:\Органайзер"):
        with open(otvet1,"r") as f:
            lines = f.readlines()
        num_line = int(input("Введите номер строки: ")) - 1
        line = lines[num_line] 
        print(line)
        time.sleep(5)
        osnova()
    else:
        print('Такого файла нет...')
        print('Миша всё фигня, давай по новой!')
        f7()
    osnova()


def f8():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('какой файл?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    otvet2 = input("что искать? — ")
    if otvet1 in os.listdir("D:\Органайзер"):
        with open(otvet1,"r") as f:
            lines = f.readlines()
        i = 0
        n = 0
        for line in lines:
            i = i + 1
            n = n + 1
            if line.find(otvet2) == 0:
                print(n)
                time.sleep(3)
                break
    else:
        print('Такого файла нет...')
        print('Миша всё фигня, давай по новой!')
        f8()
    osnova()

def f9():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('с какого файла вырезать?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    otvet2 = input("в какой файл вставлять?(просто название) — ")
    otvet2 = otvet2 + ".txt"
    f1 = open(otvet1,"r")
    text = f1.read()
    f11 = open(otvet1,"w")
    f11.write("")
    f2 = open(otvet2,"a")
    f2.write(text)
    osnova()


def f10():
    print("список файлов:", os.listdir("D:\Органайзер"))
    otvet1 = input('с какого файла копировать?(просто название) — ')
    otvet1 = otvet1 + ".txt"
    otvet2 = input("в какой файл копировать?(просто название) — ")
    otvet2 = otvet2 + ".txt"
    f1 = open(otvet1,"r")
    text = f1.read()
    f2 = open(otvet2,"w")
    f2.write(text)
    osnova()
    


def f11():
    otvet1 = input("Предоставить ссписок файлов?(1.ДА;2.Дальше)")
    if otvet1 == "1":
        print(os.listdir("D:\Органайзер"))
    otvet2 = input('какой файл?(просто название) — ')
    otvet2 = otvet2 + ".txt"
    if otvet2 in os.listdir("D:\Органайзер"):
        otvet3 = input("как переименовать?(просто название) —")
        otvet3 = otvet3 + ".txt"
        os.rename(otvet2,otvet3)
    else:
        print('Такого файла нет...')
        print('Миша всё фигня, давай по новой!')
        f11()
    osnova()

        


def osnova():
    print('Дароу, \nКороче записывай сюда разныю фигню=) \nВот мои умения=))):')
    print('1. Создать файл')
    print('2. просмотреть файл')
    print('3. Добавить содержимое')
    print('4. Переписать/написать всё содержимое файла')
    print('5. Удалить всё содержимое')
    print('6. Удалить файл')
    print('7 Посмотреть определёную строку(за номером)')
    print("8 Найти определёную строку(показывает номер строки)")
    print("9. Вырезать содержимое файла в другой файл")
    print("10. Скопировать содержимое файла в другой файл")
    print("11. Переименовать файл")
    print("12. ВЫЙТИ")
    print(datetime.datetime.now())
    MEGA_INPUT = int(input())
    if type(MEGA_INPUT) == int:
        if MEGA_INPUT == 1:
            f1()
        elif MEGA_INPUT == 2:
            f2()
        elif MEGA_INPUT == 3:
            f3()
        elif MEGA_INPUT == 4:
            f4()
        elif MEGA_INPUT == 5:
            f5()
        elif MEGA_INPUT == 6:
            f6()
        elif MEGA_INPUT == 7:
            f7()
        elif MEGA_INPUT == 8:
            f8()
        elif MEGA_INPUT == 9:
            f9()
        elif MEGA_INPUT == 10:
            f10()
        elif MEGA_INPUT == 11:
            f11()
        elif MEGA_INPUT == 12:
            os.close
        else:
            print('введи число, братуха')
            osnova()
    else:
        print("Брат я такога не могу...")
        osnova()
