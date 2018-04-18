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
from linux_story.story.challenges.challenge_8 import Step1 as NextChallengeStep


class StepTemplateCd(TerminalCd):
    challenge_number = 7


class Step1(StepTemplateCd):
    story = [
        "Dai uno {{lb:sguardo attorno}} per vedere cosa sta succedendo!"
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "ls"
    hints = "{{rb:Per guardare attorno, usa}} {{yb:ls}}"

    def next(self):
        Step2()


class Step2(StepTemplateCd):
    story = [
        "Wow, c'è tanta gente qua. Trova il {{lb:Sindaco}} e "
        "{{lb:ascolta}} cosa ha da dire."
    ]
    start_dir = "~/città"
    end_dir = "~/città"
    commands = "cat Sindaco"
    hints = "{{rb:Bloccato? Digita:}} {{yb:cat Sindaco}}"

    def next(self):
        Step3()


class Step3(StepTemplateCd):
    story = [
        "{{wb:Sindaco:}} {{Bb:\"State calmi, per favore! Abbiamo già degli investigatori "
        "che stanno indagando sulle persone scomparse, e speriamo di avere "
        "una spiegazione al più presto.\"}}\n",
        "Qualcosa di strano sta accadendo. Meglio controllare se sono tutti ok.",
        "Digita {{lb:cat}} per controllare le persone."
    ]
    start_dir = "~/città"
    end_dir = "~/città"

    # Use functions here
    command = ""
    all_commands = {
        "cat uomo-scontroso": "\n{{wb:Uomo:}} {{Bb:\"Aiuto! Non capisco cosa mi sta "
        "accadendo. Sento queste campane suonare, e ora le mie gambe sono "
        "diventate strane.\"}}",
        "cat giovane-ragazza": "\n{{wb:Ragazza:}} {{Bb:\"Puoi aiutarmi? Non riesco "
        "a trovare la mia amica Amy da nessuna parte. Se la vedi, me lo fai"
        " sapere?\"}}",
        "cat bambino": "\n{{wb:Bambino:}} {{Bb:\"Pongo? Pongo? Qualcuno "
        "ha visto il mio cane Pongo? Non era mai andato via prima d'ora...\"}}"
    }

    last_step = True

    def check_command(self):

        # If we've emptied the list of available commands, then pass the level
        if not self.all_commands:
            return True

        # If they enter ls, say Well Done
        if self.last_user_input == 'ls':
            hint = "\n{{gb:Molto bene guardarsi attorno.}}"
            self.send_text(hint)
            return False

        # check through list of commands
        end_dir_validated = False
        self.hints = [
            "{{rb:Usa}} {{yb:" + self.all_commands.keys()[0] + "}} "
            "{{rb:per continuare.}}"
        ]

        end_dir_validated = self.current_path == self.end_dir

        # if the validation is included
        if (self.last_user_input in self.all_commands.keys()) and \
                end_dir_validated:
            # Print hint from person
            hint = "\n" + self.all_commands[self.last_user_input]

            self.all_commands.pop(self.last_user_input, None)

            if len(self.all_commands) == 1:
                hint += "\n{{gb:Ben fatto! Controlla ancora 1 persona.}}\n"
            elif len(self.all_commands) > 0:
                hint += "\n{{gb:Ben fatto! Controlla ancora " + \
                    str(len(self.all_commands)) + \
                    " persone.}}\n"
            else:
                hint += "\n{{gb:Premi Invio per continuare.}}"

            self.send_text(hint)

        else:
            self.send_text("\n" + self.hints[0])

        # Always return False unless the list of valid commands have been
        # emptied
        return False

    def next(self):
        NextChallengeStep(self.xp)
