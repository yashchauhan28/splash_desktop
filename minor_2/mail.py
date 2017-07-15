from Tkinter import *
import tkMessageBox
import requests

uid = ''
email_id = ''
pwd1 = ''
class Mail:
    def __init__(self):
        self.root = Tk()
        self.str3 = 'Email+'+email_id+'+'+pwd1
        self.em = Frame(self.root, width=500, height=600, bg='PeachPuff3')
        self.em.grid(row=0, column=0, sticky='news')
        Label(self.em, text="Email",  bg='PeachPuff3').place(relx=0.45, rely=0.02)
        Label(self.em, text="To",  bg='PeachPuff3').place(relx=0.04, rely=0.12)
        Label(self.em, text="Subject",  bg='PeachPuff3').place(relx=0.04, rely=0.22)
        Label(self.em, text="Message",  bg='PeachPuff3').place(relx=0.04, rely=0.33)
        Label(self.em, text="Attach", bg='PeachPuff3').place(relx=0.04, rely=0.44)
        self.to = Entry(self.em, width=65, bd=2)
        self.to.place(relx=0.15, rely=0.12)
        self.subject = Entry(self.em, width=65, bd=2)
        self.subject.place(relx=0.15, rely=0.22)
        self.msg = Entry(self.em, width=65, bd=2)
        self.msg.place(relx=0.15, rely=0.33)
        self.path = Entry(self.em, width=65, bd=2, fg='grey')
        self.path.place(relx=0.15, rely=0.43)
        self.path.insert(0, 'for multiple files- file1,file2,etc')
        self.path.bind("<Button-1>", self.callback1)
        self.raise_frame2(self.em)
        self.sub3 = Button(self.em, text="Send", width=10, command=lambda: self.post_req2())
        self.sub3.place(relx=0.43, rely=0.7)
        self.root.mainloop()

    def callback1(self, event):
        self.path.delete(0, END)
        self.path.configure(fg='black')

    def raise_frame2(self, fr):
        fr.tkraise()

    def post_req2(self):
        if self.to.get() == "":
            messagebox.showwarning("Please enter To", "'To' cannot be empty")
            self.to.focus()

        else:
            self.str3 += '+'+self.to.get()

            if self.subject.get() != '':
                self.str3 += '+'+self.subject.get()
            if self.msg.get() != '':
                self.str3 += '+'+self.msg.get()
            if self.path.get() != "":
                if ',' in self.path.get():
                    paths = self.path.get().split(",")
                    attach = paths[0]
                    for p in paths:
                        if p != paths[0]:
                            attach = attach+','+p
                    self.str3 += '+'+attach
                else:
                    self.str3 += '+'+self.path.get()
        print(self.str3)
        url = 'http://192.168.51.54/rango/session/'+uid+'/'
        requests.post(url, data={'Requested_Android': self.str3})



# Mail()