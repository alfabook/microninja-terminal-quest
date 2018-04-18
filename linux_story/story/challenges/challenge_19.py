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

if __name__ == '__main__' and __package__ is None:
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if dir_path != '/usr':
        sys.path.insert(1, dir_path)

from linux_story.story.terminals.terminal_echo import TerminalEcho
from linux_story.story.challenges.challenge_20 import Step1 as NextStep


class StepTemplate(TerminalEcho):
    challenge_number = 19


class Step1(StepTemplate):
    username = os.environ['LOGNAME']
    story = [
        "Ruth: {{Bb:Mi hai sorpreso!",
        "Ti conosco? Hai un aspetto familiare...",
        "Aspetta, sei il figlio di}} {{lb:mamma}}{{Bb:, giusto!",
        "..."
        "Esatto? Hai una lingua?",
        "Non ti chiami}} {{yb:" + username + "}}{{Bb:?}}",
        "\n{{gb:Rispondi con}} {{yb:echo si}} "
        "{{gb:oppure}} {{yb:echo no}}."
    ]

    # Story has been moved to
    hints = [
        "{{rb:Usa}} {{lb:echo}} {{rb:per rispondere alle "
        "domande.}}",
        "{{rb:Rispondi con si usando}} {{yb:echo si}}{{rb:.}}"
    ]

    commands = [
        "echo si",
        "echo Si",
        "echo SI"
    ]

    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"

    def check_command(self):

        if self.last_user_input == "echo no" or \
                self.last_user_input == "echo No" or \
                self.last_user_input == "echo NO":
            hint = (
                "Ruth: {{Bb:\"Oh non essere ridicolo, "
                "hai proprio il suo aspetto.\"}}"
            )
            self.send_hint(hint)

        return StepTemplate.check_command(self)

    def next(self):
        Step2()


class Step2(StepTemplate):
    print_text = ["{{yb:Si}}"]

    story = [
        "Ruth: {{Bb:\"Ah, lo sapevo!\"}}",
        "{{Bb:\"Quindi vivi in quella piccola casa fuori città?}}",
        # TODO: see if this can appear as a block
        # TODO: change the colour of this.
        "{{yb:1: Si}}",
        "{{yb:2: No}}",
        "{{yb:3: Non lo so}}",
        "\n{{gb:Usa}} {{yb:echo 1}}{{gb:,}} {{yb:echo 2}} {{gb:o}} "
        "{{yb:echo 3}} {{gb:per rispondere con le opzioni 1, 2 o 3.}}\n"
    ]

    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"
    commands = ["echo 1", "echo 2", "echo 3"]
    hints = [
        "{{rb:Usa}} {{yb:echo 1}}{{rb:,}} {{yb:echo 2}} {{rb:o}} "
        "{{yb:echo 3}} {{rb:per rispondere a Ruth.}}"
    ]

    def check_command(self):
        replies = {
            "echo si": "1",
            "echo no": "2",
            "echo \"non lo so\"": "3",
            "echo non lo so": "3"
        }

        if self.last_user_input.lower() in replies:
            hint = [
                "\n{{rb:Se vuoi rispondere con \"" +
                self.last_user_input +
                "\", usa}} {{yb:echo " +
                replies[self.last_user_input.lower()] +
                "}}"
            ]
            self.send_text(hint)
        else:
            return StepTemplate.check_command(self)

    def next(self):
        Step3(self.last_user_input)


