import logging
import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts

symbole = [".", "..", "..."]
n = len(symbole)

class Epoch(plugins, Plugin):
    __author__ = 'samy'
    __version__ = '1.0.0'
    __name__ = 'epoch-counter'
    __license__ = 'MIT'
    __description__ = 'counts epochs mod 2'

    def __init__(self):
        self.epoch_counter = 0

    def on_loaded(self):
        logging.info("epochs counter loaded")

    def on_ui_setup(self, ui):
        ui.add_element('epochs', LabeledValue(color=BLACK, label='Epochs ', value = symbole[self.epoch_counter],
                                              position=(ui.width() / 2 + 50, ui.height() - 45),
                                              label_font=fonts.Bold, text_font=fonts.Medium))

    def on_ui_update(self, ui):
        ui.set('epochs', symbole[self.epoch_counter])

    def on_epoch(self, agent, epoch, epoch_data):
        self.epoch_counter = (self.epoch_counter + 1) % n
