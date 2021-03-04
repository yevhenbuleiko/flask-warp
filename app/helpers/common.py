
__all__ = ('list_keys_from_dicts', 'list_matching_keys', 'list_mismatched_keys', )

def list_keys_from_dicts(dictionaries: list, postproc=None):
	''' Make List of Keys From List Of Dictionaries '''
	key_list = []
	for (key, confdict) in dictionaries:
		key_list += confdict.keys()
	# Result Post Processing
	if postproc is not None:
		key_list = postproc(key_list)

	return key_list

def list_matching_keys(src_list: list):
	''' Get List Of Matching Keys From List '''
	maching = set()
	checked_item = src_list.pop()
	for i, val in enumerate(src_list):
		if checked_item in src_list[i:]:
			maching.add(checked_item)
		checked_item = val 
	return maching

def list_mismatched_keys(src_list: list):
	''' Get List Of Mismatching Keys From List '''
	mismaching = set()
	checked_item = src_list.pop()
	for i, val in enumerate(src_list):
		if checked_item not in src_list[i:]:
			maching.add(checked_item)
		checked_item = val 
	return mismaching