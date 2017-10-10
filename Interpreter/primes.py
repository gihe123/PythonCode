def is_prime(number):
	if number <=1:
		return False

	for element in range(2,number-1):
		if number%element==0:
			return False
	return True
def print_next_prime(number):
	index=number
	while True:
		index+=1
		if is_prime(index):
			print(index)