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
from linux_story.story.challenges.challenge_6 import Step1 as NextChallengeStep
from linux_story.step_helper_functions import unblock_commands_with_cd_hint


class StepTemplateCd(TerminalCd):
    challenge_number = 5


class Step1(StepTemplateCd):
    story = [
        "{{wb:Mamma:}} {{Bb:\"Ciao testa assonnata, la colazione è quasi pronta. "
        " Puoi andare a cercare papà?"
        " Penso sia nel}} {{bb:giardino}}{{Bb:.\"}}\n",
        "Ok, cerchiamo papà nel {{bb:giardino}}.",
        "Prima di tutto dobbiamo {{lb:lasciare}} la cucina con {{yb:cd ../}}\n"
    ]
    start_dir = "~/casa-mia/cucina"
    end_dir = "~/casa-mia"
    commands = ["cd ..", "cd ../"]
    hints = "{{rb:Per lasciare la cucina, digita}} {{yb:cd ../}}"

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step2()


class Step2(StepTemplateCd):
    story = [
        "Sei tornato nell'andito principale di casa tua.",
        "Puoi vedere il {{bb:giardino}}? Dai uno {{lb:sguardo}} attorno.\n"
    ]
    start_dir = "~/casa-mia"
    end_dir = "~/casa-mia"
    commands = "ls"
    hints = "{{rb:Digita}} {{yb:ls}} {{rb:per guardare attorno.}}"

    def next(self):
        Step3()


class Step3(StepTemplateCd):
    story = [
        "Vedi le porte per il {{bb:giardino}}, la {{bb:cucina}}, la "
        "{{bb:camera-mia}} e {{bb:camera-genitori}}.",
        "{{lb:Vai}} verso il {{bb:giardino}}.\n"
    ]
    start_dir = "~/casa-mia"
    end_dir = "~/casa-mia/giardino"
    commands = ["cd giardino", "cd giardino/"]
    hints = "{{rb:Digita}} {{yb:cd giardino/}} {{rb:per andare nel giardino.}}"

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step4()


class Step4(StepTemplateCd):
    story = [
        "Usa {{yb:ls}} per {{lb:guardare}} se in giardino c'è papà.\n"
    ]
    start_dir = "~/casa-mia/giardino"
    end_dir = "~/casa-mia/giardino"
    commands = "ls"
    hints = (
        "{{rb:Per guardare per papà, digita}} {{yb:ls}} {{rb:e premi "
        "Invio.}}"
    )

    def next(self):
        Step5()


class Step5(StepTemplateCd):
    story = [
        "Il giardino {{bb:giardino}} appare bellissimo in questo periodo dell'anno.",
        "Hmmm... Ma non vedo papà da nessuna parte.",
        "Forse è nella {{bb:serra}}.",
        "\n{{lb:Vai}} dentro la {{lb:serra}}.\n"
    ]
    start_dir = "~/casa-mia/giardino"
    end_dir = "~/casa-mia/giardino/serra"
    commands = ["cd serra", "cd serra/"]
    hints = "{{rb:Per andare nella serra, digita}} {{yb:cd serra/}}"

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step6()


class Step6(StepTemplateCd):
    story = [
        "E' li? {{lb:Guarda attorno}} con {{yb:ls}} per scoprirlo.\n"
    ]
    start_dir = "~/casa-mia/giardino/serra"
    end_dir = "~/casa-mia/giardino/serra"
    commands = "ls"
    hints = "{{rb:Digita}} {{yb:ls}} {{rb:per cercare papà.}}"

    def next(self):
        Step7()


class Step7(StepTemplateCd):
    story = [
        "Il tuo papà è stato occupato, ci sono molti ortaggi li.",
        "Hmmmm. Non è qui. Ma c'è qualcosa di strano.",
        "Vedi una nota per terra.  Usa {{yb:cat nota}} per "
        "{{lb:leggere}} cosa dice.\n"
    ]
    start_dir = "~/casa-mia/giardino/serra"
    end_dir = "~/casa-mia/giardino/serra"
    commands = "cat nota"
    hints = "{{rb:Digita}} {{yb:cat nota}} {{rb:per vedere cosa dice la nota!}}"

    def next(self):
        Step8()


class Step8(StepTemplateCd):
    story = [
        "Tornare indietro è facilissimo. Basta digitare {{yb:cd ../}} per tornare "
        "da dove sei venuto.\n"
    ]
    start_dir = "~/casa-mia/giardino/serra"
    end_dir = "~/casa-mia/giardino"
    commands = ["cd ..", "cd ../"]
    hints = "{{rb:Digita}} {{yb:cd ../}} {{rb:per tornare nel giardino.}}"

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step9()


class Step9(StepTemplateCd):
    story = [
        "Sei tornato nel giardino. Usa {{yb:cd ../}} ancora per"
        " {{lb:tornare indietro}} alla casa.",
        "{{gb:Super consiglio: Premi il tasto SU per ripetere il tuo comando precedente.}}\n"
    ]
    start_dir = "~/casa-mia/giardino"
    end_dir = "~/casa-mia"
    commands = ["cd ..", "cd ../"]
    hints = "{{rb:Digita}} {{yb:cd ../}} {{rb:per tornare alla casa.}}"

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step10()


class Step10(StepTemplateCd):
    story = [
        "Adesso {{lb:vai}} indietro nella {{bb:cucina}} e cerca mamma.\n"
    ]
    start_dir = "~/casa-mia"
    end_dir = "~/casa-mia/cucina"
    commands = ["cd cucina", "cd cucina/"]
    hints = "{{rb:Digita}} {{yb:cd cucina/}} {{rb:per tornare alla cucina.}}"

    last_step = True

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        NextChallengeStep(self.xp)
