#!/usr/bin/python

import sys,getopt

#Job.ini Vars
jobVars = [
	#general
	["description1"] = "",
	["calculation_mode1"] = "",
	["random_seed1"] = "",
	#geometry
	["sites_csv1"] = "",
	#logic tree
	["number_of_logic_tree_samples1"] = "",
	#erf
	["rupture_mesh_spacing1"] = "",
	["width_of_mfd_bin1"] = "",
	["area_source_discretization1"] = "",
	#site params
	["reference_vs30_type1"] = "",
	["reference_vs30_value1"] = "",
	["reference_depth_to_2pt5km_per_sec1"] = "",
	["reference_depth_to_1pt0km_per_sec1"] = "",
	#calculation
	["source_model_logic_tree_file1"] = "",
	["gsim_logic_tree_file1"] = "",
	["investigation_time1"] = "",
	["intensity_measure_types_and_levels1"] = "",
	["truncation_level1"] = "",
	["maximum_distance1"] = "",
	#output
	["export_dir1"] = "",
	["mean_hazard_curves1"] = "",
	["quantile_hazard_curves1"] "",
	["hazard_maps1"] = "",
	["uniform_hazard_spectra1"] = "",
	["poes1"] = "",
	["mean_hazard_curves1"] = ""
]

def setVars(args):
	#set vars
	for x in args:


def parse(): #deprecated
	try:
		opts, args = getopt.getopt(sys.argv[1:], "", [""])
	except getopt.GetoptError:
		print("Parameter Error")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h"):
			print("asd")



setVars(sys.args[1:])
