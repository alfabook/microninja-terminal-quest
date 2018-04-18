#!/usr/bin/env python

#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A terminal for one of the challenges

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# rebadged with microninja

from linux_story.story.terminals.terminal_mkdir import TerminalMkdir
from linux_story.story.terminals.terminal_nano import TerminalNano
from linux_story.helper_functions import record_user_interaction


class TerminalMkdirEleonora(TerminalMkdir):
    eleanors_speech = ""

    def check_command(self):
        if self.last_user_input == "cat Eleonora":
            self.Eleonora_speaks()
            record_user_interaction(self, "cat_Eleonora")

        else:
            return TerminalMkdir.check_command(self)

    def Eleonora_speaks(self):
        '''Use this to get Eleonora to "speak"
        '''
        if self.eleanors_speech:
            self.send_text("\n" + self.eleanors_speech)


class TerminalNanoEleonora(TerminalNano):
    eleanors_speech = ""

    def check_command(self):
        if self.last_user_input == "cat Eleonora":
            self.Eleonora_speaks()
            record_user_interaction(self, "cat_Eleonora")

        else:
            return TerminalNano.check_command(self)

    def Eleonora_speaks(self):
        '''Use this to get Eleonora to "speak"
        '''
        if self.eleanors_speech:
            self.send_text("\n" + self.eleanors_speech)
