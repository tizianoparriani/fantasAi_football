import os
import pandas as pd
from dynaconf import LazySettings
from dynaconf.utils.boxing import DynaBox
from typing import List

params = LazySettings(settings_files=[config_file])[config_mode]