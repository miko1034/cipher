from tkinter import *

#window
window = Tk()
window.geometry("250x350")

#frames
titleframe = Frame(window,bg="light blue",highlightcolor="black",highlightthickness=1)
mainframe = Frame(window,bg="light blue",highlightcolor="black",highlightthickness=1)

#objects
title = Label(titleframe,text="Enciptor and Decriptor",font=("Ubuntu", 15),bg="light blue")
title.place(x=10,y=10)


#packing

titleframe.pack()
titleframe.pack_propagate(False)
titleframe.configure(width=250,height=50,)
mainframe.pack(side=BOTTOM)
mainframe.pack_propagate(False)
mainframe.configure(width=250,height=300)
window.mainloop()

# why have i started making a ui before actually making functional code? idk you tell me