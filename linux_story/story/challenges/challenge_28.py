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

from linux_story.story.terminals.terminal_bernardo import TerminalNanoBernardo
from linux_story.story.challenges.challenge_29 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_cd_commands


class StepTemplateNano(TerminalNanoBernardo):
    challenge_number = 28


class Step1(StepTemplateNano):
    story = [
        "Sei tornato in città. Eleonora sembra sollevata stando fuori.",
        "Dove pensi che si nasconda la bibliotecaria?",
        "{{lb:Guarda attorno}} per decidere dove andare."
    ]

    start_dir = "~/città/est"
    end_dir = "~/città/est"

    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    ]

    deleted_items = ["~/città/est/negozio-capanni/Eleonora"]
    story_dict = {
        "Eleonora": {
            "path": "~/città/est"
        }
    }

    commands = [
        "ls",
        "ls -a"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Ho fame. Vedi qualche posto dove potremo mangiare?}}"
    )

    def next(self):
        Step2()


class Step2(StepTemplateNano):
    story = [
        "Non abbiamo ancora controllato il ristorante.",
        "{{lb:Andiamo}} al {{lb:ristorante}}."
    ]

    start_dir = "~/città/est"
    end_dir = "~/città/est/ristorante"

    hints = [
        "{{rb:Usa}} {{yb:cd ristorante}} {{rb:per andare al ristorante.}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Ooh, pensi che avranno sandwich da qualche parte?}}"
    )

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step3()


class Step3(StepTemplateNano):
    story = [
        "Tu e Eleonora camminate verso il ristorante.",
        "Guarda attorno {{lb:attentamente}}."
    ]

    start_dir = "~/città/est/ristorante"
    end_dir = "~/città/est/ristorante"

    hints = [
        "Eleonora: {{Bb:Ti ricordi come mi hai trovata?"
        " Hai usato}} {{yb:ls -a}} {{Bb:giusto?}}"
    ]

    commands = [
        "ls -a"
    ]

    deleted_items = ["~/città/est/Eleonora"]
    story_dict = {
        "Eleonora": {
            "path": "~/città/est/ristorante"
        }
    }

    eleanors_speech = (
        "Eleonora: {{Bb:Semba proprio vuoto qua...}}"
    )

    def next(self):
        Step4()


class Step4(StepTemplateNano):
    story = [
        "Vedi la {{bb:.cantina}}?",
        "{{lb:Andiamo}} nella {{lb:.cantina}}."
    ]

    start_dir = "~/città/est/ristorante"
    end_dir = "~/città/est/ristorante/.cantina"

    hints = [
        "{{rb:Vai nella cantina usando}} {{yb:cd .cantina}}{{rb:.}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Ho paura... potresti tenermi per mano?}}"
    )

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step5()


class Step5(StepTemplateNano):
    story = [
        "Eleonora ti prende la mano, e in due camminate nella cantina.",
        "{{lb:Guarda attorno.}}"
    ]

    start_dir = "~/città/est/ristorante/.cantina"
    end_dir = "~/città/est/ristorante/.cantina"

    hints = [
        "{{rb:Guarda attorno con}} {{yb:ls}}{{rb:.}}"
    ]

    deleted_items = ["~/città/est/ristorante/Eleonora"]
    story_dict = {
        "Eleonora": {
            "path": "~/città/est/ristorante/.cantina"
        }
    }
    commands = [
        "ls",
        "ls -a"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:...c'è qualcuno la?}}"
    )

    def next(self):
        Step6()


class Step6(StepTemplateNano):
    story = [
        "Vedi una donna {{lb:Clara}} nella cantina.",
        "{{lb:Ascolta}} cosa ha da dire."
    ]

    start_dir = "~/città/est/ristorante/.cantina"
    end_dir = "~/città/est/ristorante/.cantina"

    hints = [
        "{{rb:Usa}} {{lb:cat}} {{rb:per ascoltare cosa ha da dire.}}",
        "{{rb:Usa}} {{yb:cat Clara}} {{rb:per ascoltare Clara.}}"
    ]

    commands = [
        "cat Clara"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:...oh! Penso di aver riconosciuto quella donna!}}"
    )

    last_step = True

    def next(self):
        NextStep(self.xp)
