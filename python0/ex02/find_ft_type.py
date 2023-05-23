def all_thing_is_obj(object: any) -> int:
	if (isinstance(object, str)):
		print("{0} is in the kitchen: {1}".format(object, type(object)))
	elif (isinstance(object, int)):
		print("Type not found")
	else:
		print(type(object))
	return 42