import requests
from Alert import Alert;

class foodAlertsAPI:

    def getAlerts(self):
        r = requests.get("https://data.food.gov.uk/food-alerts/id?_limit=10")
        return Alert(r.json()["items"][1])


f = foodAlertsAPI()
alert = f.getAlerts()
print(alert.__dict__.keys())
