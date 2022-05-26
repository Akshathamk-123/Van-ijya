from tkinter import *
import tkinter.messagebox
import mysql.connector
from PIL import ImageTk, Image
import getpass
import time
 
 
# frame1: login signup buttons
# frame2: signup page
# frame3: login page
# frame4: home() function
# frame5: search page (category display)
# frame6: cart page
# frame7: checkout
 
 
def welcomepage():
    frame1 = Frame(root, height=483, width=430)
    frame1.place(x=5, y=30)
    frame1.configure(bg='#d9d9d9')
 
    log_btn = Button(frame1, text="Log In", padx=40, pady=15, borderwidth=2, fg='black', command=lambda: act1())
    log_btn.place(x=152, y=130)
 
    sign_btn = Button(frame1, text="Sign Up", padx=40, pady=15, borderwidth=2, fg='black', command=lambda: act2())
    sign_btn.place(x=146, y=300)
 
    def act1():
        frame1.destroy()
        loginClick()
 
    def act2():
        frame1.destroy()
        signupClick()
 
 
con2 = mysql.connector.connect(host="localhost", user="root", password="", database="usernpass")
unp = con2.cursor()
Log_stat = False
curr_usr = ''
 
root = Tk()
root.title("Vaańijya - Trade and Commerce")
root.configure(bg='#000080')
root.geometry("440x570")
 
 
def quitter():
    f = "DELETE FROM usrcart"
    q_con = mysql.connector.connect(host="localhost", user="root", password="", database="OnlineSeller")
    q_curs = q_con.cursor()
    q_curs.execute(f)
    q_con.commit()
    root.destroy()
 
 
p1 = PhotoImage(file=r"/Users/animesh/Documents/PycharmProjects/1st sem project/exitButton.png")
pp1 = p1.subsample(4, 8)
 
quit_btn = Button(root, text="Pink", image=pp1, borderwidth=0, command=lambda: quitter())
quit_btn.place(x=165, y=530)
 
p2 = PhotoImage(file=r"/Users/animesh/Documents/PycharmProjects/1st sem project/osHeading.png")
pp2 = p2.subsample(2, 2)
lbl = Label(root, image=pp2)
lbl.place(x=95, y=0)
 
welcomepage()
 
 
def signupClick():
    frame2 = Frame(root, height=483, width=430)
    frame2.place(x=5, y=30)
    frame2.configure(bg='#d9d9d9')
 
    usrnm = Entry(frame2, borderwidth=4)
    usrnm.place(x=125, y=100, width=180, height=30)
    t1 = Label(frame2, text="Enter your username :", font=("Arial", 20))
    t1.place(x=113, y=60)
 
    pssw = Entry(frame2, borderwidth=4)
    pssw.place(x=128, y=230, width=180, height=30)
    t2 = Label(frame2, text="Enter Password : ", font=("Arial", 20))
    t2.place(x=135, y=195)
 
    psswchk = Entry(frame2, borderwidth=4)
    psswchk.place(x=128, y=365, width=180, height=30)
    t3 = Label(frame2, text="Re-enter your password: ", font=("Arial", 20))
    t3.place(x=106, y=330)
 
    submit_btn = Button(frame2, text="Submit", height=2, width=10, borderwidth=2, fg='black', bg='white',command=lambda: sub())
    submit_btn.place(x=170, y=430)
 
    p_left = PhotoImage(file=r"/Users/animesh/Documents/PycharmProjects/1st sem project/exitButton.png")
    pp_left = p_left.subsample(10, 12)
 
    # log_btn.destroy()
    # sign_btn.destroy()
 
 
    # mysql part
    def sub():
        usrnm1 = str(usrnm.get())
        pssw1 = str(pssw.get())
        psswchk1 = str(psswchk.get())
        global Log_stat
        while True:
            if psswchk1 == pssw1 and len(usrnm1) != 0:
                tkinter.messagebox.showinfo("", "Passwords match, successfully stored")
                i = "INSERT INTO store(USERNAME, PASSWORD) VALUES (%s, %s)"
                lis = [(usrnm1, pssw1)]
                unp.executemany(i, lis)
                con2.commit()
                Log_stat = True
                break
            else:
                tkinter.messagebox.showinfo("", "Passwords Dont match or username is invalid, please try again")
                root.destroy()
        if Log_stat == True:
            tkinter.messagebox.showinfo("", "Signup successful, Welcome!")
        else:
            tkinter.messagebox.showinfo("", "Please try again")
 
        frame2.destroy()
        home()
 
 
