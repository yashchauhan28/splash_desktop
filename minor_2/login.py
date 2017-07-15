from Tkinter import *
import tkMessageBox
import facebook
import twitter
import mail
import interact
import download
import urllib
import BeautifulSoup


class Login:
    def __init__(self):
        self.eid = ''
        self.pwd = ''
        self.user = ''
        self.root = Tk()
        self.login = Frame(self.root, width=400, height=600)
        self.home = Frame(self.root, width=400, height=600, bg='dark slate gray')
        for frame in (self.login, self.home):
            frame.grid(row=0, column=0, sticky='news')

        # login
        Label(self.login, text="Username").place(relx=0.2, rely=0.1)
        Label(self.login, text="Password").place(relx=0.2, rely=0.5)
        Label(self.login, text="Email").place(relx=0.2, rely=0.3)
        self.uname = Entry(self.login, bd=5)
        self.uname.place(relx=0.4, rely=0.1)
        self.mail = Entry(self.login, bd=5, fg='grey')
        self.mail.place(relx=0.4, rely=0.3)
        self.mail.insert(0, 'your email_id')
        self.mail.bind("<Button-1>", self.default)
        self.password = Entry(self.login, bd=5, fg='grey')
        self.password.place(relx=0.4, rely=0.5)
        self.password.insert(0, 'email_id password ')
        self.password.bind("<Button-1>", self.callback)
        self.submit1 = Button(self.login, text="Submit", command=lambda: self.raise_home(self.home))
        self.submit1.place(relx=0.37, rely=0.7)

        # home
        self.fb = Button(self.home, text="Facebook", width=10, command=lambda: self.raise_fb())
        self.fb.place(relx=0.4, rely=0.1)
        self.tw = Button(self.home, text="Twitter", width=10, command=lambda: self.raise_tw())
        self.tw.place(relx=0.4, rely=0.24)
        self.email = Button(self.home, text="Email", width=10, command=lambda: self.raise_em())
        self.email.place(relx=0.4, rely=0.4)
        self.intr = Button(self.home, text="Interact", width=10, command=lambda: self.raise_int())
        self.intr.place(relx=0.4, rely=0.56)
        self.dw = Button(self.home, text="Download File", command=lambda: self.raise_dw())
        self.dw.place(relx=0.38, rely=0.72)

        self.raise_frame(self.login)
        self.root.mainloop()

    def default(self, event):
        self.mail.delete(0, END)
        self.mail.configure(fg='black')

    def callback(self, event):
        self.password.delete(0, END)
        self.password.configure(fg='black')

    # check user and raise frame home if verified

    def raise_home(self, fr1):

        self.eid = self.mail.get()
        self.pwd = self.password.get()
        self.user = self.uname.get()
        html = urllib.urlopen("http://192.168.51.54:7000/rango/")
        soup = BeautifulSoup.BeautifulSoup(html)
        flag = 0
        #print soup
        #print soup.findAll('a',href=True)
        for link in soup.findAll('a', href=True):
            if str(link.getText()) == self.user:
            	print str(link.getText())
                mail.email_id = self.eid
                mail.pwd1 = self.pwd
                mail.uid = self.user
                interact.uid = self.user
                twitter.uid = self.user
                download.uid = self.user
                facebook.uid = self.user
                self.raise_frame(fr1)
                flag = 1
        if flag == 0:
            messagebox.showwarning('Invalid user', "Username doesn't exist. Kindly Register")




    def raise_frame(self, fr):
        fr.tkraise()

    def raise_fb(self):
        facebook.Fb()

    def raise_tw(self):
        twitter.Tw()

    def raise_em(self):
        mail.Mail()

    def raise_int(self):
        interact.Inter()

    def raise_dw(self):
        download.Dw()

Login()
