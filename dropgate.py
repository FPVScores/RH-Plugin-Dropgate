import logging
from RHUI import UIField, UIFieldType, UIFieldSelectOption

class Dropgate():

    def __init__(self,rhapi):
        self.logger = logging.getLogger(__name__)
        self._rhapi = rhapi

    def init_plugin(self,args):
        ui = self._rhapi.ui
        ui.register_panel("fpvscores_dropgate", "FPVScores Dropgate", "settings")
        ui_dropgate_gpio = UIField(name = 'fpvscores_dropgate_gpio', label = 'Dropgate GPIO', field_type = UIFieldType.TEXT, desc = "Set the GPIO pin number for the dropgate", value = "17")
        fields = self._rhapi.fields
        fields.register_option(ui_dropgate_gpio, "fpvscores_dropgate")
        self.logger.info("Dropgate is ready")


    def trigger_drop(self,args):
        fpvscores_dropgate_gpio = self._rhapi.db.option("fpvscores_dropgate_gpio")
        self.logger.info("Dropping gate on GPIO: %s" % fpvscores_dropgate_gpio)        

    def reactivate_drop(self,args):
        fpvscores_dropgate_gpio = self._rhapi.db.option("fpvscores_dropgate_gpio")
        self.logger.info("Reactivating gate on GPIO: %s" % fpvscores_dropgate_gpio)