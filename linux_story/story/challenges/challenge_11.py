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

from linux_story.story.terminals.terminal_cd import TerminalCd

# Change this import statement, need to decide how to group the terminals
# together
from linux_story.story.terminals.terminal_mv import TerminalMv
from linux_story.story.challenges.challenge_12 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_commands
from linux_story.common import tq_file_system


class StepTemplateCd(TerminalCd):
    challenge_number = 11


class StepTemplateMv(TerminalMv):
    challenge_number = 11


# The next few steps should be like the disappearing of people in the città
class Step1(StepTemplateCd):
    story = [
        "Vedi un gruppo di persone impaurite che ti guardano, e un cane.",
        "{{lb:Ascolta}} cosa hanno da dire con {{lb:cat}}.\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"

    # Use functions here
    all_commands = {
        "cat Edith": "\n{{wb:Edith:}} {{Bb:\"Ci hai trovato! Edoardo, ti ho detto "
        "di abbassare la voce.\"}}",
        "cat Eleonora": "\n{{wb:Eleonora:}} {{Bb:\"Mia madre teme che "
        "la campana ci troverebbe se uscissimo fuori.\"}}",
        "cat Edoardo": "\n{{wb:Edoardo:}} {{Bb:\"Scusa Edith... ma "
        "non penso che intendano farci del male. Forse possono aiutarci?\"}}",
        "cat cane": "\n{{wb:Cane:}} {{Bb:\"Bau bau!\"}}"
    }

    def check_command(self):

        if not self.all_commands:
            return True

        # If they enter ls, say Well Done
        if self.last_user_input == 'ls':
            hint = "\n{{gb:Ottimo lavoro guardare attorno.}}"
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
        if self.last_user_input in self.all_commands.keys() and \
                end_dir_validated:
            # Print hint from person
            hint = "\n" + self.all_commands[self.last_user_input]

            self.all_commands.pop(self.last_user_input, None)

            if len(self.all_commands) > 0:
                hint += "\n{{gb:Ottimo lavoro! Controlla " + \
                    str(len(self.all_commands)) + \
                    " persone ancora.}}\n"
            else:
                hint += "\n{{gb:Premi Invio per continuare.}}"

            self.send_text(hint)

        else:
            self.send_text("\n" + self.hints[0])

        # Don't pass unless the user has emptied self.all_commands
        return False

    def next(self):
        Step2()


# After we've heard some of the story from all the people
class Step2(StepTemplateMv):
    story = [
        "Edoardo sembra che voglia dirti qualcosa.\n",
        "{{wb:Edoardo:}} {{Bb:\"Ciao. Potresti darmi un aiuto?\"",

        "\"Ho imparato questa magia per muovere oggetti da"
        " un posto all'altro. Ma non riesco a farla funzionare.\"",

        "\"Ho provato a muovere questa}} {{lb:mela}} {{Bb:dentro il}} "
        "{{lb:cesto}}{{Bb:\"}}",

        "{{Bb:\"Mi è stato detto che il comando era}} {{yb:mv mela cesto/}}{{Bb:\"}}",

        "{{Bb:\"Ma non capisco cosa significa. Tu lo sai? "
        "Potresti spiegarmelo?\"}}\n"
    ]

    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "mv mela cesto",
        "mv mela cesto/"
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:mv mela cesto/}} {{rb:per "
        "spostare la mela dentro il cesto.}}"
    ]
    # This is to add the mela into the virtual tree
    # we would like to integrate when using mv with the tree
    # automatically

    def block_command(self):
        return unblock_commands(self.last_user_input, self.commands)

    def next(self):
        Step3()


class Step3(StepTemplateMv):
    story = [
        "Guarda se sei riuscito a spostare la mela. {{lb:Guarda attorno}} "
        "in questa cartella.\n"
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
    story_dict = {
        "mela": {
            "path": "~/città/.rifugio-nascosto/cesto"
        }
    }

    def next(self):
        Step4()


class Step4(StepTemplateMv):
    story = [
        "{{gb:Ottimo lavoro! La mela non è più nella cartella.}}\n",
        "{{wn:Ora controlla se la mela è nel}} {{lb:cesto}} {{wn:usando}} "
        "{{lb:ls}}{{wn:.}}\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "ls cesto",
        "ls cesto/",
        "ls -a cesto",
        "ls -a cesto/"
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:ls cesto/}} {{rb:per guardare dentro il "
        "cesto.}}"
    ]

    def next(self):
        Step5()


# After cat-ing the person again?
class Step5(StepTemplateMv):
    story = [
        "{{gb:Eccellente, hai spostato la mela dentro il cesto!}}",
        "\n{{wb:Edoardo:}} {{Bb:\"Hey, ce l'hai fatta! Cosa stavo facendo "
        "di sbagliato?\"}}",
        "{{Bb:\"Puoi rispostare la mela dal cesto e riportarla qua?\"}}\n",
        "{{lb:Sposta}} la {{lb:mela}} dal {{lb:cesto}} "
        "verso la tua posizione corrente. Questo è rappresentato da {{lb:./}}",
        "Così {{yb:mv cesto/mela ./}} è il comando completo. "
        "Hai bisogno di {{lb:./}} !\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "mv cesto/mela .",
        "mv cesto/mela ./"
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:mv cesto/mela ./}} {{rb:per}} "
        "{{lb:m}}{{rb:o}}{{lb:v}}{{rb:e la mela dal cesto cesto alla tua "
        "posizione corrente}} {{lb:./}}"
    ]

    def block_command(self):
        if self.last_user_input == "mv cesto/mela":
            hint = (
                "{{gb:Quasi! Il comando completo è}} "
                "{{yb:mv cesto/mela ./}} {{gb:- non dimenticare il punto!}}"
            )
            self.send_hint(hint)
            return True
        else:
            return unblock_commands(self.last_user_input, self.commands)

    def next(self):
        Step6()