def loginClick():
    frame3 = Frame(root, height=483, width=430)
    frame3.place(x=5, y=30)
    frame3.configure(bg='#d9d9d9')
 
    usrnm = Entry(frame3, borderwidth=4)
    usrnm.place(x=125, y=135, width=180, height=30)
    t1 = Label(frame3, text="Enter your username :", font=("Arial", 20))
    t1.place(x=112, y=90)
 
    pssw = Entry(frame3, borderwidth=4)
    pssw.place(x=125, y=290, width=180, height=30)
    t2 = Label(frame3, text="Enter your password: ", font=("Arial", 20))
    t2.place(x=114, y=245)
 
    submit_btn = Button(frame3, text="Submit", height=2, width=10, borderwidth=2, fg='black', bg='white', command=lambda: sub())
    submit_btn.place(x=170, y=430)
 
    def sub():
        global Log_stat
        unp.execute("SELECT * FROM store")
        data = unp.fetchall()
        L = []
        for row in data:
            L.append(row)
 
        while Log_stat != True:
            usrnm1 = usrnm.get()
            pssw1 = pssw.get()
            for i in range(len(L)):
                if usrnm1.lower() == L[i][0].lower() and pssw1.lower() == L[i][1].lower():
                    Log_stat = True
                    tkinter.messagebox.showinfo("", "Logged in successfully, Welcome!")
                    break
                else:
                    continue
            else:
                tkinter.messagebox.showinfo("", "Please enter the correct username/password")
                root.destroy()
 
        frame3.destroy()
        home()
 
 
