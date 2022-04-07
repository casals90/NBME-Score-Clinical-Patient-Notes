import logging
import sys

import yaml

with open('/config/settings.yaml') as file:
    config_settings = yaml.load(file, Loader=yaml.FullLoader)

log_params = config_settings['logging']
logger = logging.getLogger(__name__)
handler_out = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    log_params['formatter']['format'], log_params['formatter']['time_format'])
handler_out.setFormatter(formatter)
logger.addHandler(handler_out)
logger.setLevel(getattr(logging, log_params['level']))
logger.propagate = False
