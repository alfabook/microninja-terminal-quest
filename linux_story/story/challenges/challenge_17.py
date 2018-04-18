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


from linux_story.story.terminals.terminal_mv import TerminalMv
from linux_story.story.terminals.terminal_echo import TerminalEcho
from linux_story.story.challenges.challenge_18 import Step1 as NextStep
from linux_story.step_helper_functions import unblock_cd_commands
from microninja_profile.apps import (
    save_app_state_variable, load_app_state_variable
)


# This is for the challenges that only need ls
class StepTemplateMv(TerminalMv):
    challenge_number = 17


# This is for that challenges that need echo
class StepTemplateEcho(TerminalEcho):
    challenge_number = 17


class Step1(StepTemplateMv):
    story = [
        "Sei nella tua stanza, in piedi di fronte allo {{bb:.scrigno}} "
        "contenente tutti i comandi imparati sinora.",
        "Forse c'è qualcos'altro nascosto nella casa?",
        "{{lb:Guarda}} nell'andito {{lb:dietro te}}. Ricorda, "
        "dietro te è {{lb:..}} or {{lb:../}}"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    hints = [
        "{{rb:Guarda dietro te}} {{yb:ls ../}}"
    ]
    commands = [
        "ls ..",
        "ls ../"
    ]

    def next(self):
        Step2()


class Step2(StepTemplateMv):
    story = [
        "Vedi porte verso il tuo {{bb:giardino}}, {{bb:cucina}}, "
        "{{bb:camera-mia}} e {{bb:camera-genitori}}.",
        "Non abbiamo ancora controllato bene la camera dei genitori.",
        "{{lb:Vai nella camera-genitori}}."
    ]

    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-genitori"

    # This is for the people who are continuing to play from the
    # beginning.
    # At the start, add the fattoria directory to the file system
    # Also add the mappa and journal in your Mum's room
    story_dict = {
        "Cobweb, Trotter, Margherita, Ruth": {
            "path": "~/fattoria/fienile"
        },
        "MKDIR, chiave-inglese, martello, sega, metro": {
            "path": "~/fattoria/capanno-attrezzi"
        },
        "casa-fattoria": {
            "path": "~/fattoria",
            "directory": True
        },
        # this should be added earlier on, but for people who have updated,
        # we should figure out how to give them the correct file system
        "ECHO, diario-mamma, mappa": {
            "path": "~/casa-mia/camera-genitori/.sicuro"
        }
    }

    path_hints = {
        "~/casa-mia/camera-mia": {
            "bloccato": "\n{{rb:Usa}} {{yb:cd ../}} {{rb:per tornare indietro.}}"
        },
        "~/casa-mia": {
            "non_bloccato": "\n{{gb:Ottimo lavoro! Ora vai nella}} {{lb:camera-genitori}}{{gb:.}}",
            "bloccato": "\n{{rb:Usa}} {{yb:cd camera-genitori/}} {{rb:per andarci.}}"
        }
    }

    def check_command(self):
        if self.current_path == self.end_dir:
            return True
        elif "cd" in self.last_user_input and not self.get_command_blocked():
            hint = self.path_hints[self.current_path]["non_bloccato"]
        else:
            hint = self.path_hints[self.current_path]["bloccato"]

        self.send_text(hint)

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step3()


class Step3(StepTemplateMv):
    story = [
        "Guarda attorno {{lb:attentamente}}."
    ]
    start_dir = "~/casa-mia/camera-genitori"
    end_dir = "~/casa-mia/camera-genitori"

    hints = [
        "{{rb:Usa il comando}} {{yb:ls -a}} {{rb:per guardare attorno attentamente.}}"
    ]
    commands = [
        "ls -a",
        "ls -a .",
        "ls -a ./"
    ]

    def block_command(self):
        return unblock_cd_commands(self.last_user_input)

    def next(self):
        Step4()


class Step4(StepTemplateMv):
    story = [
        "C'è un {{lb:.sicuro}}!",
        "Forse contiene qualcosa di utile. {{lb:Controlla}} il "
        "{{lb:.sicuro}}."
    ]

    commands = [
        "ls .sicuro",
        "ls .sicuro/",
        "ls -a .sicuro",
        "ls -a .sicuro/"
    ]
    start_dir = "~/casa-mia/camera-genitori"
    end_dir = "~/casa-mia/camera-genitori"
    hints = [
        "{{rb:Controlla in}} {{lb:.sicuro}} {{rb:con}} {{lb:ls}}{{rb:.}}",
        "{{rb:Usa}} {{yb:ls .sicuro}} {{rb:per guardare dentro .sicuro.}}"
    ]

    def next(self):
        Step5()


# This class is here so if the user checks the diary,
# they get told off
class CheckDiaryStep(StepTemplateMv):
    def __init__(self, check_diary=0):
        self.check_diary = check_diary
        StepTemplateMv.__init__(self)

    def check_command(self):
        checked_diary = load_app_state_variable(
            "linux-story", "checked_mums_diary"
        )
        # Check to see if the kid reads his/her Mum's journal
        if self.last_user_input == 'cat .sicuro/diario-mamma' and \
                not checked_diary:
            self.send_hint(
                "\n{{rb:Hai letto il diario di mamma!}} "
                "{{ob:La tua curiosaggine è stata annotata.}}"
            )
            save_app_state_variable("linux-story", "checked_mums_diary", True)
            return False

        return StepTemplateMv.check_command(self)


class Step5(CheckDiaryStep):
    story = [
        "Quindi hai trovato il diario di mamma?",
        "Probabilmente non dovresti leggerlo...",
        "Cos'altro c'è? {{lb:esaminiamo}} quella {{lb:mappa}}."
    ]
    start_dir = "~/casa-mia/camera-genitori"
    end_dir = "~/casa-mia/camera-genitori"
    hints = [
        "{{rb:Usa}} {{lb:cat}} {{rb:per leggere la}} {{lb:mappa}}{{rb:.}}",
        "{{rb:Usa}} {{yb:cat .sicuro/mappa}} {{rb:per leggere la mappa.}}"
    ]

    commands = "cat .sicuro/mappa"

    def next(self):
        Step6(self.check_diary)


class Step6(CheckDiaryStep):
    story = [
        "Quindi c'è una fattoria nei dintorni?",
        "Non sembra lontana da casa, appena dopo la via ventosa...",
        "Cos'è questa nota {{lb:ECHO}}? {{lb:Esamina}} la nota ECHO."
    ]

    start_dir = "~/casa-mia/camera-genitori"
    end_dir = "~/casa-mia/camera-genitori"
    commands = "cat .sicuro/ECHO"
    hints = [
        "{{rb:Usa il comando}} {{lb:cat}} {{rb:per leggere la nota}} {{lb:ECHO}} ",
        "{{rb:Usa}} {{yb:cat .sicuro/ECHO}} {{rb:per leggere la nota.}}"
    ]

    def next(self):
        Step7()


class Step7(StepTemplateEcho):
    story = [
        "Quindi la nota dice {{lb:echo ciao - ti farà dire ciao}}",
        "Testiamolo subito!. "
        "Usa il comando {{yb:echo ciao}}"
    ]
    hints = [
        "{{rb:Usa il comando}} {{yb:echo ciao}}"
    ]
    commands = [
        "echo ciao",
        "echo CIAO",
        "echo Ciao"
    ]
    start_dir = "~/casa-mia/camera-genitori"
    end_dir = "~/casa-mia/camera-genitori"
    last_step = True

    def next(self):
        NextStep(self.xp)
