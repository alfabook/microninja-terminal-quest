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

# At this point, Bernard disappears, so no need to keep blocking access to
# his basement.
from linux_story.story.terminals.terminal_eleonora import TerminalNanoEleonora
from linux_story.story.challenges.challenge_31 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_cd_commands


class StepNano(TerminalNanoEleonora):
    challenge_number = 30


class Step1(StepNano):
    story = [
        "{{pb:Ding. Dong.}}",
        "\nEleonora: {{Bb:...cosa è stato?}}",
        "{{lb:Guarda attorno.}}"
    ]
    start_dir = "~/città/est/ristorante/.cantina"
    end_dir = "~/città/est/ristorante/.cantina"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per controllare che tutti siano ancora presenti.}}"
    ]
    deleted_items = [
        "~/città/est/negozio-capanni/Bernardo"
    ]
    story_dict = {
        "cappello-bernardo": {
            "path": "~/città/est/negozio-capanni"
        }
    }
    eleanors_speech = (
        "Eleonora: {{Bb:......}}"
    )

    def next(self):
        Step2()


class Step2(StepNano):
    story = [
        "Sembra che ci siano ancora tutti. Cos'era quella campana?",
        "\nSembra che Clara abbia qualcosa da dire. {{lb:Ascoltala.}}"
    ]
    commands = [
        "cat Clara"
    ]
    start_dir = "~/città/est/ristorante/.cantina"
    end_dir = "~/città/est/ristorante/.cantina"
    hints = [
        "{{rb:Usa}} {{yb:cat Clara}} {{rb:per ascoltare Clara.}}"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:....Sono molto impaurita. Non penso di voler andare fuori "
        "ora.}}"
    )

    def next(self):
        Step3()


class Step3(StepNano):
    story = [
        "Clara: {{Bb:State andando la fuori voi due?}}",
        "{{gb:" + os.environ['LOGNAME'] + "}}"
        "{{Bb:, sembra che tu riesca a badare a te stesso, ma "
        "non mi sento al sicuro con Eleonora la fuori.}}",
        "\n" + "{{gb:" + os.environ['LOGNAME'] + "}}"
        "{{Bb:, me la lasceresti a me? "
        "Baderò io a lei.}}",
        "\n{{yb:1: Ottima idea, prenditi cura di lei tu.}}",
        "{{yb:2: No, non mi fido troppo di te, starà più al sicuo con me.}}",
        "{{yb:3: (Chiedi a Eleonora.) Tu vuoi stare qua?}}",
        # "{{yb:4: Do you have enough food here?}}",
        "\n{{lb:Rispondi a Clara.}}"
    ]
    commands = [
        "echo 1"
    ]
    start_dir = "~/città/est/ristorante/.cantina"
    end_dir = "~/città/est/ristorante/.cantina"
    hints = [
        "{{rb:Usa}} {{yb:echo 1}}{{rb:,}} {{yb:echo 2}} {{rb:o}} "
        "{{yb:echo 3}} {{rb:per rispondere a Clara.}}"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:Sono felice di stare qua. Clara mi piace.}}"
    )

    def check_command(self):
        if self.last_user_input == "echo 2":
            text = (
                "\nClara: {{Bb:Per favore, lasciala a me. "
                "Non penso che sia sicuro per lei andare fuori.}}"
            )
            self.send_text(text)
        elif self.last_user_input == "echo 3":
            text = "\nEleonora: {{Bb:Sono felice di stare qua. Clara mi piace.}}"
            self.send_text(text)
        # elif self.last_user_input == "echo 4":
        #    text = (
        #        "\nClara: {{Bb:There's loads of food here, look in the}} "
        #        "{{lb:larder}} {{Bb:if you don't believe me.}}"
        #    )
        #    self.send_text(text)
        else:
            return StepNano.check_command(self)

    def next(self):
        Step4()


class Step4(StepNano):
    story = [
        "Clara: {{Bb:Grazie!}}",
        "Eleonora: {{Bb:Quando trovi i miei genitori, potresti dirgli che sono "
        "qua?}}",
        "Clara: {{Bb:Dove stai andando ora?}}",
        "\nTorno a vedere {{lb:Bernardo}} e gli chiedo se ha sentito qualcosa sullo "
        "{{lb:spadaccino mascherato}}.",
        "{{lb:Dirigiti al negozio-capanni.}}"
    ]
    start_dir = "~/città/est/ristorante/.cantina"
    end_dir = "~/città/est/negozio-capanni"
    last_step = True

    path_hints = {
        "~/città/est/ristorante/.cantina": {
            "blocked": "\n{{rb:Usa}} {{yb:cd ../}} {{rb:per tornare indietro.}}"
        },
        "~/città/est/ristorante": {
            "not_blocked": "\n{{gb:Ottimo lavoro! Continua così!}}",
            "blocked": "\n{{rb:Usa}} {{yb:cd ../}} {{rb:per tornare indietro.}}"
        },
        "~/città/est": {
            "not_blocked": "\n{{gb:Ora vai verso il}} {{lb:negozio-capanni}}{{gb:.}}",
            "blocked": "\n{{rb:Usa}} {{yb:cd negozio-capanni/}}{{rb:.}}"
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
        NextStep(self.xp)
