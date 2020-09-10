import d
from d import*
import tkinter as tk
from tkinter import ttk
import ttkthemes
from ttkthemes import ThemedStyle
import time
from tkinter import font
from tkinter import *
import PIL
from PIL import Image, ImageTk
import io
import numpy as np

u = ModTk()
######################################################################





###############################################################fonts#####



fonti  = ("Segoe UI", 8, "normal")
fo = ("Segoe UI", 7, "normal")
fo1 = ("Segoe UI", 6, "normal")

################################################################################################################################
class TkButton(tk.Button):
    name = ""
    parent= ""

    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    
        
    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())

        self.configure(bg = self.bgb.get(), fg = self.fgb.get(), font = ((self.fontb.get(),int(self.fontsizeb.get()))), bd = int(self.bdb.get()) )
        self.configure(text = self.text.get())

        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)

        #34343434343434
        self.x = ttk.Entry(fr , font = fo)
        self.x.grid(row = 5, column  = 0)
        
        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Entry(fr , font = fo)
        self.y.grid(row = 7, column  = 0)


        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())

        ################
        
        l5 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "background:", font = "Consolas 10")
        l5.grid(row = 9, column  = 0,sticky = W)


        self.bgb = ttk.Entry(fr , font = fo)
        self.bgb.grid(row = 10, column  = 0)
        self.bgb.insert(1,self['bg'])

        l6 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "foreground:", font = "Consolas 10")
        l6.grid(row = 11, column  = 0,sticky = W)


        self.fgb = ttk.Entry(fr , font = fo)
        self.fgb.grid(row = 12, column  = 0)
        self.fgb.insert(1, self['fg'])

        l7 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "font:", font = "Consolas 10")
        l7.grid(row = 13, column  = 0,sticky = W)


        self.fontb = ttk.Combobox(fr , font = fo, values = list(font.families()))
        self.fontb.grid(row = 14, column  = 0)
        self.fontb.insert(1,"Consolas")

        l8 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "fontsize:", font = "Consolas 10")
        l8.grid(row = 15, column  = 0,sticky = W)
        


        self.fontsizeb = ttk.Combobox(fr , font = fo, values =  ["1","2","3","4","5","6","7","8","9","10"])
        self.fontsizeb.grid(row = 16, column  = 0)
        self.fontsizeb.insert(1, 9)
                 
        l9 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "borderwidth:", font = "Consolas 10")
        l9.grid(row = 17, column  = 0,sticky = W)


        self.bdb = ttk.Combobox(fr , font = fo, values =  ["0","1","2","3","4","5","6","7","8","9","10"])
        self.bdb.grid(row = 18, column  = 0)
        self.bdb.insert(1, self['borderwidth'])

        text = Label(fr, font = fo , text = "Text:", bg = fr['bg'], fg ="#0078ff",)
        text.grid(row= 19, column = 0)

        self.text = ttk.Entry(fr, font = fo)
        self.text.grid(row = 20, column = 0)
        self.text.insert(self[text])

        


        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 100,column = 0, sticky = E)
                 
        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 200,column = 0, sticky = E)
                 
        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())

        

    def __init__(self,master, **ar):
        Button.__init__(self, master, ar)
        

        self.bind("<Button-1>",self.click )
        self.bind("<B1-Motion>", self.draggable)








def Zero():
    def selfmaker():
        if parent.get()=="root":
            s = TkButton(t, text = "Tk Button" , font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

        else:
          
            s = TkButton(eval(parent.get()), text = "Tk Button" , font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

    global fr

    try:
        fr.destroy()
    except:pass

    l.configure(text = "Button")    
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker)
    ss.grid(row = 8,column = 0, sticky = E)

#########################################################################################################################################

class TkLabel(tk.Label):
    name = ""
    parent= ""
    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    
    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())



        self.configure(bg = self.bgb.get(), fg = self.fgb.get(), font = ((self.fontb.get(),int(self.fontsizeb.get()))), bd = int(self.bdb.get()) )
        self.configure(text = self.text.get())
        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)


        self.x = ttk.Entry(fr , font = fo)
        self.x.grid(row = 5, column  = 0)
        
        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Entry(fr , font = fo)
        self.y.grid(row = 7, column  = 0)


        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())

        ################
        
        l5 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "background:", font = "Consolas 10")
        l5.grid(row = 9, column  = 0,sticky = W)


        self.bgb = ttk.Entry(fr , font = fo)
        self.bgb.grid(row = 10, column  = 0)
        self.bgb.insert(1,self['bg'])

        l6 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "foreground:", font = "Consolas 10")
        l6.grid(row = 11, column  = 0,sticky = W)


        self.fgb = ttk.Entry(fr , font = fo)
        self.fgb.grid(row = 12, column  = 0)
        self.fgb.insert(1, self['fg'])

        l7 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "font:", font = "Consolas 10")
        l7.grid(row = 13, column  = 0,sticky = W)


        self.fontb = ttk.Combobox(fr , font = fo, values = list(font.families()))
        self.fontb.grid(row = 14, column  = 0)
        self.fontb.insert(1,"Consolas")

        l8 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "fontsize:", font = "Consolas 10")
        l8.grid(row = 15, column  = 0,sticky = W)
        


        self.fontsizeb = ttk.Combobox(fr , font = fo, values =  ["1","2","3","4","5","6","7","8","9","10"])
        self.fontsizeb.grid(row = 16, column  = 0)
        self.fontsizeb.insert(1, 9)
                 
        l9 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "borderwidth:", font = "Consolas 10")
        l9.grid(row = 17, column  = 0,sticky = W)


        self.bdb = ttk.Combobox(fr , font = fo, values =  ["0","1","2","3","4","5","6","7","8","9","10"])
        self.bdb.grid(row = 18, column  = 0)
        self.bdb.insert(1, self['borderwidth'])



        text = Label(fr, font = fo , text = "Text:", bg = fr['bg'], fg ="#0078ff",)
        text.grid(row= 19, column = 0)

        self.text = ttk.Entry(fr, font = fo)
        self.text.grid(row = 20, column = 0)
        self.text.insert(self[text])

        
        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 100,column = 0, sticky = E)
                 
        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 200,column = 0, sticky = E)
                 
        

        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())

        

    def __init__(self,master, **ar):
        Label.__init__(self, master, ar)
        

        self.bind("<Button-1>",self.click )
        self.bind("<B1-Motion>", self.draggable)







