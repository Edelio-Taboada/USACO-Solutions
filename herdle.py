right = [0 for i in range(9)]
guess = [0 for i in range(9)]
green = 0
yellow = 0
def checkYellow(g):
	for j, every in enumerate(right):
			if every == g:
				if guess[j] != every:
					return [True, j]
	return [False, -9]

			
for j in range(3):
	for i, k in enumerate(input()):
		right[i + j*3] = k
for j in range(3):
	for i, k in enumerate(input()):
		guess[i + j*3] = k
for i, each in enumerate(guess):
    if each == right[i]:
        green += 1
        right[i] = -10
    elif checkYellow(each)[0]:
        yellow +=1
        right[checkYellow(each)[1]] = -10
    guess[i] = 10
print(green)
print(yellow)
		
		
