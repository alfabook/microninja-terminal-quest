#!/usr/bin/env python
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A chapter of the story

# -*- coding: utf-8 -*-

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# Italian translation
# rebadged with microninja

import os
import sys

dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if __name__ == '__main__' and __package__ is None:
    if dir_path != '/usr':
        sys.path.insert(1, dir_path)

from linux_story.story.terminals.terminal_mv import TerminalMv
from linux_story.step_helper_functions import unblock_commands
from linux_story.story.challenges.challenge_17 import Step1 as NextStep
# import time


class StepTemplateMv(TerminalMv):
    challenge_number = 16


class Step1(StepTemplateMv):
    story = [
        "C'è un vecchio {{lb:.scrigno}} nascosto sotto il tuo letto, "
        "che non ricordi di aver visto prima.",
        "Vai verso {{bb:camera-mia}} per uno sguardo più approfondito.",
        "{{lb:Sbircia attraverso}} lo {{lb:.scrigno}} e guarda cosa contiene."
    ]

    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"

    commands = [
        'ls .scrigno',
        'ls .scrigno/',
        'ls -a .scrigno',
        'ls -a .scrigno/',
        'ls .scrigno/ -a',
        'ls .scrigno -a'
    ]

    hints = [
        "{{rb:Usa}} {{yb:ls .scrigno}} {{rb:per guardare dentro .scrigno}}"
    ]

    def next(self):
        Step2()


class Step2(StepTemplateMv):
    story = [
        "Ci sono alcuni rotoli di pergamena, simili a quelli trovati dentro "
        "il {{bb:.rifugio-nascosto}}",
        "Usa {{lb:cat}} per {{lb:leggere}} uno dei rotoli.\n"
    ]

    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"

    commands = [
        'cat .scrigno/LS',
        'cat .scrigno/CAT',
        'cat .scrigno/CD'
    ]

    hints = [
        "{{rb:Usa}} {{yb:cat .scrigno/LS}} {{rb:per leggere il rotolo LS.}}"
    ]

    def next(self):
        Step3()


# Remove this step?
'''
class Step3(StepTemplateMv):
    story = [
        "You recognise these commands.",
        "Maybe you should {{lb:move}} the one you found in the "
        "{{lb:~/town/.rifugio-nascosto/.tiny-scrigno}} to this {{lb:.scrigno}}, "
        "so they're all safe and in the same place.",
        "\n{{gb:Use the TAB key to complete the file paths - it will save you "
        "typing!}}\n"
    ]

    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"

    commands = [
        "mv ~/town/.rifugio-nascosto/.tiny-scrigno/MV .scrigno/",
        "mv ~/town/.rifugio-nascosto/.tiny-scrigno/MV .scrigno",
        "mv ../../.rifugio-nascosto/.tiny-scrigno/MV .scrigno/",
        "mv ../../.rifugio-nascosto/.tiny-scrigno/MV .scrigno",
        "mv ~/town/.rifugio-nascosto/.tiny-scrigno/MV ~/casa-mia/camera-mia/.scrigno/",
        "mv ~/town/.rifugio-nascosto/.tiny-scrigno/MV ~/casa-mia/camera-mia/.scrigno"
    ]
    hints = [
        "{{rb:You want to use the command}} "
        "{{yb:mv ~/town/.rifugio-nascosto/.tiny-scrigno/MV .scrigno/}}\n"
        "{{rb:Use the UP arrow to replay your last command if you were "
        "close!}}"
    ]

    def block_command(self):
        return unblock_commands(self.last_user_input, self.commands)

    def next(self):
        Step4()
'''


class Step3(StepTemplateMv):
    story = [
        "Mi chiedo se ci sia qualcos'altro nascosto in questo {{lb:.scrigno}}",
        "{{lb:Guarda}} per cercare altri oggetti."
    ]

    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"

    hints = [
        "{{rb:Usa}} {{yb:ls -a .scrigno}} {{rb:per vedere se ci sono altri "
        "oggetti nascosti nello scrigno.}}"
    ]

    commands = [
        "ls -a .scrigno",
        "ls -a .scrigno/",
        'ls .scrigno/ -a',
        'ls .scrigno -a'
    ]

    def next(self):
        Step4()


class Step4(StepTemplateMv):
    story = [
        "Improvvisamente, vedi una nota macchiata {{lb:.nota}}, pressata "
        "in un angolo dello {{lb:.scrigno}}.",
        "Cosa dice?\n"
    ]

    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"

    hints = [
        "{{rb:Usa}} {{yb:cat .scrigno/.nota}} {{rb:per leggere la}} "
        "{{lb:.nota}}{{rb:.}}"
    ]

    commands = [
        "cat .scrigno/.nota"
    ]

    def next(self):
        NextStep(self.xp)
