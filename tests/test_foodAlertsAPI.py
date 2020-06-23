from foodAlertsAPI import foodAlertsAPI, Alert, Problem, ProductDetails, RelatedMedia, BatchDescription, Allergen, Business, PathogenRisk
from datetime import date

f = foodAlertsAPI()

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
    
def testAlertObjectFromGetAlertHasRequiredProps():
    alert = f.getAlert("FSA-AA-01-2019")
        
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


# ---------- this section checks that the same Alert fetched from different endpoints is parsed correctly ---------- #
def testAlertObjectActionTaken():
    alert1 = f.getAlert("FSA-AA-01-2018")
        
    assert(alert1.actionTaken() != None)
    assert(isinstance(alert1.actionTaken(), str))
        
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2018"})[0]
        
    assert(alert2.actionTaken() != None)
    assert(isinstance(alert2.actionTaken(), str))
    
def testAlertObjectConsumerAdvice():
    alert1 = f.getAlert("FSA-AA-01-2018")
            
    assert(alert1.consumerAdvice() != None)
    assert(isinstance(alert1.consumerAdvice(), str))
            
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2018"})[0]
            
    assert(alert2.consumerAdvice() != None)
    assert(isinstance(alert2.consumerAdvice(), str))
    
def testAlertObjectSMSText():
    alert1 = f.getAlert("FSA-AA-01-2018")
                
    assert(alert1.SMStext() != None)
    assert(isinstance(alert1.SMStext(), str))
                
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2018"})[0]
                
    assert(alert2.SMStext() != None)
    assert(isinstance(alert2.SMStext(), str))
    
def testAlertObjectTwitterText():
    alert1 = f.getAlert("FSA-AA-01-2018")
                    
    assert(alert1.twitterText() != None)
    assert(isinstance(alert1.twitterText(), str))
                    
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2018"})[0]
                    
    assert(alert2.twitterText() != None)
    assert(isinstance(alert2.twitterText(), str))
    
def testAlertObjectAlertURL():
    alert1 = f.getAlert("FSA-AA-01-2018")
                        
    assert(alert1.alertURL() != None)
    assert(isinstance(alert1.alertURL(), str))
                        
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2018"})[0]
                        
    assert(alert2.alertURL() != None)
    assert(isinstance(alert2.alertURL(), str))
    
def testAlertObjectShortURL():
    alert1 = f.getAlert("FSA-AA-01-2018")
                            
    assert(alert1.shortURL() != None)
    assert(isinstance(alert1.shortURL(), str))
                            
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2018"})[0]
                            
    assert(alert2.shortURL() != None)
    assert(isinstance(alert2.shortURL(), str))
    

def testAlertObjectRelatedMedia():
    """getAlert() and getAlerts(detailed=True) return different types for relatedMedia. This test checks
    whether the parsing is correct and gives the same result for each case
    """ 
    
    # this alert is known to have a relatedMedia property
    alert1 = f.getAlert("FSA-AA-01-2019")
    
    assert(alert1.relatedMedia() != None)
    assert(all(isinstance(a, RelatedMedia) for a in alert1.relatedMedia()))
    assert(all(isinstance(m.id(), str) for m in alert1.relatedMedia()))
    
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2019"})[0]
    
    assert(alert2.relatedMedia() != None)
    assert(all(isinstance(a, RelatedMedia) for a in alert2.relatedMedia()))
    assert(all(isinstance(m.id(), str) for m in alert2.relatedMedia()))
    
def testAlertObjectProblem():
    # this alert is known to have the problem property
    alert1 = f.getAlert("FSA-AA-01-2019")
        
    assert(alert1.problem() != None)
    assert(all(isinstance(p, Problem) for p in alert1.problem()))
    assert(all(isinstance(p.riskStatement(), str) for p in alert1.problem()))
    
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2019"})[0]
    assert(alert2.problem() != None)
    assert(all(isinstance(p, Problem) for p in alert2.problem()))
    assert(all(isinstance(p.riskStatement(), str) for p in alert2.problem()))
    
def testAlertObjectProblemAllergen():
    alert1 = f.getAlert("FSA-AA-01-2019")
    for p in alert1.problem():
        for a in p.allergen():
            assert(isinstance(a, Allergen))
            assert(isinstance(a.label(), str))
            assert(isinstance(a.notation(), str))
            assert(isinstance(a.riskStatement(), str))
            
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2019"})[0]
    for p in alert2.problem():
        for a in p.allergen():
            assert(isinstance(a, Allergen))
            assert(isinstance(a.label(), str))
            assert(isinstance(a.notation(), str))
            assert(isinstance(a.riskStatement(), str))
            
def testAlertObjectProblemAllergenLabels():
    alert = f.getAlert("FSA-AA-01-2019")
    assert(all(isinstance(a, str) for a in alert.allergenLabels()))

            
def testAlertObjectProblemPathogenRisk():
    alert = f.getAlert("FSA-PRIN-42-2019")
        
    for p in alert.problem():
        assert(isinstance(p.pathogenRisk(), PathogenRisk))
        assert(isinstance(p.pathogenRisk().label(), str))
        assert(isinstance(p.pathogenRisk().notation(), str))
        assert(isinstance(p.pathogenRisk().riskStatement(), str))
            
        
def testAlertObjectProductDetails():
    # this alert is known to have the productDetails property
    alert1 = f.getAlert("FSA-AA-01-2019")
        
    assert(alert1.productDetails() != None)
    assert(all(isinstance(p, ProductDetails) for p in alert1.productDetails()))
    assert(all(isinstance(p.productName(), str) for p in alert1.productDetails()))
        
    for p in alert1.productDetails():
        for b in p.batchDescription():
            assert(isinstance(b, BatchDescription))
            
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-01-2019"})[0]
    assert(alert2.productDetails() != None)
    assert(all(isinstance(p, ProductDetails) for p in alert2.productDetails()))
    assert(all(isinstance(p.productName(), str) for p in alert2.productDetails()))
            
    for p in alert2.productDetails():
        for b in p.batchDescription():
            assert(isinstance(b, BatchDescription))
        
def testAlertObjectReportingBusiness():
    alert1 = f.getAlert("FSA-PRIN-23-2018")
    assert(alert1.reportingBusiness() != None)
    assert(isinstance(alert1.reportingBusiness(), str))
    
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-PRIN-23-2018"})[0]
    assert(alert2.reportingBusiness() != None)
    assert(isinstance(alert2.reportingBusiness(), str))
    
def testAlertObjectOtherBusiness():
    alert1 = f.getAlert("FSA-PRIN-23-2018")
    assert(alert1.otherBusiness() != None)
    for a in alert1.otherBusiness():
        assert(isinstance(a, Business))
        assert(isinstance(a.commonName(), str))
        
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-PRIN-23-2018"})[0]
    assert(alert2.otherBusiness() != None)
    for a in alert2.otherBusiness():
        assert(isinstance(a, Business))
        assert(isinstance(a.commonName(), str))
        
def testAlertObjectPreviousAlert():
    alert1 = f.getAlert("FSA-AA-10-2019-update-1")
    assert(alert1.previousAlert() != None)
    assert(isinstance(alert1.previousAlert(), str))
    
    alert2 = f.getAlerts(1, detailed=True, filters={"notation":"FSA-AA-10-2019-update-1"})[0]
    assert(alert2.previousAlert() != None)
    assert(isinstance(alert2.previousAlert(), str))