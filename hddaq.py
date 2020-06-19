from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
#from tkinter import filedialog
from tkinter.filedialog import askopenfile
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
r0 = 5
r1 = 5
r2 = 5
r3 = 5
r4 = 8


def start_test_warning():
    messagebox.showwarning("WARNING","You are about to start a test cycle. Before continuing please make sure the following items are completed: \n1. Safety glasses\n2.Something\n3.Something")
            
def onError():
    messagebox.showerror("Error","Could not open file")
        
def onWarning():
    messagebox.showwarning("Warning", "Deprecatred function call")
        
def onQuestion(self):
    messagebox.askquestion("Question","Are you sure you want to quit?")
        
def onInfo():
    messagebox.showinfo("Information","Download completed")
    
def onCancel():
    messagebox.askokcancel("Cancel", "Ok")
    
def onYesNo():
    messagebox.askyesno("Yes","No")
    
def onRetryCancel():
    messagebox.askretrycancel("Retry","Cancel")
        
def onOpen():
    ftypes = askopenfile(mode='r', filetypes=[('Python files', '*.py'),('All files','*')])
    if ftypes is not None:
        content = ftypes.read()
        print(content)
        
        
def readFile(self,filename):
    with open(filename,"r") as f:
        text = f.read()
    return text
        
class NoiseWindow(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("External Noise Input Menu")
        self.geometry("400x400")
        Label(self, text ="Check any factor that may have contributed to noise:").grid(row=0)
        chkbtn1 = ttk.Checkbutton(self, text = "No external noise").grid(row=1)
        chkbtn2 = ttk.Checkbutton(self, text = "Air Currents (Atmospheric Test)").grid(row=2)
        chkbtn3 = ttk.Checkbutton(self, text = "RF Interaction with the Surrounding Environment").grid(row=3)
        chkbtn4 = ttk.Checkbutton(self, text = "Magnetic Interaction").grid(row=4)
        chkbtn5 = ttk.Checkbutton(self, text = "Thermal Expansion and Contraction").grid(row=5)
        chkbtn6 = ttk.Checkbutton(self, text = "Vibration").grid(row=6)
        chkbtn7 = ttk.Checkbutton(self, text = "Electrostatic Interaction").grid(row=7)
        chkbtn8 = ttk.Checkbutton(self, text = "Outgassing").grid(row=8)
        chkbtn9 = ttk.Checkbutton(self, text = "Photon Rocket Force").grid(row=9)
        chkbtn10 = ttk.Checkbutton(self, text = "Impulsive/Thermal Signal Decoupling Error").grid(row=10)
 
#class file_opener(Toplevel):
#    def __init__(self,master=None):
#        super().__init__(master=master)
#
#        self.init_file_opener()
#
#    def init_file_opener(self):
#        self.title("Open File")
#
class colorpicker(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.initiate_color_settings()
        
    def initiate_color_settings(self):
        self.title("Color chooser")
        self.btn = Button(self, text='Choose Color', command=self.onChoose)
        self.btn.grid(row=0)
        self.frame = Frame(self, border=1, relief=SUNKEN,width=100,height=100)
        self.frame.grid(row=0,column=1)
        
    def onChoose(self):
        (rgb,hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)
        
class NewWindow(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        
    def graph_settings(self):
        self.title("Graph settings")
        self.geometry("300x300")
        graph_settings_tab = ttk.Notebook(self)
        
        general_settings = ttk.Frame(graph_settings_tab)
        filters = ttk.Frame(graph_settings_tab)

        graph_settings_tab.add(general_settings, text="General Settings")
        graph_settings_tab.add(filters, text= "Filters")
        graph_settings_tab.grid(row=0)
        
    def daq_settings(self):
        self.title("Program Settings")
        self.geometry("400x400")
        daq_settings_tab = ttk.Notebook(self)
        
        general_settings = ttk.Frame(daq_settings_tab)
        device_info = ttk.Frame(daq_settings_tab)
        
        daq_settings_tab.add(device_info, text="Device Info")
        daq_settings_tab.add(general_settings, text="Settings")
        
class menubar(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.master.title("Horizon Drive DAQ GUI")
        menu = Menu(self.master)
        toolbar = Frame(self.master,bd=1,relief=RAISED)
        
        self.master.config(menu=menu)
        
        # Adding File Menu and commands
        file = Menu(menu, tearoff = 0)
        menu.add_cascade(label="File",menu=file)
        file.add_command(label="New File",command=None)
        file.add_command(label="Open...",command=onOpen)
        file.add_command(label="Save",command=None)
        file.add_separator()
        file.add_command(label="Exit",command=None)
        
        status_menu = Menu(file)
        status_menu.add_command(label="MCC 118",command=None)
        status_menu.add_command(label='MCC 152', command=None)
        status_menu.add_command(label='MCC 134', command=None)
        file.add_cascade(label='Get Shield Info',menu=status_menu)
        
        save_as_menu = Menu(file)
        save_as_menu.add_command(label='.csv',command=None)
        save_as_menu.add_command(label='python pickle',command=None)
        save_as_menu.add_command(label='.xslx',command=None)
        file.add_cascade(label='Save as...',menu=save_as_menu)
        
        # Adding Edit Menu and commands
        edit = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='Edit', menu = edit)
        edit.add_command(label ='Cut', command = None)
        edit.add_command(label ='Copy', command = None)
        edit.add_command(label ='Paste', command = None)
        edit.add_command(label ='Select All', command = None)
        edit.add_separator()
        edit.add_command(label ='Find...', command = None)
        edit.add_command(label ='Find again', command = None)
        
        # Adding View Menu and commands
        view = Menu(menu, tearoff = 0)
        menu.add_cascade(label = 'View',menu=view)
        view.add_command(label='Show Toolbar', command=None)
        view.add_command(label='Show Module', command=None)
        view.add_command(label='Change Color',command=colorpicker)
        
          
        # Adding Help Menu
        help_ = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='Help', menu = help_)
        help_.add_command(label ='Tk Help', command = None)
        help_.add_command(label ='Demo', command = None)
        
        # Adding toolbar
        error_btn = Button(toolbar, text ="error", relief=RAISED,bitmap="error").grid(row=0,column=0)
        hourglass_btn = Button(toolbar, text ="hourglass", relief=RAISED,bitmap="hourglass").grid(row=0,column=1)
        info_btn = Button(toolbar, text ="info", relief=RAISED,bitmap="info",command=onInfo).grid(row=0,column=2)
        question_btn = Button(toolbar, text ="question", relief=RAISED,bitmap="question").grid(row=0,column=3)
        warning_btn = Button(toolbar, text ="warning", relief=RAISED,bitmap="warning").grid(row=0,column=4)
        questhead_btn = Button(toolbar, text ="questhead", relief=RAISED,bitmap="questhead").grid(row=0,column=5)
        gray1_btn = Button(toolbar, text ="gray12", relief=RAISED,bitmap="gray12").grid(row=0,column=6)
        gray2_btn = Button(toolbar, text ="gray25", relief=RAISED,bitmap="gray25").grid(row=0,column=7)
        gray3_btn = Button(toolbar, text ="gray50", relief=RAISED,bitmap="gray50").grid(row=0,column=8)
        gray4_btn = Button(toolbar, text ="gray75", relief=RAISED,bitmap="gray75").grid(row=0,column=9)
        
        toolbar.grid(row=1,column=0,sticky=W)

    
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()
    
def status_update():
    info_tuple = mcc118.info() # Return information about the shield as a named tuple
    

# driver code
if __name__ == "__main__":
    root = Tk() # Create a new GUI window
    root.title('Horizon Drive DAQ GUI')
    root.configure(background = 'light blue') # Set the background color of GUI window
    root.geometry("1237x880") # Set the configuration of GUI window
    
    app = menubar()
    
    headlabel = Label(root,text="Horizon Drive",fg='black',font=('futura',24,'italic'))
    tabControl = ttk.Notebook(root)
    
    test_run_buttons = PanedWindow(orient='vertical')
    test_run_buttons.grid(row=2,column=2,sticky=W+E+N+S)
    test_start_button = Button(root,text="START",bg="green",fg="black")
    test_start_button.bind("<Button>", lambda e: start_test_warning())
    test_pause_button = Button(root,text="STOP TEST",bg="red",fg="black")
    camera_feed_button = Button(root,text="VIEW CAMERA FEED")
    graph_btn = Button(root,text="FILTERS")
    graph_btn.bind("<Button>",lambda e: NewWindow(root).graph_settings())

    results_pane = Label(text="Results\n Q Factor:\n Thrust:\n Thrust/Power:\n",relief=RIDGE)
    active_sensor_pane = Label(text="Active Sensors:\nThermocouple\n Current Sensor\n Vacuum Pressure\n Magnetic Field\n Laser\n",relief=RIDGE)
    
    pw = PanedWindow(orient='horizontal')
    pw.grid(row=3,column=3)
    left = Label(text="Set test cycle length:")
    pw.add(left)
    cycle_length = Spinbox(from_=0,to=5)
    pw.add(cycle_length)
    
    test_run_buttons.add(active_sensor_pane)
    test_run_buttons.add(pw)
    test_run_buttons.add(test_start_button)
    test_run_buttons.add(test_pause_button)
    test_run_buttons.add(graph_btn)
    test_run_buttons.add(camera_feed_button)
    
    
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab1,text="MCC 118 ANALOG VOLTAGE INPUT")
    tabControl.add(tab2,text="MCC 134 THERMOCOUPLE INPUT")
    tabControl.add(tab3,text="MCC 152 ANALOG OUTPUT / DIGITAL I/O")

    for channels in analog_voltage_input:
        #ttk.Label(tab1,text=channels,relief=RIDGE).grid(row=r1,column=0,sticky=W+E+N+S)
        ttk.Label(tab1,text=channels,).grid(row=r1,column=1,sticky=W+E+N+S)
        avi_btn = ttk.Button(tab1,text=channels,)
        avi_btn.grid(row=r1,column=2,sticky=W+E+N+S)
        avi_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Entry(tab1,text=channels).grid(row=r1,column=3,sticky=W+E+N+S)
        r1+=1
    Button(tab1,text="Get Shield Info").grid(row=4,column=0)
    
    for channels in thermocouple_input:
        ttk.Label(tab2,text=channels,relief=RIDGE).grid(row=r2,column=0)
        ttk.Label(tab2,text=channels).grid(row=r2,column=1)
        thermo_btn = ttk.Button(tab2,text=channels)
        thermo_btn.grid(row=r2,column=2)
        thermo_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab2,text=channels).grid(row=r2,column=3)
        r2+=1
    Button(tab2,text="Get Shield Info").grid(row=4,column=0)
        
    for channels in analog_output:
        ttk.Label(tab3,text=channels,relief=RIDGE).grid(row=r3,column=0)
        ttk.Label(tab3,text=channels).grid(row=r3,column=1)
        ttk.Entry(tab3,text=channels).grid(row=r3,column=2)
        ao_btn = ttk.Button(tab3,text=channels)
        ao_btn.grid(row=r3,column=3)
        ao_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab3,text=channels).grid(row=r3,column=4)
        r3+=1
    
        
    for channels in digital_i_o:
        ttk.Label(tab3,text=channels,relief=RIDGE).grid(row=r4,column=0)
        ttk.Label(tab3,text=channels).grid(row=r4,column=1)
        dio_btn = ttk.Button(tab3,text=channels)
        dio_btn.grid(row=r4,column=2)
        dio_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab3,text=channels).grid(row=r4,column=3)
        r4+=1
    Button(tab3,text="Get Shield Info").grid(row=4,column=0)
        


    noise_btn = Button(text="External Disturbance Input\n\n (Click after a test cycle is conducted if needed.)")
    noise_btn.bind("<Button>",lambda e: NoiseWindow(root))
    test_run_buttons.add(noise_btn)
    test_run_buttons.add(results_pane)
    
    # grid method is used for placing widgets at their respective positions
    headlabel.grid(row=0,column=0,sticky=W+E+N+S,columnspan=3)
    tabControl.grid(row=2,column=0,columnspan=2,sticky=W+E+N+S)

    uN_mA_graph = Figure(figsize=(4,4),dpi=100)
    nm_uN_graph = Figure(figsize=(4,4),dpi=100)
    nm_W_graph = Figure(figsize=(4,4),dpi=100)
    em_force_as_function = uN_mA_graph.add_subplot(111,xlabel="Current (mA)",ylabel="Force (µN)")
    em_force_variations = nm_uN_graph.add_subplot(111,xlabel="Force (µN)",ylabel="Displacement (nm)")
    displacement_from_power = nm_W_graph.add_subplot(111,xlabel="Power (W)",ylabel="Displacement (nm)")
    em_force_as_function.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    em_force_variations.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    displacement_from_power.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    uN_mA_graph.suptitle("Force Produced from Current")
    #uN_mA_graph.xlabel("Current (mA)")
    #uN_mA_graph.ylabel("Force (µN)")
    nm_uN_graph.suptitle("Displacement with Varied Magnet Distances")
    #nm_uN_graph.xlabel("Force (µN)")
    #nm_uN_graph.ylabel("Displacement (nm)")
    nm_W_graph.suptitle("Displacement from Power")
    #nm_W_graph.xlabel("Power (W)")
    #nm_W_graph.ylabel("Displacement (nm)")
    
    canvas1 = FigureCanvasTkAgg(uN_mA_graph,root)
    canvas2 = FigureCanvasTkAgg(nm_uN_graph,root)
    canvas3 = FigureCanvasTkAgg(nm_W_graph,root)
    canvas1.draw()
    canvas2.draw()
    canvas3.draw()
    canvas1.get_tk_widget().grid(row=3,column=1,sticky=W+E+N+S)
    canvas2.get_tk_widget().grid(row=3,column=0,sticky=W+E+N+S)
    canvas3.get_tk_widget().grid(row=3,column=2,sticky=W+E+N+S)

    
    root.mainloop()
