x = 1
ans = 1

for num in range(1,526):
	x = num
	ans = x**2 + ans + 3
	
	# Prints new answer.
	print(ans)

# The question has four variables: x, y, previous answer (P), and answer (ans). The equation is ans = X * Y + P + 3, where X = 1, Y = 1, and P = 1.
# The question also says that x and y needs to be incremented by 1. This means X and Y are assumed to be the same. So I replaced Y with X^2.
# Set previous answer (P) equal to ans, which will make the first equation to be solved as follows: ans = (1)^2 + 1 + 3, which is 5.
# Iterate using for method.

# Password is therefore: pr0ggen


