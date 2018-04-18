#!/usr/bin/env python

# setup.py
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# rebadged with microninja

from distutils.core import setup
import os


def recursively_get_dirs(package_name, start_dir):
    '''Gets all directories from a directory'''

    start_path = os.path.join(package_name, start_dir)
    paths = []

    for root, dir, files in os.walk(start_path):
        for f in files:
            file_path = os.path.join(root, f)

            # If this is package data for linux_story
            if package_name:
                file_path = file_path.replace(package_name + "/", "")

            paths.append(file_path)

    return paths


def is_image(filepath):
    img_extensions = ['.png']
    ext = os.path.splitext(filepath)[1]

    return ext in img_extensions


story = recursively_get_dirs("linux_story", "story")
ascii_assets = recursively_get_dirs("linux_story", "ascii_assets")
gtk3 = recursively_get_dirs("linux_story", "gtk3")
media_images = recursively_get_dirs("", "media/images")
media_sounds = recursively_get_dirs("", "media/sounds")
#icons = filter(is_image, recursively_get_dirs("", "icon"))
#kdesktop = recursively_get_dirs("", "kdesktop")

setup(name='Linux Story',
      version='1.2',
      description='Story to teach people basic Linux commands',
      author='Team Scuolabook',
      author_email='info@scuolabook.it',
      url='http://www.scuolabook.it',
      packages=['linux_story'],
      package_dir={'linux_story': 'linux_story'},
      scripts=['bin/linux-story'],
      package_data={
          'linux_story': story + ascii_assets + gtk3
      },
      data_files=[
          ('/usr/share/linux-story/media/images', media_images),
          ('/usr/share/linux-story/media/sounds', media_sounds),
          #('/usr/share/microninja-desktop/kdesk/kdesktop/', kdesktop),
          #('/usr/share/icons/microninja/88x88/apps', icons),
          ('/usr/share/linux-story', ['nano-2.2.6/src/nano'])
      ]
      )
