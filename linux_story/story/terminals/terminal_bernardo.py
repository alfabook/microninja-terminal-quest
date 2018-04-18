#!/usr/bin/env python

#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A terminal for one of the challenges

# -*- coding: utf-8 -*-

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# Italian translation
# rebadged with microninja

from linux_story.story.terminals.terminal_eleonora import (
    TerminalNanoEleonora, TerminalMkdirEleonora
)

# Ideally put in the class, but otherwise have to repeat this across the
# different classes.
bernard_text = "Bernardo non ti fa guardare nello scantinato!"


class TerminalMkdirBernardo(TerminalMkdirEleonora):

    # These functions are repeated across the two classes.
    def block_command(self):
        if "cantina" in self.last_user_input and \
                (
                    "ls" in self.last_user_input or
                    "cat" in self.last_user_input
                ):
            print bernard_text
            return True
        else:
            return TerminalMkdirEleonora.block_command(self)

    def autocomplete_files(self, text, line, begidx, endidx, only_dirs=False,
                           only_exe=False):
        # if the path we're checking is in Bernard's basement, we should
        # return the same text:
        # Bernard stopped you going in the basement.
        completions = TerminalMkdirEleonora.autocomplete_files(
            self, text, line, begidx, endidx, only_dirs,
            only_exe
        )
        if "photocopier.sh" in completions:
            print "\n" + bernard_text
            return []
        else:
            return completions


class TerminalNanoBernardo(TerminalNanoEleonora):

    def block_command(self):
        if "cantina" in self.last_user_input and \
                (
                    "ls" in self.last_user_input or
                    "cat" in self.last_user_input
                ):
            print bernard_text
            return True
        else:
            return TerminalNanoEleonora.block_command(self)

    def autocomplete_files(self, text, line, begidx, endidx, only_dirs=False,
                           only_exe=False):
        completions = TerminalNanoEleonora.autocomplete_files(
            self, text, line, begidx, endidx, only_dirs,
            only_exe
        )
        if "photocopier.sh" in completions:
            print "\n" + bernard_text
            return []
        else:
            return completions
