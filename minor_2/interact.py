from Tkinter import *
import tkMessageBox
from ScrolledText import *
import urllib2
import BeautifulSoup
uid = ''


class Inter:
    def __init__(self):
        self.root = Tk()
        self.inter = Frame(self.root, width=700, height=600, bg='bisque3')
        self.inter.grid(row=0, column=0, sticky='news')
        Label(self.inter, text="Interact", font=('Courier', 13), fg='salmon4').place(relx=0.02, rely=0.02)
        Label(self.inter, text="Folder name", bg='bisque3').place(relx=0.6, rely=0.22)
        self.txt = ScrolledText(self.inter, width=40, height=25)
        self.fname = Entry(self.inter, width=42)
        self.fname.place(relx=0.6, rely=0.25)
        self.refresh = Button(self.inter, text="Refresh", width=15, command=lambda: self.do_refresh())
        self.refresh.place(relx=0.8, rely=0.62)
        self.submit = Button(self.inter, text="Submit", width=15, command=lambda: self.do_submit())
        self.submit.place(relx=0.8, rely=0.72)
        """self.scroll = Scrollbar(self.inter, orient='vertical', command=self.txt.yview)
        self.txt.config(xscrollcommand=self.scroll.set)
        self.txt.place(relx=0.1, rely=0.1)
        self.scroll.pack(side='right', fill='y')"""
        self.txt.place(relx=0.05, rely=0.15)
        self.raise_frame(self.inter)
        self.root.mainloop()

    def raise_frame(self, fr):
        fr.tkraise()

    # called on refresh
    def do_refresh(self):
        print('refresh')
        

    # called on submit
    def do_submit(self):
        print('submit')

#Inter()
