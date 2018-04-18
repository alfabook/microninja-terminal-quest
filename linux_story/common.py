# common.py

# This contains all the common names across the OS.

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# rebadged with microninja

import os
import json

# setting up directories
current_dir = os.path.abspath(os.path.dirname(__file__))

# media dir
media_local = os.path.join(current_dir, '../media')
media_usr = '/usr/share/linux-story/media'

if os.path.exists(media_local):
    common_media_dir = media_local
elif os.path.exists(media_usr):
    common_media_dir = media_usr
else:
    raise Exception('Neither local nor usr media dir found!')

css_dir = os.path.join(current_dir, 'gtk3', 'css')

# Constants

# /home/user/
home_folder = os.path.expanduser('~')

# This is where the filetree that the user interacts with.
tq_file_system = os.path.join(home_folder, '.linux-story')

# The contents of this folder are backed up online
tq_backup_folder = os.path.join(home_folder, 'Terminal-Quest-content')


def get_max_challenge_number():
    '''
    Returns:
        str: string of the maximum challenge number as saved in
            kano-profile.
    '''

    # Hardcoded path, perhapes change it later
    path = "/usr/share/microninja-profile/rules/app_profiles.json"
    f = open(path)
    str_data = f.read()
    f.close()

    dict_data = json.loads(str_data)
    max_level = dict_data['linux-story']['max-level']

    return max_level
