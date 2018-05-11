title Run Parse
:loop
python job-handler.py -description "EASTERN ARCTIC 2015 NBCC Hazard - COLLAPSED RATES" -calculation_mode classical -random_seed 23 -sites_csv "../../shared/Project_site.csv" -number_of_logic_tree_samples 0 -rupture_mesh_spacing "5.0" -width_of_mfd_bin "0.1" -area_source_discretization "10.0" -reference_vs30_type "measured" -reference_vs30_value "450.0" -reference_depth_to_2pt5km_per_sec "5.0" -reference_depth_to_1pt0km_per_sec "100.0" -source_model_logic_tree_file "EasternArctic_source_model_logic_tree.xml" -gsim_logic_tree_file "../../shared/hdf_gmpe_logic_tree.xml" -investigation_time "50.0" -intensity_measure_types_and_levels "{'PGA': [0.001, 0.003, 0.005, 0.007, 0.0098, 0.0137, 0.0192, 0.0269, 0.0376, 0.0527, 0.0738, 0.103, 0.145, 0.203, 0.284, 0.397, 0.556, 0.778, 1.09, 1.52, 2.13], "SA(0.1)": [0.001, 0.003, 0.005, 0.007, 0.0098, 0.0137, 0.0192, 0.0269, 0.0376, 0.0527, 0.0738, 0.103, 0.145, 0.203, 0.284, 0.397, 0.556, 0.778, 1.09, 1.52, 2.13, 2.50], "SA(0.2)": [0.001, 0.003, 0.005, 0.007, 0.0098, 0.0137, 0.0192, 0.0269, 0.0376, 0.0527, 0.0738, 0.103, 0.145, 0.203, 0.284, 0.397, 0.556, 0.778, 1.09, 1.52, 2.13, 2.50], "SA(0.5)": [0.001, 0.003, 0.005, 0.007, 0.0098, 0.0137, 0.0192, 0.0269, 0.0376, 0.0527, 0.0738, 0.103, 0.145, 0.203, 0.284, 0.397, 0.556, 0.778, 1.09, 1.52, 2.13], "SA(1.0)": [0.003, 0.005, 0.007, 0.0098, 0.0137, 0.0192, 0.0269, 0.0376, 0.0527, 0.0738, 0.103, 0.145, 0.203, 0.284, 0.397, 0.556, 0.778, 1.09, 1.52, 2.13, 2.50], "SA(2.0)": [0.001, 0.003, 0.005, 0.007, 0.0098, 0.0137, 0.0192, 0.0269, 0.0376, 0.0527, 0.0738, 0.103, 0.145, 0.203, 0.284, 0.397, 0.556, 0.778, 1.09, 1.52, 2.13, 2.50]}" -truncation_level "5" -maximum_distance "400.0" -export_dir "/tmp" -mean_hazard_curves "true" -quantile_hazard_curves " " -hazard_maps "true" -uniform_hazard_spectra "true" -poes "0.1 0.05 0.02 0.0049875"
pause
cls
goto loop
