from Tkinter import *
import tkMessageBox
import requests
uid = ''


class Fb:
    def __init__(self):
        self.root = Tk()
        self.str1 = 'Facebook'
        self.fb1 = Frame(self.root, width=500, height=600, bg='PeachPuff3')
        self.fb1.grid(row=0, column=0, sticky='news')
        Label(self.fb1, text="Facebook", bg='PeachPuff3').place(relx=0.43, rely=0.02)
        Label(self.fb1, text="Upload Status", bg='PeachPuff3').place(relx=0.04, rely=0.13)
        Label(self.fb1, text="Upload Image", bg='PeachPuff3').place(relx=0.04, rely=0.4)

        # Label(self.fb1, text="Download Image").place(relx=0.1, rely=0.6)
        self.status = Entry(self.fb1, width=50, bd=3)
        self.status.place(relx=0.25, rely=0.13)
        self.fb_path = Entry(self.fb1, width=50, bd=3)
        self.fb_path.place(relx=0.25, rely=0.4)

        self.sub1 = Button(self.fb1, text="Submit", width=10, command=lambda: self.post_req())
        self.sub1.place(relx=0.4, rely=0.7)



        self.raise_frame1(self.fb1)
        self.root.mainloop()

    def raise_frame1(self, fr):
        fr.tkraise()

    def post_req(self):
        if self.status.get() != "" and self.fb_path.get() == "":
            self.str1 += 'uploadstatus'+'+'+self.status.get()

        if self.fb_path.get() != "":
            self.str1 += 'uploadimage'+'+'+self.status.get()+self.fb_path.get()

        print(self.str1)
        url = 'http://192.168.51.54/rango/session/' + uid + '/'
        requests.post(url, data={'Requested_Android': self.str1})



# Fb()