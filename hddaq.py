from tkinter import *
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


analog_voltage_input = [1,2,3,4,5,6,7,8]
thermocouple_input = [1,2,3,4]
analog_output = [1,2]
digital_i_o = [1,2,3,4,5,6,7,8]
results_chart = ["Q Factor","Thrust","Thrust/P"]
counter = 0
r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 3

class NewWindow(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.geometry("400x400")
        label = Label(self,text="This is a new window.")
        #label.pack()
        label.grid(row=0,column=1)
        
class NoiseWindow(Toplevel):
    def __init__(self,master=None):
        Frame.__init__(self,master)
#        self.title("External Noise Input Menu")
#        self.geometry("400x400")
#        label = Label(self,text="This is a new window.")
#        #label.pack()
#        label.grid(row=0,column=1)
        root2 = Tk()
        Label(root2, text ="Check any factor that may have contributed to noise:").grid(row=0,column=0)
        chkbtn0 = ttk.Checkbutton(root2, text ='Checkbutton1',
        takefocus = 0).grid(row=1,column=1)
        chkbtn1 = ttk.Checkbutton(root2, text = "No external noise", justify=LEFT,offrelief=0).grid(row=2,column=0)
        chkbtn2 = ttk.Checkbutton(root2, text = "Air Currents (Atmospheric Test)", justify=LEFT).grid(row=3,column=0)
        chkbtn3 = ttk.Checkbutton(root2, text = "RF Interaction with the Surrounding Environment", justify=LEFT).grid(row=4,column=0)
        chkbtn4 = ttk.Checkbutton(root2, text = "Magnetic Interaction", justify=LEFT).grid(row=5,column=0)
        chkbtn5 = ttk.Checkbutton(root2, text = "Thermal Expansion and Contraction", justify=LEFT).grid(row=6,column=0)
        chkbtn6 = ttk.Checkbutton(root2, text = "Vibration", justify=LEFT).grid(row=7,column=0)
        chkbtn7 = ttk.Checkbutton(root2, text = "Electrostatic Interaction", justify=LEFT).grid(row=8,column=0)
        chkbtn8 = ttk.Checkbutton(root2, text = "Outgassing", justify=LEFT).grid(row=9,column=0)
        chkbtn9 = ttk.Checkbutton(root2, text = "Photon Rocket Force", justify=LEFT).grid(row=10,column=0)
        chkbtn10 = ttk.Checkbutton(root2, text = "Impulsive/Thermal Signal Decoupling Error", justify=LEFT).grid(row=11,column=0)
        
class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("HORIZON DRIVE DAQ PROGRAM")
        #self.pack(fill=BOTH,expand=1)
    
        # TOP MENU BAR COMMANDS AND FUNCTIONS
        menu=Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        edit = Menu(menu)
        view = Menu(menu)
        window_menu = Menu(menu)
        help_menu = Menu(menu)

        file.add_command(label="Exit",command=self.client_exit)
        edit.add_command(label="Undo")
        view.add_command(label="Show Toolbar",command=self.client_exit)
        window_menu.add_command(label="Resize Window", command=self.client_exit)
        help_menu.add_command(label="Search functions", command=self.client_exit)

        menu.add_cascade(label="File",menu=file)
        menu.add_cascade(label="Edit",menu=edit)
        menu.add_cascade(label="View",menu=view)
        menu.add_cascade(label="Window",menu=window_menu)
        menu.add_cascade(label="Help",menu=help_menu)

    # Function to kill the program
    def client_exit(self):
        exit()

def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()

# driver code
if __name__ == "__main__":
    root = Tk() # Create a new GUI window
    root.configure(background = 'light blue') # Set the background color of GUI window
    root.geometry("2100x1500") # Set the configuration of GUI window
    
    app = Window(root)
    headlabel = Label(root,text="Horizon Drive",fg='black',font=('futura',24,'italic'))
    tabControl = ttk.Notebook(root)

    test_start_button = Button(root,text="START",bg="green",fg="black")
    test_pause_button = Button(root,text="STOP TEST",bg="red",fg="black")
    reset_button = Button(root,text="RESET",bg="yellow",fg="black")
    clear_button = Button(root,text="CLEAR",bg="red",fg="black")
    
    test_start_button.grid(row=1,column=0)
    test_pause_button.grid(row=2,column=0)
    reset_button.grid(row=3,column=0)
    clear_button.grid(row=4,column=0)
    
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab1,text="MCC 118 ANALOG VOLTAGE INPUT")
    tabControl.add(tab2,text="MCC 134 THERMOCOUPLE INPUT")
    tabControl.add(tab3,text="MCC 152 ANALOG OUTPUT / DIGITAL I/O")
    #tabControl.pack(expand=1,fill="both")

    for channels in analog_voltage_input:
        ttk.Label(tab1,text=channels,relief=RIDGE,width=5).grid(column=0,row=r1)
        ttk.Label(tab1,text=channels,width=10).grid(row=r1,column=1)
        avi_btn = ttk.Button(tab1,text=channels,width=10)
        avi_btn.grid(row=r1,column=2)
        avi_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Entry(tab1,text=channels,width=10).grid(row=r1,column=3)
        r1+=1
        
    for channels in thermocouple_input:
        ttk.Label(tab2,text=channels,relief=RIDGE,width=5).grid(column=0,row=r2)
        ttk.Label(tab2,text=channels,width=10).grid(row=r2,column=1)
        thermo_btn = ttk.Button(tab2,text=channels,width=10)
        thermo_btn.grid(row=r2,column=2)
        thermo_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab2,text=channels,width=10).grid(row=r2,column=3)
        r2+=1
        
    for channels in analog_output:
        ttk.Label(tab3,text=channels,relief=RIDGE,width=5).grid(column=0,row=r3)
        ttk.Label(tab3,text=channels,width=10).grid(row=r3,column=1)
        ttk.Entry(tab3,text=channels,width=10).grid(row=r3,column=2)
        ao_btn = ttk.Button(tab3,text=channels,width=10)
        ao_btn.grid(row=r3,column=3)
        ao_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab3,text=channels,width=10).grid(row=r3,column=4)
        r3+=1
        
    for channels in digital_i_o:
        ttk.Label(tab3,text=channels,relief=RIDGE,width=5).grid(column=0,row=r4)
        ttk.Label(tab3,text=channels,width=10).grid(row=r4,column=1)
        dio_btn = ttk.Button(tab3,text=channels,width=10)
        dio_btn.grid(row=r4,column=2)
        dio_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab3,text=channels,width=10).grid(row=r4,column=3)
        r4+=1
        
    Message(text="Results\n Q Factor:\n Thrust:\n Thrust/Power:\n",relief=RIDGE,width=100).grid(row=5,column=1)
    Message(text="Active Sensors\n Thermocouple\n Current Sensor\n Vacuum Pressure\n Magnetic Field\n Laser\n",relief=RIDGE,width=200).grid(row=5,column=2)
    noise_btn = Button(text="External Disturbance Input\n (Click after a test cycle is conducted if needed.)")
    noise_btn.grid(row=3,column=3)
    noise_btn.bind("<Button>",lambda e: NoiseWindow(root))
    
    # grid method is used for placing widgets at their respective positions
    headlabel.grid(row=0,column=1)
    tabControl.grid(row=5,column=0)
    Label(text="Set test cycle length:").grid(row=2,column=1)
    cycle_length = Spinbox(from_=0,to=5,justify=CENTER).grid(row=3,column=1)
    
    uN_mA_graph = Figure(figsize=(4,4),dpi=100)
    nm_uN_graph = Figure(figsize=(4,4),dpi=100)
    nm_W_graph = Figure(figsize=(4,4),dpi=100)
    em_force_as_function = uN_mA_graph.add_subplot(111)
    em_force_variations = nm_uN_graph.add_subplot(111)
    displacement_from_power = nm_W_graph.add_subplot(111)
    em_force_as_function.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    em_force_variations.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    displacement_from_power.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    
    canvas1 = FigureCanvasTkAgg(uN_mA_graph,root)
    canvas2 = FigureCanvasTkAgg(nm_uN_graph,root)
    canvas3 = FigureCanvasTkAgg(nm_W_graph,root)
    canvas1.draw()
    canvas2.draw()
    canvas3.draw()
    canvas1.get_tk_widget().grid(row=6,column=0)
    canvas2.get_tk_widget().grid(row=6,column=1)
    canvas3.get_tk_widget().grid(row=6,column=2)
    
    graph1_btn = Button(text="Graph Settings")
    graph1_btn.grid(row=7,column=0)
    graph1_btn.bind("<Button>",lambda e: NewWindow(root))
    graph2_btn = Button(text="Graph Settings")
    graph2_btn.grid(row=7,column=1)
    graph2_btn.bind("<Button>",lambda e: NewWindow(root))
    graph3_btn = Button(text="Graph settings")
    graph3_btn.grid(row=7,column=2)
    graph3_btn.bind("<Button>",lambda e: NewWindow(root))
    
    root.mainloop()
