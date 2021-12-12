#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
editor: Aldrich
version: 21.121_released
description: A tool that can import a picture to convenient text.
"""

# Copyright 2021 (C) Aldrich | All Rights Reserved.
# Please download the model files and move them to "C://Users//YourName//.EasyOCR" use before.
# If your computer have CUDA, that'll dispose more faster.

# Main Libraries
from tkinter import *
import easyocr

# Other Libraries
import tkinter.messagebox
import tkinter.ttk
import pyperclip
import shutil
import windnd
import os


def file_message(files):  # Process
    filename = ''.join((item.decode('gbk') for item in files))  # Process file path
    message = ('确认您的文件为：', filename)
    make_sure = tkinter.messagebox.askquestion('提示', message)  # Confirm file path
    if make_sure:
        if filename.endswith(('jpg', 'png', 'jpeg', 'bmp')):  # Check the file
            if os.getcwd() in filename:
                n_filename = filename.replace(os.getcwd(), '')[1:]
            else:
                ex = os.path.splitext(filename)[1]
                shutil.copyfile(filename, rf'temp{ex}')
                n_filename = rf'temp{ex}'
            ocr_main(n_filename)  # Pass parameters to run the function
        else:
            tkinter.messagebox.showerror('错误', '不支持此格式！')
    else:
        pass


def ocr_main(files):  # Text recognition and display
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(f'{files}', detail=0)  # Writes the picture to memory

    def copy_all():
        pyperclip.copy(''.join(result))

    window.geometry('635x300+500+300')
    window.resizable(True, True)
    label.grid_remove()
    btn1 = tkinter.Button(window, text='复制全部', font=('微软雅黑', 12), command=copy_all, width=10)
    btn1.grid(row=2, column=0, sticky=tkinter.W)
    lis = tkinter.Listbox(window, font=('微软雅黑', 12), width=70, height=11)
    lis.grid(row=1, columnspan=3, sticky=tkinter.W)
    list_num = 0
    n_list_num = len(result) + 1

    lis.delete(0, tkinter.END)
    while True:
        if list_num == n_list_num:
            break
        else:
            pass
        lis.insert(list_num, result[list_num])
        list_num = list_num + 1


window = Tk()
window.title('OCR图片转文字工具')
window.geometry('300x300')
window.resizable(0, 0)
windnd.hook_dropfiles(window, func=file_message)
label = tkinter.Label(window, text='\n\n\n\n\n请将图片拖入此处\n（图片格式：.png、.jpg、.jpeg、.bmp）', font=('微软雅黑', 12))
label.grid(row=0, column=0, sticky=tkinter.W)
window.mainloop()
