#!/usr/bin/env python
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# FinishDialog.py
# This is the dialog that's shown when the final challenge is completed

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# rebadged with microninja
# Italian translation

from microninja.gtk3.microninja_dialog import KanoDialog


class FinishDialog(KanoDialog):

    def __init__(self):

        title_text = 'Hai completato il Terminale Magico!'
        description_text = (
            'Stiamo lavorando al prossimo capitolo. '            
        )

        KanoDialog.__init__(
            self,
            title_text=title_text,
            description_text=description_text,
            button_dict={
                'CHIUDI':
                {
                    'color': 'orange',
                    'return_value': 'close'
                }
            }
        )
