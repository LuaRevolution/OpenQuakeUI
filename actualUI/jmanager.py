#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 08, 2018 11:38:16 AM

import sys
import os
from tkinter import filedialog

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import jmanager_support


v = {
    #general
    1: {"description": ""},
    2: {"calculation_mode": ""},
    3: {"random_seed": ""},
    #geometry
    4: {"sites_csv": ""},
    #logic_tree
    5: {"number_of_logic_tree_samples": ""},
    #Erf
    6: {"rupture_mesh_spacing": ""},
    7: {"width_of_mfd_bin": ""},
    8: {"area_source_discretization": ""},
    #site_params
    9: {"reference_vs30_type": ""},
    10: {"reference_vs30_value": ""},
    11: {"reference_depth_to_2pt5km_per_sec": ""},
    12: {"reference_depth_to_1pt0km_per_sec": ""},
    #calculation
    13: {"source_model_logic_tree_file": ""},
    14: {"gsim_logic_tree_file": ""},
    15: {"investigation_time": ""},
    16: {"intensity_measure_types_and_levels": ""},
    17: {"truncation_level": ""},
    18: {"maximum_distance": ""},
    #output
    19: {"export_dir": ""},
    20: {"mean_hazard_curves": ""},
    21: {"quantile_hazard_curves": ""},
    22: {"hazard_maps": ""},
    23: {"uniform_hazard_spectra": ""},
    24: {"poes": ""}
}
atxtbox = {}

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Job_ini_Manager (root)
    jmanager_support.init(root, top)
    root.mainloop()

w = None
def create_Job_ini_Manager(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Job_ini_Manager (w)
    jmanager_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Job_ini_Manager():
    global w
    w.destroy()
    w = None

global specY
specY = 25
numMade = 0
class Job_ini_Manager:
    def __init__(self, top=None):
        sY = 25
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolorer = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolorer), ('active',_ana2color)])
        geoString = "670x625+770+312"
        top.geometry(geoString)
        top.title("Job.ini Manager")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        def send(t): #on click
            global v
            global atxtbox
            cmdString = "python ../job-handler.py "
            for x in range(0,len(v)):
                x=x+1
                curTab = v[x]
                for z in curTab:
                    curBox = atxtbox[z]
                    txt = curBox.get()
                    print("Val -> "+z+": "+txt)
                    if txt == "":

                        cmdString = cmdString+'-'+z+' " " '
                    else:
                        cmdString = cmdString+'-'+z+' "'+txt+'" '
            cmdString = cmdString+'-outputFile "'+filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("INI file","*.ini"), ("all files","*.*")))+'.ini" '
            print(cmdString)
            os.system(cmdString)

        self.Save = Button(top)
        self.Save.place(relx=0.0, rely=0.0, height=25, relwidth=1)
        self.Save.configure(activebackground="#0ba30d")
        self.Save.configure(activeforeground="white")
        self.Save.configure(activeforeground="#0ba30d")
        self.Save.configure(background="#0ba30d")
        self.Save.configure(disabledforeground="#a3a3a3")
        self.Save.configure(foreground="#000000")
        self.Save.configure(highlightbackground="#000000")
        self.Save.configure(highlightcolor="#000000")
        self.Save.configure(pady="0")
        self.Save.configure(relief=FLAT)
        self.Save.configure(text='''Save''')
        self.Save.configure(width=380)
        self.Save.bind("<Button-1>", send)
        ifPreset = 1
        global preset
        def createLBox(key,curt):
            global specY
            global numMade
            global atxtbox
            self.TLabel1 = ttk.Label(top)
            self.TLabel1.place(relx=0.0, y=specY, height=25, width=200)
            self.TLabel1.configure(background="#d9d9d9")
            self.TLabel1.configure(foreground="#000000")
            self.TLabel1.configure(font="TkDefaultFont")
            self.TLabel1.configure(relief=FLAT)
            self.TLabel1.configure(text=key)
            self.TLabel1.configure(wraplength="200")

            self.TEntry1 = ttk.Entry(top)
            self.TEntry1.place(relx=0.4, y=specY, height=25, relwidth=0.6)
            self.TEntry1.configure(takefocus="")
            self.TEntry1.configure(width=405)
            self.TEntry1.configure(cursor="ibeam")
            self.TEntry1.configure(textvariable=curt[key])
            atxtbox[key] = self.TEntry1
            numMade = numMade + 1
            specY = specY + 25
        for z in range(0,len(v)):
            z = z+1
            curTab = v[z]
            for key in curTab:
                createLBox(key,curTab)





if __name__ == '__main__':
    vp_start_gui()