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


from linux_story.story.terminals.terminal_eleonora import TerminalMkdirEleonora
from linux_story.story.challenges.challenge_25 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_cd_commands


class StepTemplateMkdir(TerminalMkdirEleonora):
    challenge_number = 24


class Step1(StepTemplateMkdir):
    story = [
        "Camminiamo lungo la strada stretta, assieme con "
        "Eleonora, finchè non raggiungi uno spazio aperto nella parte "
        "{{bb:est}} della città.",
        "\n{{lb:Guarda attorno.}}"
    ]
    commands = [
        "ls",
        "ls -a"
    ]

    start_dir = "~/città/est"
    end_dir = "~/città/est"
    hints = [
        "{{rb:Guarda attorno con}} {{yb:ls}}{{rb:.}}"
    ]
    deleted_items = ["~/città/Eleonora"]
    story_dict = {
        "Eleonora": {
            "path": "~/città/est"
        }
    }

    eleanors_speech = (
        "Eleonora: {{Bb:Non riesco a vedere i miei genitori da nessuna parte ... ma c'è una "
        "strana struttura la.}}"
    )

    def next(self):
        Step2()


class Step2(StepTemplateMkdir):
    story = [
        "Vedi un {{bb:negozio-capanni}}, una {{bb:biblioteca}} e un {{bb:ristorante}}.",
        "\nEleonora: {{Bb:Hey, cos'è quel negozio-capanni?}}",
        "{{Bb:Andiamo}} {{lb:dentro}}{{Bb:!}}"
    ]

    start_dir = "~/città/est"
    end_dir = "~/città/est/negozio-capanni"
    hints = [
        "{{rb:Usa}} {{yb:cd negozio-capanni/}} {{rb:per andare al negozio-capanni.}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Pensi che vendano dolci?}}"
    )

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step3()


# Duplicate of Step1, except that self.next is changed
class Step3(StepTemplateMkdir):
    # Have a sign with "the-best-shed-maker-in-città"

    story = [
        "Entrambi camminate lentamente verso il negozio.",
        "E' polveroso e più scuro qua che altrove.",
        "Eleonora guarda come se dovesse starnutire.",
        "\n{{lb:Guarda attorno.}}"
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"
    hints = [
        "{{rb:Guarda attorno con}} {{yb:ls}}{{rb:.}}"
    ]
    commands = [
        "ls",
        "ls -a"
    ]
    deleted_items = ["~/città/est/Eleonora"]
    story_dict = {
        "Eleonora": {
            "path": "~/città/est/negozio-capanni"
        }
    }
    eleanors_speech = (
        "Eleonora: {{Bb:Eh..eh...ecciù!! E' così polveroso qua!}}"
    )

    def next(self):
        Step4()


class Step4(StepTemplateMkdir):

    story = [
        "Vedi un uomo chiamato Bernardo, una porta e un paio "
        "di attrezzi.",
        "\nGli attrezzi appaiono {{gb:verdi}} nel Terminale.",
        "\n{{lb:Ascolta}} cosa {{lb:Bernardo}} ha da dire."
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"

    hints = [
        "{{rb:Usa}} {{yb:cat Bernardo}} {{rb:per vedere cosa Bernardo ha "
        "da dire.}}"
    ]

    commands = [
        "cat Bernardo"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:Il mio}} {{lb:gatto}} {{Bb:era un grande "
        "ascoltatore, gli ho raccontato di tutto.}}"
    )

    last_step = True

    def next(self):
        NextStep(self.xp)
