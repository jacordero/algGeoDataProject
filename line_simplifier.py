#!/usr/bin/env python

import gml_utils
import simple_rtree
import math
import random

DELTA = 0.01

def construct_polygonal_tree(polygonal_lines):
	tree = simple_rtree.SimpleRTree()
	id_counter = 0
	dict_lines_ids = {}
	for line_key, line_val in polygonal_lines.items():
		line_ids = []
		for point in line_val:
			tree.insert(point[0], point[1], id_counter)
			line_ids.append(id_counter)
			id_counter += 1
		dict_lines_ids[line_key] = line_ids

	return (tree, dict_lines_ids)

def construct_control_tree(control_points):
	tree = simple_rtree.SimpleRTree()
	id_counter = 0
	for point in control_points:
		tree.insert(point[0], point[1], id_counter)
		id_counter += 1

	return tree

def points_to_remove_per_line(polygonal_lines, points_to_remove):
	points_per_line = []
	remove_per_line = {}
	total_points = 0
	
	for line_key, line_val in polygonal_lines.items():
		points_per_line.append(len(line_val))
		total_points += len(line_val)


	if points_to_remove > total_points:
		print("Points to remove > total points in line")
		raise

	assigned = 0
	for i, n in enumerate(points_per_line):
		to_remove = (n*1.0 / total_points)*points_to_remove
		to_remove = math.floor(to_remove)
		remove_per_line[i] = to_remove
		assigned += to_remove

	not_assigned = points_to_remove - assigned
	for i in range(not_assigned):
		idx = i % len(remove_per_line)
		remove_per_line[idx] = remove_per_line[idx] + 1

	#print(points_to_remove)
	#print(not_assigned)
	return remove_per_line

def simplification_info(polygonal_lines, points_to_remove, remove_per_line):
	total_points = 0
	for line_key in polygonal_lines:
		total_points += len(polygonal_lines[line_key])

	for line_key in polygonal_lines:
		print("Pl: {}, ptr: {}, ttp: {}, ttr: {}"
			.format(len(polygonal_lines[line_key]), remove_per_line[line_key],
						total_points, points_to_remove))

