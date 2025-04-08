from typing import List

class Solution:
	# no readme file for this one, let's try to explain the code here itself with dry outputs
	def pascals_triangle(numRows: int) -> List[List[int]]:
		# Given an integer numRows, return the first numRows of Pascal's triangle.
		# Let's initialize a variable for our output which will be of type List[List[int]]
		triangles = []

		# Now here is a rough diagram of what it looks like
		"""
					1
				1		1
			1		2		1
		1		3		3		1
		"""
		# If we carefully notice, each number is the sum of two numbers above it.
		# For example, 2 = 1 + 1 and 3 = 1 + 2.
		# This gives us the formula: triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

		# Let's take row 3 as an example (i = 2, since index starts from 0)
		# The number 2 is at index 1 => triangle[2][1] = triangle[1][0] + triangle[1][1] = 1 + 1 = 2

		for i in range(numRows):
			row = [1] * (i + 1)  # All rows start and end with 1

			for j in range(1, i):  # Only update the inner elements
				row[j] = triangles[i-1][j-1] + triangles[i-1][j]

			triangles.append(row)

		return triangles
