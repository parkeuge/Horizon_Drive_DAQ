import time
import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')
from matplotlib import pyplot as plt

AVI_DEVICES = ('Device 1', 'Device 2', 'Device 3')
THERMAL_DEVICES = ('Device 1', 'Device 2', 'Device 3')
A_O_DEVICES = ('Device 1', 'Device 2', 'Device 3')
D_I_O_DEVICES = ('Device 1', 'Device 2', 'Device 3')
analog_voltage_input = [1,2,3,4,5,6,7,8]
thermocouple_input = [1,2,3,4]
analog_output = [1,2]
digital_i_o = [1,2,3,4,5,6,7,8]
results_chart = ["Q Factor","Thrust","Thrust/P"]
counter = 0

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Helvetica",10)
SMALL_FONT= ("Helvetica",8)

f = plt.figure(figsize=[5,4.15])
a = f.add_subplot(111)
f.suptitle("Displacement from Power")

#def run_single_scan():
    #if device 1
    #if device 2
    #if device 3 so forth...

# Function that opens existing files / data
def onOpen():
    ftypes = askopenfile(mode='r', filetypes=[('Python files', '*.py'),('All files','*')])
    if ftypes is not None:
        content = ftypes.read()
        print(content)

# Function that handles pop-up windows
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

# Function that handles opening up an existing file and reading it
def readFile(self,filename):
    with open(filename,"r") as f:
        text = f.read()
    return text
    
# Getting DAQ Device Info

# Get device info for Analog Input Shield
def get_118_info():
    stat_118 = tk.Toplevel()
    stat_118.title("MCC 118")
    #num_chan = '8'
    #num_chan = mcc118.a_in_scan_channel_count() # Read number of channels in current analog input scan
    #info_118 = mcc118.info()
    #firmware_version_118 = mcc118.firmware_version()
    #serial_118 = mcc118.serial()
    ttk.Label(stat_118,text="Number of active channels" + num_chan).grid(row=0,sticky='w'+'e')
    ttk.Label(stat_118,text="Shield Info:").grid(row=1,sticky='w'+'e')
    ttk.Label(stat_118,text="Firmware Version:").grid(row=2,sticky='w'+'e')
    ttk.Label(stat_118,text="Serial Number:").grid(row=3,sticky='w'+'e')

# Get device info for D/I/O / Analog output Shield
def get_152_info():
    stat_152 = tk.Toplevel()
    stat_152.title("MCC 152")
    #info_152 = mcc152.info()
    #firmware_virsion_152 = mcc152.firmware_version()
    #serial_152 = mcc152.serial()
    ttk.Label(stat_152,text="Number of active channels" + num_chan).grid(row=0,sticky='w'+'e')
    ttk.Label(stat_152,text="Shield Info:").grid(row=1,sticky='w'+'e')
    ttk.Label(stat_152,text="Firmware Version:").grid(row=2,sticky='w'+'e')
    ttk.Label(stat_152,text="Serial Number:").grid(row=3,sticky='w'+'e')

# Test length counter
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()

# Function that handles saving existing data to a specific file type
# Current file types we can save are .py, .txt, and .csv (we may want to add excel)
def save():
    files = [('All Files', '*.*'),('Python Files', '*.py'),('Text Document','*.txt'),('CSV Files','*.csv')]
    file = asksaveasfile(filetypes = files,defaultextension = files)
    
# Function that handles real-time animating / updating of graph
def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)
    a.set_xlabel("Power (W)")
    a.set_ylabel("Displacement (nm)")
    
