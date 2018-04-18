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

from linux_story.story.terminals.terminal_bernardo import (
    TerminalMkdirBernardo, TerminalNanoBernardo
)
from linux_story.story.challenges.challenge_28 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_cd_commands


class StepTemplateMkdir(TerminalMkdirBernardo):
    challenge_number = 27


class StepTemplateNano(TerminalNanoBernardo):
    challenge_number = 27


class Step1(StepTemplateMkdir):
    story = [
        "Sei tornato da Bernardo.",
        "{{lb:Ascolta}} cosa {{lb:Bernardo}} ha da dire."
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"

    hints = [
        "{{rb:Usa}} {{yb:cat Bernardo}} {{rb:per interagire con Bernardo.}}"
    ]

    commands = [
        "cat Bernardo"
    ]

    deleted_items = ["~/città/est/biblioteca/Eleonora"]
    story_dict = {
        "Eleonora": {
            "path": "~/città/est/negozio-capanni"
        }
    }
    eleanors_speech = (
        "Eleonora: {{Bb:Ecciuuu! Questo posto è davvero polveroso...*sniff*}}"
    )

    def next(self):
        Step2()


class Step2(StepTemplateNano):
    story = [
        "Bernardo: {{Bb:Ciaooooo. Sei tornato per riparare il mio script!}}",

        "Proviamo ad usare {{yb:nano migliore-corno-del-mondo.sh}} per "
        "modificarlo."
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"

    commands = [
        "nano migliore-corno-del-mondo.sh"
    ]

    hints = [
        "{{rb:Usa}} {{yb:nano migliore-corno-del-mondo.sh}} "
        "{{rb:per modificare lo script.}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Ci hanno insegnato come scrivere a scuola. "
        "Non penso che Bernardo sia molto intelligente.}}"
    )

    goal_nano_end_content = "echo \"Honk!\""
    goal_nano_filepath = "~/città/est/negozio-capanni/migliore-corno-del-mondo.sh"
    goal_nano_save_name = "migliore-corno-del-mondo.sh"

    # Overwrite the default behaviour for most of the steps - nano needs
    # slightly different behaviour.
    def check_command(self):
        if self.last_user_input == "cat Eleonora":
            self.send_text("\n" + self.eleanors_speech)
        else:
            return self.check_nano_input()

    def check_nano_content(self):
        return self.check_nano_content_default()

    def next(self):
        Step3()


class Step3(StepTemplateNano):
    story = [
        "E' ora di provare lo script!",
        "Usa {{yb:./migliore-corno-del-mondo.sh}} per provarlo."
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"

    commands = [
        "./migliore-corno-del-mondo.sh"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Sarà troppo a voce alta?}}"
    )
    hints = [
        "{{rb:Usa}} {{yb:./migliore-corno-del-mondo.sh}} "
        "{{rb:per provare lo script.}}"
    ]

    def next(self):
        Step4()


class Step4(StepTemplateNano):
    # Allow the user to ask all the questions within the same Step?
    story = [
        "{{gb:Congratulazioni, ora lo script stampa \"Honk!\"}}",

        "\nBernardo: {{Bb:L'attrezzo funziona! Fantastico! "
        "Grazie tante!}}",

        "\nSembra che non hai fatto a Bernardo molte domande "
        "su di lui.",

        "Vuoi fargli qualche domanda?",

        "\n{{yb:1 \"Come hai creato i tuoi attrezzi?\"}}",

        "{{yb:2: \"Qual'è il prossimo attrezzo che vorresti creare?\"}}",

        "{{yb:3: \"Stai andando a nasconderti ora?\"}}",

        "{{yb:4: \"Cosa c'è nello scantinato?\"}}",

        "\nUsa {{lb:echo}} per porgli una domanda."
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"
    hints = [
        "{{rb:Usa}} {{yb:echo 1}}{{rb:,}} {{yb:echo 2}}{{rb:,}} "
        "{{yb:echo 3}} {{rb:o}} {{yb:echo 4}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Ho una domanda - ha dolci nel suo "
        "scantinato?}}"
    )

    commands = [
        "echo 2"
    ]

    def check_command(self):
        if self.last_user_input == "echo 1":
            text = (
                "\nBernardo: {{Bb:Ah, segreti del mestiere. *wink*}}"
            )
            self.send_text(text)
        elif self.last_user_input == "echo 3":
            text = (
                "\nBernard: {{Bb:\"Eh, come? No, non stavo pianificando "
                "ciò. Perchè dovrei farlo?\"}}"
            )
            self.send_text(text)
        elif self.last_user_input == "echo 4":
            text = (
                "\nBernardo: {{Bb:Oh ho ho ho, non sono cose che ti riguardano.}}"
            )
            self.send_text(text)
        else:
            return StepTemplateNano.check_command(self)

    def next(self):
        Step5()


class Step5(StepTemplateNano):
    print_text = [
        "{{yb:\"Qual'è il prossimo attrezzo che vuoi creare?\"}}"
    ]

    story = [
        "Bernardo: {{Bb:Vorrei conoscere come l'}} "
        "{{lb:ala-privata}} {{Bb:è chiusa "
        "nella}} {{lb:biblioteca}}{{Bb:, e dopo fare una chiave "
        "per aprirla.}}",

        "\nEleonora: {{Bb:Io penso che sia stata la bibliotecaria a chiudere "
        "l'ala-privata.}}",

        "{{Bb:Forse potrebbe dirci come ci è riuscita! Dovremo andare a "
        "cercarla.}}",

        "\n{{lb:Lascia}} il negozio-capanni."
    ]

    hints = [
        "{{rb:Usa}} {{lb:cd}} {{rb:per lasciare il negozio-capanni.}}",
        "{{rb:Usa}} {{yb:cd ../}} {{rb:per tornare}} {{lb:indietro}} {{rb:alla città.}}",
    ]
    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est"
    eleanors_speech = (
        "Eleonora: {{Bb:Cosa pensi che sia nascosto nell'ala-privata?}}"
        "\n{{Bb:Forse Bernardo non dovrebbe vederlo...}}"
    )
    last_step = True

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        NextStep(self.xp)
