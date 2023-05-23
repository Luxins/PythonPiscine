from math import isnan

def NULL_not_found(object: any) -> int:
	try:
		if object is None:
			print('Nothing: {0} {1}'.format(object, type(object)))
		elif isinstance(object, float) and isnan(object):
			print('Cheese: {0} {1}'.format(object, type(object)))
		elif object is False:
			print(f'Fake: {object} {type(object)}')
		elif object == 0:
			print('Zero: {0} {1}'.format(object, type(object)))
		elif object == "":
			print(f'Empty: {object} {type(object)}')
		else:
			print('Type not found')
			return 1
	except:
		return 1
	return 0
