import requests
from Alert import Alert;

class foodAlertsAPI:

    def getAlerts(self):
        r = requests.get("https://data.food.gov.uk/food-alerts/id?_limit=11")
        return Alert(r.json()["items"][5])


f = foodAlertsAPI()
alert = f.getAlerts()



