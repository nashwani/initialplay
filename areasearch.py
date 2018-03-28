import urllib.request
import json
from setupCfg import SetupCfg
import ssl

class AreaSearch(object):
    # static variable
    geoCodeUrl_prefix = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/id?geoid="

    @staticmethod
    def getFilledSuffix():
        return "&minBeds="+str(1)+"&maxBeds="+str(2)

    def _init_(self, name):
        self.name = name

    def getPropertiesInGeocodeWithBeds(self, geoCode):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        propertiesInGeocodeWithBeds = AreaSearch.geoCodeUrl_prefix + \
            geoCode + AreaSearch.getFilledSuffix()
        request = urllib.request.Request(propertiesInGeocodeWithBeds)
        request.add_header("Accept", "application/json")
        request.add_header("apikey", SetupCfg().getPropValueFromIniFile('api-key'))
        webUrl = urllib.request.urlopen(request, context=ctx)
        responseData = webUrl.read()
        encoding = webUrl.info().get_content_charset('utf-8')
        responseJson = json.loads(responseData.decode(encoding))
        # print (responseJson)
        return responseJson
