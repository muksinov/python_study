# pi = 'outer pi variable'

# def print_pi():
# 	pi = 'inner pi variable'
# 	print(pi)

# print_pi()
# print(pi)




# # Local Scope

# pi = 'global pi variable'
# def inner():
# 	pi = 'inner pi variable'
# 	print(pi)

# inner()

# # Global Scope

# pi = 'global pi variable'
# def inner():
# 	pi = 'inner pi variable'
# 	print(pi)

# inner()
# print(pi)



# Enclosed Scope

pi = 'global pi variable'

def outer():
	pi = 'outer pi variable'
	def inner():
		pi = 'inner pi variable'
		nonlocal pi
		print(pi)
	inner()

outer()
print(pi)
