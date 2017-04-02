#!/usr/bin/env python

import line_simplifier
import sys
import math
import gml_utils
import time

def compute_points_to_remove(polygonal_lines, percentage_reduction):
	total_points = 0
	for key_line in polygonal_lines:
		polygonal_line = polygonal_lines[key_line]
		total_points += len(polygonal_line)

	return math.floor(total_points*(percentage_reduction/100.0))


def simplify_map(polygonal_lines, control_points, points_to_remove):
	simplified_lines = line_simplifier.simplify(
		polygonal_lines, control_points, points_to_remove
		)
	return simplified_lines


def count_points(polygonal_lines):
	points = 0
	for line_key in polygonal_lines:
		line = polygonal_lines[line_key]
		points += len(line)
	return points

def multiple_simplifications(input_folder, output_folder):
	lines_filename = input_folder + "/lines_out.txt"
	control_points_filename = input_folder + "/points_out.txt"

	polygonal_lines = gml_utils.gml_read_lines(lines_filename)
	control_points = gml_utils.gml_read_control_points(control_points_filename)

	reductions = [10, 20, 30, 40, 50, 60, 70, 80, 90]
	base_filename = "lines_out_simple_"
	total_points = count_points(polygonal_lines)
	lines_info = []

	for reduction in reductions:
		points_to_remove = compute_points_to_remove(polygonal_lines, reduction)
		#print(points_to_remove)
		#start timing measurement
		simplified_lines = simplify_map(polygonal_lines, control_points, points_to_remove)
		# stop timing measurement
		output_filename = output_folder + "/" + base_filename + str(reduction) + ".txt"
		gml_utils.save_line_content(output_filename, simplified_lines)
		lines_info.append((total_points, points_to_remove, count_points(simplified_lines)))	
	
	for val in lines_info:
		print("Initial points: {}, to reduce: {}, final points: {}".format(val[0], val[1], val[2]))


def reduce_by_90percent(input_folder, output_folder):
	lines_filename = input_folder + "/lines_out.txt"
	control_points_filename = input_folder + "/points_out.txt"
	base_filename = "lines_out_simple_"
	
	polygonal_lines = gml_utils.gml_read_lines(lines_filename)
	control_points = gml_utils.gml_read_control_points(control_points_filename)

	reduction_percentage = 90
	points_to_remove = compute_points_to_remove(polygonal_lines, reduction_percentage)
	simplified_lines = simplify_map(polygonal_lines, control_points, points_to_remove)
	
	output_filename = output_folder + "/" + base_filename + str(reduction_percentage) + ".txt"
	gml_utils.save_line_content(output_filename, simplified_lines)
	
	print("Total: {}, to remove: {}, final: {}".format(count_points(polygonal_lines),
														points_to_remove,
														count_points(simplified_lines)))


if __name__ == '__main__':

	start_time = time.time()

	if (len(sys.argv)) != 3:
		print("Usage: python map_simplification.py input_folder output_folder")
		exit()

	input_folder = sys.argv[1]
	output_folder = sys.argv[2]
	#multiple_simplifications(input_folder, output_folder)
	reduce_by_90percent(input_folder, output_folder)

	end_time = time.time()
	diff = end_time - start_time
	print("Time: {}".format(diff))


		#tikz_template_filename = base_filename + str(reduction) + ".tex"
		#create_tikz_template(tikz_template_filename, polygonal_lines, control_points)

		#compare_content_of_lines(polygonal_lines, simplified_lines)