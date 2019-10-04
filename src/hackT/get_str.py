def get_str(s):
	even, odd = '',''

	for i, c in enumerate(s):
		if i == 0:
			even += c
		elif i%2 == 0:
			even += c
		else:
			odd += c
			
	return even + ' ' + odd


#if __name__ == '__main__':
t = 'Hacker'

#for i in range(0, t):
#    s = input()

#print(get_str(t))

