#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# A terminal for one of the challenges

import os
import threading
import time
import ast
from linux_story.story.terminals.terminal_echo import TerminalEcho
from linux_story.commands_real import nano
from microninja.logging import logger


class TerminalNano(TerminalEcho):
    terminal_commands = ["ls", "cat", "cd", "mv", "echo", "mkdir", "nano"]
    SAVING_NANO_PROMPT = (
        "Salvi i cambiamenti effettuati (RISPONDERE \"No\" DISTRUGGERA' I CAMBIAMENTI) ? "
    )
    SAVE_FILENAME = "File Name to Write"

    # This is the content we want to end up with in the file.
    goal_nano_end_content = ""

    # This is the fake filepath of the nano file we want to change.
    goal_nano_filepath = ""

    # Save name we want to ask user to write
    goal_nano_save_name = ""

    def __init__(self, xp=""):

        ##############################################
        # nano variables

        # This is tracking the CURRENT nano content filepath,
        # not what we are aiming for
        self.nano_content = ""
        self.nano_running = False
        self.last_nano_prompt = ""
        self.ctrl_x = False
        self.on_nano_filename_screen = False
        self.exited_nano = True
        self.nano_x = 0
        self.nano_y = 0
        self.save_prompt_showing = False
        self.last_nano_filename = ""
        self.editable = ""
        ################################################

        TerminalEcho.__init__(self, xp)

    def do_nano(self, line):
        # line = the filepath of the nano file

        self.set_nano_running(True)

        # Read contents of the file
        text = self.read_goal_contents()
        self.set_nano_content(text)

        # Read nano in a separate thread
        t = threading.Thread(target=self.try_and_get_pipe_contents)
        t.daemon = True
        t.start()

        # If the line is given, it is the filepath of the file we are
        # adjusting.
        # if line:
        #    self.set_last_nano_filepath(line)

        nano(self.real_path, line)

    ##################################################################
    # nano functions

    def set_nano_running(self, nano_running):
        '''Set this while nano is running
        '''
        self.nano_running = nano_running

    def get_nano_running(self):
        return self.nano_running

    def quit_nano(self):
        self.cancel_everything()
        self.set_nano_running(False)

    def set_nano_content(self, nano_content):
        '''Setter for the self.nano_content for this Step
        '''
        self.nano_content = nano_content

    def get_nano_content(self):
        '''Getter for the self.nano_content for this Step
        '''
        return self.nano_content

    def set_nano_x(self, x):
        '''These can be updated by the individual Step instances
        to do something with the changed values
        '''
        self.nano_x = x

    def set_nano_y(self, y):
        '''These can be updated by the individual Step instances
        to do something with the changed values
        '''
        self.nano_y = y

    def set_ctrl_x_nano(self, ctrl_x):
        '''Setting whether the user pressed Ctrl X.
        ctrl_x is a bool.
        '''
        self.ctrl_x = ctrl_x

    def get_ctrl_x_nano(self):
        '''Getting whether the user pressed Ctrl X.
        '''
        return self.ctrl_x

    def set_last_prompt(self, last_prompt):
        '''Save last prompt.  This means we can see what the response
        is responding to.
        '''
        self.last_nano_prompt = last_prompt

    def set_on_filename_screen(self, on_filename_screen):
        self.on_nano_filename_screen = on_filename_screen

    def get_on_filename_screen(self):
        return self.on_nano_filename_screen

    def get_last_prompt(self):
        return self.last_nano_prompt

    def set_nano_content_values(self, content_dict):
        '''Set the x, y coordinates and the content.
        content_dict = {'x': 1, 'y': 2, 'text': ['line1', 'line2']}
        '''
        self.set_nano_x(content_dict["x"])
        self.set_nano_x(content_dict["y"])
        nano_content = "\n".join(content_dict["text"])
        self.set_nano_content(nano_content)
        self.set_save_prompt_showing(False)

    def cancel_everything(self):
        '''If the response of any prompt or statusbar is Cancel,
        then everything should be set to False
        '''
        self.set_save_prompt_showing(False)
        self.set_ctrl_x_nano(False)
        self.set_on_filename_screen(False)

    def set_save_prompt_showing(self, showing):
        self.save_prompt_showing = showing

    def get_save_prompt_showing(self):
        return self.save_prompt_showing

    def set_last_nano_filename(self, filename):
        '''Set the fake filepath of the actual nano file
        '''
        self.last_nano_filename = filename

    def get_last_nano_filename(self):
        '''Get the fake filepath of the actual nano file
        '''
        return self.last_nano_filename

    def get_editable(self):
        '''If nano is launched with a filename argument after,
        then when saving, the filename appears in the editable field.
        Get the last set one from this function.
        '''
        return self.editable

    def set_editable(self, editable):
        '''If nano is launched with a filename argument after,
        then when saving, the filename appears in the editable field.
        Get the last set one from this function.
        '''
        self.editable = editable

    def try_and_get_pipe_contents(self):
        try:
            self.get_pipe_contents()
        except Exception as e:
            logger.error(
                "\nErrore di nano, eccezione {}".format(str(e))
            )

            # TODO: Remove this when shipping
            print "\nErrore di nano, {}".format(str(e))
            self.send_text("\nErrore di nano, {}".format(str(e)))

    def get_pipe_contents(self):

        # Functon called when user has just opened nano
        self.opened_nano()
        pipename = "/tmp/linux-story-nano-pipe"

        if not os.path.exists(pipename):
            os.mkfifo(pipename)
        f = open(pipename)

        while self.get_nano_running():
            time.sleep(0.1)
            line = None

            for line in iter(f.readline, ''):

                # Assuming we're receiving something of the form
                # {x: 1, y: 1, text: ["line1", "line2"]}
                # {response: this is the response message}

                #############################
                # This part of the function sets all the environment variables.
                data = ast.literal_eval(line)

                if "contents" in data:
                    self.cancel_everything()
                    value = data["contents"]

                    if self.get_nano_content() != self.goal_nano_end_content:
                        self.set_nano_content_values(value)

                if "statusbar" in data:
                    value = data["statusbar"]
                    # Everything is set to False, since anything could
                    # have been cancelled
                    if value.strip().lower() == "cancelled":
                        self.cancel_everything()

                if "response" in data:
                    value = data["response"]
                    # If the last prompt is the saving nano buffer prompt,
                    # then the user has tried to exit without saving
                    # his/her work.

                    if self.get_last_prompt() == self.SAVING_NANO_PROMPT:
                        if value.lower() == "cancel":
                            self.cancel_everything()

                        elif value.lower() == "yes":
                            # Starting to save.
                            # Bring up the relevent prompt about entering
                            # the filename and pressing Y.
                            # Set variable that says the player is on this
                            # screen
                            self.set_save_prompt_showing(True)
                            self.set_on_filename_screen(True)

                        elif value.lower() == "no":
                            # Exited nano and chose not to save
                            # This may not need to be recorded.
                            self.quit_nano()

                    elif self.get_last_prompt() == self.SAVE_FILENAME:
                        if value.lower() == "no":
                            self.quit_nano()
                        elif value.lower() == "cancel":
                            self.cancel_everything()

                        # TODO: not sure this is needed
                        elif value.lower() == "aborted enter":
                            self.cancel_everything()

                if "prompt" in data:
                    value = data["prompt"]
                    self.set_last_prompt(value)

                    if "editable" in data:
                        self.set_editable(data["editable"])

                    if value == self.SAVE_FILENAME:
                        self.set_save_prompt_showing(False)
                        self.set_on_filename_screen(True)

                    # Do we set anything here?
                    elif value == self.SAVING_NANO_PROMPT:
                        self.set_save_prompt_showing(True)
                        self.set_on_filename_screen(False)

                if "saved" in data:
                    self.set_last_nano_filename(data["filename"])

                if "finish" in data:
                    self.quit_nano()
            #############################

            # This runs for any line in the for loop which is not
            # empty
            # Analogous with try, exception, else.
            # Else is called when the try (or in this case, the for loop)
            # is successful.
            else:
                if line:
                    # Run a check for self.nano_content.
                    # If this returns True, break out of the loop.
                    if self.check_nano_content():
                        return

    #########################################################################
    # Handler functions, triggered in different parts of the nano event loop.
    # Used for modifying in inheritence, so we can customise the individual
    # steps.
    def opened_nano(self):
        '''This is called when user has just opened nano.
        Use to display custom message.
        Default behaviour - if there is goal end text to be written in nano,
        display a hint telling the user what to write and how to exit.
        '''
        # Check that the opened filename matches the goal_filename
        correct_user_cmd = "nano {}".format(self.goal_nano_save_name)

        if not self.last_user_input == correct_user_cmd:
            hint = (
                "\n{{rb:Oops, hai aperto il file sbagliato! Premi}} " +
                "{{yb:Ctrl X}} {{rb:to exit.}}"
            )
            self.send_text(hint)

        elif self.goal_nano_end_content:
            hint = (
                "\n{{gb:Hai aperto nano! Ora accertati che il file dica}} "
                "{{yb:" + self.goal_nano_end_content +
                "}}{{gb:. Per uscire, premi Ctrl X.}}"
            )
            self.send_text(hint)

    #########################################################################
    def read_goal_contents(self):
        text = ""
        end_path = self.generate_real_path(self.goal_nano_filepath)

        if os.path.exists(end_path):
            # check contents of file contains the self.end_text
            f = open(end_path, "r")
            text = f.read()
            f.close()

        return text

    # TODO: better way of doing this?
    # This seems very messy.
    def check_nano_input(self):
        '''This is not called anywhere by default. The intention is that is
        this is called after nano has been closed in check_command.
        '''

        end_path = self.generate_real_path(self.goal_nano_filepath)

        if os.path.exists(end_path):
            # check contents of file contains the self.end_text
            f = open(end_path, "r")
            text = f.read()
            f.close()

            if text.strip() == self.goal_nano_end_content:
                return self.finish_if_server_ready(True)
            else:
                error_text = (
                    "\n{{rb:Il testo non è corretto! " +
                    "Digita}} {{yb:nano " + self.goal_nano_save_name + "}} "
                    "{{rb:per riprovare.}}"
                )
                self.send_text(error_text)

        else:
            error_text = (
                "\n{{rb:Il percorso del file}} {{lb:" +
                end_path +
                "}} {{rb:non esiste - hai salvato il tuo file correttamente?}}"
            )
            self.send_text(error_text)

    def check_nano_content(self):
        '''We keep this blank so we don't automatically get messages
        when opening nano.
        '''
        if not self.get_nano_running():
            return True

    def check_nano_content_default(self):
        '''We want to customise this for the individual Step classes.
        '''
        # Make the if statements cumulative, so you trickle down as less
        # conditions are satisfied.

        if not self.get_nano_running():

            # Call self.check_nano_input here?
            if self.get_last_nano_filename() == self.goal_nano_save_name:
                return True

            # This hint appears along another one, so this feels redundant.
            '''
            else:
                self.send_text(
                    "\n{{ob:Nome del file sbagliato. Prova a "
                    "digitare}} {{yb:nano}} {{ob:e premi Invio}} " +
                    self.get_last_nano_filename() + " " +
                    self.goal_nano_save_name
                )
            '''

        elif self.get_on_filename_screen() and \
                self.get_nano_content().strip() == self.goal_nano_end_content:

            if self.get_editable() == self.goal_nano_save_name:
                hint = (
                    "\n{{gb:Premi}} {{yb:Invio}} {{gb:per confermare il "
                    "nome del file.}}"
                )
            else:
                hint = (
                    "\n{{gb:Digita}} {{yb:" + self.goal_nano_save_name + "}} "
                    "{{gb:e premi}} {{yb:Invio}}"
                )
            self.send_text(hint)

        elif self.get_on_filename_screen():
            self.send_text(
                "\n{{ob:Oops, il tuo testo non è corretto. Premi}} "
                "{{yb:Ctrl C}} {{ob:per cancellare.}}"
            )

        elif self.get_save_prompt_showing():
            if self.get_nano_content().strip() == self.goal_nano_end_content:
                self.send_text(
                    "\n{{gb:Premi}} {{yb:Y}} {{gb:per confermare che vuoi "
                    "salvare.}}"
                )
            else:
                self.send_text(
                    "\n{{rb:Il testo scritto non è corretto! Digita}} {{yb:N}} "
                    "{{rb:per uscire da nano.}}"
                )

        elif self.get_nano_content().strip() == self.goal_nano_end_content:
            hint = (
                "\n{{gb:Eccellente! hai digitato}} {{lb:" +
                self.goal_nano_end_content +
                "}}{{gb:. Ora digita}} {{yb:Ctrl X}} {{gb:per uscire.}}"
            )
            self.send_text(hint)

        return False
