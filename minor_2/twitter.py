from Tkinter import *
import tkMessageBox
import requests
uid = ''
class Tw:
    def __init__(self):
        self.root = Tk()
        self.str2 = 'Twitter'
        self.tw1 = Frame(self.root, width=500, height=600, bg='PeachPuff3')
        self.tw1.grid(row=0, column=0, sticky='news')
        Label(self.tw1, text="Twitter", bg='PeachPuff3').place(relx=0.45, rely=0.02)
        Label(self.tw1, text="Tweet", bg='PeachPuff3').place(relx=0.04, rely=0.17)
        Label(self.tw1, text="Upload Image",  bg='PeachPuff3').place(relx=0.04, rely=0.4)

        # Label(self.fb1, text="Download Image").place(relx=0.1, rely=0.6)
        self.status1 = Entry(self.tw1, width=50, bd=3)
        self.status1.place(relx=0.25, rely=0.17)
        self.tw_path = Entry(self.tw1, width=50, bd=3)
        self.tw_path.place(relx=0.25, rely=0.4)
        self.sub2 = Button(self.tw1, text="Submit", width=10, command=lambda: self.post_req1())
        self.sub2.place(relx=0.4, rely=0.7)


        self.raise_frame1(self.tw1)
        self.root.mainloop()

    def raise_frame1(self, fr):
        fr.tkraise()

    def post_req1(self):
        if self.status1.get() != "" and self.tw_path.get() == "":
            self.str2 += 'tweetpost' + '+' + self.status1.get()

        if self.tw_path.get() != "":
            self.str2 += 'tweetimage+'+self.status1.get()+'+' + self.tw_path.get()

        print(self.str2)
        url = 'http://192.168.51.54:7000/rango/session/' + uid + '/'
        print url
        try:
            requests.post(url,{'Requested_Android': self.str2})
        except Exception as e:
            print str(e)
# Tw()