def compute_segments(polygonal_line, points_to_remove):
	edges = len(polygonal_line) - 1
	segments = []
	
	## create triples or segments of size greather or equal to three points
	if points_to_remove > edges / 2:
		start_point = 0
		end_point = 0
		for i in range(edges // 2):
			end_point = start_point + 2
			segments.append((start_point, end_point))
			start_point = end_point
	else:
		base_length = math.floor(1.0*edges / points_to_remove)
		residual = edges - (base_length * points_to_remove)
		start_point = 0
		end_point = 0
	
		for i in range(points_to_remove):
			end_point = start_point + base_length
			if residual > 0:
				end_point += 1
				residual -= 1

			segments.append((start_point, end_point))
			start_point = end_point

	return segments

def compute_triple(start_point, end_point, randomize):
	if randomize:
		middle_point = random.randint(start_point + 1, end_point -1)
		return (middle_point - 1, middle_point, middle_point + 1)

	return (start_point, start_point + 1, start_point + 2)

def compute_rectangle(current_line, triple):
	p0 = current_line[triple[0]]
	p1 = current_line[triple[1]]
	p2 = current_line[triple[2]]

	min_x = p0[0]
	max_x = p0[0]
	max_y = p0[1]
	min_y = p0[1]

	if p1[0] < min_x:
		min_x = p1[0]
	if p2[0] < min_x:
		min_x = p2[0]
	if p1[0] > max_x:
		max_x = p1[0]
	if p2[0] > max_x:
		max_x = p2[0]

	if p1[1] < min_y:
		min_y = p1[1]
	if p2[1] < min_y:
		min_y = p2[1]
	if p1[1] > max_y:
		max_y = p1[1]
	if p2[1] > max_y:
		max_y = p2[1]

	return (min_x - DELTA, min_y - DELTA, max_x + DELTA, max_y + DELTA)

def simplify(polygonal_lines, control_points, total_npoints_to_remove):

	polygonal_tree, dict_lines_ids = construct_polygonal_tree(polygonal_lines)
	control_tree = construct_control_tree(control_points)
	
	to_remove_per_line = points_to_remove_per_line(polygonal_lines, total_npoints_to_remove)
	simplification_info(polygonal_lines, total_npoints_to_remove, to_remove_per_line)

	simplified_lines = {}

	for pl_key in polygonal_lines:
		npoints_to_remove = to_remove_per_line[pl_key]
		current_line = polygonal_lines[pl_key]
		current_line_ids = dict_lines_ids[pl_key]

		print("\n\n -----------------Simplifying new line-------------------\n\n")
		print("line index: {}".format(pl_key))
		print("number of points to remove: {}".format(npoints_to_remove))
		print("number of points in line: {}".format(len(current_line)))
		print("current_line:\n {}".format(current_line))

		#input("continue...")

		no_points_removed = False
		no_points_removed_count = 0

		while npoints_to_remove > 0 and no_points_removed_count < 10:

			segments = compute_segments(current_line, npoints_to_remove)
			removed = 0
			points_to_remove = []

			print("segments: {}".format(segments))
			#input("continue...")

			for segment in segments:
				triple_points = compute_triple(segment[0], segment[-1], no_points_removed)
				no_points_removed = False
				(x_left, y_bottom, x_right, y_top) = compute_rectangle(current_line, triple_points)
				points_inside_rectangle = polygonal_tree.count(x_left, y_bottom, x_right, y_top)
				cpoints_inside_rectangle = control_tree.count(x_left, y_bottom, x_right, y_top)

				print("----------------------------------------------------------------------")
				print("triple_points: p1 = {}, p2 = {}, p3 = {}".format(current_line[triple_points[0]], 
																current_line[triple_points[1]],
																current_line[triple_points[2]]))
				print("x_left = {}, y_bottom = {}, x_right = {}, y_top = {}".format(x_left,
				 																	y_bottom, 
				 																	x_right,
				  																	y_top))
				print("points_inside_rectangle: {}".format(points_inside_rectangle))
				print("control_points_inside_rectangle: {}".format(cpoints_inside_rectangle))
				print("----------------------------------------------------------------------\n")

				#input("continue...")

				if points_inside_rectangle == 3 and cpoints_inside_rectangle == 0:
					points_to_remove.append(triple_points[1])
					id_to_remove = current_line_ids[triple_points[1]]
					point_to_remove = current_line[triple_points[1]]
					polygonal_tree.delete(id_to_remove, point_to_remove)
					removed += 1
				elif points_inside_rectangle < 3:
					input("continue...")

			# remove points from current line

			if removed == 0:
				no_points_removed = True
				no_points_removed_count += 1

			#print("points to remove: {}".format(points_to_remove))
			print("removed: {}".format(removed))
			#input("continue...")

			aux_line = []
			aux_ids = []
			for i, val in enumerate(zip(current_line, current_line_ids)):
				if i not in points_to_remove:
					aux_line.append(val[0])
					aux_ids.append(val[1])

			current_line = list(aux_line)
			current_line_ids = list(aux_ids)
			npoints_to_remove -= removed
		
			#print("current line:\n{}".format(current_line))
			print("number of points to remove: {}".format(npoints_to_remove))

		simplified_lines[pl_key] = current_line

		if no_points_removed_count > 10:
			print("\n*********************************************")
			print("**** failed to remove more than 10 times ****")
			print("*********************************************\n")

	return simplified_lines

def compare_content_of_lines(original_lines, simplified_lines):
	assert len(original_lines) == len(simplified_lines)

	for idx in original_lines:
		original_line = original_lines[idx]
		simplified_line = simplified_lines[idx]
		print("Original length: {}, simplified length: {}".format(len(original_line), 
																	len(simplified_line)))

if __name__ == '__main__':

	LINES_DT1 = "./training_dataset1/lines_out.txt"
	SIMPLIFIED_LINES_DT1 = "./training_dataset1/alg1_simple_lines_sf.txt"
	CONTROL_POINTS_DT1 = "./training_dataset1/points_out.txt"

	polygonal_lines = gml_utils.gml_read_lines(LINES_DT1)
	control_points = gml_utils.gml_read_control_points(CONTROL_POINTS_DT1)

	points_to_remove = 700

	simplified_lines = simplify(polygonal_lines, control_points, points_to_remove)
	gml_utils.save_line_content(SIMPLIFIED_LINES_DT1, simplified_lines)

	compare_content_of_lines(polygonal_lines, simplified_lines)