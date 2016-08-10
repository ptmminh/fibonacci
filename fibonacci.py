def fibonacci(n):
	'''input the number of terms for fibonacci sequence'''
	
	#two base cases
	if n == 1:
		return [n]
	elif n == 2:
		return [1,1]
	else:
		# recursively getting the previous sequence
		x = fibonacci(n-1)
		# the new element the sum of the last two elements
		x.append(sum(x[:-3:-1]))
		return x


def main():
	for i in range(1,11):
		print('Fibonacci sequence of length {}: {}'.format(i,fibonacci(i)))


if __name__ == '__main__':
	main()

