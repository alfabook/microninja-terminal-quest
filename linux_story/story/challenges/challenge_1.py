#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# A chapter of the story

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# Italian translation

import os
import sys

dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if __name__ == '__main__' and __package__ is None:
    if dir_path != '/usr':
        sys.path.insert(1, dir_path)

from linux_story.story.terminals.terminal_ls import TerminalLs
from linux_story.story.challenges.challenge_2 import Step1 as NextChallengeStep


class StepLs(TerminalLs):
    challenge_number = 1


class Step1(StepLs):
    story = [
        "{{wb:Sveglia}} : \"Beep beep beep! Beep beep beep!\"",
        "{{wb:Radio}} : {{Bb:\"Buongiorno, questo è il notiziario delle ore 9.\"",
        "\"La città di Microninja landia è stata svegliata da strane notizie. "
        "Sono state riportate persone scomparse"
        " e strutture danneggiate in tutta la città,"
        " e altre novità arrivano mentre parliamo.\"",
        "\"Il sindaco Hubert ha indetto una riunione di emergenza e"
        " vi terremo informati sugli eventi che accadono...\"}}\n",
        "E' ora di alzarti, testa assonnata!",
        "\n{{gb:Nuova Magia:}} Digita {{yb:ls}} e premi {{wb:Invio}} per "
        "{{lb:guardarti attorno}}.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = "ls"
    hints = [
        "{{rb:Digita}} {{yb:ls}} {{rb:e premi invio per guardarti attorno nella "
        "tua camera da letto.}}"
    ]

    last_step = True

    def next(self):
        NextChallengeStep(self.xp)
