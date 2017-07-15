from Tkinter import *
import requests

uid = ''


class Dw:
    def __init__(self):
        self.root = Tk()
        self.str4 = 'DownloadImage'
        self.dw1 = Frame(self.root, width=500, height=600,  bg='PeachPuff2')
        self.dw1.grid(row=0, column=0, sticky='news')
        Label(self.dw1, text="Download",  bg='PeachPuff2').place(relx=0.43, rely=0.02)
        Label(self.dw1, text="Enter URL",  bg='PeachPuff2').place(relx=0.04, rely=0.2)
        self.url = Entry(self.dw1, width=55, bd=3, fg='grey')
        self.url.place(relx=0.22, rely=0.2)
        self.url.insert(0, 'enter url to download')
        self.url.bind("<Button-1>", self.callback2)
        self.download = Button(self.dw1, text="Download", width=10, command=lambda: self.post_req3())
        self.download.place(relx=0.4, rely=0.6)

        self.raise_frame1(self.dw1)
        self.root.mainloop()

    def callback2(self, event):
        self.url.delete(0, END)
        self.url.configure(fg='black')

    def raise_frame1(self, fr):
        fr.tkraise()

    def post_req3(self):
        if self.url.get() != "":
            self.str4 += '+URL+' + self.url.get()

        print(self.str4)
        url = 'http://192.168.51.54/rango/session/' + uid + '/'
        requests.post(url, data={'Requested_Android': self.str4})

# Dw()