# Menu to select source of noise
class NoiseWindow(tk.Toplevel):
    def __init__(self,parent=None):
        super().__init__()
        self.title("External Noise Input Menu")
        self.geometry("500x300")
        noise = tk.IntVar()
        air = tk.IntVar()
        radio = tk.IntVar()
        magnet = tk.IntVar()
        heat = tk.IntVar()
        vibration = tk.IntVar()
        esd = tk.IntVar()
        gas = tk.IntVar()
        photon = tk.IntVar()
        decoupling = tk.IntVar()
        tk.Label(self, text ="Check any factor that may have contributed to noise:").grid(row=0,sticky='w'+'e')
        chkbtn1 = tk.Checkbutton(self, text = "No external noise",variable = noise).grid(row=2,sticky='w')
        chkbtn2 = tk.Checkbutton(self, text = "Air Currents (Atmospheric Test)",variable = air).grid(row=3,sticky='w')
        chkbtn3 = tk.Checkbutton(self, text = "RF Interaction with the Surrounding Environment",variable = radio).grid(row=4,sticky='w')
        chkbtn4 = tk.Checkbutton(self, text = "Magnetic Interaction",variable = magnet).grid(row=5,sticky='w')
        chkbtn5 = tk.Checkbutton(self, text = "Thermal Expansion and Contraction",variable = heat).grid(row=6,sticky='w')
        chkbtn6 = tk.Checkbutton(self, text = "Vibration",variable = vibration).grid(row=7,sticky='w')
        chkbtn7 = tk.Checkbutton(self, text = "Electrostatic Interaction",variable = esd).grid(row=8,sticky='w')
        chkbtn8 = tk.Checkbutton(self, text = "Outgassing",variable = gas).grid(row=9,sticky='w')
        chkbtn9 = tk.Checkbutton(self, text = "Photon Rocket Force",variable = photon).grid(row=10,sticky='w')
        chkbtn10 = tk.Checkbutton(self, text = "Impulsive/Thermal Signal Decoupling Error",variable = decoupling).grid(row=11,sticky='w')
        confirm_button = ttk.Button(self,text = "Confirm")
        confirm_button.grid(row=14,column=1)
        confirm_button.bind("<Button>", lambda e: print(str(noise.get())+str(air.get())+str(radio.get())+str(magnet.get())+str(heat.get())+str(vibration.get())+str(esd.get())+str(gas.get())+str(photon.get())+str(decoupling.get())))
        cancel_button = ttk.Button(self,text = "Cancel")
        cancel_button.grid(row=14,column=0)
        cancel_button.bind("<Button>",lambda e: self.destroy())

