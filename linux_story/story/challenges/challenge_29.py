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
from linux_story.story.terminals.terminal_bernardo import TerminalNanoBernardo
from linux_story.story.challenges.challenge_30 import Step1 as NextStep
from linux_story.helper_functions import play_sound, record_user_interaction


# Can't get all the information with this system unless you are interested.
story_replies = {
    "echo 1": [
        {
            "user": "Perchè l'ala privata della libreria è chiusa?",
            "clara": (
                "Clara: {{Bb:Contiene alcune informazioni pericolose."

                "\n...Mi spiace, ma non posso dire di più. Il capo bibliotecario "
                "era abbastanza preoccupato che nessuno entrasse la. Era l'unico che "
                "poteva aprire e chiudere.}}"
            )
        },
        {
            "user": "Come faceva a chiudere?",
            "clara": (
                "Clara: {{Bb:Non so, non avevo l'autorizzazione per "
                "saperlo.}}"

                "\n{{Bb:Penso che lui abbia imparato da uno}} "
                "{{lb:spadaccino mascherato}} {{Bb:che vive fuori città.}}"
            )
        },
        {
            "user": "Dove possiamo trovare questo spadaccino mascherato?",
            "clara": (
                "Clara: {{Bb:Ha detto che lo}} "
                "{{lb:spadaccino mascherato}} {{Bb:viveva nel bosco}}"

                "\n{{Bb:Penso che si riferisse ai boschi che stanno oltre la}} "
                "{{lb:Strada Ventosa}}{{Bb:! Quello "
                "vicino alla fattoria e quella strana casa solitaria fuori città.}}"
            )
        }
    ],

    "echo 2": [
        {
            "user": "Perchè ti nascondi qua sotto?",
            "clara": (
                "Clara: {{Bb:Ho sentito il suono della campana, e ho visto il "
                "capo bibliotecario scomparire di fronte a me. Ero così impaurita che "
                "sono corsa via, e ho trovato questa}} {{bb:.cantina}}"
                "{{Bb:.}}"
            )
        },
        {
            "user": "Hai qualche parente in città?",
            "clara": (
                "Clara: {{Bb:Ho due figli, un}} "
                "{{lb:bambino}} {{Bb:e una}} "
                "{{lb:giovane-ragazza}}{{Bb:. Spero che stiano bene.}}"
            )
        },
        {
            "user": "Perchè la biblioteca è vuota?",
            "clara": (
                "Clara: {{Bb:Avremo dovuto introdurre multe per i ritardatari molto "
                "tempo fa...}}"
            )
        }
    ],

    "echo 3": [
        {
            "user": "Conosci altra gente in città?",
            "clara": (
                "Clara: {{Bb:C'è un uomo di cui non mi fido, che ha il}} "
                "{{bb:negozio-capanni}}{{Bb:. Penso che si chiami Bernardo.}}"
            )
        },
        {
            "user": "Perchè non ti piace Bernardo?",
            "clara": (
                "Clara: {{Bb:Fa attrezzi molto semplici e chiede una fortuna "
                "per quelli.}}"
                "\n{{Bb:Suo padre era un uomo molto intelligente e ha trascorso "
                "tutto il suo tempo in biblioteca imparando comandi. Di conseguenza divenne un "
                "uomo d'affari di successo.}}"
            )
        },
        {
            "user": "Cosa è successo al padre di Bernardo?",
            "clara": (
                "Clara: {{Bb:La gente non è sicura, è scomparso un giorno. "
                "Lo hanno "
                "dato per morto. L'ho visto lasciare la biblioteca il giorno che "
                "scomparve, "
                "la lasciò di fretta. Sembrava terrorizzato.}}"
            )
        }
    ]
}


# Generate the story from the step number
def create_story(step):
    print_text = ""

    if step > 1:
        print_text = "{{yb:" + story_replies["echo 1"][step - 2]["user"] + "}}"

    story = [
        story_replies["echo 1"][step - 2]["clara"],
        "\n{{yb:1: " + story_replies["echo 1"][step - 1]["user"] + "}}",
        "{{yb:2: " + story_replies["echo 2"][0]["user"] + "}}",
        "{{yb:3: " + story_replies["echo 3"][0]["user"] + "}}"
    ]

    return (print_text, story)