def searchClick():
    s_con = mysql.connector.connect(host="localhost", user="root", password="", database="OnlineSeller")
    s_curs = s_con.cursor()
    # top = Toplevel()
 
    frame5 = Frame(root, height=483, width=430)
    frame5.place(x=5, y=30)
    frame5.configure(bg='#d9d9d9')
 
    # top.geometry("400x310")
    # cat = Entry(top, borderwidth=1).place(x=320, y=180, width=180, height=25)
    b_mc = Button(frame5, text="MC", height=3, width=9, command=lambda: f_mc())
    b_tae = Button(frame5, text="TAE", height=3, width=9, command=lambda: f_tae())
    b_mfwf = Button(frame5, text="MFWF", height=3, width=9, command=lambda: f_mfwf())
    b_hkp = Button(frame5, text="HKP", height=3, width=9, command=lambda: f_hkp())
    b_bhg = Button(frame5, text="BHG", height=3, width=9, command=lambda: f_bhg())
    b_sfbl = Button(frame5, text="SFBL", height=3, width=9, command=lambda: f_sfbl())
    b_cmi = Button(frame5, text="CMI", height=3, width=9, command=lambda: f_cmi())
    b_b = Button(frame5, text="B", height=3, width=9, command=lambda: f_b())
    back_btn = Button(root, text="Go back", height=2, width=9, command=lambda: goback())
 
    l_mc = Label(frame5, text="Mobiles/Computers")
    l_tae = Label(frame5, text="TV/Appliances/Electronics")
    l_mfwf = Label(frame5, text="Men's/Women's Fashion")
    l_hkp = Label(frame5, text="Home/Kitchen/Pets")
    l_bhg = Label(frame5, text="Beauty/Health/Grocery")
    l_sfbl = Label(frame5, text="Sports/Fitness/Bags/Luggage")
    l_cmi = Label(frame5, text="Cars/Mobiles/Industrial")
    l_b = Label(frame5, text="Books")
 
    b_mc.place(x=100, y=50)
    b_tae.place(x=250, y=50)
    b_mfwf.place(x=100, y=150)
    b_hkp.place(x=250, y=150)
    b_bhg.place(x=100, y=250)
    b_sfbl.place(x=250, y=250)
    b_cmi.place(x=100, y=350)
    b_b.place(x=250, y=350)
    back_btn.place(x=30, y=525)
 
    l_mc.place(x=61, y=27)
    l_tae.place(x=245, y=27)
    l_mfwf.place(x=32, y=127)
    l_hkp.place(x=245, y=127)
    l_bhg.place(x=40, y=227)
    l_sfbl.place(x=245, y=227)
    l_cmi.place(x=39, y=327)
    l_b.place(x=245, y=327)
 
    s_con = mysql.connector.connect(host="localhost", user="root", password="", database="OnlineSeller")
    s_curs = s_con.cursor()
 
    def goback():
        back_btn.destroy()
        home()
 
    def f_mc():
        frame5.destroy()
 
        frm_mc = Frame(root, height=483, width=430)
        frm_mc.place(x=5, y=30)
        frm_mc.configure(bg='#d9d9d9')
 
        top1 = Toplevel()
        top1.geometry("1200x300")
        scrl = Scrollbar(top1, orient='horizontal')
        scrl.pack(side=BOTTOM, fill=X)
        l2 = []
        f = "SELECT * FROM MC"
        s_curs.execute(f)
        for i in s_curs:
            l2.append(i)
        print(l2)
        prdt = "                                Name                                    |   Price  |         Description       " + "\n"
        for i in l2:
            prdt += "|" + i[0] + " " * (70 - len(i[0])) + " "
            prdt += "|" + str(i[2]) + " " * (10 - len(str(i[2])))
            prdt += "|" + i[1] + " " * 10 + "\n"
        t1 = Label(frm_mc, text="Enter the Product name/key word down below", font=("Arial", 18))
        t1.place(x=18, y=30)
 
        prod_name = Entry(frm_mc, borderwidth=4)
        prod_name.place(x=123, y=150)
        b_cart = Button(frm_mc, height=2, width=10, borderwidth=2, text="Add to cart", command=lambda: confirmCart())
        b_cart.place(x=169, y=350)
        t2 = Text(top1, width=229, height=20, wrap="none", xscrollcommand=scrl.set)
        scrl.config(command=t2.xview)
        t2.pack()
        t2.insert('end', prdt)
 
        def confirmCart():
            prod1 = prod_name.get()
            chk = False
            print(prod1)
            top1.destroy()
            for i in range(len(l2)):
                if str(prod1).lower() in l2[i][0].lower():
                    g = "insert into usrcart(PRODUCT, PRICE) values(%s, %s)"
                    lis = [(l2[i][0], l2[i][2])]
                    tkinter.messagebox.showinfo("", "Item added to cart successfully")
                    s_curs.executemany(g, lis)
                    s_con.commit()
                    chk = True
                    break
            if chk == False:
                tkinter.messagebox.showinfo("", "No such item found, please enter correct name")
            frm_mc.destroy()
            home()
            back_btn.destroy()
 
    def f_tae():
        frame5.destroy()
 
        frm_tae = Frame(root, height=483, width=430)
        frm_tae.place(x=5, y=30)
        frm_tae.configure(bg='#d9d9d9')
 
        top1 = Toplevel()
        top1.geometry("1200x300")
        scrl = Scrollbar(top1, orient='horizontal')
        scrl.pack(side=BOTTOM, fill=X)
        l2 = []
        f = "SELECT * FROM TAE"
        s_curs.execute(f)
        for i in s_curs:
            l2.append(i)
        print(l2)
        prdt = "                                Name                                    |   Price  |         Description       " + "\n"
        for i in l2:
            prdt += "|" + i[0] + " " * (70 - len(i[0])) + " "
            prdt += "|" + str(i[2]) + " " * (10 - len(str(i[2])))
            prdt += "|" + i[1] + " " * 10 + "\n"
        t1 = Label(frm_tae, text="Enter the Product name/key word down below", font=("Arial", 18))
        t1.place(x=18, y=30)
 
        prod_name = Entry(frm_tae, borderwidth=4)
        prod_name.place(x=123, y=150)
        b_cart = Button(frm_tae, height=2, width=10, borderwidth=2, text="Add to cart", command=lambda: confirmCart())
        b_cart.place(x=169, y=350)
        t2 = Text(top1, width=229, height=20, wrap="none", xscrollcommand=scrl.set)
        scrl.config(command=t2.xview)
        t2.pack()
        t2.insert('end', prdt)
 
        def confirmCart():
            prod1 = prod_name.get()
            chk = False
            print(prod1)
            top1.destroy()
            for i in range(len(l2)):
                if str(prod1).lower() in l2[i][0].lower():
                    g = "insert into usrcart(PRODUCT, PRICE) values(%s, %s)"
                    lis = [(l2[i][0], l2[i][2])]
                    tkinter.messagebox.showinfo("", "Item added to cart successfully")
                    s_curs.executemany(g, lis)
                    s_con.commit()
                    chk = True
                    break
            if chk == False:
                tkinter.messagebox.showinfo("", "No such item found, please enter correct name")
            frm_tae.destroy()
            home()
            back_btn.destroy()
 
 
    def f_mfwf():
        frame5.destroy()
 
        frm_mfwf = Frame(root, height=483, width=430)
        frm_mfwf.place(x=5, y=30)
        frm_mfwf.configure(bg='#d9d9d9')
 
        top1 = Toplevel()
        top1.geometry("1200x300")
        scrl = Scrollbar(top1, orient='horizontal')
        scrl.pack(side=BOTTOM, fill=X)
        l2 = []
        f = "SELECT * FROM MFWF"
        s_curs.execute(f)
        for i in s_curs:
            l2.append(i)
        print(l2)
        prdt = "                                Name                                    |   Price  |         Description       " + "\n"
        for i in l2:
            prdt += "|" + i[0] + " " * (70 - len(i[0])) + " "
            prdt += "|" + str(i[2]) + " " * (10 - len(str(i[2])))
            prdt += "|" + i[1] + " " * 10 + "\n"
        t1 = Label(frm_mfwf, text="Enter the Product name/key word down below", font=("Arial", 18))
        t1.place(x=18, y=30)
 
        prod_name = Entry(frm_mfwf, borderwidth=4)
        prod_name.place(x=123, y=150)
        b_cart = Button(frm_mfwf, height=2, width=10, borderwidth=2, text="Add to cart", command=lambda: confirmCart())
        b_cart.place(x=169, y=350)
        t2 = Text(top1, width=229, height=20, wrap="none", xscrollcommand=scrl.set)
        scrl.config(command=t2.xview)
        t2.pack()
        t2.insert('end', prdt)
 
        def confirmCart():
            prod1 = prod_name.get()
            chk = False
            print(prod1)
            top1.destroy()
            for i in range(len(l2)):
                if str(prod1).lower() in l2[i][0].lower():
                    g = "insert into usrcart(PRODUCT, PRICE) values(%s, %s)"
                    lis = [(l2[i][0], l2[i][2])]
                    tkinter.messagebox.showinfo("", "Item added to cart successfully")
                    s_curs.executemany(g, lis)
                    s_con.commit()
                    chk = True
                    break
            if chk == False:
                tkinter.messagebox.showinfo("", "No such item found, please enter correct name")
            frm_mfwf.destroy()
            home()
            back_btn.destroy()
 
    def f_hkp():
        frame5.destroy()
 
        frm_hkp = Frame(root, height=483, width=430)
        frm_hkp.place(x=5, y=30)
        frm_hkp.configure(bg='#d9d9d9')
 
        top1 = Toplevel()
        top1.geometry("1200x300")
        scrl = Scrollbar(top1, orient='horizontal')
        scrl.pack(side=BOTTOM, fill=X)
        l2 = []
        f = "SELECT * FROM hkp"
        s_curs.execute(f)
        for i in s_curs:
            l2.append(i)
        print(l2)
        prdt = "                                Name                                    |   Price  |         Description       " + "\n"
        for i in l2:
            prdt += "|" + i[0] + " " * (70 - len(i[0])) + " "
            prdt += "|" + str(i[2]) + " " * (10 - len(str(i[2])))
            prdt += "|" + i[1] + " " * 10 + "\n"
        t1 = Label(frm_hkp, text="Enter the Product name/key word down below", font=("Arial", 18))
        t1.place(x=18, y=30)
 
        prod_name = Entry(frm_hkp, borderwidth=4)
        prod_name.place(x=123, y=150)
        b_cart = Button(frm_hkp, height=2, width=10, borderwidth=2, text="Add to cart", command=lambda: confirmCart())
        b_cart.place(x=169, y=350)
        t2 = Text(top1, width=229, height=20, wrap="none", xscrollcommand=scrl.set)
        scrl.config(command=t2.xview)
        t2.pack()
        t2.insert('end', prdt)
 
        def confirmCart():
            prod1 = prod_name.get()
            chk = False
            print(prod1)
            top1.destroy()
            for i in range(len(l2)):
                if str(prod1).lower() in l2[i][0].lower():
                    g = "insert into usrcart(PRODUCT, PRICE) values(%s, %s)"
                    lis = [(l2[i][0], l2[i][2])]
                    tkinter.messagebox.showinfo("", "Item added to cart successfully")
                    s_curs.executemany(g, lis)
                    s_con.commit()
                    chk = True
                    break
            if chk == False:
                tkinter.messagebox.showinfo("", "No such item found, please enter correct name")
            frm_hkp.destroy()
            home()
            back_btn.destroy()
 
    def f_bhg():
        frame5.destroy()
 
        frm_bhg = Frame(root, height=483, width=430)
        frm_bhg.place(x=5, y=30)
        frm_bhg.configure(bg='#d9d9d9')
 
        top1 = Toplevel()
        top1.geometry("1200x300")
        scrl = Scrollbar(top1, orient='horizontal')
        scrl.pack(side=BOTTOM, fill=X)
        l2 = []
        f = "SELECT * FROM BHG"
        s_curs.execute(f)
        for i in s_curs:
            l2.append(i)
        print(l2)
        prdt = "                                Name                                    |   Price  |         Description       " + "\n"
        for i in l2:
            prdt += "|" + i[0] + " " * (70 - len(i[0])) + " "
            prdt += "|" + str(i[2]) + " " * (10 - len(str(i[2])))
            prdt += "|" + i[1] + " " * 10 + "\n"
        t1 = Label(frm_bhg, text="Enter the Product name/key word down below", font=("Arial", 18))
        t1.place(x=18, y=30)
 
        prod_name = Entry(frm_bhg, borderwidth=4)
        prod_name.place(x=123, y=150)
        b_cart = Button(frm_bhg, height=2, width=10, borderwidth=2, text="Add to cart", command=lambda: confirmCart())
        b_cart.place(x=169, y=350)
        t2 = Text(top1, width=229, height=20, wrap="none", xscrollcommand=scrl.set)
        scrl.config(command=t2.xview)
        t2.pack()
        t2.insert('end', prdt)
 
        def confirmCart():
            prod1 = prod_name.get()
            chk = False
            print(prod1)
            top1.destroy()
            for i in range(len(l2)):
                if str(prod1).lower() in l2[i][0].lower():
                    g = "insert into usrcart(PRODUCT, PRICE) values(%s, %s)"
                    lis = [(l2[i][0], l2[i][2])]
                    tkinter.messagebox.showinfo("", "Item added to cart successfully")
                    s_curs.executemany(g, lis)
                    s_con.commit()
                    chk = True
                    break
            if chk == False:
                tkinter.messagebox.showinfo("", "No such item found, please enter correct name")
            frm_bhg.destroy()
            home()
            back_btn.destroy()
 
    def f_sfbl():
        frame5.destroy()
 
        frm_sfbl = Frame(root, height=483, width=430)
        frm_sfbl.place(x=5, y=30)
        frm_sfbl.configure(bg='#d9d9d9')
 
        top1 = Toplevel()
        top1.geometry("1200x300")
        scrl = Scrollbar(top1, orient='horizontal')
        scrl.pack(side=BOTTOM, fill=X)
        l2 = []
        f = "SELECT * FROM SFBL"
        s_curs.execute(f)
        for i in s_curs:
            l2.append(i)
        print(l2)
        prdt = "                                Name                                    |   Price  |         Description       " + "\n"
        for i in l2:
            prdt += "|" + i[0] + " " * (70 - len(i[0])) + " "
            prdt += "|" + str(i[2]) + " " * (10 - len(str(i[2])))
            prdt += "|" + i[1] + " " * 10 + "\n"
        t1 = Label(frm_sfbl, text="Enter the Product name/key word down below", font=("Arial", 18))
        t1.place(x=18, y=30)
 
        prod_name = Entry(frm_sfbl, borderwidth=4)
        prod_name.place(x=123, y=150)
        b_cart = Button(frm_sfbl, height=2, width=10, borderwidth=2, text="Add to cart", command=lambda: confirmCart())
        b_cart.place(x=169, y=350)
        t2 = Text(top1, width=229, height=20, wrap="none", xscrollcommand=scrl.set)
        scrl.config(command=t2.xview)
        t2.pack()
        t2.insert('end', prdt)
 
        def confirmCart():
            prod1 = prod_name.get()
            chk = False
            print(prod1)
            top1.destroy()
            for i in range(len(l2)):
                if str(prod1).lower() in l2[i][0].lower():
                    g = "insert into usrcart(PRODUCT, PRICE) values(%s, %s)"
                    lis = [(l2[i][0], l2[i][2])]
                    tkinter.messagebox.showinfo("", "Item added to cart successfully")
                    s_curs.executemany(g, lis)
                    s_con.commit()
                    chk = True
                    break
            if chk == False:
                tkinter.messagebox.showinfo("", "No such item found, please enter correct name")
            frm_sfbl.destroy()
            home()
            back_btn.destroy()
 
    def f_cmi():
        frame5.destroy()
 
        frm_cmi = Frame(root, height=483, width=430)
        frm_cmi.place(x=5, y=30)
        frm_cmi.configure(bg='#d9d9d9')
 
        top1 = Toplevel()
        top1.geometry("1200x300")
        scrl = Scrollbar(top1, orient='horizontal')
        scrl.pack(side=BOTTOM, fill=X)
        l2 = []
        f = "SELECT * FROM CMI"
        s_curs.execute(f)
        for i in s_curs:
            l2.append(i)
        print(l2)
        prdt = "                                Name                                    |   Price  |         Description       " + "\n"
        for i in l2:
            prdt += "|" + i[0] + " " * (70 - len(i[0])) + " "
            prdt += "|" + str(i[2]) + " " * (10 - len(str(i[2])))
            prdt += "|" + i[1] + " " * 10 + "\n"
        t1 = Label(frm_cmi, text="Enter the Product name/key word down below", font=("Arial", 18))
        t1.place(x=18, y=30)
 
        prod_name = Entry(frm_cmi, borderwidth=4)
        prod_name.place(x=123, y=150)
        b_cart = Button(frm_cmi, height=2, width=10, borderwidth=2, text="Add to cart", command=lambda: confirmCart())
        b_cart.place(x=169, y=350)
        t2 = Text(top1, width=229, height=20, wrap="none", xscrollcommand=scrl.set)
        scrl.config(command=t2.xview)
        t2.pack()
        t2.insert('end', prdt)
 
        def confirmCart():
            prod1 = prod_name.get()
            chk = False
            print(prod1)
            top1.destroy()
            for i in range(len(l2)):
                if str(prod1).lower() in l2[i][0].lower():
                    g = "insert into usrcart(PRODUCT, PRICE) values(%s, %s)"
                    lis = [(l2[i][0], l2[i][2])]
                    tkinter.messagebox.showinfo("", "Item added to cart successfully")
                    s_curs.executemany(g, lis)
                    s_con.commit()
                    chk = True
                    break
            if chk == False:
                tkinter.messagebox.showinfo("", "No such item found, please enter correct name")
            frm_cmi.destroy()
            home()
            back_btn.destroy()
 
    def f_b():
        frame5.destroy()
 
        frm_b = Frame(root, height=483, width=430)
        frm_b.place(x=5, y=30)
        frm_b.configure(bg='#d9d9d9')
 
        top1 = Toplevel()
        top1.geometry("1200x300")
        scrl = Scrollbar(top1, orient='horizontal')
        scrl.pack(side=BOTTOM, fill=X)
        l2 = []
        f = "SELECT * FROM B"
        s_curs.execute(f)
        for i in s_curs:
            l2.append(i)
        print(l2)
        prdt = "                                Name                                    |   Price  |         Description       " + "\n"
        for i in l2:
            prdt += "|" + i[0] + " " * (70 - len(i[0])) + " "
            prdt += "|" + str(i[2]) + " " * (10 - len(str(i[2])))
            prdt += "|" + i[1] + " " * 10 + "\n"
        t1 = Label(frm_b, text="Enter the Product name/key word down below", font=("Arial", 18))
        t1.place(x=18, y=30)
 
        prod_name = Entry(frm_b, borderwidth=4)
        prod_name.place(x=123, y=150)
        b_cart = Button(frm_b, height=2, width=10, borderwidth=2, text="Add to cart", command=lambda: confirmCart())
        b_cart.place(x=169, y=350)
        t2 = Text(top1, width=229, height=20, wrap="none", xscrollcommand=scrl.set)
        scrl.config(command=t2.xview)
        t2.pack()
        t2.insert('end', prdt)
 
        def confirmCart():
            prod1 = prod_name.get()
            chk = False
            print(prod1)
            top1.destroy()
            for i in range(len(l2)):
                if str(prod1).lower() in l2[i][0].lower():
                    print(prod1)
                    g = "insert into usrcart(PRODUCT, PRICE) values(%s, %s)"
                    lis = [(l2[i][0], l2[i][2])]
                    tkinter.messagebox.showinfo("", "Item added to cart successfully")
                    s_curs.executemany(g, lis)
                    s_con.commit()
                    chk = True
                    break
            if chk == False:
                tkinter.messagebox.showinfo("", "No such item found, please enter correct name")
            frm_b.destroy()
            home()
            back_btn.destroy()
 
 
