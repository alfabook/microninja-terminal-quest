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
from linux_story.story.challenges.challenge_14 import Step1 as NextStep
from linux_story.step_helper_functions import (
    unblock_commands_with_cd_hint, unblock_commands
)


class StepTemplateMv(TerminalMv):
    challenge_number = 13


class Step1(StepTemplateMv):
    story = [
        "{{wb:Edoardo:}} {{Bb:\"Grazie tantissime per aver salvato la mia bambina!",
        "Avrei un altro favore da chiederti...",

        "Non abbiamo più cibo. Potresti trovarci qualcosa? "
        "Non abbiamo avuto il tempo di procurarcelo prima di nasconderci.\"",

        "\"Ricordi di aver visto del cibo durante questi viaggi?\"}}",

        "\n...ah! C'era tutto quel cibo in {{bb:cucina}}! "
        "Potremo darlo a questa famiglia.",

        "\nComincia {{lb:spostando}} il {{lb:cesto}} verso {{lb:~}}. "
        "Usa il comando {{yb:mv cesto ~/}}\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "mv cesto ~",
        "mv cesto/ ~",
        "mv cesto ~/",
        "mv cesto/ ~/",
        "mv cesto ../..",
        "mv cesto/ ../..",
        "mv cesto ../../",
        "mv cesto/ ../../"
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:mv cesto ~/}} "
        "{{rb:per spostare il}} {{lb:cesto}} {{rb:verso la strada ventosa}} {{lb:~}}"
    ]

    def block_command(self):
        return unblock_commands(self.last_user_input, self.commands)

    def next(self):
        Step2()


class Step2(StepTemplateMv):
    story = [
        "Ora segui il cesto. Usa {{yb:cd}} da solo "
        "per {{lb:spostarti}} verso la strada ventosa Tilde ~.\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~"
    commands = [
        "cd",
        "cd ~",
        "cd ~/"
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:cd}} {{rb:da solo "
        "per muoverti verso la strada ~}}"
    ]

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step3()


class Step3(StepTemplateMv):
    story = [
        "Sei ritornato alla strada ventosa. {{lb:Guarda attorno}} "
        "con {{yb:ls}} per accertarti di avere il cesto con te.\n"
    ]

    start_dir = "~"
    end_dir = "~"
    commands = [
        "ls"
    ]
    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:da solo "
        "per guardare attorno.}}"
    ]

    def next(self):
        Step4()


class Step4(StepTemplateMv):
    story = [
        "Hai il cesto con te, e "
        "vedi {{bb:casa-mia}} avvicinarsi.",
        "Sposta il {{lb:cesto}} verso {{lb:casa-mia/cucina}}.",
        "Non dimenticare che puoi usare il tasto TAB per completare automaticamente i comandi.\n"
    ]

    start_dir = "~"
    end_dir = "~"
    commands = [
        "mv cesto casa-mia/cucina",
        "mv cesto/ casa-mia/cucina",
        "mv cesto casa-mia/cucina/",
        "mv cesto/ casa-mia/cucina/",
        "mv cesto ~/casa-mia/cucina",
        "mv cesto/ ~/casa-mia/cucina",
        "mv cesto ~/casa-mia/cucina/",
        "mv cesto/ ~/casa-mia/cucina/"
    ]
    hints = [
        "{{rb:Usa}} {{yb:mv cesto casa-mia/cucina/}} "
        "{{rb:per spostare il cesto verso la tua cucina.}}",
    ]

    def block_command(self):
        return unblock_commands(self.last_user_input, self.commands)

    def next(self):
        Step5()


class Step5(StepTemplateMv):
    story = [
        "Ora {{lb:vai}} dentro {{lb:casa-mia/cucina}} con {{lb:cd}}.\n",
    ]

    start_dir = "~"
    end_dir = "~/casa-mia/cucina"
    commands = [
        "cd casa-mia/cucina",
        "cd casa-mia/cucina/",
        "cd ~/casa-mia/cucina",
        "cd ~/casa-mia/cucina/"
    ]
    hints = [
        "{{rb:Usa}} {{yb:cd casa-mia/cucina/}} "
        "{{rb:per andare verso la cucina.}}",
    ]
    last_step = True

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        NextStep(self.xp)
