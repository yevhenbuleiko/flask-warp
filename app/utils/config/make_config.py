from termcolor import colored
from app.helpers import list_keys_from_dicts, list_matching_keys, list_mismatched_keys
from app.config import (app_config, settings_config, )

__all__ = ('make_config', 'config_files_dictionaries')

# Dictionaries Of Config Files
config_files_dictionaries = {
	'app'      :app_config, 
	'settings' :settings_config,
}

def make_config(config_from_file: dict):
	''' Make Common Configuration Dictionary From Config Files '''

	# checking for key matches in configuration files
	matches_config_keys = list_keys_from_dicts(config_files_dictionaries.items(), list_matching_keys)
	if len(matches_config_keys):
		print(colored('*** There Is Key Match In Configuration Files ({}) ***'.\
			format(', '.join(map(str, matches_config_keys))), 'red'))

	# Result Config File
	result = dict()
	for (key, conf_file) in config_files_dictionaries.items():
		# Add Data To Result Dictionary
		result.update(conf_file)
	
	# Added(Or Change) Config Dictionary, Values From Config Yaml File
	if config_from_file:
		result.update(config_from_file)

	return result