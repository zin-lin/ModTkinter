
import ModTkinter
from ModTkinter import *
import re

def screen(self):
    e.insert(END,self)



def ac():
    e.delete(0, END)

def neg():
    ss= eval(e.get())
    e.delete(0,END)
    e.insert(END, str(-ss))

def per():
    ss= eval(e.get())
    e.delete(0,END)
    e.insert(END, str(ss/100))

f= ModTk()



f.title("Iphone-Type Calculator")

f.configure(bg="black")
f.tk.call('tk', 'scaling',2.7)

def Eq():
    try:
    
        
        p=e.get()
        r= re.split('[\+\-\*\/\**]', str(p))
        #print(r)
        for i in r:
            if re.match('0', i) and len(i)>1:
                print("true")
                t= i.replace("0","")
                o = str(p).replace(i,t)
                p= o

        p= eval(p)
        e.delete(0,END)
        e.insert(END, str(p))
    except:
        e.delete(0, END)
        e.insert(1,"Error")



ddp= Label(f ,bg=f['background'])
ddp.grid(row=0,column= 0, ipady= 18)

e= Entry(f, bg=f['background'], fg= "white", border= 0, font="Cosolas 20", width= 11 ,justify= RIGHT, insertbackground= "black")
e.grid(row= 1, column= 0, columnspan= 1)

fra = Frame(f, bg=f['background'])
fra.grid(row= 2, column= 0, columnspan= 1)

d= RoundButton(fra, text= "AC",font= "Consolas 9 bold", fg= "black", command= ac)
d.Type("Light")
d.grid(row= 1, column= 0, padx= 4 , pady= 7)

d= RoundButton(fra, text= "+/-",font= "Consolas 9 bold", fg= "black", command= neg)
d.Type("Light")
d.grid(row= 1, column= 1, padx= 4 , pady= 7)

d= RoundButton(fra, text= " % ",font= "Consolas 9 bold", fg= "black",command= per)
d.Type( "Light")
d.grid(row= 1, column=2, padx= 4 , pady= 7)

d= RoundButton(fra, text= "÷",font= "Consolas 9 bold", fg= "white",command=lambda:screen('/'))
d.Type("Orange")
d.grid(row= 1, column= 3, padx= 4 , pady= 7)

d7= RoundButton(fra, text= "7",font= "Consolas 9 bold", fg= "white", command=lambda:screen(7))
d7.Type("Dark")
d7.grid(row= 2, column= 0, padx= 4 , pady= 7)

d8= RoundButton(fra, text= "8",font= "Consolas 9 bold", fg= "white", command=lambda:screen(8))
d8.Type( "Dark")
d8.grid(row= 2, column= 1, padx= 4 , pady= 7)

d9= RoundButton(fra, text= "9",font= "Consolas 9 bold", fg= "white", command=lambda:screen(9))
d9.Type("Dark")
d9.grid(row= 2, column= 2, padx= 4 , pady= 7)

dx= RoundButton(fra, text= "x",font= "Consolas 9 bold", fg= "white",command=lambda:screen('*'))
dx.Type("Orange")
dx.grid(row= 2, column= 3, padx= 4 , pady= 7)

d4= RoundButton(fra, text= "4",font= "Consolas 9 bold", fg= "white", command=lambda:screen(4))
d4.Type("Dark")
d4.grid(row= 3, column= 0, padx= 4 , pady= 7)

d5= RoundButton(fra, text= "5",font= "Consolas 9 bold", fg= "white", command=lambda:screen(5))
d5.Type("Dark")
d5.grid(row= 3, column= 1, padx= 4 , pady= 7)

d6= RoundButton(fra, text= "6",font= "Consolas 9 bold", fg= "white", command=lambda:screen(6))
d6.Type("Dark")
d6.grid(row= 3, column= 2, padx= 4 , pady= 7)

dsub= RoundButton(fra, text= "-",font= "Consolas 9 bold", fg= "white",command=lambda:screen('-'))
dsub.Type("Orange")
dsub.grid(row= 3, column= 3, padx= 4 , pady= 7)


d1= RoundButton(fra, text= "1",font= "Consolas 9 bold", fg= "white", command=lambda:screen(1))
d1.Type("Dark")
d1.grid(row= 4, column= 0, padx= 4 , pady= 7)

d2= RoundButton(fra, text= "2",font= "Consolas 9 bold", fg= "white", command=lambda:screen(2))
d2.Type("Dark")
d2.grid(row= 4, column= 1, padx= 4 , pady= 7)

d3= RoundButton(fra, text= "3",font= "Consolas 9 bold", fg= "white", command=lambda:screen(3))
d3.Type("Dark")
d3.grid(row= 4, column= 2, padx= 4 , pady= 7)

dadd= RoundButton(fra, text= "+",font= "Consolas 9 bold", fg= "white",command=lambda:screen('+'))
dadd.Type( "Orange")
dadd.grid(row= 4, column= 3, padx= 4 , pady= 7)


d0= RoundButton(fra, text= "0",font= "Consolas 9 bold", fg= "white", command=lambda:screen(0))
d0.Type("Dark-Long",86)
d0.grid(row= 5, column= 0, padx= 4 , pady= 7, columnspan=2)

d3= RoundButton(fra, text= ".",font= "Consolas 9 bold", fg= "white",command=lambda:screen('.'))
d3.Type("Dark")
d3.grid(row= 5, column= 2, padx= 4 , pady= 7)

dadd= RoundButton(fra, text= "=",font= "Consolas 9 bold", fg= "white", command= Eq)
dadd.Type("Orange")
dadd.grid(row= 5, column= 3, padx= 4 , pady= 7)












f.mainloop()
