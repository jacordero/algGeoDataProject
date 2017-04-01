#!/usr/bin/env python
import re

CONTENT_REGEX = 'ts=\" \">(.*) </gml:coordinates>'

def gml_read_lines(filename):
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
					
			lines[line_id] = polygonal_line
			line_id += 1
	
	return lines

def save_line_content(filename, lines):
	output_file = open(filename, 'w')
	for key_line in lines:
		s = str(key_line) + ":<points>"
		for point in lines[key_line]:
			s += str(point[0]) + "," + str(point[1]) + " "
		s += "</points>\n"
		output_file.write(s)

	output_file.close()

def save_points_content(filename, points):
	output_file = open(filename, 'w')
	for idx, point in enumerate(points):
		s = str(idx) + ":<point>" + str(point[0]) + "," + str(point[1]) + "</point>\n"
		output_file.write(s)

	output_file.close()



def gml_read_control_points(filename):
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

	return control_points


if __name__ == '__main__':

	LINES_OUT = "./training_dataset1/lines_out.txt"
	CONTROL_POINTS = "./training_dataset1/points_out.txt"

	#gml_read_lines(LINES_OUT)
	gml_read_control_points(CONTROL_POINTS)