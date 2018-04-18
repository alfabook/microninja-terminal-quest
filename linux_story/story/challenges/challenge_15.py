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
from linux_story.story.challenges.challenge_16 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_commands_with_cd_hint


class StepTemplateMv(TerminalMv):
    challenge_number = 15


class Step1(StepTemplateMv):
    story = [
        "Hai l'assillante sensazione di aver dimenticato qualcosa.",
        "Qual'era la magia che ti aveva permesso di trovare questo posto?",
        "Usala nuovamente per {{lb:guardare meglio attorno}}.\n"
    ]
    hints = [
        "{{rb:Usa}} {{yb:ls -a}} {{rb:per guardare meglio attorno.}}"
    ]

    story_dict = {
        "CAT, LS, CD, .nota": {
            "path": "~/casa-mia/camera-mia/.scrigno"
        }
    }

    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "ls -a"
    ]

    def next(self):
        Step2()


class Step2(StepTemplateMv):
    story = [
        "Cos'è questo! C'è un {{lb:.minuscolo-scrigno}} in un angolo del rifugio",
        "Dai uno {{lb:sguardo dentro}} il {{lb:.minuscolo-scrigno}}."
    ]

    hints = [
        "{{rb:Usa}} {{yb:ls .minuscolo-scrigno}} {{rb:per guardare dentro}}"
    ]

    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "ls .minuscolo-scrigno",
        "ls .minuscolo-scrigno/",
        "ls -a .minuscolo-scrigno",
        "ls -a .minuscolo-scrigno/"
    ]

    def next(self):
        Step3()


class Step3(StepTemplateMv):
    story = [
        "Vedi un rotolo di pergamena dentro, con delle scritte che dicono "
        "{{lb:MV}}.",
        "{{lb:Leggi}} cosa dice."
    ]

    hints = [
        "{{rb:Usa}} {{yb:cat .minuscolo-scrigno/MV}} {{rb:per leggere la pergamena MV}}"
    ]

    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "cat .minuscolo-scrigno/MV"
    ]

    def next(self):
        Step4()


class Step4(StepTemplateMv):
    story = [
        "{{wb:Edoardo:}} {{Bb:\"Hey, è il nostro}} {{lb:.minuscolo-scrigno}}{{Bb:. Noi "
        "lo usiamo per tenere al sicuro i nostri averi. ",
        "Ho imparato come muovere gli oggetti da questa}} {{Bb:MV}} "
        "{{Bb:pergamena.",
        "Sarà probabilmente più d'aiuto a te, prendila coi miei ringraziamenti.}}",
        "\nForse dovresti tornare indietro a {{lb:casa-mia}} per guardare per altri "
        "oggetti nascosti.",
        "Per tornare rapidamente a casa, usa {{yb:cd ~/casa-mia/}}\n"
    ]

    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/casa-mia"
    commands = [
        'cd ~/casa-mia/',
        'cd ~/casa-mia'
    ]
    hints = [
        '{{rb:Nessuna scorciatoia! Usa}} {{yb:cd ~/casa-mia}} '
        '{{rb:per tornare a casa con un solo passo.}}'
    ]

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step5()


class Step5(StepTemplateMv):
    story = [
        "Vediamo se troviamo qualcosa, nascosto qua attorno!",
        "Dove pensi che potresti trovare oggetti nascosti?",
        "Prova {{lb:guardando attentamente}} in {{lb:camera-mia}} per prima cosa."
    ]

    start_dir = '~/casa-mia'

    hints = [
        "{{rb:Bloccato? Dai uno sguardo in}} {{yb:camera-mia}}{{rb:.}}",
        "{{rb:Usa}} {{yb:ls -a camera-mia}} {{rb:per cercare file nascosti in}} "
        "{{lb:camera-mia}}{{rb:.}}"
    ]

    last_step = True

    def check_output(self, output):
        # Need to check that .scrigno is shown in the output of the command
        if not output:
            return False

        if '.scrigno' in output:
            return True

        return False

    def next(self):
        NextStep(self.xp)
