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
from linux_story.story.terminals.terminal_eleonora import TerminalMkdirEleonora
from linux_story.story.challenges.challenge_24 import Step1 as NextStep


class StepMkdir(TerminalMkdir):
    challenge_number = 23


class StepMkdirEleonora(TerminalMkdirEleonora):
    challenge_number = 23


class Step1(StepMkdir):
    story = [
        "Hai visto Eleonora. Ascolta cosa ha da dire."
    ]
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "cat Eleonora"
    ]
    hints = [
        "{{rb:Usa}} {{yb:cat Eleonora}} {{rb:per vedere cosa ha da dire.}}"
    ]

    def next(self):
        Step2()


class Step2(StepMkdir):
    story = [
        "Eleonora: {{Bb:\"Oh, sei tu!",
        # "My parents went outside as we ran out of food."
        "Hai visto mia madre e mio padre?\"}}",
        # TODO: change colour
        "\n{{yb:1: \"Mi spiace, no. Quando li hai visti per l'ultima volta?\"}}",
        "{{yb:2: \"Non erano con te nel rifugio-nascosto?\"}}",
        "{{yb:3: \"(bugia) Si, li ho visti in città.\"}}",
        "\nUsa il comando {{lb:echo}} per parlare con Eleonora."
    ]

    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città/.rifugio-nascosto"
    commands = [
        "echo 1",
        "echo 2",
        "echo 3"
    ]

    def check_command(self):
        if self.last_user_input in self.commands:
            return True
        elif self.last_user_input.startswith("echo"):
            text = (
                "\nEleonora: {{Bb:\"Scusa? Cosa hai detto?\"}}"
            )
        else:
            text = (
                "\n{{rb:Usa}} {{yb:echo 1}}{{rb:,}} {{yb:echo 2}} "
                "{{rb:o}} {{yb:echo 3}} {{rb:per rispondere.}}"
            )

        self.send_text(text)

    def next(self):
        Step3(self.last_user_input)


class Step3(StepMkdirEleonora):
    start_dir = "~/città/.rifugio-nascosto"
    end_dir = "~/città"

    hints = [
        "{{rb:Usa}} {{yb:cd ../}} {{rb:per andare verso la città.}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Yay, stiamo andando verso l'avventura!}}"
    )

    def __init__(self, prev_command="echo 1"):
        self.story = []

        if prev_command == "echo 1":
            self.print_text = [
                "{{yb:\"Mi spiace, no. Quando li hai visti per l'ultima volta?\"}}"
            ]
            self.story += [
                "Eleonora: {{Bb:\"Non da tanto. Il cane è uscito di nuovo, "
                "e sono andati fuori a cercarlo.\"}}"
            ]

        elif prev_command == "echo 2":
            self.print_text = [
                "{{yb:\"Non erano nel rifugio-nascosto?\"}}"
            ]
            self.story += [
                "Eleonora: {{Bb:No, sono andati fuori. "
                "Il cane è uscito di nuovo, così sono andati fuori a "
                "cercarlo. Forse si sono persi?\"}}"
            ]

        elif prev_command == "echo 3":
            self.print_text = [
                "{{yb:\"(bugia) Si, li ho visti in città.\"}}"
            ]
            self.story += [
                "Eleonora: {{Bb:\"Oh ottimo! Il cane è uscito di nuovo, "
                "e così sono andati fuori a cercarlo.",
                "La campana mi aveva spaventata, ma sono felice che stiano bene.\"}}"
            ]

        self.story += [
            "{{Bb:\"Andiamo in città assieme e troviamoli. Starò al sicuro se "
            "rimarrò con te.\"}}",

            "\n{{gb:Eleonora ti accoglie come un compagno! Ora puoi controllare se "
            "è in qualunque momento con te}} {{yb:cat Eleonora}}{{gb:.}}",

            "\n{{lb:Lascia}} il {{lb:.rifugio-nascosto.}} "
            "Non preoccuparti, Eleonora ti seguirà!"
        ]

        StepMkdirEleonora.__init__(self)

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step4()


class Step4(StepMkdirEleonora):
    start_dir = "~/città"
    end_dir = "~/città"
    hints = [
        "Eleonora: {{Bb:Ti sei dimenticato come guardare attorno? "
        "Devi usare}} {{yb:ls}}{{Bb:.}}",

        "{{rb:Guarda attorno con}} {{yb:ls}}{{rb:.}}"
    ]
    commands = [
        "ls",
        "ls -a"
    ]
    deleted_items = ["~/città/.rifugio-nascosto/Eleonora"]

    story = [
        "Eleonora: {{Bb:Andiamo verso la parte}} {{lb:est}} "
        "{{Bb:della città.}}",
        "{{Bb:Non l'hai ancora notato prima? E' la sopra! "
        "Guarda in alto.}}",
        "\Usa {{yb:ls}} per vedere cosa Eleonora cerca di mostrarti."
    ]

    story_dict = {
        "Bernardo": {
            "path": "~/città/est/negozio-capanni"
        },
        "migliore-costruttore-capanni-del-mondo.sh": {
            "path": "~/città/est/negozio-capanni",
            "permissions": 0755
        },
        "migliore-corno-del-mondo-sbagliato.sh": {
            "name": "migliore-corno-del-mondo.sh",
            "path": "~/città/est/negozio-capanni",
            "permissions": 0755
        },
        "fotocopiatrice.sh, diario-bernardo-1, diario-bernardo-2": {
            "path": "~/città/est/negozio-capanni/scantinato"
        },
        "NANO": {
            "path": "~/città/est/biblioteca/ala-pubblica"
        },
        "ala-privata": {
            "path": "~/città/est/biblioteca",
            # Remove all read and write permissions
            "permissions": 0000,
            "directory": True
        },
        "Clara": {
            "path": "~/città/est/ristorante/.cantina"
        },
        "Eleonora": {
            "path": "~/città"
        }
    }

    eleanors_speech = (
        "\nEleonora: {{Bb:Perchè mi stai guardando? "
        "Dovresti guardare proprio LA.}}"
    )

    def next(self):
        Step5()


class Step5(StepMkdirEleonora):
    story = [
        "Guardi nella direzione che indica Eleonora.",
        "C'è una strada stretta che porta ad un'altra parte della città.",
        "Questa ci porterà alla parte est.",
        "Eleonora: {{Bb:Andiamo la e vediamo se troveremo i miei "
        "genitori.}}",
        "\n{{lb:Vai}} verso la parte {{lb:est}} della città."
    ]
    start_dir = "~/città"
    end_dir = "~/città/est"

    hints = [
        "{{rb:Usa}} {{lb:cd}} {{rb:per andare verso la "
        "parte est della città}}",
        "{{rb:Usa}} {{yb:cd est/}} {{rb:}}"
    ]
    last_step = True

    eleanors_speech = (
        "\nEleonora: {{Bb:Andiamo ad}} {{lb:est}} "
        "{{Bb:della città. Muoviti sei lento!}}"
    )

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        NextStep(self.xp)
