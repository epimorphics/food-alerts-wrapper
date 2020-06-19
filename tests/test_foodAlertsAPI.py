from foodAlertsAPI import foodAlertsAPI, Alert, Problem, ProductDetails, RelatedMedia
from datetime import date

f = foodAlertsAPI()

"""
Classes tests

-----------------------

getAlerts() tests

1. check that getAlerts returns array of Alert objects
2. check that getAlerts limit filter works
3. check that getAlerts type filters work
4. check that getAlerts offset parameter works - can't test because non deterministic API?
5. check that getAlerts sortby parameter works
 
"""

# getAlerts()

def testGetAlertsReturnsAlertList():
    alerts = f.getAlerts(10)
    
    assert all(isinstance(a, Alert) for a in alerts)
    
def testGetAlertsLimitWorks():
    alertsSize5 = f.getAlerts(5)
    assert len(alertsSize5) == 5
    
    alertsSize1 = f.getAlerts(1)
    assert len(alertsSize1) == 1
    
def testGetAlertsTypeFiltersWork():
    alertsAA = f.getAlerts(10, filters={"type":"AA"})
    assert all(alert.type()=="AA" for alert in alertsAA)
    
    alertsFAFA = f.getAlerts(10, filters={"type":"FAFA"})
    assert all(alert.type()=="FAFA" for alert in alertsFAFA)
    
    alertsPRIN = f.getAlerts(10, filters={"type":"PRIN"})
    assert all(alert.type()=="PRIN" for alert in alertsPRIN)

def testGetAlertsSortByWorks():
    alerts = f.getAlerts(10, sortBy="created")
    
    assert all(date.fromisoformat(alerts[i].created()) <= date.fromisoformat(alerts[i+1].created()) for i in range(len(alerts)-1))
    

# searchAlerts()

def testSearchAlertsReturnsAlertList():
    alerts = f.searchAlerts("milk", limit=5)
    
    assert all(isinstance(a, Alert) for a in alerts)
    
def testSearchAlertsLimitWorks():
    alertsSize5 = f.searchAlerts("milk", limit=5)
    assert len(alertsSize5) == 5
    
    alertsSize1 = f.searchAlerts("milk", limit=1)
    assert len(alertsSize1) == 1

def testSearchAlertsTypeFiltersWork():
    alertsAA = f.searchAlerts("milk", limit=5, filters={"type":"AA"})
    assert all(alert.type()=="AA" for alert in alertsAA)
    
    alertsFAFA = f.searchAlerts("eggs", limit=5, filters={"type":"FAFA"})
    assert all(alert.type()=="FAFA" for alert in alertsFAFA)
    
    alertsPRIN = f.searchAlerts("meat", limit=5, filters={"type":"PRIN"})
    assert all(alert.type()=="PRIN" for alert in alertsPRIN)
    
def testSearchAlertsSortByWorks():
    alerts = f.searchAlerts("milk", limit=5, sortBy="created")
        
    assert all(date.fromisoformat(alerts[i].created()) <= date.fromisoformat(alerts[i+1].created()) for i in range(len(alerts)-1))
    
# getAlert()

def testGetAlertReturnsAlertObject():
    alert = f.getAlert("FSA-AA-01-2018")
    
    assert(isinstance(alert, Alert))
    
# Classes

def testAlertObjectsHaveRequiredPropsInDefaultView():
    alert = f.getAlerts(1)[0]
    
    # any alert should have these fields in default view
    assert(alert.id() != None and isinstance(alert.id(), str))
    assert(alert.title() != None and isinstance(alert.title(), str))
    assert(alert.created() != None and isinstance(alert.created(), str))
    assert(alert.modified() != None and isinstance(alert.modified(), str))
    assert(alert.notation() != None and isinstance(alert.notation(), str))
    assert(alert.problem() != None and all(isinstance(a, Problem) for a in alert.problem()))
    assert(alert.productDetails() != None and all(isinstance(a, ProductDetails) for a in alert.productDetails()))
    assert(alert.status() != None and isinstance(alert.id(), str))
    assert(alert.type() != None and isinstance(alert.id(), str))
    
def testAlertObjectsHaveRequiredPropsInFullView():
    alert = f.getAlerts(1, detailed=True)[0]
    
    # any alert should have these fields in full view
    assert(alert.id() != None and isinstance(alert.id(), str))
    assert(alert.title() != None and isinstance(alert.title(), str))
    assert(alert.shortTitle() != None and isinstance(alert.shortTitle(), str))
    assert(alert.description() != None and isinstance(alert.description(), str))
    assert(alert.created() != None and isinstance(alert.created(), str))
    assert(alert.modified() != None and isinstance(alert.modified(), str))
    assert(alert.notation() != None and isinstance(alert.notation(), str))
    assert(alert.problem() != None and all(isinstance(a, Problem) for a in alert.problem()))
    assert(alert.productDetails() != None and all(isinstance(a, ProductDetails) for a in alert.productDetails()))
    assert(alert.status() != None and isinstance(alert.status(), str))
    assert(alert.type() != None and isinstance(alert.type(), str))
    
def testAlertObjectRelatedMedia():
    # this alert is known to have a relatedMedia property
    alert = f.getAlert("FSA-AA-01-2019")
    
    assert(alert.relatedMedia() != None)
    assert(all(isinstance(a, RelatedMedia) for a in alert.relatedMedia()))
    assert(all(isinstance(m.id(), str) for m in alert.relatedMedia()))
    