def Zero1():

    def selfmaker1():
        if parent.get()=="root":
            s = TkLabel(t, text = "Tk Label" , font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

        else:
          
            s = TkLabel(eval(parent.get()), text = "Tk Label" , font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

    global fr

    try:
        fr.destroy()
    except:pass

    l.configure(text = "Label")
        
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker1)
    ss.grid(row = 8,column = 0, sticky = E)
    
####################################################################################################################

class TkEntry(tk.Entry):
    name = ""
    parent= ""
    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    
    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())


        self.configure(bg = self.bgb.get(), fg = self.fgb.get(), font = ((self.fontb.get(),int(self.fontsizeb.get()))), bd = int(self.bdb.get()) )



        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)


        self.x = ttk.Entry(fr , font = fo)
        self.x.grid(row = 5, column  = 0)
        
        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Entry(fr , font = fo)
        self.y.grid(row = 7, column  = 0)


        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())

        ################
        
        l5 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "background:", font = "Consolas 10")
        l5.grid(row = 9, column  = 0,sticky = W)


        self.bgb = ttk.Entry(fr , font = fo)
        self.bgb.grid(row = 10, column  = 0)
        self.bgb.insert(1,self['bg'])

        l6 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "foreground:", font = "Consolas 10")
        l6.grid(row = 11, column  = 0,sticky = W)


        self.fgb = ttk.Entry(fr , font = fo)
        self.fgb.grid(row = 12, column  = 0)
        self.fgb.insert(1, self['fg'])

        l7 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "font:", font = "Consolas 10")
        l7.grid(row = 13, column  = 0,sticky = W)


        self.fontb = ttk.Combobox(fr , font = fo, values = list(font.families()))
        self.fontb.grid(row = 14, column  = 0)
        self.fontb.insert(1,"Consolas")

        l8 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "fontsize:", font = "Consolas 10")
        l8.grid(row = 15, column  = 0,sticky = W)
        


        self.fontsizeb = ttk.Combobox(fr , font = fo, values =  ["1","2","3","4","5","6","7","8","9","10"])
        self.fontsizeb.grid(row = 16, column  = 0)
        self.fontsizeb.insert(1, 9)
                 
        l9 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "borderwidth:", font = "Consolas 10")
        l9.grid(row = 17, column  = 0,sticky = W)


        self.bdb = ttk.Combobox(fr , font = fo, values =  ["0","1","2","3","4","5","6","7","8","9","10"])
        self.bdb.grid(row = 18, column  = 0)
        self.bdb.insert(1, self['borderwidth'])

        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 19,column = 0, sticky = E)
                 
        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 20,column = 0, sticky = E)
                 
        

        


            
        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())

        

    def __init__(self,master, **ar):
        Entry.__init__(self, master, ar)
        

        self.bind("<Button-1>",self.click )
        self.bind("<B1-Motion>", self.draggable)



def Zero2():
    def selfmaker1():
        if parent.get()=="root":
            s = TkEntry(t, text = "Tk Label" , font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

        else:
          
            s = TkEntry(eval(parent.get()), text = "Tk Label" , font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

    global fr

    try:
        fr.destroy()
    except:pass

    l.configure(text = " Tk Entry")
        
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker1)
    ss.grid(row = 8,column = 0, sticky = E)

#####################################################################################################################
class TtkCombobox(ttk.Combobox):

    name = ""
    parent= ""

    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    

    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())


        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)


        self.x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
        self.x.grid(row = 5, column  = 0)

        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
        self.y.grid(row = 7, column  = 0)

        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 8,column = 0, sticky = E)

        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())
        
       

        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 20,column = 0, sticky = E)
                 
        

  
            
        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())

        

    def __init__(self,master, **ar):
        ttk.Combobox.__init__(self, master)
        self.configure(ar)
        

        self.bind("<Button-1>",self.click )
        self.bind("<B1-Motion>", self.draggable)



def Zero3():
    def selfmaker1():
        if parent.get()=="root":
            s = TtkCombobox(t ,font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

        else:
          
            s = TtkCombobox(eval(parent.get()) , font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

    global fr

    try:
        fr.destroy()
    except:pass

    l.configure(text = "TTkCombobox")
    
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker1)
    ss.grid(row = 8,column = 0, sticky = E)



    
##########################################################################################################

class TkCB(tk.Checkbutton):

    name = ""
    parent= ""

    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    

    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())


        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)


        self.x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
        self.x.grid(row = 5, column  = 0)

        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
        self.y.grid(row = 7, column  = 0)

        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 8,column = 0, sticky = E)
        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())
        

        
        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 20,column = 0, sticky = E)
                 
        

  

            
        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())

        

    def __init__(self,master, **ar):
        Checkbutton.__init__(self, master, ar)
        

        self.bind("<Button-1>",self.click )
        self.bind("<B1-Motion>", self.draggable)


def Checkboxx():


    def selfmaker1():
        if parent.get()=="root":
            s = TkCB(t)
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

        else:
          
            s = TkCB(eval(parent.get()))
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

    global fr

    try:
        fr.destroy()
    except:pass
    l.configure(text = "CheckButton")
        
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker1)
    ss.grid(row = 8,column = 0, sticky = E)





    
##########################################################################################################

class TtkButton(ttk.Button):
    name = ""
    parent= ""

    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    

    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())


        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)


        self.x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
        self.x.grid(row = 5, column  = 0)

        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
        self.y.grid(row = 7, column  = 0)

        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 8,column = 0, sticky = E)

        
        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())
        

        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 20,column = 0, sticky = E)
                 
        

  
            
        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())

        

    def __init__(self,master, **ar):
        ttk.Button.__init__(self, master)
        self.configure(ar)
        

        self.bind("<Button-1>",self.click )
        self.bind("<B1-Motion>", self.draggable)
    

    
def ttkbutton():
    def selfmaker1():
        if parent.get()=="root":
            s = TtkButton(t ,text = "Ttk Button")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

        else:
          
            s = TtkButton(eval(parent.get()) ,text = "Ttk Button")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

    global fr

    try:
        fr.destroy()
    except:pass
    l.configure(text = "TTkButton")
        
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker1)
    ss.grid(row = 8,column = 0, sticky = E)

###################################################################################################    

class TkText(tk.Text):
    name = ""
    parent= ""

    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    

    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())

        self.configure(bg = self.bgb.get(), fg = self.fgb.get(), font = ((self.fontb.get(),int(self.fontsizeb.get()))), bd = int(self.bdb.get()) )


        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)

        self.x = ttk.Entry(fr , font = fo)
        self.x.grid(row = 5, column  = 0)
        
        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Entry(fr , font = fo)
        self.y.grid(row = 7, column  = 0)


        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())

        ################
        
        l5 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "background:", font = "Consolas 10")
        l5.grid(row = 9, column  = 0,sticky = W)


        self.bgb = ttk.Entry(fr , font = fo)
        self.bgb.grid(row = 10, column  = 0)
        self.bgb.insert(1,self['bg'])

        l6 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "foreground:", font = "Consolas 10")
        l6.grid(row = 11, column  = 0,sticky = W)


        self.fgb = ttk.Entry(fr , font = fo)
        self.fgb.grid(row = 12, column  = 0)
        self.fgb.insert(1, self['fg'])

        l7 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "font:", font = "Consolas 10")
        l7.grid(row = 13, column  = 0,sticky = W)


        self.fontb = ttk.Combobox(fr , font = fo, values = list(font.families()))
        self.fontb.grid(row = 14, column  = 0)
        self.fontb.insert(1,"Consolas")

        l8 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "fontsize:", font = "Consolas 10")
        l8.grid(row = 15, column  = 0,sticky = W)
        


        self.fontsizeb = ttk.Combobox(fr , font = fo, values =  ["1","2","3","4","5","6","7","8","9","10"])
        self.fontsizeb.grid(row = 16, column  = 0)
        self.fontsizeb.insert(1, 9)
                 
        l9 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "borderwidth:", font = "Consolas 10")
        l9.grid(row = 17, column  = 0,sticky = W)


        self.bdb = ttk.Combobox(fr , font = fo, values =  ["0","1","2","3","4","5","6","7","8","9","10"])
        self.bdb.grid(row = 18, column  = 0)
        self.bdb.insert(1, self['borderwidth'])

        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 19,column = 0, sticky = E)
                 
        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 20,column = 0, sticky = E)
                 
        
   


            
        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())

        

    def __init__(self,master, **ar):
        Text.__init__(self, master, ar)
        

        self.bind("<Button-1>",self.click )
        self.bind("<B1-Motion>", self.draggable)

    
