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
	query_result = tree.rectangle_query(0.9, 0.9, 5.1, 3.1)
	if (len(query_result) > 3):
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
	query_result = tree.rectangle_query(1.9, 0.9, 5.6, 3.1)
	if (len(query_result) > 3):
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
	query_result = tree.rectangle_query(1.9, 0.9, 5.6, 3.1)
	if (len(query_result) > 3):
		print("A point from the triple can not be removed")
	else:
		print("A point from the triple can be removed")
	print(query_result)



def test():
	test_case_1()
	test_case_2()
	test_case_3()

if __name__ == "__main__":
	test()


