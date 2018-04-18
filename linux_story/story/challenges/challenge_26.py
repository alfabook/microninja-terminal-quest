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


from linux_story.story.terminals.terminal_bernardo import TerminalMkdirBernardo
from linux_story.story.challenges.challenge_27 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_cd_commands


class StepTemplateMkdir(TerminalMkdirBernardo):
    challenge_number = 26


class Step1(StepTemplateMkdir):
    story = [
        "Sei tornato in città. Eleonora ondeggia le sue braccia e punta "
        "verso una costruzione in distanza.",
        "\n{{lb:Gurada attorno}} per vedere dove sta puntando Eleonora."
    ]

    start_dir = "~/città/est"
    end_dir = "~/città/est"

    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    ]

    commands = [
        "ls",
        "ls -a"
    ]

    deleted_items = ["~/città/est/negozio-capanni/Eleonora"]
    story_dict = {
        "Eleonora": {
            "path": "~/città/est"
        }
    }
    eleanors_speech = "Eleonora: {{Bb:La biblioteca è proprio la!}}"

    def next(self):
        Step2()


class Step2(StepTemplateMkdir):
    story = [
        "Vai alla {{bb:biblioteca}} davanti.",

        "Eleonora: {{Bb:Eccola! La}} {{bb:biblioteca}} "
        "{{Bb:E' proprio la!}} {{lb:Entriamo dentro.}}"
    ]

    start_dir = "~/città/est"
    end_dir = "~/città/est/biblioteca"

    hints = [
        "{{rb:Usa}} {{yb:cd biblioteca/}} {{rb:per entrare nella biblioteca.}}"
    ]
    eleanors_speech = "Eleonora: {{Bb:Amo la biblioteca! Entriamo!}}"

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step3()


class Step3(StepTemplateMkdir):
    story = [
        "Eleonora si precipita dentro la biblioteca, e tu la segui.",
        "{{lb:Guarda attorno}} la biblioteca."
    ]

    start_dir = "~/città/est/biblioteca"
    end_dir = "~/città/est/biblioteca"

    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    ]
    commands = [
        "ls",
        "ls -a"
    ]
    deleted_items = ["~/città/est/Eleonora"]
    story_dict = {
        "Eleonora": {
            "path": "~/città/est/biblioteca"
        }
    }
    eleanors_speech = "Eleonora: {{Bb:Che acustica che c'è...}}"

    def next(self):
        Step4()


class Step4(StepTemplateMkdir):
    story = [
        "Sei in un corridoio che porta a due porte "
        "con delle targhette. "
        "Una ha il cartello {{bb:ala-pubblica}}, l'altra "
        "{{bb:ala-privata}}.",

        "Eleonora: {{Bb:C'era una bibliotecaria qua.",

        "Ci direbbe che potremo guardare nell'}} "
        "{{bb:ala-privata?}}.",

        "{{Bb:Cosa pensi ci sia la dentro? Proviamo a}} "
        "{{lb:guardarci dentro}}{{Bb:.}}"
    ]

    start_dir = "~/città/est/biblioteca"
    end_dir = "~/città/est/biblioteca"

    commands = [
        "ls ala-privata/",
        "ls ala-privata"
    ]

    hints = [
        "{{rb:Usa}} {{yb:ls ala-privata/}} {{rb:per guardare "
        "nell'ala-privata della biblioteca.}}"
    ]
    eleanors_speech = "Eleonora: {{Bb:Cosa c'è nell'ala privata?}}"

    def next(self):
        Step5()


class Step5(StepTemplateMkdir):

    story = [
        "Eleonora: {{Bb:Credo che l'ala-privata sia chiusa agli esterni...",

        "Vediamo se troviamo qualcosa di utile nell'}} "
        "{{bb:ala pubblica.}}",

        "\nUsa {{lb:ls}} per guardare dentro {{lb:ala-pubblica}}."
    ]

    start_dir = "~/città/est/biblioteca"
    end_dir = "~/città/est/biblioteca"
    commands = [
        "ls ala-pubblica",
        "ls ala-pubblica/",
        "ls -a ala-pubblica",
        "ls -a ala-pubblica/"
    ]
    hints = [
        "{{rb:Usa}} {{lb:ls}} {{rb:per guardare nell'ala pubblica.}}",
        "{{rb:Usa}} {{yb:ls ala-pubblica}} {{rb:per guardare dentro ala-"
        "pubblica.}}"
    ]
    eleanors_speech = "Eleonora: {{Bb:Cosa c'è nell'ala-pubblica?}}"

    def next(self):
        Step6()


class Step6(StepTemplateMkdir):
    story = [
        "Eleonora: {{Bb:Wow, tutti i comandi sono scomparsi.",
        "Mi chiedo se qualcuno li abbia rubati!}}",

        "{{Bb:Cos'è quel foglio}} {{lb:NANO}} {{Bb:?}}",
        "{{lb:Esaminiamolo}} {{Bb:.}}"
    ]
    start_dir = "~/città/est/biblioteca"
    end_dir = "~/città/est/biblioteca"
    commands = [
        "cat ala-pubblica/NANO"
    ]
    hints = [
        "{{rb:Esamina il foglio NANO con}} {{yb:cat ala-pubblica/NANO}}"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:La biblioteca avrà aggiunto multe per i "
        "ritardatari.}}"
    )

    def next(self):
        Step7()


class Step7(StepTemplateMkdir):
    story = [
        "Eleonora: {{Bb:Quindi nano ti permette di "
        "modificare file?}}",

        "{{Bb:Forse possiamo usarlo per riparare quello script "
        "migliore-corno-nel-mondo.sh?}}",

        "{{lb:Torniamo indietro}} {{Bb:al}} {{lb:negozio-capanni}}{{Bb:.}}"
    ]
    start_dir = "~/città/est/biblioteca"
    end_dir = "~/città/est/negozio-capanni"
    eleanors_speech = (
        "Eleonora: {{Bb:... Dobbiamo vedere di nuovo quel sinistro Bernardo?}}"
    )
    last_step = True

    path_hints = {
        "~/città/est/biblioteca": {
            "blocked": "\n{{rb:Usa}} {{yb:cd ../}} {{rb:per tornare indietro.}}"
        },
        "~/città/est": {
            "not_blocked": "\n{{gb:Ottimo lavoro! Andiamo al}} {{lb:negozio-capanni}}{{gb:.}}",
            "blocked": "\n{{rb:Usa}} {{yb:cd negozio-capanni/}} {{rb:per andare al negozio-capanni.}}"
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
