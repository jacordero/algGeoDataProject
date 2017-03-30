#!/usr/bin/env python
import re

CONTENT_REGEX = 'ts=\" \">(.*) </gml:coordinates>'

def read_input_lines(filename):
	input_file = open(filename, 'r')
	file_content = input_file.readlines()
	input_file.close()

	line_id = 0
	lines = {}

	for entry in file_content:
		match = re.search(CONTENT_REGEX, entry)
		if match:
			polygonal_line = []
			points = match.group(1).split(" ")
			for point in points:
				x, y = point.split(",")
				polygonal_line.append((float(x), float(y)))
			
			print(polygonal_line)
		
			lines[line_id] = polygonal_line
			line_id += 1
	
	return lines

def read_control_points(filename):
	input_file = open(filename, 'r')
	file_content = input_file.readlines()
	input_file.close()

	control_points = []
	for entry in file_content:
		match = re.search(CONTENT_REGEX, entry)
		if match:
			point = match.group(1).strip()
			x, y = point.split(",")
			control_points.append((float(x), float(y)))

	print(control_points)
	return control_points


if __name__ == '__main__':

	LINES_OUT = "./training_dataset1/lines_out.txt"
	CONTROL_POINTS = "./training_dataset1/points_out.txt"

	#read_input_lines(LINES_OUT)
	read_control_points(CONTROL_POINTS)