def cartClick():
    top = Toplevel()
 
    frame6 = Frame(root, height=483, width=430)
    frame6.place(x=5, y=30)
    frame6.configure(bg='#d9d9d9')
 
    top.geometry("1200x300")
    s_con = mysql.connector.connect(host="localhost", user="root", password="", database="OnlineSeller")
    s_curs = s_con.cursor()
    g = "select * from usrcart"
    s_curs.execute(g)
    temp_l = []
    for i in s_curs:
        temp_l.append(i)
    checking = ''
    prn = "|                                       Name                                        |         Price         |\n"
    for i in temp_l:
        prn += "|" + i[0] + " " * (80 - len(i[0])) + ' '
        prn += "|" + str(i[1]) + " " * 10 + "\n"
 
    scrl = Scrollbar(top, orient='horizontal')
    scrl.pack(side=BOTTOM, fill=X)
 
    crt_dsply = Text(top, borderwidth=2, height=30, width=229, xscrollcommand=scrl.set)
    scrl.config(command=crt_dsply.xview)
    crt_dsply.pack(expand=True)
    crt_dsply.insert('end', prn)
 
    cnfrm_msg = Label(frame6, text="Would you like to proceed to checkout?", font=("Arial", 20))
    yes_btn = Button(frame6, text="Yes", padx=30, pady=15, borderwidth=2, command=lambda: yy())
    no_btn = Button(frame6, text="No", padx=30, pady=15, borderwidth=2, command=lambda: nn())
    cnfrm_msg.place(x=40, y=100)
    yes_btn.place(x=70, y=230)
    no_btn.place(x=265, y=230)
 
    def yy():
        top.destroy()
        yes_click()
 
    def nn():
        top.destroy()
        no_click()
 
    def yes_click():
        # top4 = Toplevel()
        frame6.destroy()
 
        top3 = Toplevel()
        top3.geometry("1200x300")
        s_con1 = mysql.connector.connect(host="localhost", user="root", password="", database="OnlineSeller")
        s_curs1 = s_con1.cursor()
 
        v_scr = Scrollbar(top3)
        v_scr.pack(side=RIGHT, fill=Y)
        h_scr = Scrollbar(top3, orient=HORIZONTAL)
        h_scr.pack(side=BOTTOM, fill=X)
 
        g = "select * from usrcart"
        s_curs1.execute(g)
        temp_l = []
        for i in s_curs1:
            temp_l.append(i)
        chkt_lbl = Label(top3, text="THIS IS YOUR CHECKOUT: ")
        # chkt_lbl.place(x=5, y=5)
        prn = "|                                      Name                                       |         Price         |\n"
        for i in temp_l:
            prn += "|" + i[0] + " " * (80 - len(i[0])) + ' '
            prn += "|" + str(i[1]) + " " * 10 + "\n"
 
        crt_dsply1 = Text(top3, yscrollcommand=v_scr.set, xscrollcommand=h_scr.set, width=150, height=60)
        crt_dsply1.insert(END, prn)
        crt_dsply1.pack(side=LEFT)
        v_scr.config(command=crt_dsply1.yview)
        h_scr.config(command=crt_dsply1.xview)
 
        q = "select * from usrcart"
        s_curs1.execute(q)
        temp_l = []
        for i in s_curs1:
            temp_l.append(i)
        lc = temp_l
        s = 0
        t_chng = 0
        for j in temp_l:
            s += int(j[1])
 
        frame7 = Frame(root, height=483, width=430)
        frame7.place(x=5, y=30)
        frame7.configure(bg='#d9d9d9')
 
        bill = Label(frame7, text="The bill total is: ", font=("Arial", 38))
        bill.place(x=90, y=50)
 
        price = "Rs. " + str(s)
        b1 = Label(frame7, text=price, font=("Arial", 26))
        b1.place(x=155, y=145)
 
        bill2 = Label(frame7, text="Thank you for Shopping with us, See you next time!", font=("Arial", 18))
        bill2.place(x=5, y=250)
 
        thx = PhotoImage(file=r"/Users/animesh/Documents/PycharmProjects/1st sem project/Thanks3.png")
        thx1 = thx.subsample(10,10)
        thx2 = Label(root, width=10, height=10, image=thx)
 
 
    def no_click():
        frame6.destroy()
        top.destroy()
        home()
 
 
