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

import time
from linux_story.story.terminals.terminal_nano import TerminalNano
from linux_story.step_helper_functions import unblock_cd_commands


class StepTemplateNano(TerminalNano):
    challenge_number = 31


class Step1(StepTemplateNano):
    story = [
        "Sei arrivato al negozio-capanni. {{lb:Guarda intorno.}}"
    ]
    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    ]

    def next(self):
        Step2()


class Step2(StepTemplateNano):
    story = [
        "Huh, non puoi vedere Bernardo da nessuna parte.",

        "Mi chiedo dove sia andato.",

        "Forse è nel suo {{lb:scantinato}}? {{lb:Andiamo}} dentro."
    ]
    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni/scantinato"
    hints = [
        "{{rb:Vai nello scantinato con}} {{yb:cd scantinato/}}"
    ]

    def check_command(self):
        if self.last_user_input == "cat cappello-bernardo":
            self.send_text(
                "\nE' il cappello di Bernardo? "
                "Strano che l'abbia lasciato la..."
            )
        else:
            return TerminalNano.check_command(self)

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step3()


class Step3(StepTemplateNano):
    story = [
        "Cammini nello scantinato di Bernardo. {{lb:Guarda attorno.}}"
    ]
    start_dir = "~/città/est/negozio-capanni/scantinato"
    end_dir = "~/città/est/negozio-capanni/scantinato"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Guarda attorno con}} {{yb:ls}}{{rb:.}}"
    ]

    def next(self):
        Step4()


class Step4(StepTemplateNano):
    story = [
        "Vedi quello che sembra un altro attrezzo e un paio di diari.",
        "{{lb:Esaminiamoli}}."
    ]
    start_dir = "~/città/est/negozio-capanni/scantinato"
    end_dir = "~/città/est/negozio-capanni/scantinato"
    commands = [
        "cat diario-bernardo-1",
        "cat diario-bernardo-2",
        "cat fotocopiatrice.sh"
    ]
    hints = [
        "{{rb:Usa}} {{lb:cat}} {{rb:per esaminare gli oggetti.}}"
    ]

    def check_command(self):
        if self.last_user_input in self.commands:
            self.commands.remove(self.last_user_input)

            if not self.commands:
                text = (
                    "\n{{gb:Premi Invio per continuare.}}"
                )
                self.send_text(text)

            else:
                text = (
                    "\n{{gb:Ottimo! Guarda gli altri oggetti!.}}"
                )
                self.send_text(text)

        elif not self.last_user_input and not self.commands:
            return True

        else:
            return StepTemplateNano.check_command(self)

    def next(self):
        Step5()


class Step5(StepTemplateNano):
    story = [
        "Basta camminare qua. Andiamo a cercare di trovare lo "
        "{{lb:spadaccino mascherato}} nei boschi, e vediamo che "
        "informazioni ci può dare.",
        "\n{{gb:Premi Invio per continuare.}}"
    ]
    start_dir = "~/città/est/negozio-capanni/scantinato"
    end_dir = "~/città/est/negozio-capanni/scantinato"
    last_step = True

    def next(self):
        self.exit()

        time.sleep(3)
