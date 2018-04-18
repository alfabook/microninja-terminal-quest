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

from linux_story.step_helper_functions import (
    unblock_cd_commands, unblock_commands_with_mkdir_hint,
    unblock_commands
)
from linux_story.story.terminals.terminal_mkdir import TerminalMkdir
from linux_story.story.challenges.challenge_22 import Step1 as NextStep


class StepTemplateMkdir(TerminalMkdir):
    challenge_number = 21


class Step1(StepTemplateMkdir):
    story = [
        "{{gb:Carino! Hai costruito un igloo! Hai imparato una nuova abilità, "
        "mkdir!}}",
        "\nRuth: {{Bb:Meraviglioso! Per favore aiutami a costruire un rifugio!",
        "Potremo costruirlo nel}} {{lb:fienile}}{{Bb:, e dopo sarebbe più facile "
        "spostare gli animali dentro.}}",
        "\n{{lb:Vai}} indietro verso il {{lb:fienile}}."
    ]
    start_dir = "~/fattoria/capanno-attrezzi"
    end_dir = "~/fattoria/fienile"
    deleted_items = [
        "~/fattoria/capanno-attrezzi/Ruth"
    ]
    story_dict = {
        "Ruth": {
            "path": "~/fattoria/fienile",
        }
    }

    path_hints = {
        "~/fattoria/capanno-attrezzi": {
            "blocked": "\n{{rb:Usa}} {{yb:cd ../}} {{rb:per tornare indietro.}}"
        },
        "~/fattoria": {
            "not_blocked": "\n{{gb:Ottimo lavoro! Ora vai verso il}} {{lb:fienile}}{{gb:.}}",
            "blocked": "\n{{rb:Usa}} {{yb:cd fienile/}} {{rb:per andare verso il fienile.}}"
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
        Step2()


class Step2(StepTemplateMkdir):
    story = [
        "Ruth: {{Bb:Tutti saranno in grado di trovare l'igloo "
        "appena costruito.",
        "E' possibile costruire qualcosa nascosto?}}\n",
        "{{yb:1: Se lo chiamassimo}} {{lb:rifugio-nascosto}}"
        "{{yb:, questo lo renderebbe nascosto.}}",
        "{{yb:2: Mettere un . di fronte al nome rende le cose nascoste.}}",
        "{{yb:3: E' impossibile fare un rifugio nascosto.}}\n",
        "Usa {{lb:echo}} per dire a Ruth come fare le cose nascoste."
    ]
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"
    commands = [
        "echo 1",
        "echo 2",
        "echo 3"
    ]
    hints = [
        "Ruth: {{Bb:Dovresti davvero parlare a voce più alta, "
        "non riesco a capire nulla di quello che stai dicendo.}}",
        "{{rb:Usa}} {{yb:echo 1}}{{rb:,}} {{yb:echo 2}} {{rb:o}} "
        "{{yb:echo 3}} {{rb:per rispondere a Ruth.}}"
    ]

    def __init__(self):
        self.next_class = Step4
        StepTemplateMkdir.__init__(self)

    def check_command(self):
        if self.last_user_input == "echo 1":
            self.next_class = Step3
            return True
        elif self.last_user_input == "echo 2":
            self.next_class = Step6
            return True
        elif self.last_user_input == "echo 3":
            hint = (
                "\nRuth: {{Bb:...Davvero? Sei sicuro?}}"
            )
            self.send_text(hint)
        else:
            self.send_hint()

    def next(self):
        self.next_class()


# First fork - try making a hidden rifugio
class Step3(StepTemplateMkdir):
    print_text = [
        "{{yb:Se lo chiamassimo}} {{lb:rifugio-nascosto}}"
        "{{yb:, questo lo renderebbe nascosto.}}"
    ]
    story = [
        "Ruth: {{Bb:Quindi creare un}} {{lb:rifugio-nascosto}} "
        "{{Bb:lo renderebbe nascosto? Ok, proviamo.}}\n",
        "Prova a {{lb:costruire}} un rifugio chiamato {{lb:rifugio-nascosto}}."
    ]
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"
    commands = [
        "mkdir rifugio-nascosto",
    ]
    hints = [
        "{{rb:Devi fare un rifugio chiamato}} {{yb:rifugio-nascosto}}"
        "{{rb:.}}",
        "{{rb:Usa il comando}} {{yb:mkdir rifugio-nascosto}} "
        "{{rb:pr costruire il rifugio.}}"
    ]

    def check_command(self):
        if self.last_user_input == "mkdir .rifugio-nascosto":
            hint = (
                "\nRuth: {{Bb:Ma tu mi avevi detto che il rifugio doveva chiamarsi}} "
                "{{lb:rifugio-nascosto}}{{Bb:, non}} {{lb:.rifugio-nascosto}}"
                "{{Bb:.}}"
                "\n{{yb:Premi SU per riscrivere i vecchi comandi, e modificarli.}}"
            )
            self.send_text(hint)
        else:
            return StepTemplateMkdir.check_command(self)

    def block_command(self):
        return unblock_commands_with_mkdir_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step4()


class Step4(StepTemplateMkdir):
    story = [
        "{{lb:Guarda attorno}} e vedi se è nascosto come si deve."
    ]
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"
    commands = [
        "ls"
    ]
    hints = [
        "{{rb:Guarda attorno con}} {{yb:ls}}{{rb:.}}"
    ]
    ls_a_hint = True

    def check_command(self):
        if self.last_user_input == "ls -a" and self.ls_a_hint:
            hint = (
                "\n{{gb:Quasi!}} {{ob:Ma devi controllare se il "
                "rifugio è nascosto, quindi non guardare "
                "attorno}} {{yb:troppo attentamente}}{{rb:.}}"
            )
            self.send_text(hint)
            self.ls_a_hint = False
        else:
            return StepTemplateMkdir.check_command(self)

    def next(self):
        Step5()


class Step5(StepTemplateMkdir):
    story = [
        "Ruth: {{Bb:Hai fatto}} {{lb:rifugio-nascosto}}{{Bb:!}}",
        "{{Bb:...Il problema è che posso vederlo anche io. Non penso che abbia funzionato.",
        "In che altri modi possiamo nascondere le cose?}}",
        "\n{{yb:1: Se metti un . davanti al nome, lo rende nascosto.}}",
        "{{yb:2: Stai sbagliando. Non puoi vedere il rifugio-nascosto, è "
        "nascosto.}}\n",
        "Usa {{lb:echo}} per parlare a Ruth.",
    ]
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"
    commands = [
        "echo 1"
    ]
    hints = [
        "Ruth: {{Bb:Tu DEVI parlare più chiaramente. Non posso capirti.}}",
        "{{rb:Usa}} {{yb:echo 1}} {{rb:o}} {{yb:echo 2}} {{rb:per rispondere.}}"
    ]

    def check_command(self):
        if self.last_user_input == "echo 1":
            return True

        elif self.last_user_input == "echo 2":
            hint = (
                "\nRuth: {{Bb:....",
                "Stai attento bambino, non sono stupida. Quel rifugio non è nascosto.\n"
                "Come farne uno che lo sia?}}"
            )
            self.send_text(hint)

        else:
            self.send_hint()

    def next(self):
        Step6()


###########################################
# Second fork

class Step6(StepTemplateMkdir):
    print_text = [
        "{{yb:Se metti un . di fronte al nome, lo rende nascosto.}}"
    ]
    story = [
        "Ruth: {{Bb:Quindi se chiamassimo il rifugio}} {{lb:.rifugio}}"
        "{{Bb:, lo renderebbe nascosto? Proviamo!}}",
        "{{lb:Costruisci}} un rifugio chiamato {{lb:.rifugio}}"
    ]
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"

    hints = [
        "{{rb:Costruisci}} {{lb:.rifugio}} {{rb:usando}} {{yb:mkdir .rifugio}}"
        "{{rb: - ricorda il punto!}}"
    ]
    commands = [
        "mkdir .rifugio"
    ]

    def block_command(self):
        return unblock_commands_with_mkdir_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step7()


class Step7(StepTemplateMkdir):
    story = [
        "Controlla se è davvero nascosto. Usa {{yb:ls}} per "
        "controllare se è visibile."
    ]

    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"

    commands = [
        "ls"
    ]

    hints = [
        "{{rb:Usa}} {{yb:ls}}{{rb:, non ls -a, per controllare se il tuo rifugio "
        "è nascosto.}}"
    ]

    def next(self):
        Step8()


class Step8(StepTemplateMkdir):
    story = [
        "{{gb:Ottimo, non possiamo vederlo nel fienile.}}",
        "Ora controlliamo con {{yb:ls -a}} per vedere se esiste veramente!"
    ]
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"
    commands = [
        "ls -a"
    ]
    hints = [
        "{{rb:Usa}} {{yb:ls -a}} {{rb:per guardare.}}"
    ]

    def next(self):
        Step9()


class Step9(StepTemplateMkdir):
    story = [
        "{{gb:Ha funzionato! Hai davvero creato qualcosa nascosto.}}",
        "\nRuth: {{Bb:Hai fatto qualcosa... di fantastico!",
        "... ma sfortunatamente io non posso vederlo... potresti mettere me "
        "e gli animali la dentro?}}\n",
        "{{lb:Sposta}} tutti dentro {{lb:.rifugio}}, "
        "uno a uno.\n"
    ]
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile"
    all_commands = [
        "mv Trotter .rifugio/",
        "mv Trotter .rifugio",
        "mv Margherita .rifugio/",
        "mv Margherita .rifugio",
        "mv Cobweb .rifugio/",
        "mv Cobweb .rifugio",
        "mv Ruth .rifugio/",
        "mv Ruth .rifugio"
    ]

    def block_command(self):
        return unblock_commands(self.last_user_input, self.all_commands)

    def check_command(self):

        # If we've emptied the list of available commands, then pass the level
        if not self.all_commands:
            return True

        # If they enter ls, say Well Done
        if self.last_user_input == 'ls' or self.last_user_input == "ls -a":
            hint = "\n{{gb:Ottimo lavoro guardare attorno.}}"
            self.send_text(hint)
            return False

        # check through list of commands
        end_dir_validated = False
        self.hints = [
            "{{rb:Usa}} {{yb:" + self.all_commands[0] + "}} "
            "{{rb:per continuare}}"
        ]

        end_dir_validated = self.current_path == self.end_dir

        # if the validation is included
        if self.last_user_input in self.all_commands and \
                end_dir_validated:

            # Remove both elements, with a slash and without a slash
            if self.last_user_input[-1] == "/":
                self.all_commands.remove(self.last_user_input)
                self.all_commands.remove(self.last_user_input[:-1])
            else:
                self.all_commands.remove(self.last_user_input)
                self.all_commands.remove(self.last_user_input + "/")

            if len(self.all_commands) == 1:
                hint = (
                    "\n{{gb:Ottimo! spostane ancora uno nel}}"
                    " {{yb:.rifugio}}"
                )
            elif len(self.all_commands) > 0:
                hint = "\n{{gb:Ottimo! Spostane " + \
                    str(len(self.all_commands) / 2) + \
                    " altri.}}"
            else:
                hint = "\n{{gb:Premi Invio per continuare}}"

            self.send_text(hint)

        else:
            self.send_text("\n" + self.hints[0])

        # Always return False unless the list of valid commands have been
        # emptied
        return False

    def next(self):
        Step10()


class Step10(StepTemplateMkdir):
    story = [
        "{{lb:Vai}} verso {{lb:.rifugio}} con Ruth e con gli "
        "animali."
    ]
    start_dir = "~/fattoria/fienile"
    end_dir = "~/fattoria/fienile/.rifugio"
    hints = [
        "{{rb:Digita}} {{yb:cd .rifugio/}} {{rb:per andare dentro il}} "
        "{{lb:.rifugio}}{{rb:.}}"
    ]

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step11()


class Step11(StepTemplateMkdir):
    story = [
        "Dai uno {{lb:sguardo attorno}} per controllare se hai spostato tutti."
    ]
    start_dir = "~/fattoria/fienile/.rifugio"
    end_dir = "~/fattoria/fienile/.rifugio"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Guarda attorno usando}} {{yb:ls}}{{rb:.}}"
    ]
    last_step = True

    def next(self):
        NextStep(self.xp)
