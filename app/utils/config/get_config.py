from termcolor import colored
from .make_config import config_files_dictionaries

__all__ = ('get_config')

def get_config(config_value_path):
	''' Get Configuration Data From Config Filea By Path And Name '''
	'''
	using: get_config('settings.subdict.TEST_VAL')
	'''
	config_path_steps = config_value_path.split('.')
	result = config_files_dictionaries[config_path_steps[0]]
	for step in config_path_steps[1:]:
		result = result.get(step, None)
		if result is None:
			print(colored('Not Available Key In Config Path By {}'.format(step), \
				'red'))
			break

	return result
