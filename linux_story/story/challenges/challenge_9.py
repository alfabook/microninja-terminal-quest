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

from linux_story.story.terminals.terminal_cd import TerminalCd
from linux_story.story.challenges.challenge_10 import Step1 as NextStep
from linux_story.helper_functions import play_sound
from linux_story.step_helper_functions import unblock_commands_with_cd_hint


class StepTemplateCd(TerminalCd):
    challenge_number = 9


class Step1(StepTemplateCd):
    story = [
        "Oh no! Controlliamo se mamma sta bene.",
        "Digita {{yb:cd ../}} per lasciare la {{bb:città}}."
    ]
    start_dir = "~/città"
    end_dir = "~"
    commands = ["cd ..", "cd ../", "cd"]
    hints = "{{rb:Usa}} {{yb:cd ../}} {{rb:per dirigerti verso casa.}}"

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        play_sound('bell')
        Step2()


class Step2(StepTemplateCd):
    story = [
        "{{pb:Ding. Dong.}}\n",

        "Digita {{yb:cd casa-mia/cucina/}} per andare dritto in "
        "{{bb:cucina}}.",

        "{{gb:Premi TAB per velocizzare la digitazione!}}"
    ]
    start_dir = "~"
    end_dir = "~/casa-mia/cucina"
    commands = ["cd casa-mia/cucina", "cd casa-mia/cucina/"]
    hints = [
        "{{rb:Usa}} {{yb:cd casa-mia/cucina/}} {{rb:per andare in "
        "cucina.}}"
    ]
    story_dict = {
        "nota_cucina": {
            "name": "nota",
            "path": "~/casa-mia/cucina"
        }
    }
    # Remove the note as well.
    deleted_items = ['~/casa-mia/cucina/mamma', '~/città/nota']

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step3()


class Step3(StepTemplateCd):
    story = [
        "Guarda attorno per accertarti che sia tutto OK."
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    commands = "ls"
    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per vedere se tutto sta dove "
        "dovrebbe essere.}}"
    ]

    def next(self):
        Step4()


class Step4(StepTemplateCd):
    story = [
        "Oh no - Anche mamma è sparita!",
        "Aspetta, c'è un'altra {{lb:nota}}.",
        "Usa {{lb:cat}} per {{lb:leggere}} la {{lb:nota}}."
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    commands = "cat nota"
    hints = "{{rb:Usa}} {{yb:cat nota}} {{rb:per leggere la nota.}}"
    last_step = True

    def next(self):
        NextStep(self.xp)
