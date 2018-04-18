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
from linux_story.story.challenges.challenge_11 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_commands_with_cd_hint


class StepTemplateCd(TerminalCd):
    challenge_number = 10


class Step1(StepTemplateCd):
    story = [
        "Sei a casa. Sembri solo.",
        "Usa {{lb:cat}} per {{lb:esaminare}} alcuni oggetti attorno a te.\n"
    ]
    allowed_commands = [
        "cat banana",
        "cat torta",
        "cat croissant",
        "cat acini",
        "cat latte",
        "cat giornale",
        "cat forno",
        "cat crostata",
        "cat sandwich",
        "cat tavolo"
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    counter = 0
    deleted_items = ["~/casa-mia/cucina/nota"]
    story_dict = {
        "Eleonora, Edoardo, Edith, mela, cane": {
            "path": "~/città/.rifugio-nascosto",
        },
        "bottiglia-vuota": {
            "path": "~/città/.rifugio-nascosto/cesto"
        },
        "MV": {
            "path": "~/città/.rifugio-nascosto/.minuscolo-scrigno"
        }
    }
    # for check_command logic
    first_time = True

    def check_command(self):

        if self.last_user_input in self.allowed_commands:
            self.counter += 1
            self.allowed_commands.remove(self.last_user_input)
            hint = (
                "\n{{gb:Ben fatto! Guarda un altro "
                "oggetto.}}"
            )

        else:
            if self.first_time:
                hint = (
                    "\n{{rb:Usa}} {{lb:cat}} {{rb:per guardare due "
                    "oggetti attorno a te.}}"
                )
            else:
                hint = (
                    '\n{{rb:Usa il comando}} {{yb:' + self.allowed_commands[0] +
                    '}} {{rb:per continuare.}}'
                )

        level_up = (self.counter >= 2)

        if not level_up:
            self.send_text(hint)
            self.first_time = False
        else:
            return level_up

    def next(self):
        Step2()


class Step2(StepTemplateCd):
    story = [
        "Sembra che qua ci sia soltanto molto cibo.",
        "Guarda nuovamente se puoi trovare qualcos'altro in {{bb:città}}.",
        "Prima di tutto, usa {{yb:cd ../}} per {{lb:lasciare}} la cucina.\n"
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/città"
    commands = [
        "cd ~/città",
        "cd ~/città/",
        "cd ..",
        "cd ../",
        "cd città",
        "cd città/",
        "cd ../..",
        "cd ../../",
        "cd"
    ]
    num_turns_in_home_dir = 0

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def show_hint(self):

        # decide command needed to get to next part of città
        if self.current_path == '~/casa-mia/cucina' or \
                self.current_path == '~/casa-mia':

            # If the last command the user used was to get here
            # then congratulate them
            if self.last_user_input == "cd .." or \
                    self.last_user_input == 'cd ../':
                hint = (
                    "\n{{gb:Ottimo lavoro! Ora ridai l'ultimo comando usando "
                    "il tasto SU della tua tastiera.}}"
                )

            # Otherwise, give them a hint
            else:
                hint = (
                    '\n{{rb:Usa}} {{yb:cd ../}} {{rb:per dirigerti verso la città.}}'
                )

        elif self.current_path == '~':
            # If they have only just got to the home directory,
            # then they used an appropriate command
            if self.num_turns_in_home_dir == 0:
                hint = (
                    "\n{{gb:Ottimo lavoro! Ora usa}} {{yb:cd città/}} {{gb: "
                    "per dirigerti verso la città.}}"
                )

            # Otherwise give them a hint
            else:
                hint = '\n{{rb:Usa}} {{yb:cd città/}} {{rb:per andare in città.}}'

            # So we can keep track of the number of turns they've been in the
            # home directory
            self.num_turns_in_home_dir += 1

        # print the hint
        self.send_text(hint)

    def next(self):
        Step3()


class Step3(StepTemplateCd):
    story = [
        "Usa {{yb:ls}} per {{lb:guardare attorno}}.\n",
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "ls"
    hints = "{{rb:Usa}} {{yb:ls}} {{rb:per dare uno sguardo attorno alla città.}}"

    def next(self):
        Step4()


class Step4(StepTemplateCd):
    story = [
        "Il posto appare deserto.",
        "Però, ti sembra di sentire dei bisbigli.",
        # TODO make this writing small
        "\n{{Bn:\".....se usassero}} {{yb:ls -a}}{{Bn:, ci vederebbero...\"}}",
        "{{Bn:\"..Shhh!  ...potrebbe sentire....\"}}\n"
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "ls -a"
    hints = [
        "{{rb:Hai sentito bisbigli riferirsi a}} {{yb:ls -a}}"
        "{{rb:, prova a usarlo!}}",
    ]

    def next(self):
        Step5()


class Step5(StepTemplateCd):
    story = [
        "Vedi un {{bb:.rifugio-nascosto}} che non avevi notato prima.",
        "{{gb:Ciò che comincia con . è normalmente nascosto alla vista.}}",
        "Sembra che i bisbigli vengano da li. Prova ad andarci.\n"
    ]
    start_dir = "~/città"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "cd .rifugio-nascosto",
        "cd .rifugio-nascosto/"
    ]
    hints = [
        "{{rb:Prova ad andare dentro il}} {{lb:.rifugio-nascosto}} {{rb:usando }}"
        "{{lb:cd}}{{rb:.}}",
        "{{rb:Usa il comando}} {{yb:cd .rifugio-nascosto/ }}"
        "{{rb:per entrare.}}"
    ]

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step6()


class Step6(StepTemplateCd):
    story = [
        "C'è qualcuno qua? {{lb:Guarda attorno}}.\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    ]
    last_step = True

    def next(self):
        NextStep(self.xp)
