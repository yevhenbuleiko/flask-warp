from termcolor import colored
from pathlib import Path
import yaml

__all__ = ('dict_from_yaml_file')

def dict_from_yaml_file(yaml_file=None):
	''' Get Config Date From File - app/config.yaml '''

	# If Without Config File - return empty dictionary
	if not yaml_file:
		return {}

	# Get File By Path - The File - config.yaml - Should Be In The Folder - app
	try:
		# Get Config File Path
		default_file = Path(__file__).resolve().parents[1] / yaml_file
		# Get Config Data From File
		with open(default_file, 'r') as f:
			data = yaml.safe_load(f)
		# Terminal Message - Load With Config Data From File
		print(colored('*** Config Values From: {} file ***'.format(yaml_file), 'blue'))
		return data
	except FileNotFoundError:
		# Terminal Message - If Config File Not Found
		print(colored('*** Error Reading Config File ( FileNotFoundError ) ***', 'red'))
		# return empty dict
		return {}