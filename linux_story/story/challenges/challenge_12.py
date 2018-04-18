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

# Change this import statement, need to decide how to group the terminals
# together
from linux_story.story.terminals.terminal_mv import TerminalMv
from linux_story.story.challenges.challenge_13 import Step1 as NextStep
from linux_story.common import tq_file_system
from linux_story.step_helper_functions import unblock_commands


class StepTemplateMv(TerminalMv):
    challenge_number = 12


# Thanks you for saving the little girl
class Step1(StepTemplateMv):
    story = [
        "{{wb:Edith:}} {{Bb:Grazie per averla salvata!}}",
        "{{wb:Eleonora:}} {{Bb:Cagnolino!}}",
        "{{wb:Edith:}} {{Bb:Potresti salvare anche il suo cane? Sono preoccupato che "
        "possa accadergli qualcosa se continua a stare fuori.}}\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "mv ../cane .",
        "mv ../cane ./",
        "mv ~/città/cane ~/città/.rifugio-nascosto",
        "mv ~/città/cane ~/città/.rifugio-nascosto/",
        "mv ~/città/cane .",
        "mv ~/città/cane ./",
        "mv ../cane ~/città/.rifugio-nascosto",
        "mv ../cane ~/città/.rifugio-nascosto/",
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:mv ../cane ./}} {{rb:per salvare il cane.}}"
    ]
    cane_file = os.path.join(tq_file_system, 'città/.rifugio-nascosto/cane')

    def block_command(self):
        return unblock_commands(self.last_user_input, self.commands)

    def next(self):
        Step2()


# Save both the cane and the little girl
class Step2(StepTemplateMv):
    story = [
        "{{wb:Eleonora:}} {{Bb:Yay, cagnolino!}}",
        "{{wb:cane:}} {{Bb:Ruff!}}",
        "{{wb:Edith:}} {{Bb:Grazie tantissimo per averli riportati indietro entrambi.",
        "Mi ero sbagliato su di te. Sei un eroe!}}\n",
        "{{lb:Ascolta tutti}} e vedi se puoi fare qualcos'altro "
        "per aiutarli.\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = "cat Edoardo"
    all_commands = {
        "cat Edith": "\n{{wb:Edith:}} {{Bb:\"Grazie tantissime! "
        "Eleonora, non andare di nuovo fuori - mi hai fatto prendere un grandissimo "
        "spavento!\"}}",

        "cat Eleonora": "\n{{wb:Eleonora:}} {{Bb:\"Dove pensi che la "
        "campana ci avrebbe portati?\"}}",

        "cat cane": "\n{{wb:cane:}} {{Bb:\"Bau! Bau Bau!\"}}"
    }
    hints = [
        "{{gb:Edoardo guarda come se avesse qualcosa da dire. "
        "Ascolta Edoardo con}} {{yb:cat Edoardo}}"
    ]
    last_step = True

    def show_hint(self):
        if self.last_user_input in self.all_commands.keys():
            hint = self.all_commands[self.last_user_input]
            self.send_hint(hint)
        else:
            # Show default hints.
            self.send_hint()

    def next(self):
        NextStep(self.xp)
