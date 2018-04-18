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

from linux_story.story.terminals.terminal_cat import TerminalCat
from linux_story.story.challenges.challenge_3 import Step1 as NextChallengeStep
from microninja_profile.apps import save_app_state_variable


class StepCat(TerminalCat):
    challenge_number = 2


class Step1(StepCat):
    story = [
        "Fantastico, ora puoi vedere gli oggetti attorno a te.",
        "C'è il tuo letto, una sveglia...",
        "Euuughh... spegni quella sveglia!",
        "\n{{gb:Nuova magia}}: per {{lb:esaminare}} oggetti, digita {{lb:cat}} "
        "e il nome dell'oggetto.",
        "\nUsa {{yb:cat sveglia}} per {{lb:esaminare}} la sveglia.\n",

    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = "cat sveglia"
    hints = "{{rb:Digita}} {{yb:cat sveglia}} {{rb:per esaminare la sveglia.}}"

    def next(self):
        Step2()


class Step2(StepCat):
    story = [
        "Ok - è spenta. Meglio vestirsi...",

        "Digita {{yb:ls guardaroba/}} per {{lb:guardare dentro}} il tuo "
        "{{lb:guardaroba}}.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = ["ls guardaroba", "ls guardaroba/"]
    hints = (
        "{{rb:Digita}} {{yb:ls guardaroba/}} {{rb:per cercare qualcosa "
        "da indossare.}}"
    )

    def next(self):
        Step3()


class Step3(StepCat):
    story = [
        "Controlla quella {{lb:maglietta}}!",
        "{{lb:Esamina}} la maglietta con {{yb:cat guardaroba/maglietta}} "
        "per vedere come appare.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = "cat guardaroba/maglietta"
    hints = (
        "{{rb:Digita}} {{yb:cat guardaroba/maglietta}} "
        "{{rb:per esaminarne l'aspetto.}}"
    )

    def next(self):
        Step4()


class Step4(StepCat):
    story = [
        "Proprio bella! Indossala e guarda anche gli altri vestiti.",
        "{{lb:Esamina}} la {{lb:maglietta}} o i {{lb:pantaloni}}.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = [
        "cat guardaroba/gonna",
        "cat guardaroba/pantaloni"
    ]
    hints = (
        "{{rb:Digita}} {{yb:cat guardaroba/pantaloni}} {{rb:o}} "
        "{{yb:cat guardaroba/gonna}} {{rb:per vestirti.}}"
    )
    checked_outside_wardrobe = False

    def check_command(self):
        if self.last_user_input == self.commands[0]:
            save_app_state_variable('linux-story', 'outfit', 'skirt')
        elif self.last_user_input == self.commands[1]:
            save_app_state_variable('linux-story', 'outfit', 'trousers')
        elif not self.checked_outside_wardrobe and \
                (self.last_user_input == "cat pantaloni" or
                 self.last_user_input == "cat gonna"):
            self.send_text(
                "\n{{rb:Devi guardare nel tuo}} {{lb:guardaroba}} "
                "{{rb:per questo oggetto.}}"
            )
            self.checked_outside_wardrobe = True

        return StepCat.check_command(self)

    def next(self):
        Step5()


class Step5(StepCat):
    story = [
        "Fantastico, hai quasi finito di vestirti.",
        "Ora, controlla questo {{lb:berretto}}.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = [
        "cat guardaroba/berretto"
    ]
    hints = (
        "{{rb:Digita}} {{yb:cat guardaroba/berretto}} {{rb:per}} "
        "{{lb:esaminare}} {{rb:il berretto.}}"
    )

    last_step = True

    def next(self):
        NextChallengeStep(self.xp)
