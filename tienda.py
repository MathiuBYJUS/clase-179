from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()
root.title("Tienda de jugos")
root.geometry("400x400")
root.config(bg="lightblue")

image1=ImageTk.PhotoImage(Image.open("logo.png"))
image2=ImageTk.PhotoImage(Image.open("orange.png"))
image3=ImageTk.PhotoImage(Image.open("mango_img.png"))
image4=ImageTk.PhotoImage(Image.open("apple_img.png"))

jugos=["Manzana","Mango","Naranja"]


    
    

label_1=Label(root,text="Tienda de jugos")
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)
label_2=Label(root,image=image1,bg="lightblue")
label_2.place(relx=0.1,rely=0.2,anchor=CENTER)
label_3=Label(root,text="Selecciona un jugo e ingresa la cantidad")
label_3.place(relx=0.5,rely=0.4,anchor=CENTER)
label_4=Label(root,text="cantidad a pagar")
label_4.place(relx=0.5,rely=0.7,anchor=CENTER)
label_5=Label(root,text="a")
label_5.place(relx=0.5,rely=0.8,anchor=CENTER)
label_6=Label(root,image=image2)
label_6.place(relx=0.5,rely=0.9,anchor=CENTER)
input1=Entry(root)
input1.place(relx=0.5,rely=0.6,anchor=CENTER)

combobox1=ttk.Combobox(root,state="readonly",values=jugos)
combobox1.place(relx=0.5,rely=0.5,anchor=CENTER)



class clase:
    def __init__(self,fruit_name,quantity):
        self.fruit= fruit_name
        self.quantity=int(quantity)
        self.var1 = 200
        
    def b(self):
        var2=self.quantity*self.var1
        print(var2)
        if (self.fruit=="Manzana"):
            var3=self.quantity*52
            label_6["image"]=image4
        elif(self.fruit=="Naranja"):
            var3=self.quantity*60
            label_6["image"]=image2
        elif(self.fruit=="Mango"):
            var3=self.quantity*62
            label_6["image"]=image3
            
        
            
        print(self.fruit +"  " +  str(self.quantity) +"  " +  str(var3))
        label_5["text"]=self.fruit +"  " +  str(self.quantity) +"  " +  str(var3)
        
    def getCost(self):
            self.b()
        
        
def c():
    fruit = combobox1.get()
    quantity = input1.get()
    obj1=clase(fruit,quantity)
    obj1.getCost()
button_1=Button(root,text="Calcular calorias",command=c)
button_1.place(relx=0.8,rely=0.4,anchor=CENTER)


root.mainloop()