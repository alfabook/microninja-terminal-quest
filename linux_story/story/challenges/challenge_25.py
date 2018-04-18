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
from linux_story.story.challenges.challenge_26 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_cd_commands


class StepTemplateMkdir(TerminalMkdirBernardo):
    challenge_number = 25


class Step1(StepTemplateMkdir):
    story = [
        "Bernardo: {{Bb:Ciao! Shhhhh, non dire una parola.}}",

        "{{Bb:So perchè sei qui. Vuoi un capanno!",

        "Ho proprio la cosa giusta per te. Io ho il}} "
        "{{lb:migliore-costruttore-capanni-del-mondo.sh}}",

        "\nBernardo sembra abbastanza entusiasta di questo. {{lb:Esamina}} l'attrezzo "
        "{{lb:migliore-costruttore-capanni-del-mondo.sh}}",

        "\n{{gb:Usa TAB per velocizzare la digitazione.}}"
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"

    hints = [
        "{{rb:Usa}} {{lb:cat}} {{rb:per esaminare il}} "
        "{{lb:migliore-costruttore-capanni-del-mondo.sh}}",

        "{{rb:Usa}} {{yb:cat migliore-costruttore-capanni-del-mondo.sh}} "
        "{{rb:per esaminare l'attrezzo.}}"
    ]

    commands = [
        "cat migliore-costruttore-capanni-del-mondo.sh"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:Bernardo mi fa un po' paura...}}"
    )

    def check_command(self):
        if self.last_user_input == "cat migliore-corno-del-mondo.sh":
            self.send_text(
                "\n{{rb:Stai leggendo il file sbagliato! "
                "Devi leggere}} {{lb:migliore-costruttore-capanni-del-mondo.sh}}"
                "{{rb:.}}"
            )
        else:
            return StepTemplateMkdir.check_command(self)

    def next(self):
        Step2()


class Step2(StepTemplateMkdir):
    story = [
        "L'attrezzo ha una scritta che dice {{lb:mkdir capanno}}.",
        "Tu riconosci il comando {{lb:mkdir}}. E' lo stesso che hai usato "
        "per aiutare Ruth alla fattoria.",

        "\nBernardo: {{Bb:E' magia! Lanci il comando, "
        "e ottieni un nuovo capanno.}}",

        "{{Bb:Provalo! Usalo con}} "
        "{{yb:./migliore-costruttore-capanni-del-mondo.sh}}",

        "\n{{gb:Usa TAB per velocizzare la scrittura.}}"
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"

    hints = [
        "{{rb:Fai quello che dice Bernardo - usa}} "
        "{{yb:./migliore-costruttore-capanni-del-mondo.sh}} "
        "{{rb:per lanciare lo script}}"
    ]
    commands = [
        "./migliore-costruttore-capanni-del-mondo.sh"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:Non è la stessa cosa che digitare}} "
        "{{yb:mkdir shed}}{{Bb:?}}"
    )

    def check_command(self):
        if self.last_user_input == "./migliore-corno-del-mondo.sh":
            self.send_text(
                "\n{{rb:Stai lanciando lo script sbagliato. "
                "Devi lanciare}} "
                "{{yb:./migliore-costruttore-capanni-del-mondo.sh}}"
            )
        else:
            return StepTemplateMkdir.check_command(self)

    def next(self):
        Step3()


class Step3(StepTemplateMkdir):
    story = [
        "{{lb:Guarda attorno}} per vedere se hai creato un capanno."
    ]
    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Usa}} {{yb:ls}} {{rb:per guardare attorno.}}"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:Ah, guarda la!}}"
    )

    def next(self):
        Step4()


class Step4(StepTemplateMkdir):
    story = [
        "Ha funzionato! puoi vedere una nuova capanna nella stanza.",
        "Cosa succede se lo faccio ancora?",
        "{{gb:Premi SU due volte per rilanciare il comando.}}"
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"

    hints = [
        "{{rb:Guarda cosa succede se rilanci lo script.}}",

        "{{rb:Rilancia lo script usando}} "
        "{{yb:./migliore-costruttore-capanni-del-mondo.sh}} "
        "{{rb:per vedere cosa succede.}}"
    ]
    commands = [
        "./migliore-costruttore-capanni-del-mondo.sh"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:Non penso che funzionerà...}}"
    )

    def next(self):
        Step5()


class Step5(StepTemplateMkdir):
    story = [
        "Ottieni l'errore {{yb:mkdir: impossibile creare la directory `capanno': "
        "file già esistente}}",
        "\nBernardo: {{Bb:Certo che non funziona la seconda volta - "
        "hai già un capanno!",

        "Sto lavorando sulla prossima, grande cosa:}} "
        "{{lb:migliore-corno-del-mondo.sh}}{{Bb:.}}",

        "{{Bb:Può avvisare tutti che stai arrivando. "
        "Sto avendo qualche problema ai denti, "
        "ma sono sicuro che lo riparerò presto.}}",

        "\n{{lb:Esamina migliore-corno-del-mondo.sh}} e vedi se puoi "
        "identificare il problema.",

        "{{gb:Ricordati di usare TAB!}}"
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"
    commands = [
        "cat migliore-corno-del-mondo.sh"
    ]

    hints = [
        "{{rb:Usa}} {{lb:cat}} {{rb:per esaminare l'attrezzo.}}",
        "{{rb:Usa}} {{yb:cat migliore-corno-del-mondo.sh}} {{rb:per esaminare "
        "l'attrezzo.}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Penso che questo attrezzo sia un po' rotto.}}"
    )

    def check_command(self):
        if self.last_user_input == "cat migliore-costruttore-capanni-del-mondo.sh":
            self.send_text(
                "\n{{rb:Stai esaminando l'attrezzo sbagliato. Devi guardare "
                "at}} {{yb:migliore-corno-del-mondo.sh}}"
            )

        else:
            return StepTemplateMkdir.check_command(self)

    def next(self):
        Step6()


class Step6(StepTemplateMkdir):
    story = [
        "L'attrezzo contiene {{yb:eco \"Honk!\"}}",
        "Forse dovrebbe contenere {{yb:echo \"Honk!\"}} invece...",
        "Come facciamo a cambiare l'attrezzo?",
        "\nBernardo: {{Bb:Ho ho, sembra che hai capito il problema.}}",
        "Eleonora: {{Bb:Se hai bisogno di altro aiuto, potremo andare alla "
        "biblioteca, era giusto la fuori.}}",
        "\nPrima di andare, dai uno {{lb:sguardo}} nello {{lb:scantinato}}."
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est/negozio-capanni"

    commands = [
        "ls scantinato",
        "ls scantinato/",
        "ls -a scantinato",
        "ls -a scantinato/",
    ]

    hints = [
        "{{rb:Usa}} {{lb:ls}} {{rb:per guardare attorno.}}",
        "{{rb:Usa}} {{yb:ls scantinato/}} {{rb:per guardare dentro.}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:OooOOoh, ci sono dolci la?}}"
    )

    def next(self):
        Step7()


class Step7(StepTemplateMkdir):
    story = [
        "Bernardo: {{Bb:Oooh birbantella, non puoi guardare la.}}",
        "\n{{lb:Lasciamo}} il negozio di capanni per tornare in città."
    ]

    start_dir = "~/città/est/negozio-capanni"
    end_dir = "~/città/est"
    hints = [
        "{{rb:Lascia il negozio-capanni usando}} {{yb:cd ../}}"
    ]
    eleanors_speech = (
        "Eleonora: {{Bb:Yay, mi piace la biblioteca. Torniamo in città!}}"
    )

    last_step = True

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        NextStep(self.xp)
