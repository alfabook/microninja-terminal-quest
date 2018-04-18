#!/usr/bin/env python
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
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

# from linux_story.Step import Step
from linux_story.story.terminals.terminal_cd import TerminalCd
from linux_story.story.challenges.challenge_5 import Step1 as NextChallengeStep
from linux_story.helper_functions import play_sound
from linux_story.step_helper_functions import unblock_commands_with_cd_hint


class StepTemplateCd(TerminalCd):
    challenge_number = 4


class Step1(StepTemplateCd):
    story = [
        "Strano. Ma non c'è tempo per questo ora - andiamo a cercare mamma.",
        "\n{{gb:Nuova magia}}: {{lb:cd}} ti permette di spostarti in posti diversi.",
        "\nUsa il comando {{yb:cd ../}} to {{lb:lasciare}} la tua camera.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia"
    commands = [
        "cd ..",
        "cd ../",
        "cd ~/casa-mia",
        "cd ~/casa-mia/"
    ]
    hints = [
        "{{rb:Digita}} {{yb:cd ../}} {{rb:per lasciare la tua stanza. Il}} "
        "{{lb:..}} "
        "{{rb:è la camera dietro te.}}",
        "{{rb:Digita}} {{yb:cd ../}} {{rb:per lasciare la tua stanza.}}"
    ]

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step2()


class Step2(StepTemplateCd):
    story = [
        "Hai abbandonato {{bb:camera-mia}} e sei nell'andito di {{bb:casa-mia}}.",
        "{{lb:Osserva}} tutte le diverse stanze con {{yb:ls}}.\n"
    ]
    start_dir = "~/casa-mia"
    end_dir = "~/casa-mia"
    commands = "ls"
    hints = "{{rb:Digita}} {{yb:ls}} {{rb:e premi Invio.}}"
    story_dict = {
        "nota_serra": {
            "name": "nota",
            "path": "~/casa-mia/giardino/serra"
        }
    }
    deleted_items = ['~/casa-mia/giardino/serra/papà']

    def next(self):
        play_sound('bell')
        Step3()


class Step3(StepTemplateCd):
    story = [
        "{{pb:Ding. Dong.}}\n",
        "Cos'è? Una campana? Un po' strano.",
        "Guarda la porta per la {{bb:cucina}}, and ascolta il rumore di come si "
        "cucina.",
        "Sembra che qualcuno stia preparando la colazione!",
        "Per {{lb:entrare nella cucina}}, usa {{yb:cd cucina/}}"
    ]
    start_dir = "~/casa-mia"
    end_dir = "~/casa-mia/cucina"
    commands = ["cd cucina", "cd cucina/"]
    hints = ["{{rb:Digita}} {{yb:cd cucina/}} {{rb:e premi Invio.}}"]

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step4()


class Step4(StepTemplateCd):
    story = [
        "Grande, sei in cucina.",
        "{{lb:Guarda}} mamma con {{yb:ls}}."
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    commands = "ls"
    hints = "{{rb:Non riesci a trovarla? Digita}} {{yb:ls}} {{rb:e premi Invio.}}"

    def next(self):
        Step5()


class Step5(StepTemplateCd):
    story = [
        "La vedi molto impegnata, in una nuvola di vapore.",

        "{{lb:Ascoltiamo}} cosa {{lb:mamma}} ha da dire "
        "usando {{lb:cat}}."
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    commands = "cat mamma"
    hints = (
        "{{rb:Bloccato? Digita:}} {{yb:cat mamma}}. "
        "{{rb:Non dimenticare lo spazio e occhio alle maiuscole/minuscole!}}"
    )

    last_step = True

    def next(self):
        NextChallengeStep(self.xp)
