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
import time
import threading

dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if __name__ == '__main__' and __package__ is None:
    if dir_path != '/usr':
        sys.path.insert(1, dir_path)

from linux_story.story.terminals.terminal_cd import TerminalCd
from linux_story.story.challenges.challenge_9 import Step1 as NextChallengeStep
from linux_story.helper_functions import play_sound


class StepTemplateCd(TerminalCd):
    challenge_number = 8


class StepTemplateCdBell(StepTemplateCd):

    def play_bell_delay(self):
        time.sleep(3)
        play_sound('bell')

    def __init__(self, xp=""):
        t = threading.Thread(target=self.play_bell_delay)
        t.start()
        StepTemplateCd.__init__(self, xp)


class Step1(StepTemplateCd):

    story = [
        "{{pb:Ding. Dong.}}\n",
        "Sembra proprio la campana sentita prima.",
        "Usa {{yb:ls}} per {{lb:guardare attorno}} di nuovo."
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "ls"
    hints = "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    deleted_items = ["~/città/uomo-scontroso"]

    def __init__(self, xp=""):
        play_sound("bell")
        StepTemplateCd.__init__(self, xp)

    def next(self):
        # This was the code we had originally.  Did the bell ring properly?
        Step2()


class Step2(StepTemplateCdBell):

    story = [
        "{{wb:Bambino:}} {{Bb:Oh no! Quell'}} {{lb:uomo-scontroso}} "
        "{{Bb:con le gambe strane è scomparso!}} "
        "{{Bb:Hai sentito la campana giusto prima che scomparisse??}}",
        "{{wb:Giovane-ragazza:}} {{Bb:Ho paura...}}",
        "\n{{pb:Ding. Dong.}}\n",
        "{{wb:Giovane-ragazza:}} {{Bb:Oh! L'ho sentita di nuovo!}}",
        "\nDai uno {{lb:sguardo attorno}} per controllare."
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "ls"
    hints = "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    deleted_items = ["~/città/bambino"]

    def next(self):
        Step3()


class Step3(StepTemplateCdBell):

    story = [
        "{{wb:Giovane-ragazza:}} {{Bb:Aspetta, c'era un}} {{lb:bambino}} "
        "{{Bb:qua... giusto?",
        "Ogni volta che la campana suona, qualcuno scompare!}}",
        "{{wb:Sindaco:}} {{Bb:Forse hanno semplicemente deciso di tornare a casa...?}}",
        "\n{{pb:Ding. Dong.}}\n",
        "{{lb:Guarda attorno.}}"
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "ls"
    hints = "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    deleted_items = ["~/città/giovane-ragazza"]

    def next(self):
        Step4()


class Step4(StepTemplateCd):

    story = [
        "Sei da solo con il Sindaco.",
        "{{lb:Ascolta}} cosa ha da dire il Sindaco ."
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "cat Sindaco"
    hints = "{{rb:Usa}} {{yb:cat Sindaco}} {{rb:per parlare al Sindaco.}}"

    def next(self):
        Step5()


class Step5(StepTemplateCdBell):

    story = [
        "{{wb:Sindaco:}} {{Bb:\"Tutti... sono scomparsi??\"",
        "....Dovrei andare a casa ora...}}",
        "\n{{pb:Ding. Dong.}}\n"
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "ls"
    hints = "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    deleted_items = ["~/città/Sindaco"]
    story_dict = {
        "nota_città": {
            "name": "nota",
            "path": "~/città"
        }
    }

    def next(self):
        Step6()


class Step6(StepTemplateCd):
    story = [
        "Non c'è più nessuno.",
        "Aspetta - c'è una nota per terra.",
        "Usa {{lb:cat}} per leggere la nota."
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "cat nota"
    hints = "{{rb:Usa}} {{yb:cat nota}} {{rb:per leggere la nota.}}"
    last_step = True

    def next(self):
        NextChallengeStep(self.xp)