class Step6(StepTemplateMv):
    story = [
        "{{wb:Edith:}} {{Bb:\"Dovresti smetterla di giocare con quello, è l'unico cibo "
        "che ci è rimasto.\"}}",
        "{{Bb:\"Ah! Il cane corre fuori!\"}}",
        "{{wb:Eleonora:}} {{Bb:\"Cagnolinoo!\"}}",
        "{{wb:Edith:}} {{Bb:\"No! Non andare fuori!\"}}",
        "\n{{lb:Eleonora}} segue il suo {{lb:cane}} e lascia il rifugio "
        "{{lb:.rifugio-nascosto}}.",
        "{{lb:Guarda attorno}} per controllare.\n"
    ]
    story_dict = {
        "Eleonora": {
            "path": "~/città"
        },
        "cane": {
            "path": "~/città"
        }
    }
    deleted_items = [
        '~/città/.rifugio-nascosto/Eleonora',
        '~/città/.rifugio-nascosto/cane'
    ]

    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "ls", "ls -a"
    ]
    hints = [
        "{{rb:Guarda attorno usando}} {{yb:ls}} {{rb:per controllare se Eleonora è "
        "qua.}}"
    ]

    def next(self):
        Step7()


class Step7(StepTemplateMv):
    story = [
        "{{wb:Edith:}} {{Bb:\"No!! Cagnolino, torna indietro!!\"}}",
        "{{Bb:\"Ehi tu, salva la mia piccola bimba!\"}}\n",
        "Prima di tutto, {{lb:guarda attorno}} per cercare Eleonora con {{yb:ls ../}}",

    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = ""
    commands = [
        "ls ..",
        "ls ../",
        "ls ~/città",
        "ls ~/città/"
    ]
    hints = [
        "{{rb:Guarda nella cartella città usando}} {{yb:ls ../}} "
        "{{rb:oppure}} {{yb:ls ~/città/}}"
    ]

    def next(self):
        Step8()


class Step8(StepTemplateMv):
    story = [
        "Ora {{lb:sposta Eleonora}} dalla città {{lb:..}} alla "
        "tua posizione corrente {{lb:.}}\n"
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "mv ../Eleonora .",
        "mv ../Eleonora ./",
        "mv ~/città/Eleonora ~/città/.rifugio-nascosto",
        "mv ~/città/Eleonora ~/città/.rifugio-nascosto/",
        "mv ~/città/Eleonora .",
        "mv ~/città/Eleonora ./",
        "mv ../Eleonora ~/città/.rifugio-nascosto",
        "mv ../Eleonora ~/città/.rifugio-nascosto/",
    ]
    hints = [
        "{{rb:Rapido! Usa}} {{yb:mv ../Eleonora ./}} "
        "{{rb:per riportare Eleonora in sicurezza.}}"
    ]
    last_step = True
    girl_file = os.path.join(tq_file_system, 'città/.rifugio-nascosto/Eleonora')

    def block_command(self):
        return unblock_commands(self.last_user_input, self.commands)

    def check_command(self):

        if os.path.exists(self.girl_file):
            return True

        else:
            self.send_hint()
            return False

    def next(self):
        NextStep(self.xp)