# Want to eliminate the story that the user has already seen
def pop_story(user_input):
    # if the user_input is echo 1, echo 2 or echo 3
    if user_input in story_replies:
        reply = story_replies[user_input][0]
        story_replies[user_input].remove(reply)
        return reply


class StepNano(TerminalNanoBernardo):
    challenge_number = 29


class StepNanoStory(StepNano):
    commands = [
        "echo 1"
    ]

    start_dir = "~/città/est/ristorante/.cantina"
    end_dir = "~/città/est/ristorante/.cantina"
    hints = [
        "{{rb:Parla con Clara usando}} {{yb:echo 1}}{{rb:,}} "
        "{{yb:echo 2}} {{rb:o}} {{yb:echo 3}}{{rb:.}}"
    ]

    def __init__(self, xp="", step_number=None):
        self.echo_hit = {
            "echo 2": True,
            "echo 3": True
        }

        if step_number:
            self.print_text = [create_story(step_number)[0]]
            self.story = create_story(step_number)[1]

        StepNano.__init__(self, "")

    def check_command(self):

        # If self.last_user_input equal to "echo 1" or "echo 3"
        if self.last_user_input in story_replies:

            if self.last_user_input == "echo 1":
                return True

            else:
                if self.echo_hit[self.last_user_input]:
                    self.echo_hit[self.last_user_input] = False
                    reply = pop_story(self.last_user_input)["clara"]
                    self.send_text("\n\n" + reply)

                    # Record that the user got optional info
                    # Replace spaces with underscores
                    user_input = "_".join(self.last_user_input.split(" "))
                    state_name = "clara_{}".format(user_input)
                    record_user_interaction(self, state_name)
                else:
                    self.send_text(
                        "\n{{rb:Hai già chiesto questo a Clara. "
                        "Chiedi qualcos'altro.}}"
                    )

        else:
            return TerminalNanoBernardo.check_command(self)


class Step1(StepNanoStory):
    story = [
        "Clara: {{Bb:Cosa? Chi sei?}}",

        "\nEleonora: {{Bb:Ciao! Sono Eleonora, e questo è}} {{gb:" +
        os.environ["LOGNAME"] + "}}{{Bb:.}}",
        "{{Bb:Ti riconosco! Lavoravi in biblioteca!}}",

        "\nClara: {{Bb:...ah, Eleonora! Si, mi ricordo di te, venivi "
        "quasi tutti i giorni.}}",

        # Options
        "\n{{yb:1: Perchè l'ala privata della biblioteca è chiusa?}}",
        "{{yb:2: Perchè sei nscosta qua sotto?}}",
        "{{yb:3: Conosci altre persone in città?}}",

        "\nUsa {{lb:echo}} per fare la domanda a Clara."
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Non sono più spaventata, mi piace Clara.}}"
    )

    def next(self):
        Step2(step_number=2)


class Step2(StepNanoStory):

    eleanors_speech = (
        "Eleonora: {{Bb:Cosa c'è di così pericoloso nell'ala-privata?}}"
    )

    def next(self):
        Step3(step_number=3)


class Step3(StepNanoStory):

    eleanors_speech = (
        "Eleonora: {{Bb:Vogliamo davvero aprire qualcosa di così pericoloso?}}"
    )

    def next(self):
        Step4()


class Step4(StepNanoStory):
    last_step = True

    print_text = "{{yb:Dove possiamo trovare lo spadaccino mascherato?}}",
    story = [
        "Clara: {{Bb:Diceva che lo}} "
        "{{lb:spadaccino mascherato}} {{Bb:viveva nei boschi.}}",

        "{{Bb:Penso che si riferisse ai boschi che stanno oltre la}} "
        "{{lb:Strada Ventosa}}{{Bb:! Quello "
        "vicino alla fattoria e quella strana casa solitaria fuori città.}}",

        "\n{{gb:Premi invio per continuare.}}"
    ]

    eleanors_speech = (
        "Eleonora: {{Bb:Uno spadaccino mascherato??}}"
    )

    def check_command(self):
        return True

    def next(self):
        play_sound("bell")
        NextStep(self.xp)
