from tkinter import *
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
from carProps import carProps

class application:        
    def __init__(self, window):
        ###################################################################
        ##################   Designs the tabs for GUI #####################
        ###################################################################
        self.master = window
        self.tab_control = ttk.Notebook(window)
        
        # Creates the desirable tabs for GUI 
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)
        self.tab5 = ttk.Frame(self.tab_control)
        self.tab6 = ttk.Frame(self.tab_control)
        
        # Tab for entering inputs and calculating the whole things
        self.tab_control.add(self.tab1, text='Inputs')
        
        # Plots the torque and power curves
        self.tab_control.add(self.tab2, text='Torque Curve')
        
        # Plots resistance curves for every gear at the torque curve
        # and the last gear x power output (under/overrevs or optimum project)
        self.tab_control.add(self.tab3, text='Power Curve')
        
        # Speed maps
        self.tab_control.add(self.tab4, text='Speed Maps')
        
        # Tractive forces
        self.tab_control.add(self.tab5, text='Tractive Forces')

        # About
        self.tab_control.add(self.tab6, text='About')
        
        # You're free to change the entire code, but please do not delete this part. 
        # It is very important to me to receive feedbacks.
        Title = "Geabox Calculator v1.0"
        appInfos ="""
        This software was originally designed by Rafael Basilio Chaves.
        The original version can be found at: https://github.com/rafaelbasilio/gearboxCalculator
        Feel free to distribute and modify it as you want.\n
        This sofrware is 100% free and OpenSource and it must stay like this. 
        The commercial use of it is allowed, but it is extrictly vorbiden to sell this software for any price.
        Feedbacks, improvements and suggestions are always welcome!
        Please get in touch with me: doutorautomovel@gmail.com
        Have Fun! 
        """
        self.title = Label(self.tab6, text=Title, font=("Helvetica", 14, 'bold'))
        self.title.pack(pady=30)
        self.information = Label(self.tab6, text=appInfos)
        self.information.pack()
        
        
        
        ###################################################################
        #######################  Tab 1: Inputs   ##########################
        ###################################################################
        self.LabelDescription = Label(self.tab1, text='Engine', font=("Helvetica", 10, 'bold'), padx=5, pady=15)
        self.LabelDescription.grid(column=0, row=0, sticky=W)
        
        # Torque input
        self.LabelDescription1 = Label(self.tab1, text='Torque (Nm)', padx=5, pady=5)
        self.LabelDescription1.grid(column=0, row=1, sticky=W)
        self.ValueDescription1 = Entry(self.tab1,width=20)
        self.ValueDescription1.insert(END, '266.4, 357.0, 386.3, 393.2, 392.3, 390.0, 391.6, 380.1, 349.9')
        self.ValueDescription1.grid(column=1, row=1)
        
        # Revs
        self.LabelDescription2 = Label(self.tab1, text='RPM', padx=5, pady=5)
        self.LabelDescription2.grid(column=0, row=2, sticky=W)
        self.ValueDescription2 = Entry(self.tab1,width=20)
        self.ValueDescription2.insert(END, '2000, 2500,3000,3500,4000,4500,5000,5500,6000')
        self.ValueDescription2.grid(column=1, row=2)
        
        self.LabelDescription = Label(self.tab1, text='General', font=("Helvetica", 10, 'bold'), padx=5, pady=15)
        self.LabelDescription.grid(column=0, row=3, sticky=W)
        
        # Mass
        self.LabelDescription3 = Label(self.tab1, text='Mass (kg)', padx=5, pady=5)
        self.LabelDescription3.grid(column=0, row=4, sticky=W)
        self.ValueDescription3 = Entry(self.tab1,width=20)
        self.ValueDescription3.insert(END, '1540')
        self.ValueDescription3.grid(column=1, row=4)
        
        # Ramp
        self.LabelDescription4 = Label(self.tab1, text='Max. Ramp (deg)', padx=5, pady=5)
        self.LabelDescription4.grid(column=0, row=5, sticky=W)
        self.ValueDescription4 = Entry(self.tab1,width=20)
        self.ValueDescription4.insert(END, '17')
        self.ValueDescription4.grid(column=1, row=5)
               
        # Dynamic Radius
        self.LabelDescription5 = Label(self.tab1, text='r_d (m)', padx=5, pady=5)
        self.LabelDescription5.grid(column=0, row=6, sticky=W)
        self.ValueDescription5 = Entry(self.tab1,width=20)
        self.ValueDescription5.insert(END, '0.34')
        self.ValueDescription5.grid(column=1, row=6)
        
        # Intertia
        self.LabelDescription6 = Label(self.tab1, text='Rotational Inertia Coeff.', padx=5, pady=5)
        self.LabelDescription6.grid(column=0, row=7, sticky=W)
        self.ValueDescription6 = Entry(self.tab1,width=20)
        self.ValueDescription6.insert(END, '1.3')
        self.ValueDescription6.grid(column=1, row=7)
        
        # Acceleration Inertia
        self.LabelDescription7 = Label(self.tab1, text='Max. Acc. from Inertia (g)', padx=5, pady=5)
        self.LabelDescription7.grid(column=0, row=8, sticky=W)
        self.ValueDescription7 = Entry(self.tab1,width=20)
        self.ValueDescription7.insert(END, '0.6')
        self.ValueDescription7.grid(column=1, row=8)
        
        # Rolling Resistance
        self.LabelDescription8 = Label(self.tab1, text='Rolling Resistance Coeff.', padx=5, pady=5)
        self.LabelDescription8.grid(column=0, row=9, sticky=W)
        self.ValueDescription8 = Entry(self.tab1,width=20)
        self.ValueDescription8.insert(END, '0.01')
        self.ValueDescription8.grid(column=1, row=9)
        
        self.LabelDescription = Label(self.tab1, text='Aerodynamics', font=("Helvetica", 10, 'bold'), padx=5, pady=15)
        self.LabelDescription.grid(column=0, row=10, sticky=W)
        
        # Drag
        self.LabelDescription9 = Label(self.tab1, text='Drag Coeff.', padx=5, pady=5)
        self.LabelDescription9.grid(column=0, row=11, sticky=W)
        self.ValueDescription9 = Entry(self.tab1,width=20)
        self.ValueDescription9.insert(END, '0.24')
        self.ValueDescription9.grid(column=1, row=11)
        
        # Frontal Area
        self.LabelDescription10 = Label(self.tab1, text='Frontal Area (m²)', padx=5, pady=5)
        self.LabelDescription10.grid(column=0, row=12, sticky=W)
        self.ValueDescription10 = Entry(self.tab1,width=20)
        self.ValueDescription10.insert(END, '2.34')
        self.ValueDescription10.grid(column=1, row=12)
        
        # Rho
        self.LabelDescription11 = Label(self.tab1, text='Air Density (kg/m³)', padx=5, pady=5)
        self.LabelDescription11.grid(column=0, row=13, sticky=W)
        self.ValueDescription11 = Entry(self.tab1,width=20)
        self.ValueDescription11.insert(END, '1.225')
        self.ValueDescription11.grid(column=1, row=13)
        
        # Top Speed
        self.LabelDescription12 = Label(self.tab1, text='Top Speed (km/h)', padx=5, pady=5)
        self.LabelDescription12.grid(column=0, row=14, sticky=W)
        self.ValueDescription12 = Entry(self.tab1,width=20)
        self.ValueDescription12.insert(END, '300')
        self.ValueDescription12.grid(column=1, row=14)
        
        # Calls the calculation methods
        self.calc = Button(self.tab1, text="Calculate", padx=10, pady=10, command=self.clicked)
        self.calc.grid(column=1, row=15, pady=15, padx = 20, sticky=W)
        
        # Closes Application
        self.quit = Button(self.tab1, text="Quit", padx=10, pady=10, command=self.master.destroy)
        self.quit.grid(column=0, row=15, pady=15, padx = 20, sticky=W)
        
        # Other parameters
        self.LabelDescription = Label(self.tab1, text='Other Parameters', font=("Helvetica", 10, 'bold'), padx=5, pady=15)
        self.LabelDescription.grid(column=3, row=0, padx = 20, sticky=W)
        
        # Differential
        self.LabelDescription13 = Label(self.tab1, text='Differential Ratio', padx=5, pady=5)
        self.LabelDescription13.grid(column=3, row=1,padx = 20, sticky=W)
        self.ValueDescription13 = Entry(self.tab1,width=20)
        self.ValueDescription13.insert(END, '3.0')
        self.ValueDescription13.grid(column=4, row=1, sticky=W)

        # RPM Top Speed
        self.LabelDescription14 = Label(self.tab1, text='RPM @ Top Speed', padx=5, pady=5)
        self.LabelDescription14.grid(column=3, row=2,padx = 20, sticky=W)
        self.ValueDescription14 = Entry(self.tab1,width=20)
        self.ValueDescription14.insert(END, '5500')
        self.ValueDescription14.grid(column=4, row=2, sticky=W)

        # Number of Gears
        self.LabelDescription15 = Label(self.tab1, text='Number of Gears', padx=5, pady=5)
        self.LabelDescription15.grid(column=3, row=3,padx = 20, sticky=W)
        self.ValueDescription15 = Entry(self.tab1,width=20)
        self.ValueDescription15.insert(END, '7')
        self.ValueDescription15.grid(column=4, row=3, sticky=W)

        # Text area for results
        self.text = Text(self.tab1, height=20, width=55, wrap=WORD)
        self.text.config(state=NORMAL)
        self.text.delete(1.0,END)
        self.text.insert(END,'Results will apear here!')
        self.text.config(state=DISABLED)
        self.text.grid(column=3, row=4, padx = 20, sticky=N+W+E, rowspan = 12, columnspan = 3)

        # Packs the entire tabs
        self.tab_control.pack(expand=1, fill='both')
        
    def clicked(self):
        torque =  [float(k) for k in self.ValueDescription1.get().split(',')]
        rpm =  [float(k) for k in self.ValueDescription2.get().split(',')]
        m = float(self.ValueDescription3.get())
        angle = float(self.ValueDescription4.get())
        r_d = float(self.ValueDescription5.get())
        L = float(self.ValueDescription6.get())
        a = float(self.ValueDescription7.get())
        f_r = float(self.ValueDescription8.get())
        c_x = float(self.ValueDescription9.get())
        A_f = float(self.ValueDescription10.get())
        rho = float(self.ValueDescription11.get())
        v = float(self.ValueDescription12.get())
        i_D = float(self.ValueDescription13.get())
        rpm_topSpeed = float(self.ValueDescription14.get())
        z = int(self.ValueDescription15.get())

        newCar = carProps(m,r_d,rpm,torque,angle,L,a,f_r,c_x,A_f,rho,v, i_D, rpm_topSpeed,z)

        results = 'To be sure that the top speed is reached, please check where the resistance torques are crossing the engine torque output at the next tabs.\n\n'
        results = results+'Theoretical Top Speed: '+str(round(newCar.topSpeed,2))+' km/h \n\n'

        for x in range(0,len(newCar.i)):
            results = results+'Gear '+str(x+1)+': '+str(round(newCar.i[x],2))+'\n'

        # Frist results
        self.text.config(state=NORMAL)
        self.text.delete(1.0,END)
        self.text.insert(END,results)
        self.text.config(state=DISABLED)

        # Plots Torques at tab2
        newCar.plotTorque()
        self.figtab2 = ttk.Frame(self.tab2)
        self.figtab2.grid(row=0, column=0)
        canvas1 = FigureCanvasTkAgg(newCar.figTorque, master=self.figtab2)
        canvas1.draw()
        canvas1.get_tk_widget().pack()

        # Plots Power at tab3
        newCar.plotPower()
        self.figtab3 = ttk.Frame(self.tab3)
        self.figtab3.grid(row=0, column=0)
        canvas2 = FigureCanvasTkAgg(newCar.figPower, master=self.figtab3)
        canvas2.draw()
        canvas2.get_tk_widget().pack()

        # Plots Power at tab4
        newCar.speedMap()
        self.figtab4 = ttk.Frame(self.tab4)
        self.figtab4.grid(row=0, column=0)
        canvas3 = FigureCanvasTkAgg(newCar.figSpeedMap, master=self.figtab4)
        canvas3.draw()
        canvas3.get_tk_widget().pack()

        # Plots Power at tab5
        newCar.tractiveForces()
        self.figtab5 = ttk.Frame(self.tab5)
        self.figtab5.grid(row=0, column=0)
        canvas4 = FigureCanvasTkAgg(newCar.figTractiveForces, master=self.figtab5)
        canvas4.draw()
        canvas4.get_tk_widget().pack()

window = Tk()
window.title("Smart Gearbox Calculator v1.0")
window.geometry('800x600')
window.resizable(width=False, height=False)
app = application(window)
window.mainloop()


