# Write a Python program to count the number of even and odd numbers from a series of numbers.

# list of numbers
list1 = [1, 34, 56, 23, 4, 7, 89, 78, 57, 98, 100, 43, 77, 33]

even_count = 0
odd_count = 0


for num in list1:

	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
