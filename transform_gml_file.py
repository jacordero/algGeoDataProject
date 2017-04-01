#!/usr/bin/python env
import gml_utils
import sys

def transform_lines(input_filename, output_filename):
		#gml_read_lines(LINES_OUT)
	lines = gml_utils.gml_read_lines(input_filename)
	gml_utils.save_line_content(output_filename, lines)

def transform_points(input_filename, output_filename):
	points = gml_utils.gml_read_control_points(input_filename)
	gml_utils.save_points_content(output_filename, points)

if __name__ == '__main__':
	if len(sys.argv) == 4:
		type = int(sys.argv[1])
		input_filename = sys.argv[2]
		output_filename = sys.argv[3]
		if type == 1:
			transform_lines(input_filename, output_filename)
		elif type == 2:
			transform_points(input_filename, output_filename)
		else:
			print("type must be 1 (for lines) or 2 (for points)")
	else:
		print("Usage: ./transform_gml_file.py type[1 for lines/2 for points] input_file, output_file")