def helpClick():
 
    tt = """
    
This is a platform we have created for those Shopaholic out 
there!!
 
•Please SIGN UP if you haven’t created an account. If you
already have an account please LOGIN.
 
•You can Then Search the items you want to shop. Now select the 
 Category from which you want to shop.
 
•The categories are as follows:
    MC → Mobiles and Computers 
    BHG→ Beauty, Health and Grocery
    SFBL→ Sports, fitness, bag and Luggage
    TAE → TV, Appliances and electronics 
    MFWF → Men’s and Women’s fashion
    CMI → Cars, MotorBikes and Industrial 
    B→ Books 
    HKP→ Home, Kitchen and Pets
 
•You can choose from the categories and select the items you
 want to buy.
 
•Once you are done selecting the items, you can view the 
 items in your cart. From there you can proceed to checkout
 or continue shopping.
 
 
 
 
 
 
 
~****************** HAPPY SHOPPING :) *********************~
"""
 
    txt = Text(root, borderwidth=1, width=60, height=37)
    txt.place(x=5, y=30)
    txt.insert(END, tt)
 
    def goback():
        txt.destroy()
        home()
        back_btn.destroy()
 
    back_btn = Button(root, text="Go back", height=2, width=9, command=lambda: goback())
    back_btn.place(x=30, y=525)
 
 
def home():
    frame4 = Frame(root, height=483, width=430)
    frame4.place(x=5, y=30)
    frame4.configure(bg='#d9d9d9')
 
    search_btn = Button(frame4, text="Search", padx=40, pady=15, command=lambda: act1())
    search_btn.place(x=147, y=100)
 
    cart_btn = Button(frame4, text="Cart", padx=40, pady=15, command=lambda: act2())
    cart_btn.place(x=155, y=210)
 
    help_btn = Button(frame4, text="Help", padx=40, pady=15, command=lambda: act3())
    help_btn.place(x=153, y=320)
 
    def act1():
        frame4.destroy()
        searchClick()
 
    def act2():
        frame4.destroy()
        cartClick()
 
    def act3():
        frame4.destroy()
        helpClick()
 
 
root.mainloop()
 
