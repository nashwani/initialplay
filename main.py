from areasearch import AreaSearch
from setupCfg import SetupCfg

areaSearch = AreaSearch()
propertyDetails = areaSearch.getPropertiesInGeocodeWithBeds('PL0820000')
print(propertyDetails['status'])
print(SetupCfg().getPropValueFromIniFile('version'))
