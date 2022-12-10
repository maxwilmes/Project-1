from tkinter import *
from tkinter import ttk
import math


class GUI:
    def __init__(self, window):
        self.window = window
        self.tabControl = ttk.Notebook(self.window)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tab5 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='AREA')
        self.tabControl.add(self.tab2, text='PERIMETER')
        self.tabControl.add(self.tab3, text='VOLUME')
        self.tabControl.add(self.tab4, text='DERIVATIVE')
        self.tabControl.pack(expand=1, fill="both")

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result, height=10,width=50, font=('', 16))
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        self.frame_compute = Frame(self.window)
        self.button_compute = Button(self.frame_compute,height=2,width=15,text='COMPUTE',command=lambda: self.compute())
        self.button_clear = Button(self.frame_compute,height=2,width=15,text='CLEAR',command=lambda: self.clear())
        self.button_compute.pack(side='left',pady=10,padx=10)
        self.button_clear.pack(side='right',pady=10,padx=10)
        self.frame_compute.pack(pady=10)

        # Window setup for area tab

        self.frame_area = Frame(self.tab1)
        self.label_area = Label(self.frame_area, text='SELECT SHAPE\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_area_square = Radiobutton(self.frame_area, text='SQUARE', variable=self.radio_1, value=1,
                                             command=lambda: self.select_shape())
        self.radio_area_rectangle = Radiobutton(self.frame_area, text='RECTANGLE', variable=self.radio_1, value=2,
                                                command=lambda: self.select_shape())
        self.radio_area_triangle = Radiobutton(self.frame_area, text='TRIANGLE', variable=self.radio_1, value=3,
                                               command=lambda: self.select_shape())
        self.radio_area_circle = Radiobutton(self.frame_area, text='CIRCLE', variable=self.radio_1, value=4,
                                             command=lambda: self.select_shape())
        self.label_area.pack(side='left', padx=5)
        self.radio_area_square.pack(side='left')
        self.radio_area_rectangle.pack(side='left')
        self.radio_area_triangle.pack(side='left')
        self.radio_area_circle.pack(side='left')
        self.frame_area.pack(anchor='w', pady=10)

        # Window setup for perimeter tab

        self.frame_perimeter = Frame(self.tab2)
        self.label_perimeter = Label(self.frame_perimeter, text='SELECT SHAPE\t')
        self.radio_per_square = Radiobutton(self.frame_perimeter, text='SQUARE', variable=self.radio_1, value=5,
                                            command=lambda: self.select_shape())
        self.radio_per_rectangle = Radiobutton(self.frame_perimeter, text='RECTANGLE', variable=self.radio_1, value=6,
                                               command=lambda: self.select_shape())
        self.radio_per_triangle = Radiobutton(self.frame_perimeter, text='TRIANGLE', variable=self.radio_1, value=7,
                                              command=lambda: self.select_shape())
        self.radio_per_circle = Radiobutton(self.frame_perimeter, text='CIRCLE', variable=self.radio_1, value=8,
                                            command=lambda: self.select_shape())
        self.label_perimeter.pack(side='left', padx=5)
        self.radio_per_square.pack(side='left')
        self.radio_per_rectangle.pack(side='left')
        self.radio_per_triangle.pack(side='left')
        self.radio_per_circle.pack(side='left')
        self.frame_perimeter.pack(anchor='w', pady=10)

        # Setup for volume tab

        self.frame_volume = Frame(self.tab3)
        self.label_volume = Label(self.frame_volume, text='SELECT SHAPE')
        self.radio_vol_square = Radiobutton(self.frame_volume, text='CUBE', variable=self.radio_1, value=9,
                                            command=lambda: self.select_shape())
        self.radio_vol_rectangle = Radiobutton(self.frame_volume, text='RECTANGULAR PRISM', variable=self.radio_1, value=10,
                                               command=lambda: self.select_shape())
        self.radio_vol_triangle = Radiobutton(self.frame_volume, text='TRIANGULAR PRISM', variable=self.radio_1, value=11,
                                              command=lambda: self.select_shape())
        self.radio_vol_circle = Radiobutton(self.frame_volume, text='SPHERE', variable=self.radio_1, value=12,
                                            command=lambda: self.select_shape())
        self.label_volume.pack(side='left', padx=5)
        self.radio_vol_square.pack(side='left')
        self.radio_vol_rectangle.pack(side='left')
        self.radio_vol_triangle.pack(side='left')
        self.radio_vol_circle.pack(side='left')
        self.frame_volume.pack(anchor='w', pady=10)

        self.square_area_frame = Frame(self.tab1)
        self.square_area_label = Label(self.square_area_frame, text='SIDE LENGTH\t')
        self.square_area_entry = Entry(self.square_area_frame,width=50)

        self.rectangle_area_frame_1 = Frame(self.tab1)
        self.rectangle_area_label_1 = Label(self.rectangle_area_frame_1, text='WIDTH\t')
        self.rectangle_area_entry_1 = Entry(self.rectangle_area_frame_1,width=50)
        self.rectangle_area_frame_2 = Frame(self.tab1)
        self.rectangle_area_label_2 = Label(self.rectangle_area_frame_2, text='LENGTH\t')
        self.rectangle_area_entry_2 = Entry(self.rectangle_area_frame_2,width=50)

        self.triangle_area_frame_1 = Frame(self.tab1)
        self.triangle_area_label_1 = Label(self.triangle_area_frame_1, text='BASE\t')
        self.triangle_area_entry_1 = Entry(self.triangle_area_frame_1,width=50)
        self.triangle_area_frame_2 = Frame(self.tab1)
        self.triangle_area_label_2 = Label(self.triangle_area_frame_2, text='HEIGHT\t')
        self.triangle_area_entry_2 = Entry(self.triangle_area_frame_2,width=50)

        self.circle_area_frame = Frame(self.tab1)
        self.circle_area_label = Label(self.circle_area_frame, text='RADIUS\t')
        self.circle_area_entry = Entry(self.circle_area_frame,width=50)

        self.square_perimeter_frame = Frame(self.tab2)
        self.square_perimeter_label = Label(self.square_perimeter_frame, text='SIDE LENGTH\t')
        self.square_perimeter_entry = Entry(self.square_perimeter_frame,width=50)

        self.rectangle_perimeter_frame_1 = Frame(self.tab2)
        self.rectangle_perimeter_label_1 = Label(self.rectangle_perimeter_frame_1, text='WIDTH\t')
        self.rectangle_perimeter_entry_1 = Entry(self.rectangle_perimeter_frame_1,width=50)
        self.rectangle_perimeter_frame_2 = Frame(self.tab2)
        self.rectangle_perimeter_label_2 = Label(self.rectangle_perimeter_frame_2, text='LENGTH\t')
        self.rectangle_perimeter_entry_2 = Entry(self.rectangle_perimeter_frame_2,width=50)

        self.triangle_perimeter_frame_1 = Frame(self.tab2)
        self.triangle_perimeter_label_1 = Label(self.triangle_perimeter_frame_1, text='SIDE 1 LENGTH\t')
        self.triangle_perimeter_entry_1 = Entry(self.triangle_perimeter_frame_1,width=50)
        self.triangle_perimeter_frame_2 = Frame(self.tab2)
        self.triangle_perimeter_label_2 = Label(self.triangle_perimeter_frame_2, text='SIDE 2 LENGTH\t')
        self.triangle_perimeter_entry_2 = Entry(self.triangle_perimeter_frame_2,width=50)
        self.triangle_perimeter_frame_3 = Frame(self.tab2)
        self.triangle_perimeter_label_3 = Label(self.triangle_perimeter_frame_3, text='SIDE 3 LENGTH\t')
        self.triangle_perimeter_entry_3 = Entry(self.triangle_perimeter_frame_3,width=50)

        self.circle_perimeter_frame = Frame(self.tab2)
        self.circle_perimeter_label = Label(self.circle_perimeter_frame, text='RADIUS\t')
        self.circle_perimeter_entry = Entry(self.circle_perimeter_frame,width=50)

        self.square_volume_frame = Frame(self.tab3)
        self.square_volume_label = Label(self.square_volume_frame, text='SIDE LENGTH\t')
        self.square_volume_entry = Entry(self.square_volume_frame, width=50)

        self.rectangle_volume_frame_1 = Frame(self.tab3)
        self.rectangle_volume_label_1 = Label(self.rectangle_volume_frame_1, text='WIDTH\t')
        self.rectangle_volume_entry_1 = Entry(self.rectangle_volume_frame_1, width=50)
        self.rectangle_volume_frame_2 = Frame(self.tab3)
        self.rectangle_volume_label_2 = Label(self.rectangle_volume_frame_2, text='LENGTH\t')
        self.rectangle_volume_entry_2 = Entry(self.rectangle_volume_frame_2, width=50)
        self.rectangle_volume_frame_3 = Frame(self.tab3)
        self.rectangle_volume_label_3 = Label(self.rectangle_volume_frame_3, text='DEPTH\t')
        self.rectangle_volume_entry_3 = Entry(self.rectangle_volume_frame_3, width=50)

        self.triangle_volume_frame_1 = Frame(self.tab3)
        self.triangle_volume_label_1 = Label(self.triangle_volume_frame_1, text='BASE\t')
        self.triangle_volume_entry_1 = Entry(self.triangle_volume_frame_1, width=50)
        self.triangle_volume_frame_2 = Frame(self.tab3)
        self.triangle_volume_label_2 = Label(self.triangle_volume_frame_2, text='HEIGHT\t')
        self.triangle_volume_entry_2 = Entry(self.triangle_volume_frame_2, width=50)
        self.triangle_volume_frame_3 = Frame(self.tab3)
        self.triangle_volume_label_3 = Label(self.triangle_volume_frame_3, text='DEPTH\t')
        self.triangle_volume_entry_3 = Entry(self.triangle_volume_frame_3, width=50)

        self.circle_volume_frame = Frame(self.tab3)
        self.circle_volume_label = Label(self.circle_volume_frame, text='RADIUS\t')
        self.circle_volume_entry = Entry(self.circle_volume_frame, width=50)

    def select_shape(self):
        selection = self.radio_1.get()
        if selection == 1 or selection == 5 or selection == 9:
            # Removing old widgets
            self.rectangle_area_frame_1.pack_forget()
            self.rectangle_area_frame_2.pack_forget()
            self.rectangle_perimeter_frame_1.pack_forget()
            self.rectangle_perimeter_frame_2.pack_forget()
            self.rectangle_volume_frame_1.pack_forget()
            self.rectangle_volume_frame_2.pack_forget()
            self.rectangle_volume_frame_3.pack_forget()
            self.triangle_area_frame_1.pack_forget()
            self.triangle_area_frame_2.pack_forget()
            self.triangle_perimeter_frame_1.pack_forget()
            self.triangle_perimeter_frame_2.pack_forget()
            self.triangle_perimeter_frame_3.pack_forget()
            self.triangle_volume_frame_1.pack_forget()
            self.triangle_volume_frame_2.pack_forget()
            self.triangle_volume_frame_3.pack_forget()
            self.circle_area_frame.pack_forget()
            self.circle_perimeter_frame.pack_forget()
            self.circle_volume_frame.pack_forget()
            # Re-Packing desired widgets
            self.square_perimeter_label.pack(side='left')
            self.square_perimeter_entry.pack(side='left')
            self.square_perimeter_frame.pack(anchor='w', padx=5, pady=5)
            self.square_area_label.pack(side='left')
            self.square_area_entry.pack(side='left')
            self.square_area_frame.pack(anchor='w', padx=5, pady=5)
            self.square_volume_label.pack(side='left')
            self.square_volume_entry.pack(side='left')
            self.square_volume_frame.pack(anchor='w', padx=5, pady=5)

        elif selection == 2 or selection == 6 or selection == 10:
            # Removing old widgets
            self.square_area_frame.pack_forget()
            self.square_perimeter_frame.pack_forget()
            self.square_volume_frame.pack_forget()
            self.triangle_area_frame_1.pack_forget()
            self.triangle_area_frame_2.pack_forget()
            self.triangle_perimeter_frame_1.pack_forget()
            self.triangle_perimeter_frame_2.pack_forget()
            self.triangle_perimeter_frame_3.pack_forget()
            self.triangle_volume_frame_1.pack_forget()
            self.triangle_volume_frame_2.pack_forget()
            self.triangle_volume_frame_3.pack_forget()
            self.circle_area_frame.pack_forget()
            self.circle_perimeter_frame.pack_forget()
            self.circle_volume_frame.pack_forget()
            # Re-Packing desired widgets
            self.rectangle_area_label_1.pack(side='left')
            self.rectangle_area_entry_1.pack(side='left')
            self.rectangle_area_label_2.pack(side='left')
            self.rectangle_area_entry_2.pack(side='left')
            self.rectangle_area_frame_1.pack(anchor='w', padx=5, pady=5)
            self.rectangle_area_frame_2.pack(anchor='w', padx=5, pady=5)
            self.rectangle_perimeter_label_1.pack(side='left')
            self.rectangle_perimeter_entry_1.pack(side='left')
            self.rectangle_perimeter_label_2.pack(side='left')
            self.rectangle_perimeter_entry_2.pack(side='left')
            self.rectangle_perimeter_frame_1.pack(anchor='w', padx=5, pady=5)
            self.rectangle_perimeter_frame_2.pack(anchor='w', padx=5, pady=5)
            self.rectangle_volume_label_1.pack(side='left')
            self.rectangle_volume_entry_1.pack(side='left')
            self.rectangle_volume_label_2.pack(side='left')
            self.rectangle_volume_entry_2.pack(side='left')
            self.rectangle_volume_label_3.pack(side='left')
            self.rectangle_volume_entry_3.pack(side='left')
            self.rectangle_volume_frame_1.pack(anchor='w', padx=5, pady=5)
            self.rectangle_volume_frame_2.pack(anchor='w', padx=5, pady=5)
            self.rectangle_volume_frame_3.pack(anchor='w', padx=5, pady=5)
        elif selection == 3 or selection == 7 or selection == 11:
            # Removing old widgets
            self.square_area_frame.pack_forget()
            self.square_perimeter_frame.pack_forget()
            self.square_volume_frame.pack_forget()
            self.rectangle_area_frame_1.pack_forget()
            self.rectangle_area_frame_2.pack_forget()
            self.rectangle_perimeter_frame_1.pack_forget()
            self.rectangle_perimeter_frame_2.pack_forget()
            self.rectangle_volume_frame_1.pack_forget()
            self.rectangle_volume_frame_2.pack_forget()
            self.rectangle_volume_frame_3.pack_forget()
            self.circle_area_frame.pack_forget()
            self.circle_perimeter_frame.pack_forget()
            self.circle_volume_frame.pack_forget()
            # Re-Packing desired widgets
            self.triangle_area_label_1.pack(side='left')
            self.triangle_area_entry_1.pack(side='left')
            self.triangle_area_label_2.pack(side='left')
            self.triangle_area_entry_2.pack(side='left')
            self.triangle_area_frame_1.pack(anchor='w', padx=5, pady=5)
            self.triangle_area_frame_2.pack(anchor='w', padx=5, pady=5)
            self.triangle_perimeter_label_1.pack(side='left')
            self.triangle_perimeter_entry_1.pack(side='left')
            self.triangle_perimeter_label_2.pack(side='left')
            self.triangle_perimeter_entry_2.pack(side='left')
            self.triangle_perimeter_label_3.pack(side='left')
            self.triangle_perimeter_entry_3.pack(side='left')
            self.triangle_perimeter_frame_1.pack(anchor='w', padx=5, pady=5)
            self.triangle_perimeter_frame_2.pack(anchor='w', padx=5, pady=5)
            self.triangle_perimeter_frame_3.pack(anchor='w', padx=5, pady=5)
            self.triangle_volume_label_1.pack(side='left')
            self.triangle_volume_entry_1.pack(side='left')
            self.triangle_volume_label_2.pack(side='left')
            self.triangle_volume_entry_2.pack(side='left')
            self.triangle_volume_label_3.pack(side='left')
            self.triangle_volume_entry_3.pack(side='left')
            self.triangle_volume_frame_1.pack(anchor='w', padx=5, pady=5)
            self.triangle_volume_frame_2.pack(anchor='w', padx=5, pady=5)
            self.triangle_volume_frame_3.pack(anchor='w', padx=5, pady=5)
        elif selection == 4 or selection == 8 or selection == 12:
            # Removing old widgets
            self.square_area_frame.pack_forget()
            self.square_perimeter_frame.pack_forget()
            self.square_volume_frame.pack_forget()
            self.rectangle_area_frame_1.pack_forget()
            self.rectangle_area_frame_2.pack_forget()
            self.rectangle_perimeter_frame_1.pack_forget()
            self.rectangle_perimeter_frame_2.pack_forget()
            self.rectangle_volume_frame_1.pack_forget()
            self.rectangle_volume_frame_2.pack_forget()
            self.rectangle_volume_frame_3.pack_forget()
            self.triangle_area_frame_1.pack_forget()
            self.triangle_area_frame_2.pack_forget()
            self.triangle_perimeter_frame_1.pack_forget()
            self.triangle_perimeter_frame_2.pack_forget()
            self.triangle_perimeter_frame_3.pack_forget()
            self.triangle_volume_frame_1.pack_forget()
            self.triangle_volume_frame_2.pack_forget()
            self.triangle_volume_frame_3.pack_forget()
            # Re-Packing desired widgets
            self.circle_area_label.pack(side='left')
            self.circle_area_entry.pack(side='left')
            self.circle_area_frame.pack(anchor='w', padx=5, pady=5)
            self.circle_perimeter_label.pack(side='left')
            self.circle_perimeter_entry.pack(side='left')
            self.circle_perimeter_frame.pack(anchor='w', padx=5, pady=5)
            self.circle_volume_label.pack(side='left')
            self.circle_volume_entry.pack(side='left')
            self.circle_volume_frame.pack(anchor='w', padx=5, pady=5)

    def compute(self):
        selection = self.radio_1.get()
        try:
            if selection == 1:
                side_length = float(self.square_area_entry.get())
                if side_length <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    area = side_length ** 2
                    self.label_result.config(text=f'Area of square is {area:,.2f}')
            if selection == 2:
                width = float(self.rectangle_area_entry_1.get())
                length = float(self.rectangle_area_entry_2.get())
                if width <= 0 or length <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    area = length * width
                    self.label_result.config(text=f'Area of rectangle is {area:,.2f}')
            if selection == 3:
                base = float(self.triangle_area_entry_1.get())
                height = float(self.triangle_area_entry_2.get())
                if base <= 0 or height <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    area = base * height * 0.5
                    self.label_result.config(text=f'Area of triangle is {area:,.2f}')
            if selection == 4:
                radius = float(self.circle_area_entry.get())
                if radius <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    area = math.pi * radius ** 2
                    self.label_result.config(text=f'Area of circle is {area:,.2f}')
            if selection == 5:
                side_length = float(self.square_perimeter_entry.get())
                if side_length <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    perimeter = side_length * 4
                    self.label_result.config(text=f'Perimeter of square is {perimeter:,.2f}')
            if selection == 6:
                width = float(self.rectangle_perimeter_entry_1.get())
                length = float(self.rectangle_perimeter_entry_2.get())
                if width <= 0 or length <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    perimeter = (length + width) * 2
                    self.label_result.config(text=f'Perimeter of rectangle is {perimeter:,.2f}')
            if selection == 7:
                side1 = float(self.triangle_perimeter_entry_1.get())
                side2 = float(self.triangle_perimeter_entry_2.get())
                side3 = float(self.triangle_perimeter_entry_3.get())
                if side1 <= 0 or side2 <= 0 or side3 <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    perimeter = side1 + side2 + side3
                    self.label_result.config(text=f'Perimeter of triangle is {perimeter:,.2f}')
            if selection == 8:
                radius = float(self.circle_perimeter_entry.get())
                if radius <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    perimeter = math.pi * radius * 2
                    self.label_result.config(text=f'Circumference of circle is {perimeter:,.2f}')
            if selection == 9:
                side_length = float(self.square_volume_entry.get())
                if side_length <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    volume = side_length ** 3
                    self.label_result.config(text=f'Volume of cube is {volume:,.2f}')
            if selection == 10:
                width = float(self.rectangle_volume_entry_1.get())
                length = float(self.rectangle_volume_entry_2.get())
                height = float(self.rectangle_volume_entry_3.get())
                if width <= 0 or height <= 0 or length <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    volume = length * width * height
                    self.label_result.config(text=f'Volume of rectangular prism is {volume:,.2f}')
            if selection == 11:
                base = float(self.triangle_volume_entry_1.get())
                height = float(self.triangle_volume_entry_2.get())
                depth = float(self.triangle_volume_entry_3.get())
                if base <= 0 or height <= 0 or depth <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    volume = base * height * depth * 0.5
                    self.label_result.config(text=f'Volume of triangle is {volume:,.2f}')
            if selection == 12:
                radius = float(self.circle_volume_entry.get())
                if radius <= 0:
                    self.label_result.config(text=f'Nonzero positive values only!')
                else:
                    volume = math.pi * (radius ** 3) * 4 / 3
                    self.label_result.config(text=f'Volume of sphere is {volume:,.2f}')
        except(ValueError):
            self.label_result.config(text=f'Enter Numeric Values!')


    def clear(self):
        self.label_result.config(text='')
        self.square_area_entry.delete(0, END)
        self.square_perimeter_entry.delete(0, END)
        self.square_volume_entry.delete(0, END)
        self.rectangle_area_entry_1.delete(0, END)
        self.rectangle_area_entry_2.delete(0, END)
        self.rectangle_perimeter_entry_1.delete(0, END)
        self.rectangle_perimeter_entry_2.delete(0, END)
        self.rectangle_volume_entry_1.delete(0, END)
        self.rectangle_volume_entry_2.delete(0, END)
        self.rectangle_volume_entry_3.delete(0, END)
        self.triangle_area_entry_1.delete(0, END)
        self.triangle_area_entry_2.delete(0, END)
        self.triangle_perimeter_entry_1.delete(0, END)
        self.triangle_perimeter_entry_2.delete(0, END)
        self.triangle_perimeter_entry_3.delete(0, END)
        self.triangle_volume_entry_1.delete(0, END)
        self.triangle_volume_entry_2.delete(0, END)
        self.triangle_volume_entry_3.delete(0, END)
        self.circle_area_entry.delete(0, END)
        self.circle_perimeter_entry.delete(0, END)
        self.circle_volume_entry.delete(0, END)
