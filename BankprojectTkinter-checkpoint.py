#!/usr/bin/env python
# coding: utf-8

# In[1]:


def AccountIn():
            import tkinter as tk
            root=tk.Tk()
            root.configure(bg="gray")
            root.geometry("600x300")
            tk.Label(root,text=f" Welcome user",bg="black",fg="white",font=('Arial',20)).pack()
            tk.Label(root,text="AccNo",bg="black",fg="white",font=('Arial',15)).place(x=100,y=150)
            tk.Label(root,text="EnterPin",bg="black",fg="white",font=('Arial',15)).place(x=100,y=200)
            e1=tk.Entry(root)
            e1.place(x=200,y=150)
            e2=tk.Entry(root)
            e2.place(x=200,y=200)
            def checkin():
                accnum=int(e1.get())
                pin=int(e2.get())
                print(f"pin :{pin}")
                import mysql.connector as ms
                conn=ms.connect(host="localhost",user="root",password="",database="bank")
                cur=conn.cursor()
                qu=f"select * from  `{tablename}`"
                cur.execute(qu)
                data=cur.fetchall()
                #for i in data:
                    #print(i[3])
                #conn.close()
                if accnum==data[0][3] and pin==data[0][2]  :
                    def userdetails():
                        print("hello match")
                        import tkinter as tk
                        root=tk.Tk()
                        root.configure(bg="gray")
                        root.geometry("600x500")
                        tk.Label(root,text="Welcome our bank",bg="black",fg="white",font=('Arial',20)).pack()
                        e1=tk.Entry(root)
                        e1.place(x=255,y=100)
                        def deposits():
                                de=int(e1.get())
                                if de>0:
                                    acc.deposit(de)
                                    print("deposit:",de)
                                    import mysql.connector as ms
                                    conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                    query=f"insert into `{tablename}` values(%s,%s,%s,%s,%s)"
                                    dval=acc.getdeposit()
                                    value=(nm,dval,pin,accnum,acc.getbalance())
                                    msg.showinfo("msg",f" Deposit:,{acc.getdeposit()}")
                                    cur=conn.cursor()
                                    cur.execute(query,value)
                                    conn.commit()
                                    conn.close()
                                else:
                                    print("amount not valid")
                                    #msg.showinfo("msg","amount not valid")
                        def withdraw():
                            am=int(e1.get())
                            if acc.getbalance()>0:
                                acc.withdrawal(am)
                                import mysql.connector as ms
                                conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                query=f"insert into `{tablename}` values(%s,%s,%s,%s,%s)"
                                dval=acc.getwithdraw()
                                value=(nm,dval,pin,accnum,acc.getbalance())
                                cur=conn.cursor()
                                cur.execute(query,value)
                                conn.commit()
                                conn.close()
                                print("withdrawal:",am)
                                msg.showinfo("msg",f"with:,{acc.getwithdraw()}")
                            else:
                                print("amount not valid")
                                #tk.Label(root,text="amount not valid",bg="black",fg="white",font=('Arial',15)).place(x=200,y=350)
                        def getBalance():
                            print("bbl:",acc.getbalance())
                            tk.Label(root,text=f"New balance:,{acc.getbalance()}",bg="black",fg="white",font=('Arial',15)).place(x=200,y=350)
                        def histroy():
                            import mysql.connector as ms
                            conn=ms.connect(host="localhost",user="root",password="",database="bank")
                            qu=f"select * from `{tablename}`"
                            cur=conn.cursor()
                            cur.execute(qu)
                            print("hello")
                            data=cur.fetchall()
                            import tkinter as tk
                            root=tk.Tk()
                            root.title("Histroy")
                            root.configure(bg="gray")
                            root.geometry("600x400")
                            for i in data:
                                print(i)
                                tk.Label(root,text=f"{i}\n",font=('Arial',14),fg="white",bg="black").pack()
                            cur.close()
                            conn.close()
                        tk.Button(root,text="Deposit",bg="blue",fg="white",command=deposits,font=('Arial',16)).place(x=100,y=150)
                        tk.Button(root,text="Withdraw",bg="blue",fg="white",command=withdraw,font=('Arial',16)).place(x=100,y=225)
                        tk.Button(root,text="Balance Check",bg="blue",fg="white",command=getBalance,font=('Arial',16)).place(x=400,y=150)
                        tk.Button(root,text="Change pin",bg="blue",fg="white",command=checkin,font=('Arial',16)).place(x=400,y=225)
                        tk.Button(root,text="Histroy",bg="blue",fg="white",command=histroy,font=('Arial',16)).place(x=400,y=300)
                        tk.Button(root,text="transaction",bg="red",fg="white",command=transactions,font=('Arial',16)).place(x=100,y=300)
                    userdetails()
                else:
                    print("not match")
            tk.Button(root,text="submit",bg="blue",fg="white",command=checkin,font=('Arial',16)).place(x=235,y=230)
            #


