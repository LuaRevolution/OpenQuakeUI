#!/usr/bin/python

import sys,getopt

alphabet = ("first",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

#Job ini Vars
jobVars = []
txtOutput = """
	[general]

	description = 0asd2390
	calculation_mode = 1asd2390
	random_seed = 2asd2390

	[geometry]

	sites_csv = 3asd2390

	[logic_tree]

	number_of_logic_tree_samples = 4asd2390

	[erf]

	rupture_mesh_spacing = 5asd23
	width_of_mfd_bin = 6asd2390
	area_source_discretization = 7asd2390

	[site_params]

	reference_vs30_type = 8asd2390
	reference_vs30_value = 9asd2390
	reference_depth_to_2pt5km_per_sec = Jasd2390
	reference_depth_to_1pt0km_per_sec = Kasd2390

	[calculation]

	source_model_logic_tree_file = Lasd2390
	gsim_logic_tree_file = Masd2390
	investigation_time = Nasd2390
	intensity_measure_types_and_levels = Oasd2390
	truncation_level = Pasd2390
	maximum_distance = Qasd2390

	[output]

	export_dir = Rasd2390
	mean_hazard_curves = Sasd2390
	quantile_hazard_curves = Tasd2390
	hazard_maps = Uasd2390
	uniform_hazard_spectra = Vasd2390
	poes = Wasd2390
	mean_hazard_curves = Xasd2390
""" #24 total vars

def parse(): #deprecated
	try:
		opts, args = getopt.getopt(sys.argv[1:], "", [""])
	except getopt.GetoptError:
		print("Parameter Error")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h"):
			print("asd")

#Setting vars
for x in sys.argv[1:]:
	jobVars.append(x)
	#print("Parameter: "+str(x))

#Setting Text
loopCount = 0
for x in jobVars:
	if loopCount > 9:
		print()
		txtOutput = txtOutput.replace(alphabet[loopCount]+"asd2390",x)
	elsif:
		txtOutput = txtOutput.replace(str(loopCount)+"asd2390",x)
	#print("String set: "+x)
	loopCount = loopCount + 1
print(txtOutput)
