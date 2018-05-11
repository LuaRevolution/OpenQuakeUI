import configparser
import sys
import json
import os

##########
# Setup
##########


parser = configparser.SafeConfigParser()
fileName = "job.ini"
outputFile = open(fileName, "w")



def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts
args = getopts(sys.argv)

#Create all lists
v = {} #Root list. V = value


#Create all the sections by hand...
parser.add_section("general") # General
parser.add_section("geometry") # Geometry
parser.add_section("logic_tree") # Logic_Tree
parser.add_section("erf") # Erf
parser.add_section("site_params") # Site_Params
parser.add_section("calculation") # Calculation
parser.add_section("output") #Output

def set(sect, name): #Function for pure laziness
    parser.set(sect, name, v[name])
    print(sect+" : "+name+" -> "+v[name])

##########
# Turning parameters into the v list
##########

#General
v["description"] = args['-description']
v["calculation_mode"] = args['-calculation_mode']
v["random_seed"] = args['-random_seed']

#Geometry
v["sites_csv"] = args['-sites_csv']

#Logic_Tree
v["number_of_logic_tree_samples"] = args['-number_of_logic_tree_samples']

#erf
v["rupture_mesh_spacing"] = args['-rupture_mesh_spacing']
v["width_of_mfd_bin"] = args['-width_of_mfd_bin']
v["area_source_discretization"] = args['-area_source_discretization']

#site_params
v["reference_vs30_type"] = args['-reference_vs30_type']
v["reference_vs30_value"] = args['-reference_vs30_value']
v["reference_depth_to_2pt5km_per_sec"] = args['-reference_depth_to_2pt5km_per_sec']
v["reference_depth_to_1pt0km_per_sec"] = args['-reference_depth_to_1pt0km_per_sec']

#calculation
v["source_model_logic_tree_file"] = args['-source_model_logic_tree_file']
v["gsim_logic_tree_file"] = args['-gsim_logic_tree_file']
v["investigation_time"] = args['-investigation_time']
v["intensity_measure_types_and_levels"] = args['-intensity_measure_types_and_levels']
v["truncation_level"] = args['-truncation_level']
v["maximum_distance"] = args['-maximum_distance']

#output
v["export_dir"] = args['-export_dir']
v["mean_hazard_curves"] = args['-mean_hazard_curves']
v["quantile_hazard_curves"] = args['-quantile_hazard_curves']
v["hazard_maps"] = args['-hazard_maps']
v["uniform_hazard_spectra"] = args['-uniform_hazard_spectra']
v["poes"] = args['-poes']

##########
# Turning v into .ini format
##########

#general
set("general", "description")
set("general", "calculation_mode")
set("general", "random_seed")
#Geometry
set("geometry", "sites_csv")
#Logic_Tree
set("logic_tree", "number_of_logic_tree_samples")
#erf
set("erf", "rupture_mesh_spacing")
set("erf", "width_of_mfd_bin")
set("erf", "area_source_discretization")
#site_params
set("site_params", "reference_vs30_type")
set("site_params", "reference_vs30_value")
set("site_params", "reference_depth_to_2pt5km_per_sec")
set("site_params", "reference_depth_to_1pt0km_per_sec")
#calculation
set("calculation", "source_model_logic_tree_file")
set("calculation", "gsim_logic_tree_file")
set("calculation", "investigation_time")
set("calculation", "intensity_measure_types_and_levels")
set("calculation", "truncation_level")
set("calculation", "maximum_distance")
#output
set("output", "export_dir")
set("output", "mean_hazard_curves")
set("output", "quantile_hazard_curves")
set("output", "hazard_maps")
set("output", "uniform_hazard_spectra")
set("output", "poes")
set("output", "mean_hazard_curves")

##########
# Output and write
##########
print("Writing to "+fileName+"...")
writeTo = open(args["-outputFile"],"w")
parser.write(writeTo)
os.system("cls")
print("############### COMPLETED ###############")
print("############### COMPLETED ###############")
print("############### COMPLETED ###############\n")
