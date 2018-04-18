#!/usr/bin/env python
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU Gpl v2
#
# A chapter of the story

# -*- coding: utf-8 -*-

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# Italian translation
# rebadged with microninja

from linux_story.step_helper_functions import (
    unblock_commands_with_mkdir_hint, unblock_cd_commands
)
from linux_story.story.terminals.terminal_echo import TerminalEcho
from linux_story.story.terminals.terminal_mkdir import TerminalMkdir
from linux_story.story.challenges.challenge_21 import Step1 as NextStep


class StepTemplateEcho(TerminalEcho):
    challenge_number = 20


class StepTemplateMkdir(TerminalMkdir):
    challenge_number = 20


class Step1(StepTemplateEcho):
    print_text = [
        "{{yb:\"Alcune persone sono sopravvissute nascondendosi.\"}}"
    ]
    story = [
        "Ruth: {{Bb:Oh! Questo mi fa pensare, mio marito "
        "costruiva rifugi speciali per conservare il raccolto durante tutto l'inverno. "
        "Penso abbia usato un attrezzo specifico. "
        "Dovremo dare uno sguardo nel suo capanno degli attrezzi per vedere se possiamo trovarlo.}}",
        "\nUsa il comando {{lb:cd}} per andare nel capanno degli attrezzi.\n"
    ]

    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/capanno-attrezzi"
    hints = [
        "{{rb:Vai al capanno-attrezzi in un passo"
        " con}} {{yb:cd ../capanno-attrezzi/}}"
    ]

    path_hints = {
        "~/fattoria/fienile": {
            "blocked": "\n{{rb:Usa}} {{yb:cd ../}} {{rb:per tornare indietro.}}"
        },
        "~/fattoria": {
            "not_blocked": "\n{{gb:Ottimo lavoro! ora vai al}} {{lb:capanno-attrezzi}}{{gb:.}}",
            "blocked": "\n{{rb:Usa}} {{yb:cd capanno-attrezzi/}} {{rb:per andare al capanno-attrezzi.}}"
        }
    }

    def check_command(self):
        if self.current_path == self.end_dir:
            return True
        elif "cd" in self.last_user_input and not self.get_command_blocked():
            hint = self.path_hints[self.current_path]["not_blocked"]
        else:
            hint = self.path_hints[self.current_path]["blocked"]

        self.send_text(hint)

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step2()


class Step2(StepTemplateEcho):
    story = [
        "Ruth ti segue dentro il {{bb:capanno-attrezzi}}. E' un larghissimo "
        "spazio con attrezzi disposti lungo il muro.",
        "Ruth: {{Bb:Bene!}} {{lb:Guarda attorno}} {{Bb:per "
        "qualunque cosa possa essere utile.}}\n"
    ]
    start_dir = "~/fattoria/capanno-attrezzi"
    end_dir = "~/fattoria/capanno-attrezzi"
    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    ]
    commands = [
        "ls",
        "ls -a",
        "ls .",
        "ls ./",
        "ls -a .",
        "ls -a ./"
    ]
    # Move Ruth into capanno-attrezzi
    story_dict = {
        "Ruth": {
            "path": "~/fattoria/capanno-attrezzi"
        }
    }
    deleted_items = ["~/fattoria/fienile/Ruth"]

    def next(self):
        Step3()


class Step3(StepTemplateEcho):
    story = [
        "Ruth: {{Bb:Ah, guarda! ci sono delle istruzioni "
        "sotto}} {{lb:MKDIR}}{{Bb:.}}",
        "{{Bb:Cosa dicono?}}",
        "\n{{lb:Esamina}} le istruzioni {{lb:MKDIR}}."
    ]
    hints = [
        "Ruth: {{Bb:\"...sei in grado di leggere, giusto? Usa}} {{lb:cat}} "
        "{{Bb:per leggere.\"}}",
        "Ruth: {{Bb:\"Cosa imparate voi bambini nelle scuole di oggi...\""
        "\n\"Basta usare}} {{yb:cat MKDIR}} {{Bb:per leggere il foglio.\"}}",
        "{{rb:Usa}} {{yb:cat MKDIR}} {{rb:per leggere.}}"
    ]
    start_dir = "~/fattoria/capanno-attrezzi"
    end_dir = "~/fattoria/capanno-attrezzi"
    commands = "cat MKDIR"

    def next(self):
        Step4()


class Step4(StepTemplateMkdir):
    story = [
        "Ruth: {{Bb:Questo dice che puoi costruire usando qualcosa "
        "chiamato}} {{lb:mkdir}}{{Bb:?}}",
        "\n{{gb:Proviamo a fare un igloo con}} {{yb:mkdir igloo}}"
    ]
    hints = [
        "{{rb:Crea un igloo usando}} {{yb:mkdir igloo}}\n"
    ]
    start_dir = "~/fattoria/capanno-attrezzi"
    end_dir = "~/fattoria/capanno-attrezzi"
    commands = [
        "mkdir igloo"
    ]

    def block_command(self):
        return unblock_commands_with_mkdir_hint(
            self.last_user_input, self.commands
        )

    def check_command(self):
        if self.last_user_input == "cat MKDIR":
            self.send_hint("\n{{gb:Ottimo lavoro controllare ancora la pagina!}}")
            return False

        return StepTemplateMkdir.check_command(self)

    def next(self):
        Step5()


class Step5(StepTemplateMkdir):
    story = [
        "Ora dai uno {{lb:sguardo attorno}} e vediamo cosa è cambiato."
    ]
    start_dir = "~/fattoria/capanno-attrezzi"
    end_dir = "~/fattoria/capanno-attrezzi"
    commands = [
        "ls",
        "ls -a",
        "ls .",
        "ls ./"
    ]
    hints = [
        "{{rb:Guarda attorno usando}} {{yb:ls}}{{rb:.}}"
    ]
    last_step = True

    def next(self):
        NextStep(self.xp)
