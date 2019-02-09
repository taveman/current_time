import os
import logging
import json
from core.manager import TimeManager
from core.speaker import Speaker
from tools.tools import init_logger


root_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
parent_dir = os.path.abspath(os.path.dirname(root_dir))

# Reading project configuration file
config_file = os.path.join(parent_dir, 'config.json')
with open(config_file, 'r') as f:
    config = json.load(f)

sound_samples_dir = os.path.join(parent_dir, config['sound_dir'])
time_sample_dir = os.path.join(sound_samples_dir, config['sound_time_dir'])

init_logger(
    logger_name='time_speaker',
    info_logger_path=os.path.join(parent_dir, 'logs/info.log'),
    debug_logger_path=os.path.join(parent_dir, 'logs/debug.log')
)
logger = logging.getLogger('time_speaker')

speaker = Speaker()

time_speaker = TimeManager(
    speaker=speaker,
    root_sound_sample_dir=time_sample_dir,
    logger=logger
)

if __name__ == '__main__':
    print(time_speaker.__class__.__name__)
