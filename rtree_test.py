#!/usr/bin/env python
from rtree import index

def insert_point_into_tree(x, y, ltree, id):
	left, bottom, right, top = (x, y, x, y)
	ltree.insert(id, (left, bottom, right, top))
	return ltree

## points from line 1: (1, 2.5), (1, 2), (2, 3), (5, 1), (5.5, 2.5)
## points from line 2: (0, 2), (5, 0.5)
## points from line 1 inside rectangle: (1, 2), (2, 3), (5, 1)
## points from line 2 inside rectangle: None
def test_case_1():
	ltree = index.Index()

	## points from line 1
	ltree = insert_point_into_tree(-1, 2.5, ltree, 0)
	ltree = insert_point_into_tree(1, 2, ltree, 1)
	ltree = insert_point_into_tree(2, 3, ltree, 2)
	ltree = insert_point_into_tree(5, 1, ltree, 3)
	ltree = insert_point_into_tree(5.5, 2.5, ltree, 4)

	## points from line 2
	ltree = insert_point_into_tree(0, 2, ltree, 5)
	ltree = insert_point_into_tree(5, 0.5, ltree, 6)

	## rectangle query
	## (0.9, 0-9) - (5.1, 3.1)
	query_result = list(ltree.intersection((0.9, 0.9, 5.1, 3.1)))
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
	ltree = index.Index()

	## points from line 1
	ltree = insert_point_into_tree(0, 2, ltree, 0)
	ltree = insert_point_into_tree(2, 3, ltree, 1)
	ltree = insert_point_into_tree(4, 1, ltree, 2)
	ltree = insert_point_into_tree(5.5, 2.5, ltree, 3)

	## points from line 2
	ltree = insert_point_into_tree(1.5, 3.5, ltree, 4)
	ltree = insert_point_into_tree(5.2, 2.8, ltree, 5)

	## rectangle query
	query_result = list(ltree.intersection((1.9, 0.9, 5.6, 3.1)))
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
	ltree = index.Index()

	## points from line 1
	ltree = insert_point_into_tree(0, 2, ltree, 0)
	ltree = insert_point_into_tree(2, 3, ltree, 1)
	ltree = insert_point_into_tree(4, 1, ltree, 2)
	ltree = insert_point_into_tree(5.5, 2.5, ltree, 3)

	## points from line 2
	ltree = insert_point_into_tree(1.5, 3.5, ltree, 4)
	ltree = insert_point_into_tree(4.0, 2.5, ltree, 5)

	## rectangle query
	query_result = list(ltree.intersection((1.9, 0.9, 5.6, 3.1)))
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


