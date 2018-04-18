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
from linux_story.story.terminals.terminal_cat import TerminalCat
from linux_story.story.challenges.challenge_4 import Step1 as NextChallengeStep


class StepTemplateCat(TerminalCat):
    challenge_number = 3


class Step1(StepTemplateCat):
    story = [
        "Amorevole! Indossalo rapidamente.",
        "C'è altra roba molto interessante nella tua camera.",
        "{{lb:Guarda}} nei tuoi {{lb:scaffali}} con {{lb:ls}}.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = ["ls scaffali", "ls scaffali/"]
    hints = "{{rb:Digita}} {{yb:ls scaffali/}} {{rb:per osservare i tuoi libri.}}"

    def next(self):
        Step2()


class Step2(StepTemplateCat):
    story = [
        "Sai che puoi usare il tasto TAB per velocizzare la digitazione?",
        "Prova controllando quei fumetti. {{lb:Esaminali}} con "
        "{{yb:cat scaffali/fumetti}}",
        "Premi il tasto TAB prima di finire di digitare!\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = "cat scaffali/fumetti"
    hints = "{{rb:Digita}} {{yb:cat scaffali/fumetti}} {{rb:per leggere i fumetti}}"

    def next(self):
        Step3()


class Step3(StepTemplateCat):
    story = [
        "Perchè è coperta da impronte?",
        "Aspetta, hai visto? C'è una {{lb:nota}} tra i tuoi libri.",
        "{{lb:Leggi}} la nota con {{lb:cat}}.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = "cat scaffali/nota"
    hints = "{{rb:Digita}} {{yb:cat scaffali/nota}} {{rb:per leggere la nota.}}"

    last_step = True

    def next(self):
        NextChallengeStep(self.xp)