def text():

    def selfmaker1():
        if parent.get()=="root":
            s = TkText(t ,font = "Consolas 9")
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()
            s.insert(1.0, "Text")

        else:
          
            s = TkText(eval(parent.get()),font =fo )
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()
            s.insert(1.0, "Text")

    global fr

    try:
        fr.destroy()
    except:pass

    l.configure(text = "Text")
        
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker1)
    ss.grid(row = 8,column = 0, sticky = E)


#############################################################################################################################################

class TtkEntry(ttk.Entry):

    name = ""
    parent= ""


    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    
    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())


        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)


        self.x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
        self.x.grid(row = 5, column  = 0)

        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
        self.y.grid(row = 7, column  = 0)

        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 8,column = 0, sticky = E)

        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())
        
        

        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 20,column = 0, sticky = E)
                 
        

  
            
        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())

        

    def __init__(self,master, **ar):
        ttk.Entry.__init__(self, master)
        self.configure(ar)
        

        self.bind("<Button-1>",self.click )
        self.bind("<B1-Motion>", self.draggable)



    
def ttke():
    def selfmaker1():
        if parent.get()=="root":
            s = TtkEntry(t, font = "Consolas 9" )
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

        else:
          
            s = TtkEntry(eval(parent.get()) )
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()

    global fr

    try:
        fr.destroy()
    except:pass

    l.configure(text = "TTkEntry")

        
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker1)
    ss.grid(row = 8,column = 0, sticky = E)