# Class to select backgroud color
class colorpicker(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.initiate_color_settings()
        
    def initiate_color_settings(self):
        self.title("Color chooser")
        self.btn = ttk.Button(self, text='Choose Color', command=self.onChoose)
        self.btn.grid(row=0)
        self.frame = ttk.Frame(self, border=1, relief=SUNKEN,width=100,height=100)
        self.frame.grid(row=0,column=1)
        
    def onChoose(self):
        (rgb,hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)

# Class that displays graph settings and filters
class GraphWindow(tk.Toplevel):
    def __init__(self,parent=None):
        super().__init__()
        
        self.title("Graph settings") # Graph settings
        self.geometry("500x310")
        graph_settings_tab = ttk.Notebook(self)
        
        general_settings = ttk.Frame(graph_settings_tab)
        filters = ttk.Frame(graph_settings_tab)
        
        noise = tk.IntVar() # Graph filters
        air = tk.IntVar()
        radio = tk.IntVar()
        magnet = tk.IntVar()
        heat = tk.IntVar()
        vibration = tk.IntVar()
        esd = tk.IntVar()
        gas = tk.IntVar()
        photon = tk.IntVar()
        decoupling = tk.IntVar()

        graph_settings_tab.add(filters, text= "Graph Filters")
        graph_settings_tab.add(general_settings, text="Graph Settings")
        graph_settings_tab.grid(row=0)
        
        chkbtn1 = tk.Checkbutton(filters, text = "No external noise",variable = noise).grid(row=2,sticky='w')
        chkbtn2 = tk.Checkbutton(filters, text = "Air Currents (Atmospheric Test)",variable = air).grid(row=3,sticky='w')
        chkbtn3 = tk.Checkbutton(filters, text = "RF Interaction with the Surrounding Environment",variable = radio).grid(row=4,sticky='w')
        chkbtn4 = tk.Checkbutton(filters, text = "Magnetic Interaction",variable = magnet).grid(row=5,sticky='w')
        chkbtn5 = tk.Checkbutton(filters, text = "Thermal Expansion and Contraction",variable = heat).grid(row=6,sticky='w')
        chkbtn6 = tk.Checkbutton(filters, text = "Vibration",variable = vibration).grid(row=7,sticky='w')
        chkbtn7 = tk.Checkbutton(filters, text = "Electrostatic Interaction",variable = esd).grid(row=8,sticky='w')
        chkbtn8 = tk.Checkbutton(filters, text = "Outgassing",variable = gas).grid(row=9,sticky='w')
        chkbtn9 = tk.Checkbutton(filters, text = "Photon Rocket Force",variable = photon).grid(row=10,sticky='w')
        chkbtn10 = tk.Checkbutton(filters, text = "Impulsive/Thermal Signal Decoupling Error",variable = decoupling).grid(row=11,sticky='w')
        
        confirm_button = ttk.Button(self,text = "Confirm")
        confirm_button.grid(row=14,column=1)
        confirm_button.bind("<Button>", lambda e: print(str(noise.get())+str(air.get())+str(radio.get())+str(magnet.get())+str(heat.get())+str(vibration.get())+str(esd.get())+str(gas.get())+str(photon.get())+str(decoupling.get())))
        cancel_button = ttk.Button(self,text = "Cancel")
        cancel_button.grid(row=14,column=0)
        cancel_button.bind("<Button>",lambda e: self.destroy())
    
# Class that handles DAQ Shield settings
class DAQWindow(tk.Toplevel):
    def __init__(self,parent=None):
        super().__init__()
        
        self.title("Program Settings")
        self.geometry("400x400")
        daq_settings_tab = ttk.Notebook(self)
        
        general_settings = ttk.Frame(daq_settings_tab)
        device_info = ttk.Frame(daq_settings_tab)
        
        daq_settings_tab.add(device_info, text="Device Info")
        daq_settings_tab.add(general_settings, text="Settings")
 
# Class that handles camera window should we need to install one
class CameraWindow(tk.Toplevel):
    def __init__(self,parent=None):
        super().__init__()
        
        self.title("Camera")
        self.geometry("350x350")
 
# Main class of GUI that displays the respective subpages
class HorizonDriveDAQ(tk.Tk):
    def __init__(self,*args,**kwargs):
    
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self,"Horizon Drive DAQ")
        
        container = tk.Frame(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Creation of menu tabs
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0) # File menu tab
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="New File",command=None)
        filemenu.add_command(label="Open...",command=onOpen)
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        status_menu = tk.Menu(menubar,tearoff=1)
        status_menu.add_command(label="MCC 118",command=get_118_info) # Status menu tab
        status_menu.add_command(label='MCC 152', command=get_152_info)
        menubar.add_cascade(label='Get Shield Info',menu=status_menu)
        
        view = tk.Menu(menubar, tearoff = 1) # View menu tab
        menubar.add_cascade(label = 'View',menu=view)
        view.add_command(label='Show Toolbar', command=None)
        view.add_command(label='Show Module', command=None)
        view.add_command(label='Change Color',command=colorpicker)
        
        help_ = tk.Menu(menubar, tearoff = 1) # Help menu tab
        menubar.add_cascade(label ='Help', menu = help_)
        help_.add_command(label ='Tk Help', command = None)
        help_.add_command(label ='Demo', command = None)
        
        tk.Tk.config(self,menu=menubar)
        
        self.frames = {}
        
        for F in (StartPage,HomePage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    
# Class that displays GUI home message page
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=("""ALPHA GUI system use at your own risk."""), font=LARGE_FONT)
        label.pack()
        button = ttk.Button(self, text="Agree",command=lambda: controller.show_frame(HomePage))
        button.pack()
        button2 = ttk.Button(self, text="Disagree",command=quit)
        button2.pack()
 