# In[3]:


def main():
    import tkinter as tk
    root=tk.Tk()
    root.title("Bank")
    root.configure(bg="gray")
    root.geometry("600x300")
    class Account():
            _balance=0
            _pin=0
            name=""
            _withdrawal=0
            _deposit=0
            def __init__(self):
                print("hello")
            def user(self,name):
                self.name=name
                print("name: ",self.name)
            def deposit(self,amount):
                self._balance+=amount
                self._deposit=amount
                print(f"total balance: {self._balance}\n deposit amount{amount}")
        
            def withdrawal(self,amount):
                self._balance-=amount
                self._withdrawal=amount
                print(f"total balance: {self._balance}\n withdrawal amount{amount}")
        
            def getbalance(self):
                return self._balance

            def generatepin(self,pin):
                self._pin=pin
                print("pin ",self._pin)

            def getpin(self):
                return self._pin
            def getusername(self):
                return self.name
            def getwithdraw(self):
                return self._withdrawal
            def getdeposit(self):
                return self._deposit
    acc=Account()
    acc.getbalance()
    acc.getdeposit()
    acc.getwithdraw()
    wamount=0
    dval=0
    def AccountOpen():    
            root=tk.Tk()
            root.configure(bg="gray")
            root.geometry("600x500")
            tk.Label(root,text="Welcome to our Bank ",bg="black",fg="white",font=('Arial',20)).pack()
            tk.Label(root,text="name",bg="black",fg="white",font=('Arial',15)).place(x=100,y=100)
            e1=tk.Entry(root)
            e1.place(x=250,y=100)
            tk.Label(root,text="age minimum 15 years",bg="red",fg="white",font=('Arial',8)).place(x=250,y=135)
            tk.Label(root,text="age",bg="black",fg="white",font=('Arial',15)).place(x=100,y=150)
            e4=tk.Entry(root)
            e4.place(x=250,y=150)
            tk.Label(root,text="amount",bg="black",fg="white",font=('Arial',16)).place(x=100,y=210)
            tk.Label(root,text="minimum amount 1000",bg="red",fg="white",font=('Arial',8)).place(x=250,y=195)
            e2=tk.Entry(root)
            e2.place(x=250,y=210)
            tk.Label(root,text="generatePin",bg="black",fg="white",font=('Arial',14)).place(x=100,y=260)
            tk.Label(root,text="pin minimum 4 number",bg="red",fg="white",font=('Arial',8)).place(x=250,y=240)
            e3=tk.Entry(root,show="*")
            e3.place(x=250,y=260)
            def getdata():
                global nm
                nm=e1.get()
                am=int(e2.get())
                global pin
                pin=int(e3.get())
                ag=int(e4.get())
                if am>=1000 and len(str(pin))>=4 and ag>=15:
                    acc.deposit(am)
                    acc.generatepin(pin)
                    acc.user(nm)
                    def newtable():
                            import mysql.connector as ms
                            con=ms.connect(host="localhost",user="root",password="",database="bank")
                            cursor=con.cursor()
                            global tablename
                            tablename=f"{nm}{ag}"
                            qu=f"create table `{tablename}` (name varchar(20),damount int,pin int,AccNo int,wamount int,bbl int)"
                            #qu1="create table  Alluserdetail (name varchar(20),pin int,AccNo int,tablenames varchar(20))"
                            cursor.execute(qu)
                            con.commit()
                            con.close
                            #cursor.execute(qu1)
                            import random as rd
                            num=rd.randint(1000,9999)
                            num
                            print(num)
                            qu3=f"insert into `{tablename}` values(%s,%s,%s,%s,%s,%s)"
                            qu4="insert into Alluserdetail values(%s,%s,%s,%s)"
                            val=(nm,am,pin,num,wamount,am)
                            val4=(nm,pin,num,tablename)
                            cursor.execute(qu3,val)
                            cursor.execute(qu4,val4)
                            con.commit()
                            con.close()
                            tk.Label(root,text=f"Congratulations! Your account is now active \n account number: {num} pin:{pin}").place(x=100,y=340)
                    newtable()
                    e1.delete(0, tk.END)
                    e2.delete(0, tk.END)
                    e3.delete(0, tk.END)
                    e4.delete(0, tk.END)
                    def AccountIn():
                            import tkinter as tk
                            root=tk.Tk()
                            root.configure(bg="gray")
                            root.geometry("600x300")
                            tk.Label(root,text=f" Welcome user",bg="black",fg="white",font=('Arial',20)).pack()
                            tk.Label(root,text="AccNo",bg="black",fg="white",font=('Arial',15)).place(x=100,y=150)
                            tk.Label(root,text="EnterPin",bg="black",fg="white",font=('Arial',15)).place(x=100,y=200)
                            e1=tk.Entry(root)
                            e1.place(x=200,y=150)
                            e2=tk.Entry(root)
                            e2.place(x=200,y=200)
                            def checkin():
                                accnum=int(e1.get())
                                pin=int(e2.get())
                                print(f"pin :{pin}")
                                import mysql.connector as ms
                                conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                cur=conn.cursor()
                                qu=f"select * from  `{tablename}`"
                                cur.execute(qu)
                                data=cur.fetchall()
                                if accnum==data[0][3] and pin==data[0][2]  :
                                    def userdetails():
                                        print("hello match")
                                        import tkinter as tk
                                        root=tk.Tk()
                                        root.configure(bg="gray")
                                        root.geometry("600x500")
                                        tk.Label(root,text="Welcome our bank",bg="black",fg="white",font=('Arial',20)).pack()
                                        e1=tk.Entry(root)
                                        e1.place(x=255,y=100)
                                        def deposits():
                                                wamount=0
                                                de=int(e1.get())
                                                if de>0:
                                                    acc.deposit(de)
                                                    print("deposit:",de)
                                                    import mysql.connector as ms
                                                    conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                                    query=f"insert into `{tablename}` values(%s,%s,%s,%s,%s,%s)"
                                                    dval=acc.getdeposit()
                                                    nbb=acc.getbalance()
                                                    value=(nm,dval,pin,accnum,wamount,nbb)
                                                    cur=conn.cursor()
                                                    cur.execute(query,value)
                                                    conn.commit()
                                                    tk.Label(root,text="Deposit:: Success",bg="black",fg="white",font=('Arial',15)).place(x=200,y=330)
                                                    e1.delete(0, tk.END)
                                                    conn.close()
                                                else:
                                                    print("amount not valid")
                                                    #msg.showinfo("msg","amount not valid")
                                        def withdraw():
                                            am=int(e1.get())
                                            getbb=acc.getbalance()
                                            dval=0
                                            if 0<am<=getbb:
                                                acc.withdrawal(am)
                                                import mysql.connector as ms
                                                conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                                query=f"insert into `{tablename}` values(%s,%s,%s,%s,%s,%s)"
                                                wamount=acc.getwithdraw()
                                                nbb=acc.getbalance()
                                                value=(nm,dval,pin,accnum,wamount,nbb)
                                                cur=conn.cursor()
                                                cur.execute(query,value)
                                                conn.commit()
                                                conn.close()
                                                print("withdrawal:",am)
                                                e1.delete(0, tk.END)
                                                tk.Label(root,text="withdrawal:: Success",bg="black",fg="white",font=('Arial',15)).place(x=200,y=330)
                                            else:
                                                print("amount not valid")
                                                tk.Label(root,text="amount not valid",bg="black",fg="white",font=('Arial',15)).place(x=200,y=330)
                                        def getBalance():
                                            bbl=acc.getbalance()
                                            print("bbl:",bbl)
                                            tk.Label(root,text=f"New balance:,{bbl}",bg="black",fg="white",font=('Arial',15)).place(x=200,y=350)
                                        def histroy():
                                            import mysql.connector as ms
                                            conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                            qu=f"select * from `{tablename}`"
                                            cur=conn.cursor()
                                            cur.execute(qu)
                                            print("hello")
                                            data=cur.fetchall()
                                            import tkinter as tk
                                            root=tk.Tk()
                                            root.title("Histroy")
                                            root.configure(bg="gray")
                                            root.geometry("600x400")
                                            for i in data:
                                                print(i)
                                                tk.Label(root,text=(f"name:{i[0]}\t pin:{i[2]}\t Accno:{i[3]} \t deposit {i[1]} \t withdrawl {i[4]} \t New balance:{i[5]}"),font=('Arial',8),fg="white",bg="black").pack()
                                            conn.close()
                                        tk.Button(root,text="Deposit",bg="blue",fg="white",command=deposits,font=('Arial',16)).place(x=100,y=150)
                                        tk.Button(root,text="Withdraw",bg="blue",fg="white",command=withdraw,font=('Arial',16)).place(x=100,y=225)
                                        tk.Button(root,text="Balance Check",bg="blue",fg="white",command=getBalance,font=('Arial',16)).place(x=400,y=150)
                                        tk.Button(root,text="Change pin",bg="blue",fg="white",command=checkin,font=('Arial',16)).place(x=400,y=225)
                                        tk.Button(root,text="Histroy",bg="blue",fg="white",command=histroy,font=('Arial',16)).place(x=400,y=300)
                                    userdetails()
                                else:
                                    print("not match")
                            tk.Button(root,text="submit",bg="blue",fg="white",command=checkin,font=('Arial',16)).place(x=235,y=230)
                    AccountIn()         
                else:
                   tk.Label(root,text=f"not valid data try again").place(x=100,y=330)
                print(f"{nm}\n{am}\n{pin}")
            tk.Button(root,text="submit",bg="blue",fg="white",font=('Arial',16),command=getdata).place(x=250,y=320)
    def AccountCheckIn():
            import tkinter as tk
            root=tk.Tk()
            root.configure(bg="gray")
            root.geometry("600x300")
            unm=acc.getusername()
            tk.Label(root,text=f" Welcome,{unm}",bg="black",fg="white",font=('Arial',20)).pack()
            tk.Label(root,text="AccNo",bg="black",fg="white",font=('Arial',15)).place(x=100,y=150)
            tk.Label(root,text="EnterPin",bg="black",fg="white",font=('Arial',15)).place(x=100,y=200)
            e1=tk.Entry(root)
            e1.place(x=200,y=150)
            e2=tk.Entry(root)
            e2.place(x=200,y=200)
            def checkin():
                accnum=int(e1.get())
                pin=int(e2.get())
                print(f"pin :{pin}acc:{accnum}")
                import mysql.connector as ms
                con=ms.connect(host="localhost",user="root",password="",database="bank")
                cur=con.cursor()
                qu2="select tablenames from alluserdetail where AccNo=%s and pin=%s"
                value=(accnum,pin)
                cur.execute(qu2,value)
                da=cur.fetchall()
                print(type(da))
                b=len(da)
                print(b)
                if b>0:
                    tbnm=da[0][0]
                    print("match",tbnm)
                    #con.close()
                    def userdetails():
                        print("hello match")
                        import tkinter as tk
                        root=tk.Tk()
                        root.configure(bg="gray")
                        root.geometry("100x100")
                        tk.Label(root,text="Data Match").pack()
                        import tkinter as tk
                        root=tk.Tk()
                        root.configure(bg="gray")
                        root.geometry("600x500")
                        tk.Label(root,text="Welcome to your Home Page",bg="black",fg="white",font=('Arial',15)).pack()
                        e1=tk.Entry(root)
                        e1.place(x=255,y=100)
                        def deposits():
                                de=int(e1.get())
                                if de>0:
                                    acc.deposit(de)
                                    print("deposit:",de)
                                    import mysql.connector as ms
                                    conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                    query=f"insert into `{tbnm}` values(%s,%s,%s,%s,%s,%s)"
                                    dval=acc.getdeposit()
                                    qu=f"select * from `{tbnm}` ORDER BY AccNo DESC LIMIT 1"
                                    cur=conn.cursor()
                                    cur.execute(qu)
                                    data=cur.fetchall()
                                    if data:
                                        bb=data[0][5]
                                        print(bb)
                                        ttbl=dval+bb
                                        nms=data[0][0]
                                        value=(nms,dval,pin,accnum,wamount,ttbl)
                                        tk.Label(root,text="Deposit:: Success",bg="black",fg="white",font=('Arial',15)).place(x=200,y=330)
                                        #tk.Label(root,text=f" Deposit:,{acc.getdeposit()}",bg="black",fg="white",font=('Arial',15)).place(x=200,y=330)
                                        cur=conn.cursor()
                                        cur.execute(query,value)
                                        conn.commit()
                                        conn.close()
                                        e1.delete(0, tk.END)
                                    else:
                                        print("empty")
                                else:
                                    print("amount not valid")
                                    tk.Label(root,text="Deposit:amount not valid",bg="black",fg="white",font=('Arial',15)).place(x=200,y=330)
                                    #msg.showinfo("msg","amount not valid")
                        def withdraw():
                            am=int(e1.get())
                            import mysql.connector as ms
                            conn=ms.connect(host="localhost",user="root",password="",database="bank")
                            qu=f"select * from `{tbnm}` ORDER BY AccNo DESC LIMIT 1"
                            cur=conn.cursor()
                            cur.execute(qu)
                            data=cur.fetchall()
                            bb=data[0][5]
                            print(bb)
                            print("bbl:",bb)
                            conn.close()
                            if 0<am<=bb:
                                acc.withdrawal(am)
                                import mysql.connector as ms
                                conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                query=f"insert into `{tbnm}` values(%s,%s,%s,%s,%s,%s)"
                                wamount=acc.getwithdraw()
                                qu=f"select * from `{tbnm}` ORDER BY AccNo DESC LIMIT 1"
                                cur=conn.cursor()
                                cur.execute(qu)
                                data=cur.fetchall()
                                if data:
                                    bb=data[0][5]
                                    print(bb)
                                    ttbl=bb-wamount
                                    nms=data[0][0]
                                    value=(nms,dval,pin,accnum,wamount,ttbl)
                                    cur=conn.cursor()
                                    cur.execute(query,value)
                                    conn.commit()
                                    conn.close()
                                    print("withdrawal:",am)
                                    #tk.Label(root,text=f"withdrawl:{am}",bg="black",fg="white",font=('Arial',15)).place(x=200,y=350)
                                    tk.Label(root,text="withdrawl Success",bg="black",fg="white",font=('Arial',15)).place(x=200,y=330)
                                    e1.delete(0, tk.END)
                                    
                                else:
                                   print("empty")
                            else:
                                print("amount not valid")
                                tk.Label(root,text="withdrawl amount not valid",bg="black",fg="white",font=('Arial',15)).place(x=200,y=330)
                                
                        def getBalance():
                                import mysql.connector as ms
                                conn=ms.connect(host="localhost",user="root",password="",database="bank")
                                qu=f"select * from `{tbnm}` ORDER BY AccNo DESC LIMIT 1"
                                cur=conn.cursor()
                                cur.execute(qu)
                                data=cur.fetchall()
                                if data:
                                    bb=data[0][5]
                                    print(bb)
                                    print("bbl:",bb)
                                    tk.Label(root,text=f"New balance:,{bb}",bg="black",fg="white",font=('Arial',15)).place(x=200,y=370)
                                    conn.close()
                        def pinchange():
                               import tkinter as tk
                               root=tk.Tk()
                               root.configure(bg="gray")
                               root.geometry("600x300")
                               unm=acc.getusername()
                               tk.Label(root,text=f" Welcome,{unm}",bg="black",fg="white",font=('Arial',20)).pack()
                               tk.Label(root,text="oldpin",bg="black",fg="white",font=('Arial',15)).place(x=100,y=150)
                               tk.Label(root,text="newpin",bg="black",fg="white",font=('Arial',15)).place(x=100,y=200)
                               e1=tk.Entry(root)
                               e1.place(x=200,y=150)
                               e2=tk.Entry(root)
                               e2.place(x=200,y=200)
                               def checkpin():
                                     oldpin=int(e1.get())
                                     newpin=int(e2.get())
                                     print(f"pin :{pin}acc:{accnum}")
                                     import mysql.connector as ms
                                     con=ms.connect(host="localhost",user="root",password="",database="bank")
                                     cur=con.cursor()
                                     qu=f"select * from `{tbnm}`"
                                     cur.execute(qu)
                                     data=cur.fetchall()
                                     a=data[0][2]
                                     ac=data[0][3]
                                     print("old pin",a)
                                     if oldpin==a:
                                             query=f"update `{tbnm}` set pin =%s where AccNo=%s"
                                             query1="update alluserdetail set pin =%s where AccNo=%s"
                                             val=(newpin,ac)
                                             cur.execute(query,val)
                                             cur.execute(query1,(newpin,ac))
                                             con.commit()
                                             qu=f"select * from `{tbnm}`"
                                             cur.execute(qu)
                                             data=cur.fetchall()
                                             newpin=data[0][2]
                                             print("newpin",newpin)
                                             con.close()
                                             import tkinter as tk
                                             root=tk.Tk()
                                             root.configure(bg="gray")
                                             root.geometry("100x100")
                                             tk.Label(root,text=f"new pin{newpin}  ").pack()
                                     else:
                                       print("old pin check")
                                       import tkinter as tk
                                       root=tk.Tk()
                                       root.configure(bg="gray")
                                       root.geometry("100x100")
                                       tk.Label(root,text="old pin check").pack()
                               tk.Button(root,text="Submit",bg="blue",fg="white",command=checkpin,font=('Arial',16)).place(x=130,y=200)
                        def histroy():
                            import mysql.connector as ms
                            conn=ms.connect(host="localhost",user="root",password="",database="bank")
                            qu=f"select * from `{tbnm}`"
                            cur=conn.cursor()
                            cur.execute(qu)
                            print("hello")
                            data=cur.fetchall()
                            import tkinter as tk
                            root=tk.Tk()
                            root.title("Histroy")
                            root.configure(bg="gray")
                            root.geometry("600x400")
                            for i in data:
                                #print(i)
                                print(f"name:{i[0]}\t pin:{i[2]}\t Accno:{i[3]} \t deposit {i[1]} \t withdrawl {i[4]} \t New balance:{i[5]}")
                                tk.Label(root,text=(f"name:{i[0]}\t pin:{i[2]}\t Accno:{i[3]} \t deposit {i[1]} \t withdrawl {i[4]} \t New balance:{i[5]}"),font=('Arial',8),fg="white",bg="black").pack()
                                conn.close()
                        def transactions():
                            import tkinter as tk
                            root=tk.Tk()
                            root.configure(bg="gray")
                            root.geometry("600x500")
                            tk.Label(root,text=" Transactions Page",bg="black",fg="white",font=('Arial',20)).pack()
                            tk.Label(root,text="SenderAccNo",bg="black",fg="white",font=('Arial',15)).place(x=100,y=100)
                            e1=tk.Entry(root)
                            e1.place(x=250,y=100)
                            def exists():
                                sender=int(e1.get())
                                import mysql.connector as ms
                                con=ms.connect(host="localhost",user="root",password="",database="bank")
                                cur=con.cursor()
                                query="select tablenames from alluserdetail where AccNo=%s"
                                cur.execute(query,(sender,))
                                data=cur.fetchall()
                                print(data)
                                if len(data)>0:
                                    def sendmoney():
                                          print("found")
                                          import tkinter as tk
                                          root=tk.Tk()
                                          root.configure(bg="gray")
                                          root.geometry("600x500")
                                          tk.Label(root,text=" Send Money here",bg="black",fg="white",font=('Arial',20)).pack()
                                          tk.Label(root,text="amount",bg="black",fg="white",font=('Arial',15)).place(x=100,y=100)
                                          tk.Label(root,text="pin",bg="black",fg="white",font=('Arial',15)).place(x=100,y=150)
                                          e1=tk.Entry(root)
                                          e2=tk.Entry(root)
                                          e1.place(x=250,y=100)
                                          e2.place(x=250,y=150)
                                          newtbnm=data[0][0]
                                          query1=f"select * from `{newtbnm}` ORDER BY AccNo DESC LIMIT 1"
                                          cur.execute(query1)
                                          data1=cur.fetchall()
                                          print(data1)
                                          sebb=data1[0][5]
                                          print("sender total balcnce",sebb)
                                          query2=f"select * from `{tbnm}` ORDER BY AccNo DESC LIMIT 1"
                                          cur.execute(query2)
                                          data2=cur.fetchall()
                                          print(data2)
                                          bb=data2[0][5]
                                          pinuser=data2[0][2]
                                          print("bank balnce user",bb)
                                          print("pin  user",pinuser)
                                          print("bbl:",bb)
                                          def senddata():
                                               sendmo=int(e1.get())
                                               upin=int(e2.get())
                                               if bb>0 and bb>sendmo and upin==pinuser:
                                                  print("balnce",bb)
                                                  acc.withdrawal(sendmo)
                                                  wamt=acc.getwithdraw()
                                                  print("withdrawl amount after transaction ",wamt)
                                                  query2=f"insert into `{tbnm}` values(%s,%s,%s,%s,%s,%s)"
                                                  nms=data2[0][0]
                                                  dval=0
                                                  pin=data2[0][2]
                                                  accnum=data2[0][3]
                                                  ttbl=bb-wamt
                                                  print("bank balance  after transaction bank balance ",ttbl)
                                                  value2=(nms,dval,pin,accnum,wamt,ttbl)
                                                  cur.execute(query2,value2)
                                                  con.commit()
                                                  query3=f"insert into `{newtbnm}` values(%s,%s,%s,%s,%s,%s)"
                                                  nms=data1[0][0]
                                                  acc.deposit(wamt)
                                                  dval=acc.getdeposit()
                                                  print("tranfer/deposit amount after transaction",dval)
                                                  pin=data1[0][2]
                                                  accnum=data1[0][3]
                                                  ttbl=sebb+wamt
                                                  print("sender total new balcnce after transaction",ttbl)
                                                  wi=0
                                                  value3=(nms,dval,pin,accnum,wi,ttbl)
                                                  cur.execute(query3,value3)
                                                  con.commit()
                                                  import tkinter as tk
                                                  root=tk.Tk()
                                                  root.configure(bg="gray")
                                                  root.geometry("100x100")
                                                  tk.Label(root,text=f"Payment Success:{wamt}").pack()
                                               else:
                                                 print("data not valid")
                                                 import tkinter as tk
                                                 root=tk.Tk()
                                                 root.configure(bg="gray")
                                                 root.geometry("100x100")
                                                 tk.Label(root,text="data not valid").pack()
                                          tk.Button(root,text="Submit",bg="blue",fg="white",command=senddata,font=('Arial',16)).place(x=130,y=200)
                                    sendmoney()
                                    tk.Button(root,text="Submit",bg="blue",fg="white",command=exists,font=('Arial',16)).place(x=100,y=150)
                                else:
                                    print("notfound")
                            tk.Button(root,text="Submit",bg="blue",fg="white",command=exists,font=('Arial',16)).place(x=100,y=150)
                        tk.Button(root,text="Deposit",bg="blue",fg="white",command=deposits,font=('Arial',16)).place(x=100,y=150)
                        tk.Button(root,text="Withdraw",bg="blue",fg="white",command=withdraw,font=('Arial',16)).place(x=100,y=225)
                        tk.Button(root,text="Balance Check",bg="blue",fg="white",command=getBalance,font=('Arial',16)).place(x=400,y=150)
                        tk.Button(root,text="Change pin",bg="blue",fg="white",command=pinchange,font=('Arial',16)).place(x=400,y=225)
                        tk.Button(root,text="Histroy",bg="blue",fg="white",command=histroy,font=('Arial',16)).place(x=400,y=300)
                        tk.Button(root,text="transaction",bg="red",fg="white",command=transactions,font=('Arial',16)).place(x=100,y=300)
                    userdetails()
                else:
                    print("not match")
                    import tkinter as tk
                    root=tk.Tk()
                    root.configure(bg="gray")
                    root.geometry("100x100")
                    tk.Label(root,text="Data Not Found").pack()
                    #msg.showinfo("msg","Accno and pin not match try again")
            tk.Button(root,text="submit",bg="blue",fg="white",command=checkin,font=('Arial',16)).place(x=235,y=210)
             #tk.Button(root,text="submit",bg="blue",fg="white",font=('Arial',16),command=getdata).place(x=300,y=320)
    tk.Label(root,text="Welcome To Maharishi Arvind College",bg="black",fg="white",font=('Arial',20)).pack()
    tk.Button(root,text="Account open",bg="black",fg="white",command=AccountOpen,font=('Arial',16)).place(x=125,y=150)
    tk.Button(root,text="Account CheckIn",bg="black",fg="white",command=AccountCheckIn,font=('Arial',16)).place(x=310,y=150)
    root.mainloop()
main()  


# In[ ]:




