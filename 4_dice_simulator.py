import random
from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry('400x400')
root.title("Dice Rolling Simulator")

Label(root,text="").pack()  # Add a Blank Line to Manage the heading space
Label(root,text="Dice Rolling Simulator",font='Helvetica 20 bold italic',bg='dark green',fg='light green').pack()

# Adding The Images
images = ['./Dice/die1.png','./Dice/die2.png','./Dice/die3.png',
            './Dice/die4.png','./Dice/die5.png','./Dice/die6.png']

image_name = random.choice(images)
image = ImageTk.PhotoImage(Image.open(image_name))

img_label = Label(root,image=image)
img_label.image = image
img_label.pack(expand=True)

image_pos = images.index(image_name) + 1
dice_number = Label(root,text=str(image_pos),font='Helvetica 20 bold')
dice_number.pack()

# Function to change the Image and the number outputted.
def roll():
    image_name = random.choice(images)
    image = ImageTk.PhotoImage(Image.open(image_name))
    img_label.configure(image=image)
    img_label.image = image

    image_pos = images.index(image_name) + 1
    dice_number.configure(text=str(image_pos))

Button(root,text='Roll the Dice',command=roll,fg='blue').pack(expand=True)
root.mainloop()