# Option here to add a little exerpt where she mentions her dog was
# chasing a rabbit, and that we have to find the dog.
# We could go to the woods here, but not enter them.
class Step3(StepTemplate):
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"

    # echo 3 should NOT pass this level
    commands = [
        "echo 1",
        "echo 2"
    ]
    hints = [
        "Ruth: {{Bb:\"Come? Cosa hai detto? "
        "Tu sai come usare il comando}} {{lb:echo}} {{Bb:, esatto?\"}}",
        "{{rb:Usa}} {{yb:echo 1}}{{rb:,}} {{yb:echo 2}} {{rb:o}} "
        "{{yb:echo 3}} {{rb:per rispondere.}}"
    ]

    def __init__(self, prev_command='echo 1'):
        if prev_command == "echo 1":  # yes
            self.print_text = ["{{yb:Si}}"]
            self.story = ["Ruth: {{Bb:\"Lo sapevo!\"}}"]
        elif prev_command == "echo 2":  # no
            self.print_text = ["{{yb:No}}"]
            self.story = ["Ruth: {{Bb:Non dire bugie, lo so che lo sai.}}"]
        elif prev_command == "echo 3":  # I don't know
            self.print_text = ["{{yb:Non lo so}}"]
            self.story = ["Ruth: {{Bb:Non lo sai? Preoccupante...}}"]

        self.story = self.story + [
            "\n{{Bb:Hai fatto tutta quella strada partendo dalla città? "
            "Hai visto mio marito la?",
            "E' piuttosto}} {{lb:uomo-scontroso}}{{Bb:, stava andando "
            "in città per via di quell'incontro "
            "con il Sindaco.}}",
            "\n{{yb:1: \"Sono dispiaciuto tanto, è scomparso davanti ai miei occhi.\"}}",
            "{{yb:2: \"Non ho visto tuo marito, ma le persone "
            "scomparivano in città.\"}}",
            "{{yb:3: \"Non so nulla.\"}}",
            "\nRispondi con una delle seguenti opzioni usando "
            "{{lb:echo}} e il numero scelto.\n"
        ]
        StepTemplate.__init__(self)

    def check_command(self):
        if self.last_user_input == "echo 1":  # Disappeared in front of me
            # go to next step
            return StepTemplate.check_command(self)

        elif self.last_user_input == "echo 2":  # I didn't see him
            hint = (
                "Ruth: {{Bb:\"Uhmmm... sento che mi stai nascondendo "
                "qualcosa...\"}}"
            )
            self.send_hint(hint)
            return False

        elif self.last_user_input == "echo 3":  # I don't know anything
            hint = (
                "Ruth: {{Bb:Davvero? Sicuro di non aver visto un}} "
                "{{lb:uomo-scontroso}}{{Bb: in città?}}"
            )
            self.send_hint(hint)
            return False

        else:
            # Show default hint
            self.send_hint()
            return False

    def next(self):
        Step4()


class Step4(StepTemplate):
    print_text = [
        "{{yb:\"Sono dispiaciuto tanto, è scomparso davanti ai miei occhi.\"}}"
    ]
    story = [
        "Ruth: {{Bb:\"E' scomparso davanti ai tuoi occhi?? Oh no! "
        "Stavano proprio parlando alla radio delle persone "
        "che scomparivano... Cosa potrei fare?\"}}",
        "\n{{yb:1: \"Alcune persone sono sopravvissute nascondendosi.\"}}",
        "{{yb:2: \"Penso che dovresti andare a cercare tuo marito.\"}}\n"
    ]

    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"
    last_step = True

    commands = [
        "echo 1",
        "echo 2"
    ]

    hints = [
        "Ruth: {{Bb:Cosa hai detto? Non l'ho capito.}}",
        "{{rb:Usa}} {{yb:echo 1}} {{rb:o}} {{yb:echo 2}} {{rb:per rispondere.}}"
    ]

    def check_command(self):
        if self.last_user_input == "echo 1":  # Correct response
            # Can we asssume this is alright?
            return True
        elif self.last_user_input == "echo 2":
            response = (
                "Ruth: {{Bb:\"Dovrei, ma ho paura di scomparire anche io."
                "\nPotrebbe tornare, è meglio stare "
                "qua in caso lo facesse. Puoi farti venire in mente "
                "qualcos'altro?\"}}"
            )
            self.send_hint(response)
        else:
            self.send_hint()

    def next(self):
        NextStep(self.xp)