# Class that displays GUI's main screen
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
  
        test_run_buttons = ttk.PanedWindow(self) # Creation of button pane
        test_start_button = ttk.Button(self,text="START") # Creation of test start button
        test_start_button.bind("<Button>", lambda e: HomePage.onCancel(progress))
        test_pause_button = ttk.Button(self,text="STOP TEST") # Creation of test pause button
        test_pause_button.bind("<Button>", lambda e: HomePage.stop_test(progress))
        camera_feed_button = ttk.Button(self,text="VIEW CAMERA FEED") # Creation of camera feed button
        camera_feed_button.bind("<Button>",lambda e: CameraWindow())
        graph_btn = ttk.Button(self,text="GRAPH FILTERS") # Creation of graph settings / filteres button
        graph_btn.bind("<Button>",lambda e: GraphWindow())
        noise_btn = ttk.Button(self,text="External Disturbance Input\n (Click after a test cycle is conducted if needed.)") # Creation of noise button
        noise_btn.bind("<Button>",lambda e: NoiseWindow())
        return_home_button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        
        test_cycle_length = ttk.PanedWindow(self,orient='horizontal') # Creation of pane that displays test cycle length
        cycle_label = ttk.Label(self,text="Test cycle length:")
        self.cycle_length = ttk.Spinbox(self,from_=1,to=5)
        self.cycle_length.bind("<Return>",self.grab)
        cycle_confirm = ttk.Button(self,text="Set")
        cycle_confirm.bind("<Button>",self.grab)
        test_cycle_length.add(cycle_label)
        test_cycle_length.add(self.cycle_length)
        test_cycle_length.add(cycle_confirm)
      
        results_pane = ttk.Label(self,text="\nRESULTS:\n Q Factor:\n Thrust:\n Thrust/Power:") # Window pane that shows sensor data
        active_sensor_pane = ttk.Label(self,text="\nACTIVE SENSORS:\n Thermocouple\n Current Sensor\n Vacuum Pressure\n Magnetic Field\n Laser") # Pane that shows active sensors
        
        test_progress_bar = ttk.PanedWindow(self,orient='horizontal') # Creation of test progres bar
        test_progress_label = ttk.Label(self,text="Test progress:")
        progress = ttk.Progressbar(self)
        progress.config(orient='horizontal',length='300',mode='determinate')
        test_progress_bar.add(test_progress_label)
        test_progress_bar.add(progress)
        
        test_run_buttons.add(active_sensor_pane)
        test_run_buttons.add(results_pane)
        test_run_buttons.add(test_progress_bar)
        test_run_buttons.add(test_cycle_length)
        test_run_buttons.add(test_start_button,weight=1)
        test_run_buttons.add(test_pause_button,weight=1)
        test_run_buttons.add(graph_btn,weight=1)
        test_run_buttons.add(camera_feed_button,weight=1)
        test_run_buttons.add(noise_btn,weight=1)
        test_run_buttons.add(return_home_button,weight=1)
        test_run_buttons.pack(side='right',fill='both')
        
        # Configuring channels on DAQ Shields
        tabControl = ttk.Notebook(self,padding=0.25)
        tab1 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab1,text="MCC 118 ANALOG VOLTAGE INPUT") # Tab for MC118
        tabControl.add(tab3,text="MCC 152 ANALOG OUTPUT / DIGITAL I/O") # Tab for MC152
        tabControl.pack(fill='both')
        
        ttk.Label(tab1,text="Channel Number").grid()
        ttk.Label(tab1,text="1.").grid(row=1,column=0)
        ttk.Label(tab1,text="2.").grid(row=2,column=0)
        ttk.Label(tab1,text="3.").grid(row=3,column=0)
        ttk.Label(tab1,text="4.").grid(row=4,column=0)
        ttk.Label(tab1,text="5.").grid(row=5,column=0)
        ttk.Label(tab1,text="6.").grid(row=6,column=0)
        ttk.Label(tab1,text="7.").grid(row=7,column=0)
        ttk.Label(tab1,text="8.").grid(row=8,column=0)
        ttk.Combobox(tab1,values=AVI_DEVICES).grid(row=1,column=1)
        ttk.Combobox(tab1,values=AVI_DEVICES).grid(row=2,column=1)
        ttk.Combobox(tab1,values=AVI_DEVICES).grid(row=3,column=1)
        ttk.Combobox(tab1,values=AVI_DEVICES).grid(row=4,column=1)
        ttk.Combobox(tab1,values=AVI_DEVICES).grid(row=5,column=1)
        ttk.Combobox(tab1,values=AVI_DEVICES).grid(row=6,column=1)
        ttk.Combobox(tab1,values=AVI_DEVICES).grid(row=7,column=1)
        ttk.Combobox(tab1,values=AVI_DEVICES).grid(row=8,column=1)
        ttk.Button(tab1,text="Run Scan",command=None).grid(row=1,column=2)
        ttk.Button(tab1,text="Run Scan",command=None).grid(row=2,column=2)
        ttk.Button(tab1,text="Run Scan",command=None).grid(row=3,column=2)
        ttk.Button(tab1,text="Run Scan",command=None).grid(row=4,column=2)
        ttk.Button(tab1,text="Run Scan",command=None).grid(row=5,column=2)
        ttk.Button(tab1,text="Run Scan",command=None).grid(row=6,column=2)
        ttk.Button(tab1,text="Run Scan",command=None).grid(row=7,column=2)
        ttk.Button(tab1,text="Run Scan",command=None).grid(row=8,column=2)
        ttk.Label(tab1,text="Result").grid(row=1,column=3)
        ttk.Label(tab1,text="Result").grid(row=2,column=3)
        ttk.Label(tab1,text="Result").grid(row=3,column=3)
        ttk.Label(tab1,text="Result").grid(row=4,column=3)
        ttk.Label(tab1,text="Result").grid(row=5,column=3)
        ttk.Label(tab1,text="Result").grid(row=6,column=3)
        ttk.Label(tab1,text="Result").grid(row=7,column=3)
        ttk.Label(tab1,text="Result").grid(row=8,column=3)
        avi_button = ttk.Button(tab1,text="Get Shield Info")
        avi_button.grid(row=9,column=0)
        avi_button.bind("<Button>",lambda e: get_118_info())
        
        ttk.Label(tab3,text="Channel Number").grid()
        ttk.Label(tab3,text="1.").grid(row=1,column=0)
        ttk.Label(tab3,text="2.").grid(row=2,column=0)
        ttk.Label(tab3,text="3.").grid(row=3,column=0)
        ttk.Label(tab3,text="4.").grid(row=4,column=0)
        ttk.Label(tab3,text="5.").grid(row=5,column=0)
        ttk.Label(tab3,text="6.").grid(row=6,column=0)
        ttk.Label(tab3,text="7.").grid(row=7,column=0)
        ttk.Label(tab3,text="8.").grid(row=8,column=0)
        ttk.Label(tab3,text="9.").grid(row=9,column=0)
        ttk.Label(tab3,text="10.").grid(row=10,column=0)
        ttk.Combobox(tab3,values=D_I_O_DEVICES).grid(row=1,column=1)
        ttk.Combobox(tab3,values=D_I_O_DEVICES).grid(row=2,column=1)
        ttk.Combobox(tab3,values=D_I_O_DEVICES).grid(row=3,column=1)
        ttk.Combobox(tab3,values=D_I_O_DEVICES).grid(row=4,column=1)
        ttk.Combobox(tab3,values=D_I_O_DEVICES).grid(row=5,column=1)
        ttk.Combobox(tab3,values=D_I_O_DEVICES).grid(row=6,column=1)
        ttk.Combobox(tab3,values=D_I_O_DEVICES).grid(row=7,column=1)
        ttk.Combobox(tab3,values=D_I_O_DEVICES).grid(row=8,column=1)
        ttk.Combobox(tab3,values=A_O_DEVICES).grid(row=9,column=1)
        ttk.Combobox(tab3,values=A_O_DEVICES).grid(row=10,column=1)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=1,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=2,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=3,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=4,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=5,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=6,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=7,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=8,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=9,column=2)
        ttk.Button(tab3,text="Run Scan",command=None).grid(row=10,column=2)
        ttk.Label(tab3,text="Result").grid(row=1,column=3)
        ttk.Label(tab3,text="Result").grid(row=2,column=3)
        ttk.Label(tab3,text="Result").grid(row=3,column=3)
        ttk.Label(tab3,text="Result").grid(row=4,column=3)
        ttk.Label(tab3,text="Result").grid(row=5,column=3)
        ttk.Label(tab3,text="Result").grid(row=6,column=3)
        ttk.Label(tab3,text="Result").grid(row=7,column=3)
        ttk.Label(tab3,text="Result").grid(row=8,column=3)
        ttk.Label(tab3,text="Result").grid(row=9,column=3)
        ttk.Label(tab3,text="Result").grid(row=10,column=3)
        dio_button = ttk.Button(tab3,text="Get Shield Info")
        dio_button.grid(row=11,column=0)
        dio_button.bind("<Button>",lambda e: get_152_info())
        
        canvas = FigureCanvasTkAgg(f, self) # Code that helps display graph on GUI
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self) # Code that helps display matplotlib toolbar butttons
        toolbar.update()
        canvas._tkcanvas.pack()
        
        '''
        GRAPHS REMAINING TO DISPLAY SHOULD WE NEED THEM
        
        canvas2 = FigureCanvasTkAgg(f, self)
        canvas2.draw()
        canvas2.get_tk_widget().pack()

        toolbar2 = NavigationToolbar2Tk(canvas2, self)
        toolbar2.update()
        canvas2._tkcanvas.pack()
        
        canvas3 = FigureCanvasTkAgg(f, self)
        canvas3.draw()
        canvas3.get_tk_widget().pack()

        toolbar3 = NavigationToolbar2Tk(canvas3, self)
        toolbar3.update()
        canvas3._tkcanvas.pack()
        
        em_force_as_function = uN_mA_graph.add_subplot(111,xlabel="Current (mA)",ylabel="Force (µN)")
        em_force_variations = nm_uN_graph.add_subplot(111,xlabel="Force (µN)",ylabel="Displacement (nm)")
        uN_mA_graph.suptitle("Force Produced from Current")
        nm_uN_graph.suptitle("Displacement with Varied Magnet Distances")
        
        '''
        
    def run_test(progress): # Function that begins the test cycle
        import time
        progress['maximum'] = 100
        for i in range (101):
            time.sleep(0.05)
            progress['value'] = i
            progress.update()

        messagebox.showinfo("Test Status", "Test Completed Successfully")
        progress['value'] = 0
            
    def stop_test(progress): # Function that pauses the current test cycle
        import time
        progress.stop()
     
    # Various warning / popup messages that may appear
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
        
    def onCancel(progress):
        ok = messagebox.askokcancel(message="You are about to start a test cycle. Before continuing please make sure the following items are completed: \n1. Safety glasses\n2.Something\n3.Something")
        if ok:
            HomePage.run_test(progress)
            
    def onYesNo():
        messagebox.askyesno("Yes","No")
        
    def onRetryCancel():
        messagebox.askretrycancel("Retry","Cancel")
        
    def listitems(self,event):
        print(event.widget)
    
    def grab(self,event):
        length_test = self.cycle_length.get()
        print(length_test)

# Main driver code
if __name__ == "__main__":
    app = HorizonDriveDAQ()
    app.geometry("1000x800")
    ani = animation.FuncAnimation(f,animate,interval=1000)
    app.mainloop()
