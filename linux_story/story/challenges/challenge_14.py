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
from linux_story.common import tq_file_system
from linux_story.story.challenges.challenge_15 import Step1 as NextStep
from linux_story.step_helper_functions import (
    unblock_commands_with_cd_hint, unblock_commands
)


class StepTemplateMv(TerminalMv):
    challenge_number = 14


class Step1(StepTemplateMv):
    story = [
        "{{lb:Guarda attorno}} per vedere che cibo c'è "
        "in cucina.\n"
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per}} {{lb:guardare}} "
        "{{rb:la cucina.}}"
    ]

    def next(self):
        Step2()


# Move three pieces of food into the cesto
class Step2(StepTemplateMv):
    story = [
        "{{lb:Sposta}} tre cibi dentro il tuo cesto.",
        "Puoi spostare tre oggetti contemporaneamente usando {{lb:mv <oggetto1> <oggetto2>"
        " <oggetto3> cesto/}}.\n"
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    passable_items = [
        'banana',
        'torta',
        'croissant',
        'crostata',
        'acini',
        'latte',
        'sandwich'
    ]
    unmovable_items = {
        "giornale": "{{rb:Hanno chiesto cibo, probabilmente non potrebbero "
        "mangiare il giornale.}}",

        "forno": "{{rb:E' un po' troppo pesante da trasportare!}}",

        "tavolo": "{{rb:E' un po' troppo ingombrante da trasportare!}}"
    }
    moved_items = []

    def block_command(self):
        separate_words = self.last_user_input.split(' ')

        if "cd" in self.last_user_input:
            return True

        if separate_words[0] == 'mv' and (separate_words[-1] == 'cesto' or
                                          separate_words[-1] == 'cesto/'):
            for item in separate_words[1:-1]:
                if item not in self.passable_items:
                    if item in self.unmovable_items:
                        self.send_hint(self.unmovable_items[item])
                        return True
                    else:
                        hint = (
                            "{{rb:Stai cercando di spostare qualcosa che "
                            "non è nella cartella.\nProva ad usare}} "
                            "{{yb:mv %s cesto/}}"
                            % self.passable_items[0]
                        )
                        self.send_hint(hint)
                        return True

            return False

    def check_command(self):

        separate_words = self.last_user_input.split(' ')
        all_items = []

        if self.get_command_blocked():
            hint = '{{rb:Prova ad usare}} {{yb:mv %s cesto/}}' \
                % self.passable_items[0]

        elif separate_words[0] == 'mv' and (separate_words[-1] == 'cesto' or
                                            separate_words[-1] == 'cesto/'):
            for item in separate_words[1:-1]:
                all_items.append(item)

            for item in all_items:
                self.passable_items.remove(item)

            hint = '\n{{gb:Ottimo! Continua così.}}'

        else:
            hint = '{{rb:Prova ad usare}} {{yb:mv %s cesto/}}' \
                % self.passable_items[0]

        self.send_hint(hint)

    # Check that the cesto folder contains the correct number of files?
    def check_output(self, output):
        cesto_dir = os.path.join(tq_file_system, 'casa-mia/cucina/cesto')
        food_files = [
            f for f in os.listdir(cesto_dir)
            if os.path.isfile(os.path.join(cesto_dir, f))
        ]

        if len(food_files) > 3:
            return True
        else:
            return False

    def next(self):
        Step3()


class Step3(StepTemplateMv):
    story = [
        "\nOra vogliamo ridirigerci verso {{bb:.rifugio-nascosto}} col "
        "cesto.",
        "{{lb:Sposta}} il {{lb:cesto}} verso la {{lb:~}}.\n"
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia/cucina"
    commands = [
        "mv cesto ~",
        "mv cesto/ ~",
        "mv cesto ~/",
        "mv cesto/ ~/"
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:mv cesto ~/}} "
        "{{rb:per spostare il cesto verso la strada ventosa ~}}"
    ]

    def block_command(self):
        return unblock_commands(self.last_user_input, self.commands)

    def next(self):
        Step4()


