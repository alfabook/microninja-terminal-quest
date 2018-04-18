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

from linux_story.step_helper_functions import unblock_cd_commands
from linux_story.story.terminals.terminal_mkdir import TerminalMkdir
from linux_story.helper_functions import play_sound
from linux_story.story.challenges.challenge_23 import Step1 as NextStep


class StepTemplateMkdir(TerminalMkdir):
    challenge_number = 22


class Step1(StepTemplateMkdir):
    story = [
        "{{gb:Ottimo lavoro, sembra che siano tutti qui!}}",
        "\nRuth: {{Bb:Grazie tanto!}}",
        "{{Bb:Resteremo qua e staremo al sicuro. Ti sono grata per tutto "
        "quello che hai fatto.}}",
        "\nUsa {{lb:cat}} per controllare se gli animali sono felici qua."
    ]

    start_dir = "~/fattoria/fienile/.rifugio"
    end_dir = "~/fattoria/fienile/.rifugio"

    commands = [
        "cat Margherita",
        "cat Trotter",
        "cat Cobweb"
    ]
    hints = [
        "{{rb:Usa}} {{lb:cat}} {{rb:per esaminare un animale, esempio:}} "
        "{{yb:cat Margherita}}{{rb:.}}"
    ]

    # Remove all the food
    deleted_items = [
        "~/città/.rifugio-nascosto/cesto",
        "~/città/.rifugio-nascosto/mela"
    ]

    def next(self):
        play_sound("bell")
        Step2()


class Step2(StepTemplateMkdir):
    story = [
        "{{pb:Ding. Dong.}}",
        "Ruth: {{Bb:Cosa?? Ho sentito una campana! Cosa significa?}}",
        "\nRapido! {{lb:guarda attorno}} e controlla se manca qualcuno."
    ]

    start_dir = "~/fattoria/fienile/.rifugio"
    end_dir = "~/fattoria/fienile/.rifugio"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Guarda attorno con}} {{yb:ls}}{{rb:.}}"
    ]

    # Remove Edith
    deleted_items = [
        "~/città/.rifugio-nascosto/Edith"
    ]

    def next(self):
        play_sound("bell")
        Step3()


class Step3(StepTemplateMkdir):
    story = [
        "Sembra che tutti siano ancora qua...",
        "\n{{pb:Ding. Dong.}}",
        "\nRuth: {{Bb:L'ho sentita ancora! E' questo il suono che hai sentito "
        "quando è scomparso mio marito?}}",
        "Dai un altro rapido {{lb:sguardo attorno}}."
    ]

    start_dir = "~/fattoria/fienile/.rifugio"
    end_dir = "~/fattoria/fienile/.rifugio"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Guarda attorno con}} {{yb:ls}}{{rb:.}}"
    ]
    # Remove Edoardo
    deleted_items = [
        "~/città/.rifugio-nascosto/Edoardo"
    ]

    def next(self):
        play_sound("bell")
        Step4()


# TODO: FIX THIS STEP
class Step4(StepTemplateMkdir):
    story = [
        "Ruth: {{Bb:Va tutto bene. Siamo al sicuro, siamo ancora tutti qua. "
        "Mi chiedo proprio perché suona!}}",
        "\nForse dovremo investigare su questo suono. Chi conosciamo "
        "per poterci aiutare?",
        "Forse dovresti tornare alla famiglia nel "
        "{{lb:.rifugio-nascosto}} e parlargli, con la tua nuova voce echo!",

        "\nComincia a ridirigerti verso il {{lb:.rifugio-nascosto}} con {{lb:cd}}."
    ]

    start_dir = "~/fattoria/fienile/.rifugio"
    end_dir = "~/città/.rifugio-nascosto"

    hints = [
        "{{rb:Possiamo andare direttamente al}} {{lb:.rifugio-nascosto}} "
        "{{rb:usando}} {{yb:cd ~/città/.rifugio-nascosto/}}"
    ]

    # Remove the dog
    deleted_items = [
        "~/città/.rifugio-nascosto/cane"
    ]

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def check_command(self):
        # If the command passes, then print a nice hint.
        if self.last_user_input.startswith("cd") and \
                not self.get_command_blocked() and \
                not self.current_path == self.end_dir:
            hint = "\n{{gb:Ottimo! Continua così!}}"
            self.send_text(hint)
        else:
            return StepTemplateMkdir.check_command(self)

    def next(self):
        Step5()


class Step5(StepTemplateMkdir):
    story = [
        "Dai uno {{lb:sguardo attorno}}."
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
