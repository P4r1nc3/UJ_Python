def rotation_iteratively(L, left, right):
	tmp = 0
	while(right != left):
		tmp = L[left]
		L[left] = L[right]
		L[right] = tmp
		right = right - 1
		left = left +1
	return L

def rotation_recursively(L, left , right):
	tmp = 0
	if left != right:
		tmp = L[left]
		L[left] = L[right]
		L[right] = tmp
		L = rotation_recursively(L, left+1, right-1)
	return L

if __name__ == "__main__":
	list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print("Before rotation: ")
	print(list)

	print("After rotation: ")
	print(rotation_iteratively(list, 0, 8))

	print("Before rotation: ")
	print(list)

	print("After rotation: ")
	print(rotation_recursively(list, 0, 8))