class Step4(StepTemplateMv):
    story = [
        "Segui il cesto usando {{yb:cd}}.\n"
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~"
    commands = [
        "cd",
        "cd ~",
        "cd ~/"
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:cd}} {{rb:da solo "
        "per andare verso la strada ventosa ~}}"
    ]

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step5()


class Step5(StepTemplateMv):
    story = [
        "Ora porta il cesto pieno alla famiglia.",
        "{{lb:Sposta}} il {{lb:cesto}} verso {{lb:città/.rifugio-nascosto}}.",
    ]

    start_dir = "~"
    end_dir = "~"
    commands = [
        "mv cesto città/.rifugio-nascosto",
        "mv cesto/ città/.rifugio-nascosto",
        "mv cesto città/.rifugio-nascosto/",
        "mv cesto/ città/.rifugio-nascosto/",
        "mv cesto ~/città/.rifugio-nascosto",
        "mv cesto/ ~/città/.rifugio-nascosto",
        "mv cesto ~/città/.rifugio-nascosto/",
        "mv cesto/ ~/città/.rifugio-nascosto/"
    ]
    hints = [
        "{{rb:Usa}} {{yb:mv cesto città/.rifugio-nascosto/}} "
        "{{rb:per portare il cesto alla famiglia.}}"
    ]

    def block_command(self):
        return unblock_commands(self.last_user_input, self.commands)

    def next(self):
        Step6()


class Step6(StepTemplateMv):
    story = [
        "{{gb:Quasi fatto!}} Finalmente {{lb:vai}} dentro "
        "{{lb:città/.rifugio-nascosto}} usando {{lb:cd}}.\n",
    ]

    start_dir = "~"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "cd città/.rifugio-nascosto",
        "cd città/.rifugio-nascosto/",
        "cd ~/città/.rifugio-nascosto",
        "cd ~/città/.rifugio-nascosto/"
    ]
    hints = [
        "{{rb:Usa}} {{yb:cd città/.rifugio-nascosto/}} "
        "{{rb:per riunirti alla famiglia.}}",
    ]

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step7()


class Step7(StepTemplateMv):
    story = [
        "{{wn:Controlla ciascuno con}} {{lb:cat}} {{wn:per vedere se "
        "sono contenti del cibo.}}\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    hints = [
        "{{rb:Controlla ciascuno usando}} {{yb:cat}}"
    ]
    allowed_commands = {
        "cat Edith": (
            "\n{{wb:Edith:}} {{Bb:Hai salvato la mia bambina ed il cane, "
            "e ora ci hai salvato dalla fame...come posso "
            "ringraziarti?}}\n"
        ),
        "cat Eleonora": (
            "\n{{wb:Eleonora:}} {{Bb:Yummy! Vedi, te lo dicevo cagnolino, "
            "qualcuno ci avrebbe aiutato.}}\n"
        ),
        "cat Edoardo": (
            "\n{{wb:Edoardo:}} {{Bb:Grazie! Sapevo che saresti venuto "
            "per noi. Sei davvero un eroe!}}\n"
        ),
        "cat cane": (
            "\n{{wb:Cane:}} {{Bb:\"Bau!\"}} {{wn:\nIl cane sembra davvero "
            "felice.\n}}"
        )
    }

    last_step = True

    def check_command(self):
        if not self.allowed_commands:
            return True

        if self.last_user_input in self.allowed_commands.keys():

            hint = self.allowed_commands[self.last_user_input]
            del self.allowed_commands[self.last_user_input]
            num_people = len(self.allowed_commands.keys())

            if num_people == 0:
                hint += '\n{{gb:Premi Invio per continuare.}}'

            # If the hint is not empty
            elif hint:
                hint += (
                    "\n{{gb:Controlla}} {{yb:" + str(num_people) +
                    "}} {{gb:altr}}"
                )
                if num_people > 1:
                    hint += "{{gb:i.}}"
                else:
                    hint += "{{gb:o.}}"
        else:
            hint = (
                "{{rb:Usa}} {{yb:" + self.allowed_commands.keys()[0] +
                "}} {{rb:per continuare.}}"
            )

        self.send_hint(hint)

    def next(self):
        NextStep(self.xp)
