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
from linux_story.story.challenges.challenge_7 import Step1 as NextChallengeStep
from linux_story.step_helper_functions import unblock_commands_with_cd_hint


class StepTemplateCd(TerminalCd):
    challenge_number = 6


class Step1(StepTemplateCd):
    story = [
        "Informiamo mamma su papà. Digita {{yb:cat mamma}}"
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    commands = "cat mamma"
    hints = (
        "{{rb:Per parlare a mamma, digita}} {{yb:cat mamma}} {{rb:e premi "
        "Invio.}}"
    )

    def next(self):
        Step2()


class Step2(StepTemplateCd):
    story = [
        "{{wb:mamma:}} {{Bb:\"Non l'hai trovato? Strano, "
        "non lascia mai casa senza prima dirmelo.\"",
        "\"Forse è andato all'incontro cittadino col sindaco,"
        " quello di cui stavano parlando i notiziari. "
        "Perchè non vai a controllare? Io starò a casa, nel caso che torni "
        "indietro.\"}}\n",
        "Dirigiamoci verso la {{bb:città}}. Per lasciare la casa, usa {{yb:cd}} da solo."
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~"
    commands = "cd"
    hints = "{{rb:Digita}} {{yb:cd}} {{rb:per cominciare il viaggio.}}"

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step3()


class Step3(StepTemplateCd):
    story = [
        "Sei fuori di casa, nella lunga strada ventosa chiamata Tilde, "
        "oppure {{lb:~}}",
        "{{lb:Guarda attorno}} ancora per vedere dove andare."
    ]
    start_dir = "~"
    end_dir = "~"
    commands = "ls"
    hints = "{{rb:Bloccato? digita}} {{yb:ls}} {{rb:per guardare attorno.}}"

    def next(self):
        Step4()


class Step4(StepTemplateCd):
    story = [
        "Puoi vedere una {{bb:città}} in lontananza! {{lb:Andiamo}} "
        "la usando {{lb:cd}}."
    ]
    start_dir = "~"
    end_dir = "~/città"
    commands = ["cd città", "cd città/"]
    hints = "{{rb:Digita}} {{yb:cd città/}} {{rb:per camminare dentro la città.}}"

    last_step = True

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        NextChallengeStep(self.xp)
