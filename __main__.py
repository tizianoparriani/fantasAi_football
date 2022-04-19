import argparse
from dynaconf import LazySettings

parser = argparse.ArgumentParser(description='Personal information')
parser.add_argument('--config_file', dest='config_file', type=str, help='Path to config file')
parser.add_argument('--config_mode', dest='config_mode', type=str, help='Config mode', default='default')

args = parser.parse_args()

params = LazySettings(settings_files=[args.config_file])[args.config_mode]

print(params)