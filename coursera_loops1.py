1m-freelabs-561 - qwiklabs codedef counter(start, stop):
	x = start
	if start>stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string +=str(x)
			if x>stop:
				return_string+=","
			x=x-1
			
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x<stop:
				return_string+=","
			x=x+1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"