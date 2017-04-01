#!/usr/bin/env python

import simple_rtree

## points from line 1: (1, 2.5), (1, 2), (2, 3), (5, 1), (5.5, 2.5)
## points from line 2: (0, 2), (5, 0.5)
## points from line 1 inside rectangle: (1, 2), (2, 3), (5, 1)
## points from line 2 inside rectangle: None
def test_case_1():
	tree = simple_rtree.SimpleRTree()

	tree_id = 0

	## points from line 1
	tree.insert(-1, 2.5, tree_id)
	tree.insert(1, 2, tree_id)
	tree.insert(2, 3, tree_id)
	tree.insert(5, 1, tree_id)
	tree.insert(5.5, 2.5, tree_id)

	## points from line 2
	tree.insert(0, 2, tree_id)
	tree.insert(5, 0.5, tree_id)

	## rectangle query
	## (0.9, 0-9) - (5.1, 3.1)
	query_result = tree.count(0.9, 0.9, 5.1, 3.1)
	if (query_result > 3):
		print("A point from the triple can not be removed")
	else:
		print("A point from the triple can be removed")
	print(query_result)


## points from line 1: (0, 2), (2, 3), (4, 1), (5.5, 2)
## points from line 2: (1.5, 3.5), (5.2, 2.8)
## points from line 1 inside rectangle: (2, 3), (4, 1), (5.5, 2), 
## points from line 2 inside rectangle: (5.2, 2.8)
## rectangle: (1.9, 0.9), (5.6, 3.1)
def test_case_2():
	tree = simple_rtree.SimpleRTree()

	tree_id = 1

	## points from line 1
	tree.insert(0, 2, tree_id)
	tree.insert(2, 3, tree_id)
	tree.insert(4, 1, tree_id)
	tree.insert(5.5, 2.5, tree_id)

	## points from line 2
	tree.insert(1.5, 3.5, tree_id)
	tree.insert(5.2, 2.8, tree_id)

	## rectangle query
	query_result = tree.count(1.9, 0.9, 5.6, 3.1)
	if (query_result > 3):
		print("A point from the triple can not be removed")
	else:
		print("A point from the triple can be removed")
	print(query_result)

## points from line 1: (0, 2), (2, 3), (4, 1), (5.5, 2.5)
## points from line 2: (1.5, 3.5), (4.0, 2.5)
## points from line 1 inside rectangle: (2, 3), (4, 1), (5.5, 2), 
## points from line 2 inside rectangle: (4.0, 2.5)
## rectangle: (1.9, 0.9), (5.6, 3.1)
def test_case_3():
	tree = simple_rtree.SimpleRTree()

	tree_id = 2

	## points from line 1
	tree.insert(0, 2, tree_id)
	tree.insert(2, 3, tree_id)
	tree.insert(4, 1, tree_id)
	tree.insert(5.5, 2.5, tree_id)

	## points from line 2
	tree.insert(1.5, 3.5, tree_id)
	tree.insert(4.0, 2.5, tree_id)

	## rectangle query
	query_result = tree.count(1.9, 0.9, 5.6, 3.1)
	if (query_result > 3):
		print("A point from the triple can not be removed")
	else:
		print("A point from the triple can be removed")
	print(query_result)


def test_rectangle_count():
	tree = simple_rtree.SimpleRTree()

	p1 = (-7976513.843937492, 5357665.108234091)
	p2 = (-7976472.321767421, 5357241.582554582)
	p3 = (-7974834.812057852, 5357842.933691362)
	x_left = -7976513.853937492
	y_bottom = 5357241.572554582
	x_right = -7974834.802057852
	y_top = 5357842.943691362


	## points from line 1
	tree.insert(p1[0], p1[1], 0)
	tree.insert(p2[0], p2[1], 0)
	tree.insert(p3[0], p3[1], 0)

	## rectangle query
	## (0.9, 0-9) - (5.1, 3.1)
	query_result = tree.count(x_left, y_bottom, x_right, y_top)
	print("points inside rectangle: {}".format(query_result))


def test():
	#test_case_1()
	#test_case_2()
	#test_case_3()
	test_rectangle_count()

if __name__ == "__main__":
	test()


