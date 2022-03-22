def hello():
	print("Hello User! What a nice day!")

def pack(a,b,c):
	return [a,b,c]

def eat_lunch(foods):
	if len(foods) == 0:
		print("My lunchbox is empty!")
	else:
		for i in range(len(foods)):
			if i == 0:
				print(f"First I eat {foods[0]}")
			else:
				print(f"Next I eat {foods[i]}")

#CALL FUNCS FOR TESTING
hello()
first = pack('q','w','e')
second = pack(1,2,3)
print(first, '\n', second)
eat_lunch([])
eat_lunch(['orange'])
eat_lunch(['sandwich','chips','pretzels','cheese','meatstick','water','cake','oreos','the lunchbox'])
		
