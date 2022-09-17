from tkinter import * 
import random
root = Tk()
root.geometry("600x600")
root.title("Dictionary")



dictionary = {"Colors" : ["red","orange", "yellow", "green", "blue", "black", "purple", "pink", "cyan"]}
             
def changebg():
    color = random.randint(0, 8)
    dictionary["Colors"][color]
    print(color)
    root.configure(background = dictionary["Colors"][color])

    
    
b_color = Button(root, text = "Change Background Color", command = changebg, fg = "black" , bg = "gold" )
b_color.place(relx = 0.5, rely = 0.5, anchor = CENTER)



root.mainloop();