#######################################################################################################################################
class Conx(tk.Frame):

    def clan(self):
        from tkinter import messagebox
        
        m = messagebox.askyesnocancel(title = "Reassurance", message = "Do you actually want to delete this Widget?", icon = "warning")
        if m:
            self.destroy()
            global fr
            fr.destroy()

            
            fr = Frame(con1, bg  = "#0078ff")

            fr.grid(row = 1, column = 0, padx = 15, sticky = S)

            frx = Frame(fr, bg  = "white")

            frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


            lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo)
            lbbbc.grid(row = 0, column = 0, padx = 15)

            l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
            l1.grid(row = 1, column = 0, padx = 15)

            l1c = WebButton(frx, text  = "About", fg = "#d3d3d3", font  = fo, relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
            l1c.grid(row = 2, column = 0, padx = 15,pady = 1)
            l.configure(text = "Configurations")    

    def design(self):
        self.name = self.namel.get()
        self.parentl.get()

        if self.parent != "root":

            self.master = eval(self.parentl.get())
            self.master = self.parentl.get()

        self.place(x = self.x.get() , y = self.y.get())
        self.configure(bg = self.bgb.get())

        
    def click(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc

        self.dsd_sdsd_d = event.x
        self.ccfv_cxc_dc= event.y
        '''
        print(dsd_sdsd_d)
        print(ccfv_cxc_dc)

        
        '''

        global fr

        try:
            fr.destroy()
        except:pass

        

        fr  = Frame(con1,  bg = conf["bg"])
        fr.grid(row = 1, column = 0, padx = 15)

        l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
        l1.grid(row = 0, column  = 0,sticky = W)
        


        self.namel = ttk.Entry(fr , font = fo)
        self.namel.grid(row = 1, column  = 0)
        self.namel.insert(1, self.name)

        l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
        l2.grid(row = 2, column  = 0,sticky = W)


        self.parentl = ttk.Entry(fr , font = fo)
        self.parentl.grid(row = 3, column  = 0)
        self.parentl.insert(1, self.parent)


        l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
        l3.grid(row = 4, column  = 0,sticky = W)


        self.x = ttk.Entry(fr , font = fo)
        self.x.grid(row = 5, column  = 0)

        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
        l4.grid(row = 6, column  = 0,sticky = W)


        self.y = ttk.Entry(fr , font = fo)
        self.y.grid(row = 7, column  = 0)

        ss = ttk.Button(fr,  text = "Change", command = self.design)
        ss.grid(row = 18,column = 0, sticky = E)

        self.x.insert(1, self.winfo_rootx()-self.master.winfo_rootx())
        self.y.insert(1, self.winfo_rooty()-self.master.winfo_rooty())

        l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "background:", font = "Consolas 10")
        l4.grid(row = 11, column  = 0,sticky = W)

        self.bgb = ttk.Entry(fr , font = fo)
        self.bgb.grid(row = 12, column  = 0)
        

        ssd = ttk.Button(fr,  text = "Delete", command = self.clan, style = "shit.TButton")
        ssd.grid(row = 20,column = 0, sticky = E)
                 
        

  
            
        

    def draggable(self,event):
        #global dsd_sdsd_d , ccfv_cxc_dc
        self.p=self.winfo_rootx()-u.winfo_x()
        
        self.p1=self.winfo_rooty()-u.winfo_y()
        self.place(x = self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx() , y = self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())
        #print(str(s.winfo_pointerx()-dsd_sdsd_d-t.winfo_rootx())+"px","+",str(s.winfo_pointery()-ccfv_cxc_dc-t.winfo_rooty())+"px")

        self.x.delete(0,END)
        self.y.delete(0,END)
        
        self.x.insert(1,self.winfo_pointerx()-self.dsd_sdsd_d-self.master.winfo_rootx())
        self.y.insert(1,self.winfo_pointery()-self.ccfv_cxc_dc-self.master.winfo_rooty())



    def __init__(self,master,):
        tk.Frame.__init__(self,master)

        self.can = Canvas(self, bg = "#d3d3d3", highlightthickness = 1)
        self.can.pack(fill =  BOTH, expand = 1)

        self.frame  = Frame(self.can)
        self.can.bind("<Configure>", lambda x: self.can.configure(scrollregion = self.frame.bbox("all")))
        self.can.bind("<Button-1>",self.click)
        self.can.bind("<B1-Motion>",self.draggable)
        self.can.create_window((0,0), window = self.frame, anchor = "ne")
        

    
def Conn():

    def selfmaker1():
        if parent.get()=="root":
            s = Conx(t )
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()
            #s.insert(1.0, "Text")
            
            s.can.update()
            print(int(s.can.winfo_height()/1.5))
            s.can.configure(width =int( s.can.winfo_width()/1.5 ), height =int( s.can.winfo_height()/1.5))


        else:
          
            s = Conx(eval(parent.get()) )
            s.place(x = x.get(), y = y.get())
            s.name = name.get()
            s.parent= parent.get()
            #s.insert(1.0, "Text")
            s.can.update()
            s.can.configure(width =int( s.can.winfo_width()/1.5 ), height =int( s.can.winfo_height()/1.5))




    global fr

    try:
        fr.destroy()
    except:pass

    l.configure(text = "Container")
        
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "name", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    name = ttk.Entry(fr , font = fo)
    name.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "parent", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    parent.insert(1, "root")


    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "x:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    x = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    x.grid(row = 5, column  = 0)

    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "y:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    y = ttk.Combobox(fr , font = fo, values = ["1","2","3","4","5","6","7","8","9","10"])
    y.grid(row = 7, column  = 0)

    ss = ttk.Button(fr,  text = "Create", command = selfmaker1)
    ss.grid(row = 8,column = 0, sticky = E)

#####################################################################################################################################
    
def utilprinter():

    print("OK, Now User Utility is up and running #info_info #modtkinter #rhizome #base64 #ttk #Distributed by Zin-Lin-Htun(Damian-James)")

    
    print("#             #                       #")
    time.sleep(0.03)
    print("# #         # #                       #")
    time.sleep(0.03)
    print("#  #       #  #                       #")
    time.sleep(0.03)
    print("#   #     #   #      ######      ######")
    time.sleep(0.03)
    print("#    #   #    #      #    #      #    #")
    time.sleep(0.03)
    print("#      #      #      ######      ######")
    time.sleep(0.03)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    print("################################################       ##                                 ##")
    time.sleep(0.03)
    print("                        ##                             ##                              ##    ")
    time.sleep(0.03)
    print("                        ##                             ##                           ##       ")
    time.sleep(0.03)
    print("                        ##                             ##                        ##          ")
    time.sleep(0.03)
    print("                        ##                             ##                     ##             ")
    time.sleep(0.03)
    print("                        ##                             ##                  ##                ")
    time.sleep(0.03)
    print("                        ##                             ##               ##                   ")
    time.sleep(0.03)
    print("                        ##                             ##            ##                      ")
    time.sleep(0.03)
    print("                        ##                             ##         ##                        ")
    time.sleep(0.03)
    print("                        ##                             ##      ##                            ")
    time.sleep(0.03)
    print("                        ##                             ##   ##                               ")
    time.sleep(0.03)
    print("                        ##                             ##")
    time.sleep(0.03)
    print("                        ##                             ##   ##                               ")
    time.sleep(0.03)
    print("                        ##                             ##      ##                            ")
    time.sleep(0.03)
    print("                        ##                             ##         ##                        ")
    time.sleep(0.03)
    print("                        ##                             ##            ##                      ")
    time.sleep(0.03)
    print("                        ##                             ##               ##                   ")
    time.sleep(0.03)
    print("                        ##                             ##                  ##                ")
    time.sleep(0.03)
    print("                        ##                             ##                     ##             ")
    time.sleep(0.03)
    print("                        ##                             ##                        ##          ")
    time.sleep(0.03)
    print("                        ##                             ##                           ##       ")
    time.sleep(0.03)
    print("                        ##                             ##                             ##    ")
    time.sleep(0.03)
    print("                        ##                             ##                                ##")  

import base64
from base64 import*

ic =b'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GRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRmZY5r/By+uBToT6TynAAAAAElFTkSuQmCCKAAAAIAAAAAAAQAAAQAgAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ2UIwGglSQDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmHaGWJqehliYbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmoaGWJuihliZeoJYlCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliY+oZYm46GWJs2hliZvoZYmTp+TJQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJj6hliZioZYm/aGWJsahliYtoZYmYaCVJQQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoJUmLqGWJmGhliaAoZYm/6GWJsehliYYoZYmXaGWJhcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYaoZYmop+VJAGhliaooZYm/6GWJsmhliYRoZYmRKGWJkCflCMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ+UJAWhlia/oZYmHaGWJguhlibPoZYm/6GWJsmgliYIoZYmFqGWJlKhliYyoJUlCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJnuhliZsAAAAAKGWJh2hlibmoZYm/6GWJkUAAAAAAAAAAKGWJhyhliZeoZYmP6GWJhMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoJUlMqGWJrQAAAAAAAAAAKGWJjKhlibwoZYm56GWJiAAAAAAAAAAAKGWJi+hjiYAoZYmIaGWJiaglSUVn5QkBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIt0FwCglSUboJUlAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgliYMoZYmxKGWJhIAAAAAAAAAAKGWJjyhlib0oZYm1aGWJhYAAAAAoZYmOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCWJQShliZNoZYmEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliZ6oZYmYAAAAAAAAAAAAAAAAKGWJkGhlibzoZYm2aGWJh2hliY4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCVJQGhliZboZYmQgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJi+hliamAAAAAAAAAAAAAAAAAAAAAKGWJjmhlibuoZYm3aGWJk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliZDoZYmfKCWJQcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoJUlAaGWJrihliYhAAAAAAAAAAAAAAAAAAAAAKGWJjChlibuoZYm7KGWJisAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYhoZYmmqGWJhYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmWaGWJouhliYvoZYmPqGWJkihliZHoZYmPaGWJmGhlib0oZYm5qGWJiwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYPoZYmnaCWJQUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJiWjmS3cycWi/Nvb2//b29v/29vb/9vb2//b29v/29va/tra2Pva2tn+s6xe/KGWJv+imCv+z8y1/LCoVPGhliYeAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJjChliaor6dT+MO/kfzLyKn42NjT/aeeOuehliULAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYfoZYmhaSZLty2rmb7urNz+qGWJmwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoJUlAqGWJlOhlibSoZYmnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCVJAGglSUDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8/////////////////////H////////////////////4f///////////////////+B////////////////////gP///////////////////4B///////////////////+AH///////////////////gAf//////////////////8hh///////////////////MMD8f////////////////xhf/j////////////////+cH/8f////////////////nh//x////////////////48P/+P////////////////AB//x////////////////x4D/4f///////////////+fgH4P////////////////n8AGf////////////////5/AAB/////////////////f4AAP////////////////3+AAB//9+f/////////////gAAP/4Ph/////////////4AAB/4DwD////////////+AAAP4AcAP////////////gAAI+ACAD////////////4AABGAQBw////////////+AAAIASA8P////////////gAABGEgfH/////////7//4AAAPxkHx/////////+f/8AAAAcZ/4YP////////z//AAAAAHP+AD////////+P/wAAAABz/wA/////////z/8AAAAA+f+AH////////+f/AAAACfAP3h/////////z/wAAAAfgA/8P////////+f8AAAADwAH/D/////////z/AAAAAYJB/g/////////+BgAAAACGYPgP/////////+AAAAAADzDwP//////////+AAAAAA848H///////////gAAAAAPmPH///////////4AAAAAB5jwf//////////+AAAAAAPA8D///////////wAAAAAAQPgP//////////+AAAAAAAH+D///////////wAAAAAAB/w///////////+AAAAAAB/8P///////////wAAAACA/eH///////////+AAAAAf/gB////////////gAAAAD/wA////////////8AAAAAf4AP////////////gAAAAD+HD////////////4AAAAAHx//////////////AAAAAB8f/////////////4AQAAAPD/////////////+AEAAABw//////////////wBgAAAAP/////////////8AcAAAAD//////////////gPAAAAH//////////////4D4AAAD///////////////A/AAAAf//////////////4P4AAAD//////////////+D+AAAAf//////////////w/wAAAD//////////////8f+AAAA/////////////+fn/gAAAH/////////////n5/8AAAA/////////////4+//AAAAH////////////+Hv/4AAAA/////////////w7/+AAAAP////////////8O//wAAAB/////////////Jv/+AAAAP////////////yL//gAAAAP///////////+w//8AAAAwf///////////mP//AAAAPj///////////5z//4AAAP+f///////////f//+AAAB/z///////////z///wAAAP8///////////8///8AAAB/n///////////v///gAAAP8///////////54//4AAAB/n///////////eH//AAAAP8///////////z0//wAAAB/H//////////+cj/+AAAAP5///////////nMf/gAAAD/P//////////8Dj/8AAAAf7///////////w8f/AAAAD/////////////Pn/4AAAA//////////////8//AAAAH//////////////n/4AAAA//////////////8v+AAAAH//////////////h/wYAAB//////////////8f8HAAAP////////////////h8AAD////////////////8/gAAf/////////////////8AAH//////////////////gAA//////////////////8AAH//////////////////gAB//////////////////8AAP//////////////////wAB//////////////////+AAP//////////////////wAD//////////////////+AAf//////////////////wAD///////////////////AAf//////////////////4AD///////////////////AAf//////////////////4AD///////////////////gA////////////////////gH///////////////////+B////////////////////4f////////////////////n////////////////////////////////////////////////////////////////ygAAABAAAAAgAAAAAEAIAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACflCQBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmWaGWJligliUCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJh+hlibEoZYmbKGWJhkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYSoZYmYaGWJtuhliZUoZYmJ5+UIwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAn5QkAaGWJnGhliY+oZYm66GWJhmhliYooZYmKqGWJgUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliZtoZYmBKGWJlihlia0oZYmBqGWJhqhliYSoJUlBgAAAAAAAAAAAAAAAKCVJQihliYXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmKqGWJkIAAAAAoZYmW6GWJrChliYiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmF6GWJkCgliUCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCVJQChliZvoZYmG6GWJiShliZvoZYmvKGWJgsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYIoZYmV6CWJQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmTaCWJQQAAAAAoJUlAqGWJlWjmCzYvrmCjqmgQDygliUDAAAAAAAAAAChliYDoZYmRKGWJkqhlSYCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGVJgiglSUIAAAAAAAAAAAAAAAAoZYmeqqgQf7Pzbf9xsKZ7bqzc6unnTlnoZYmKKGWJkqSkiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAn5QlAwAAAAAAAAAAAAAAAKCWJQKkmjHjqJ89/tbVyv7b29v/2dnW/sjEn/erokSBoZYmSaCWJgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHFxcQEAAAAAAAAAAPb29gBwcHABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYvx8Od/aqhQv6upU3+2dnV/9vb2//b29v/0tC+/qmgQGehliZNoZYmDQAAAAAAAAAAAAAAAAAAAABUVFQEDQ0NUQYGBrsICAiaAAAAAAAAAAAPDw9OBAQE2QoKCnEkJCQRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAopcpctjX0P7S0L/+pJow/ravaP3b29v/2NfQ/9nZ1v/Myav2pJoxOqGWJkShliYbAAAAAAAAAAAlJBQ6LisO4iYjC+YKCgp/AgIC8hAQEDwnJycMAwMD4QoKCpIFBQXAAgIC9AsLC3UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKyjSXXb29v/29vb/8rGpf6hlif/wbyK/dvb2//S0L//2dnW/8jEnuujmCstoZYmN6GWJjOhliYxYFoeXAMDA/GRiTcOoZYmHgoKCnEDAwPbBQUFuQYGBr9/f38BAAAAAAcHB6gICAiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACxqVd529vb/9vb2//b29v/vrmC/aKXKP/LyKn+29vb/9LQv//b29v/xsKb56KXKiqhliYVoZYmB0pKSgQCAgLzFxcXKqGWJh95dDgICAgIhQYGBowUFBQnAAAAAAAAAAAFBQXcDAwMRQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAn5QkAaCVJQ4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtKxhf9vb2//Y2NP/29vb/9vb2v+zrF/+pZoy/tHQvf7V1Mr/29vb/9vb2//BvZbtKScPtQgICHoQEBBKAwMD6gsLC1mAgAAAoZYmIQAAAAAAAAAAAAAAAAAAAAAvLy8PAQEB/A8PD2gKCgppBgYGowsLC3gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChlSUDoZYmIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALixbovb29v/2dnV/9TTx//b29v/2NfS/qqhQ/6onjv+2NfQ/tja2P/O0sn829vb/6unf/4bGgrCBQUF4gcHB6JSUlIDAAAAAKGWJh+hlSYCAAAAAAAAAAAAAAAAAAAAAA4ODlsEBATwBQUFuAsLC5UDAwPsLy8vCQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJgWhliYlAAAAAAAAAAAAAAAAAAAAAAAAAAC+uICl29vb/9vb2//U08b/19bN/9vb2//S0cD+pJox/rKqWv620tn3dsLV7c/PxP/b29v/wLqG06GWJhWenp4BAAAAADIyMgUKCgl6HBoK2AMDA9oHBwecGBgYGwAAAAAAAAAAoKCgAQAAAADAwMAABQUF0QoKCl8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmCaGWJiUAAAAAAAAAAAAAAAAAAAAAxL+T1dvb2//b29v/29vb/8nNuv25x7L7zM67/srGpf6ilyj/ka199WLE9POKurz/29ra/9vb2v+/uYLQoZYmFJ6engAICAitBAQEzjw4FGsODg5CCAgIogMDA+McHBwXAAAAAAAAAAAAAAAAJSUlDAYGBrUGBgbEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYHoZYmH6GWJiChliYeoZYmK8rHp/3b29v/29vb/9vb2/+Sz+jvZsz/6GfL++h6yOXsibSX8qGWJv99tqfxYsHw9a3Du//b29v/29va/764gc82MxdTAwMD6SEhIRChliYEoZYmIMbGxgAHBwetCAgIiwAAAAAAAAAAEBAQRwQEBOEGBga+FhYWJwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJlHU08b+29vb/9vb2//b29v/0tfT/H7I3+xmzP/oZsz/6GbM/+iLqnj0oJcr/nW+yOxqxOruxM3F/9vb2//b29r/paF1+yspD6gAAAAAAAAAAKGWJiWglSUACQkJWwMDA78AAAAAAAAAAAUFBagHBweTkJCQAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYbubJx6tvb2v/b29v/29vb/9vb2//S1c39gcXW7WbM/+hmzP/oZ8v66JOjWfidmjb9abrT+HG60v3U1tD929vb/9vb2//Gwp3xqJ48UQAAAAChliYDoZYmIwkJCXcGBgauAAAAAAAAAAAKCgqYAwMD3BAQEEYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJjG5s3Lq29va/9vb2//b29v/29vb/9TVzf2ExdLtZsz/6GbM/+howufxl5pA/5acRv5pyPDqjcfS7tra1/7Au4fvu7eN+LSua/uhliY5oZYmJGJcIEgDAwPqDw8PTQAAAAAAAAAAT09PAgwMDGgDAwPvCgoKmQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmNb23fvPb29v/29vb/9vb2//b29v/0tPG+4jF0O5mzP/oZMf57mi0yP+emDH+kaVg92fL/Oinycfzysen7UZCG2IEBAToBAQE1wYGBckeHAn6CwsLeO7u7gAAAAAAAAAAAAAAAAAAAAAABwcHoAgICJIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChlidcycaj/tvb2//b29v/19fQ/tnY1P7X19L+j8XL72bM/+hfvev8d7Sv9KCXKf+Gq4L2Z8bx7sLPx/nDv5HRcGooGQ0NDUoODg5WGBgYGwAAAAAAAAAAHx8fEgkJCXcNDQ0/LS0tHQICAvUTExMoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAn5UjAKifPajW1cz+29vb/9PSw/zb29v/29vb/9nY1P6VxcbwYsT18l265/99pof+oZYm/3atoP51xN/v1NXO/b+6hcChliYLAAAAAAAAAAAAAAAAKysrCwUFBc0FBQXRBAQE4gEBAf4GBga9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYUtq9o59vb2//Pzbb829vb/9fWz/6uplDy1tbN/pnEwvJlyfvsZ8v76I2ob/Oflyv/c7zI8JTGzPDa2tn/v7qEvl1YIxw9PT0DAAAAAEdHRwQDAwP0FRUVLAAAAAAiIiIdEhISIQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJlvLyKn+19bO/tTTx/3Qzrj+oZYmaLiyb+La2tf/msXB8mbM/+hoyPTqkJxR/5ybOPxuxeLqtsrB99vb2v+ZlW//KScScgAAAAAAAAAABQUFvQsLC2QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACglSUBrqVOxdra2f/X18/8xcGW/aGWJiuhliZDyMSg/Nra1/+ZxMHxY8b372O21f6XmT7/l6BM+mu50vrKz8X+29vb/66qhPOOhTIiDw8PRwQEBNIGBgaeAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJjzGwpj929vb/7ixbuqhliUBAAAAAKifPY3V1Mj+2dnW/5PDwvFjxfbxarXI+p2XL/+LomX9gMTU7dfX0f7b29v/qqaB+hUUB+YJCQmAHR0dGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArKNIs9ra1/+so0izAAAAAAAAAAChliYHs6tdzNra2P/Y19L+isPI72bM/+h4u7vuoJcp/oWwjfKdyMry29vb/9vb2//Ev5LWoZYmFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJjLCvY37oZYnjAAAAAAAAAAAAAAAAKGWJiO/uYLv29vb/9TUyv18xNTsZsz/6H+1ovChlif/f7an7tnZ1f3b29v/29vb/765gsGhliYGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAppw1r6GWJnwAAAAAAAAAAAAAAAAAAAAAo5gsZNDOuP7b29v/x828+2zH7OlmzP/oh66G85+YLP7PzbX929vb/9vb2//a2df/t7BqlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmMaGWJhgAAAAAAAAAAKGWJjmhliZCAAAAAAAAAAAAAAAAAAAAAKGWJgKzq17K29vb/9vb2/+zx7n3mMjN8aPN1fKvq1/9p504/tXUyP7b29v/29vb/9XUyP6vp1JgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJhmhliZUoZYmBwAAAAChliYpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmRMrHqP7b29v/29vb/9vb2//b29v/2djU/qyjSf6rokb+0tC//tPRwv/S0L//z82196edOTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmNaGWJkEAAAAAoZYmNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCVJACxqFe829va/9vb2//b29v/29vb/9vb2//U08b+ppw2/rOsX/7b29r/1dTJ/9bVzP/FwZjfoZYmDwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJjGhliYToZYmNaGWJjUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmOsnFov3b29v/29vb/9vb2//b29r/29vb/8fDnfyjmCv+vbd9/dvb2//U08X/2trY/7StYZChliYVoZYmDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYroZUmAqGWJi+hliZSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwp1S029va/9vb2//b29v/2NfR/9vb2//OzLP+vbh+/KGWJ//Gwpr929vb/8rHpvu0rGGJAAAAAKGWJhGhliYeoZYmHgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmBKGWJiUAAAAAoZYmKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmM8jEn/3b29v/29vb/9XUyP/b29v/2NjT/sS/kv29t339o5gr/87Lsf2yqlvBoZYmEAAAAAAAAAAAAAAAAKGWJguhliYcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACvplCu2trZ/9vb2//T0sP/29vb/9vb2/++uID829va/7OsX/6mnDb+09HB/rq0dtahliYTAAAAAAAAAAAAAAAAoZYmHKGWJg0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmHKGWJgoAAAAAoZYmDqGWJikAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmL8bCmvzb29v/1NPG/9vb2//b29v/wLqG/dXUx/7Y2NP+rKNI/quiRv7X1s/+tq9nv6GWJgcAAAAAAAAAAAAAAAChliYkoZYmBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYkAAAAAKCVJQOhliZAoZYmMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACtpEup2trX/9jX0P/Y19D/29vb/9HQvf7JxqT929vb/9TTx/6mnTf+s6te/tjX0P6yqluloJYlAQAAAAAAAAAAAAAAAKGWJh6flSQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmHKGWJg4AAAAAoZYmMKGWJguhliYyi4sXAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmJ8K9jPjb29v/1NLF/9vb2//b29v/0tC//NnZ1f7b29v/z8y1/qOYLP+9t3391dTI/qyjSXYAAAAAAAAAAAAAAACglSUBoJUlCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYzoZYmOqGWJkgAAAAAoZYmBaGWJi6SkiQAAAAAAAAAAAAAAAAAAAAAAAAAAACmnDWC09HC/tPSxP/b29v/29vb/9vb2//Oy7L829vb/9vb2//IxJ/9oZYn/8bCm/3Lyav4opcqNgAAAAAAAAAAAAAAAJOKFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYUAAAAAAAAAAChliYFoZYmIgAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmBrGpWM3V1Mn/2NjT/9vb2//b29v/2djU/tDNt/zb29v/29vb/765gv2jmCz/zsy0/sC7h96hliYRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJgeglSUQm5AfAAAAAAAAAAAAAAAAAAAAAAChliYrwLuG9tTTx/+3sGvcubJw3NXUyP7Z2dX+0M65/NnZ1f7b29r/ta5l/aedN/7U08X+tK1hpJ+AIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoJUlA6CVJROglSUEAAAAAAAAAAAAAAAAAAAAAKWaMX+9uH/9oZYmPqGWJgepoECPzcqv/dvb2//U0sX91NPF/NnZ1f+upU7+raRK/s/Mtf2kmi9DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYHoZYmhqCVJQEAAAAAAAAAAKWbNGXKxqX729vb/9ra1//U08f81NPG/aifPf62r2j9vriAz6CWJQIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApJkvUcbCmvXb29v/29vb/9nZ1f3S0L79pZs0/r+5g/2qoUJjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACilyg6wbyJ6dvb2//b29v/29vb/8/Mtf6lmzT+u7R26aGWJhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJiK6tHTT2dnW/9vb2//b29v/zMms/q2kSv22r2i2oZYmAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmD7SsYbbW1cz+29vb/9vb2//LyKn+uLFt/LGpWIkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYDraVNitDOuP3b29v/1dTI/8rHp/3Au4j8qJ47ZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACnnjpdyMWh9tbWzf/Nyq//zsyz/cfDnPqlmzNPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJjG6tHbR0tC+/s3Kr//Rz7r9yMSg9KKXKTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmBaGWJkeqoUN/vbd9583Kr/u8tnrSoZYlAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJgijmCtZr6dTx6GWJkIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCVJACglSUBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////////////////7//////////j/////////+H/////////4H/////////gH/////////AOf///////8j8f///////wH4////////kDD///////+cAf///////9wA/2f//////AB4Yf/////8ADAA//////wAAAT////7/AAADP////n8AAB4H////PwAATwP///+fAACBo////88AAADj////4AAAAMP////+AAAwx/////4AABDH/////wAAAMP/////gAAA8//////AAAMD/////8AADgf/////4AACJ//////wAAM///////AAAD//////+CAAP//////4YAB///////xwAD///////ngAP//////meAAf/////+L8AA//////8vwAB//////w/gAB//////D/AAR/////8v8ABz/////7/4ADn/////k/gAHP/////R/AAOf////8h8AA5/////4j4AB3/////7PgAD//////+PAAH//////8eAAf///////4wA/////////gD/////////AH////////+AP////////8A/////////4B/////////4D/////////wH/////////gP/////////w//////////z//////////8oAAAAMAAAAGAAAAABACAAAAAAAAAkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoZYmAaGWJjKhliUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJn+hliZvoZYmDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJkWhliaioZYmYaGWJhqglSYCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJjuhliYnoZYms6GWJiChliYmoZYmD6CVJQEAAAAAi3QXAKCVJQcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGWJgehliZKoZYmFaGWJp+hliYtAAAAAAAAAAAAAAAAAAAAAKGWJg2hliYvoJYlAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChliYLpZoxWqGWJgMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////////AAD///////8AAP///////wAA////////AAD/j/////8AAP/H/////wAA/8H/////AAD/wE////8AAP/B4////wAA/+Bz////AAD/5AP///8AAP/mA/b//wAA//4AgB//AAD//gAAH/8AAP9+AACf/wAA/x4AAwf/AAD/jgAQg/8AAP/OAABj/wAA/+AAAEP/AAD//AAAR/8AAP/8AABD/wAA//4AAAP/AAD//wABA/8AAP//gAEH/wAA///AAJ//AAD//8AAH/8AAP//4gA//wAA///jAB//AAD//5MAD/8AAP//k4AP/wAA///HwAf/AAD//8fAAP8AAP//x+AEfwAA///P4AI/AAD//+DwAT8AAP//4HABnwAA///wOADfAAD///8YAH8AAP///4wAPwAA/////kA/AAD/////4B8AAP/////wHwAA//////gPAAD//////gcAAP//////AwAA//////+BAAD///////EAAP///////wAAKAAAACAAAABAAAAAAQAgAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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'
fddicon = base64.b64decode(ic)


utilprinter()


u.configure(bg = "white")
u.title("TkToolKit-Users'tool")

fddicon = Image.open(io.BytesIO(fddicon))
ico = ImageTk.PhotoImage(fddicon)

u.wm_iconphoto(True, ico)

u = Frame(u,bg = "#f5f5f5")
u.pack(fill = BOTH, expand = 1)

stylex = ThemedStyle(u)
style = ttk.Style()
style.theme_use("breeze")
style.configure("TButton",font = "Consolas 9", )

style1 = ttk.Style()
style1.configure("TScrollbar", background ='white', )

style12 = ttk.Style()
style.theme_use("breeze")
style.configure("shit.TButton", background ='white', foreground = "red")


menubar = ModFrame(u, border = 0, bg = "white")

menubar.pack( anchor = 'e', fill = X, side = TOP)


u1 = Frame(u , bg = u["bg"])
u1.pack(fill = BOTH, expand = 1, side = LEFT, pady = 1)

u2 = Frame(u1 , bg = u["bg"])
u2.pack(fill = BOTH, expand = 1, anchor = "e")


'''
n = WiWebButtonton(u2, text = "+", command = Zero, )
n.pack()'''
####################################################################################################################################################
f = Frame(u2 , bg = u["bg"])
f.grid(row = 0, column = 1)

f1 = Frame(u2 , bg = u["bg"])
f1.grid(row = 0, column = 2, sticky = NE)

fv = IOSFrame(f1, highlightbackground = "#111111", bg = "#000000", border = 0,)
fv.pack(padx = 1, pady = 0, anchor = "ne")

conc  = Frame(fv.frame, bg = "white")
conc.pack(fill =BOTH, side = RIGHT, anchor = "n")


modechan = Canvas(conc, bg = "white", highlightthickness = 0, width = 170, height = 290)
modechan.pack(fill = BOTH, anchor = "nw", side = LEFT)

con = Frame(modechan, bg ="white" , )
con.bind("<Configure>", lambda a:modechan.configure(scrollregion = con.bbox("all")))
modechan.create_window((0,0),window = con, anchor = "nw")

srcx = ttk.Scrollbar(conc, command = modechan.yview, style = "TScrollbar")
srcx.pack(fill = Y, anchor = "e", expand = 1, side = RIGHT)
modechan.configure(yscrollcommand  =  srcx.set)


conf = Frame(u2, bg = "white")
conf.grid(row = 0, column = 3,pady = 0,padx = 2, sticky = NE)


modechan1 = Canvas(conf, bg = "white", highlightthickness = 0, width = 312, height = 350)
modechan1.pack(fill = BOTH, anchor = "nw", side = LEFT)

con1 = Frame(modechan1, bg ="white" , )
con1.bind("<Configure>", lambda a:modechan1.configure(scrollregion = con1.bbox("all")))
modechan1.create_window((0,0),window = con1, anchor = "nw")

l = Label(con1, text  = "Configurations", fg = "#0078ff", bg  = "white", font  = fonti)
l.grid(row = 0, column = 0, padx = 15)

global fr
fr = Frame(con1, bg  = "#0078ff")

fr.grid(row = 1, column = 0, padx = 15, sticky = S)

frx = Frame(fr, bg  = "white")

frx.grid(row = 1, column = 0, padx = 0.5, sticky = S, pady= 0.5)


lbbbc = Label(frx, text  = "No prperty chosen", fg = "red", bg  = "white", font  = fo1)
lbbbc.grid(row = 0, column = 0, padx = 15)

l1 = Label(frx, text  = "Create objects to\nconfigure", fg = "#d3d3d3", bg  = "white", font  = fonti)
l1.grid(row = 1, column = 0, padx = 15)

l1c = WebButton(frx, text  = "ⓘ About ", fg = "#d3d3d3", font  = fo, borderradius = 2 ,relief = SUNKEN, bg =[0,106,255,255], abg =[10,126,255,255])
l1c.grid(row = 2, column = 0, padx = 15,pady = 1)



srcx1 = ttk.Scrollbar(conf, command = modechan1.yview, style = "TScrollbar")
srcx1.pack(fill = Y, anchor = "e", expand = 1, side = RIGHT)
modechan1.configure(yscrollcommand  =  srcx1.set)



##########################################

def op(event):
    modechan.yview_scroll(-1*(event.delta//120), "units")
def op1(event):
    modechan1.yview_scroll(-1*(event.delta//120), "units")
    


####################################
def event1(event1):
    modechan.bind_all("<MouseWheel>", op)
def event2(event2):
    modechan1.bind_all("<MouseWheel>", op1)

############################################################

modechan.bind("<Enter>", event1)
modechan1.bind("<Enter>", event2)

############################################################

button = Button(con, command = Zero, font = fo,border= 0 ,text =  "  +Button  ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 0, column = 0, sticky = N)

button = Button(con, command = Zero1, font = fo,border= 0 ,text =  "  +Label  ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 6, column = 0, sticky = N)


button = Button(con, command = Zero2, font = fo,border= 0 ,text =  "  +Entry  ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 7, column = 0, sticky = N)


button = Button(con, command = Zero3, font = fo,border= 0 ,text =  "  +Combobox  ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 8, column = 0, sticky = N)

button = Button(con, command = ttke, font = fo,border= 0 ,text =  "  +ttk.Entry  ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 9, column = 0, sticky = N)


button = Button(con, command = text, font = fo,border= 0 ,text =  "  +Text  ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 10, column = 0, sticky = N)

button = Button(con, command = ttkbutton, font = fo,border= 0 ,text =  "  +ttk.Button  ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 11, column = 0, sticky = N)


button = Button(con, command = Checkboxx, font = fo,border= 0 ,text =  "  +Checkbox ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 12, column = 0, sticky = N)

button = Button(con, command = Conn, font = fo,border= 0 ,text =  "  +Container ",  bg = con['bg'], fg = "#0078ff")
button.grid(row = 13, column = 0, sticky = N)


############################################################################################################################################





#################################################################################################################################################


lxf = Label(menubar, border= 0 ,text = "User's tool", font =fonti, bg  = "white",  fg = "#0078ff")


sq1 = Button(menubar, command = Zero, font = fo,border= 0 ,text =  "+Wiget")
sq2 = Button(menubar, font = fo, border= 0 ,text =  "  📁  ")
sq3 = Button(menubar, font = fo, border= 0 ,text = "  🔧  ")

menubar.FrameContainsHor([lxf,sq1,sq2,sq3], 'white' , "#0078ff")




t1 = Text(f, border = 0, state = "disabled", bg ="#0078ff")
t1.pack(fill = BOTH, anchor = "ne",  side = LEFT)
t1.config( width =int((1920/1.5/15.05)+0.5), height = int((1080/1.5/15.05/2.07)+0.5))



t = Text(t1, border = 0, state = "disabled")
t.pack( anchor = "ne", )


t.config( width =int(1920/1.5/15.05), height = int(1080/1.5/15.05/2.07))


u.tk.call('tk', 'scaling' , 2)

'''
src = ttk.Scrollbar(f, command = t.yview, style = "TScrollbar")
src.pack(fill = Y, anchor = "e", expand = 1, side = RIGHT)
t.configure(yscrollcommand  =  src.set)'''
#t.destroy()


###########################################

def dff(selfoexp):

    def selfmarker1():


        bkc = bk.get()
        geoc = geo.get()

        geoc1 = geo1.get()


        t.configure(state = "normal", bg = bkc)

        if not int(geoc) > 1920: 
            if geoc == "full-size":
                t.config(width = 85)

            else:
                t.config(width = int(int(geoc)/1.5/15.05))

        if not int(geoc1) > 1080: 
            if geoc1 == "full-size":
                t.config(height = 23)

            else:
                t.config(height = int(int(geoc1)/1.5/15.05/2.07))
            
            t.configure(state = "disable")
        

    global fr

    try:
        fr.destroy()

    except:
        pass

    l.configure(text = "root window")
    
    fr  = Frame(con1,  bg = conf["bg"])
    fr.grid(row = 1, column = 0, padx = 15)

    l1 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "background", font = "Consolas 10")
    l1.grid(row = 0, column  = 0,sticky = W)


    bk = ttk.Entry(fr , font = fo)
    bk.grid(row = 1, column  = 0)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "geometry x:", font = "Consolas 10")
    l2.grid(row = 2, column  = 0,sticky = W)


    geo = ttk.Entry(fr , font = fo)
    geo.grid(row = 3, column  = 0)
    geo.insert(1, int(t['width']*1.5*15.05)+2)


    l2 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "geometry y:", font = "Consolas 10")
    l2.grid(row = 4, column  = 0,sticky = W)

    geo1 = ttk.Entry(fr , font = fo)
    geo1.grid(row = 5, column  = 0)
    geo1.insert(1, int(t['height']*1.5*15.05*2.07)+6)

    bk.insert(1, t['bg'])



    '''
    l3 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "width:", font = "Consolas 10")
    l3.grid(row = 4, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    
    l4 = Label(fr , bg = fr['bg'], fg ="#0078ff", text = "height:", font = "Consolas 10")
    l4.grid(row = 6, column  = 0,sticky = W)


    parent = ttk.Entry(fr , font = fo)
    parent.grid(row = 3, column  = 0)
    '''
    
    ss = ttk.Button(fr,  text = "Config", command = selfmarker1)
    ss.grid(row = 13 ,column = 0, sticky = E)    
    

##########################################

t.tk.call('tk', 'scaling',1.5)
print(font.families())

t.bind("<Button-1>", dff)
t.config(cursor=  "arrow")

'''
ffg = AssistiveTouch(master= u, bgcolor = '#0078ff', text= "Assistive\ntouch ")
ffg.camn.config(font = "Consolas", fg = "#d3d3d3")
'''




#print(t['width'],t['height'])
u.mainloop()






























