from functools import wraps
from datetime import datetime, timezone
from time import perf_counter

# Decorator that allows to run a function only at odd seconds, else prints out "We're even!"
def odd_it(fn: "Function"):
	"""
	Func which behaves like a closure and provides a functionality as decorator
	---------
	Params: fn: Input function to be run on odd seconds
	---------
	Returns: inner function object
	"""
	# MISSING CODE
	@wraps(fn)
	def inner(*args, **kwargs):
		"""
		Inner function which provides implementation of the logic. 
		Decorator @wraps decorates the function to fix the metadata of our inner function in this decorator.
		--------
		Parameters: *args: contains all arguments of diff types, which can vary.
				**kwargs: contains all keyword arguments
		"""
		result = None
		if datetime.now().second % 2 != 0:
			result = fn(*args, **kwargs)
		else:
			print("We're even!")
		return result
	return inner

# The same logger that we coded in the class
# it will be tested against a function that will be sent 2 parameters, and 
# it would return some random string. 
def logger(fn: "Function"):
	"""
	Function to return object of another function which generates logs
	----------
	Params:
	fn: Function to be called about which logs are to be generated

	----------
	Returns:
	inner function object
	"""
	@wraps(fn)
	def inner(*args, **kwargs):
		"""
		Function which binds the properties of function passed to wraps decorator
		----------
		Params:
		*args: takes arguments of function fn
		**kwargs: keyword args of function fn

		----------
		Returns:
		result: output after function exection
		"""
		secs = perf_counter()
		run_dt = datetime.now(timezone.utc)
		result = fn(*args, **kwargs)
		all_params = [arg for arg in args]
		kw_params = [kwarg for kwarg in kwargs]

		type_params = [type(ar) for ar in all_params]
		type_kw_params = [type(kar) for kar in kw_params]

		print(f'{fn.__name__}: called at: {run_dt} \nExecution time: {secs} secs \
				\nFunction description: {fn.__doc__} \nFunction annotation:')
		for arg, typ in zip(all_params, type_params):
			print(arg, typ)

		for karg, ktyp in zip(kw_params, type_kw_params):
			print(karg, ktyp)
		
		return result

	return inner



# start with a decorator_factory that takes an argument one of these strings, 
# high, mid, low or no
# then write the decorator that has 4 free variables
# based on the argument set by the factory call, give access to 4, 3, 2 or 1 arguments
# to the function being decorated from var1, var2, var3, var4
# YOU CAN ONLY REPLACE "#potentially missing code" LINES WITH MULTIPLE LINES BELOW
# KEEP THE REST OF THE CODE SAME
def decorator_factory(access:str):
	# MISSING CODE
	"""
	Returns list of elements based on access specified
	"""
	def outer(fn: "Function"):
		#free variables
		high, mid, low, no = 4, 3, 2, 1
		@wraps(fn)
		def inner(*args, **kwargs):
			if access == "high":
				return [high, mid, low, no]

			elif access == "mid":
				return [mid, low, no]

			elif access == "low":
				return [low, no]

			elif access == "no":
				return [no]

			else:
				return "Improper access keyword set"

		return inner
	return outer


# The authenticate function. Start with a dec_factory that sets the password. It's inner
# will not be called with "password", *args, **kwargs on the fn
def authenticate(set_password):
	"""
	takes in actual password as input parameter
	-------
	Params:
		set_password: actual password to be match against

	-------
	Returns:
		object of outer function
	"""
	def outer(fn: "Function"):
		"""
		--------
		Params:
			fn: function implementing the decorator for password validation
		--------
		Returns:
			object of inner function
		"""
		@wraps(fn)
		def inner(*args):
			"""
			Function which takes entered password from user as argument. Raises TypeError on no input parameter
			--------
			Params: 
				*args: containing the entered password
			--------
			Returns:
				String: "Amazing!" on a match and "Wrong Password" on no match. 
			"""
			if len(args) == 0:
				raise TypeError("Function should have an input parameter")

			else:
				if args[0] == set_password:
					return "Amazing!"

				else:
					return  "Wrong Password"

		return inner
	return outer


# The timing function
def timed(reps):
	"""
	Executes an input function / implementing function reps number of times
	"""
	def outer(fn: "Function"):
		@wraps(fn)
		def inner(*args, **kwargs):
			time_elapsed = 0
			for i in range(reps):
				start = perf_counter()
				result = fn(*args, **kwargs)
				time_elapsed += (perf_counter() - start)

			avg_time = time_elapsed / reps
			print(f'Average time taken: {avg_time} for {reps} repetitions')

			return result
		return inner
	return outer