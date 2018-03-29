#!/usr/bin/python

import configparser
import os

class SetupCfg(object):
    HERE = os.path.dirname(os.path.abspath(__file__))
    SETUP_FILENAME = 'setup.ini'
    def getPropValueFromIniFile(self, propertyName):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), SetupCfg.SETUP_FILENAME))
        propertyValue = config.get('global', propertyName)
        return propertyValue