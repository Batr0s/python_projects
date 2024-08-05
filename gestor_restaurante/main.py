from tkinter import *

# Start tkinter
app = Tk()

# Screen size and location
app.geometry('1000x600+0+0')

# Prevent size adjustment
app.resizable(0, 0)

# Screen title
app.title('Restaurante - Sistema de facturación')

# Screen background color
app.config(bg='#87CEFA')

# Top panel
top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# Title label
title_label = Label(top_panel, text='Sistema de facturación', fg='black', font=('Dosis', 50),  bg='#87CEFA', width=27)
title_label.grid(row=0, column=0)

# Left panel
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Costs panel
costs_panel = Frame(left_panel, bd=1, relief=FLAT)
costs_panel.pack(side=BOTTOM)

# Food panel
food_panel = LabelFrame(app, text='Comida', font=('Dosis', 19, 'bold'), fg='black', bd=1, relief=FLAT)
food_panel.pack(side=LEFT)

# Drinks panel
drinks_panel = LabelFrame(app, text='Drinks', font=('Dosis', 19, 'bold'), fg='black', bd=1, relief=FLAT)
drinks_panel.pack(side=LEFT)

# Desserts panel
desserts_panel = LabelFrame(app, text='Desserts', font=('Dosis', 19, 'bold'), fg='black', bd=1, relief=FLAT)
desserts_panel.pack(side=LEFT)

# Right panel
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calc_panel = Frame(right_panel, bd=1, relief=FLAT)
calc_panel.pack()

# Bill panel
bills_panel = Frame(right_panel, bd=1, relief=FLAT)
bills_panel.pack()

# Buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT)
buttons_panel.pack()

# Food list
foods_list = ['Pollo', 'Cordero', 'Cerdo', 'Ternera', 'Pizza', 'Salmon', 'Bacalao', 'Sardinas']
drinks_list = ['Agua', 'Refresco', 'Cerveza', 'Cava', 'Gaseosa', 'Zumo']
desserts_list = ['Pastel', 'Cheesecake', 'Carrotcake', 'Flan', 'Crema catalana', 'Yogur', 'Fruta']

# Food items
counter = 0
food_var = []
for food in foods_list:
    food_var.append('')
    food_var[counter] = IntVar()
    # onvalue and offvalue are the value when the checkbox is activated or not
    food_button = Checkbutton(food_panel, text=food, font=('Dosis', 19), onvalue=1,
                              offvalue=0, variable=food_var[counter])
    # stick is for justify content to the left
    food_button.grid(row=counter, column=0, sticky=W)
    counter += 1

# Drinks items
counter = 0
drinks_var = []
for drink in drinks_list:
    drinks_var.append('')
    drinks_var[counter] = IntVar()
    # onvalue and offvalue are the value when the checkbox is activated or not
    drinks_button = Checkbutton(drinks_panel, text=drink, font=('Dosis', 19),
                                onvalue=1, offvalue=0, variable=drinks_var[counter])
    # stick is for justify content to the left
    drinks_button.grid(row=counter, column=0, sticky=W)
    counter += 1

# Desserts items
counter = 0
desserts_var = []
for dessert in desserts_list:
    desserts_var.append('')
    desserts_var[counter] = IntVar()
    # onvalue and offvalue are the value when the checkbox is activated or not
    desserts_button = Checkbutton(desserts_panel, text=dessert, font=('Dosis', 19),
                                  onvalue=1, offvalue=0, variable=desserts_var[counter])
    # stick is for justify content to the left
    desserts_button.grid(row=counter, column=0, sticky=W)
    counter += 1

# Run app
app.mainloop()

