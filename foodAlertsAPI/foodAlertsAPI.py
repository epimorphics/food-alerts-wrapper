import requests
from foodAlertsAPI.Alert import Alert;

class foodAlertsAPI:

    # a negative limit value would return all entries
    def getAlerts(self, quantifier=None):

        # if quantifier is an int, then use the limit param
        try:
            limit = int(quantifier)
            r = requests.get(f"https://data.food.gov.uk/food-alerts/id?_limit={limit}")
        
        except ValueError:
            # if quantifier is not an int, try if it works as an iso datetime string
            try: 
                since = quantifier
                r = requests.get(f"https://data.food.gov.uk/food-alerts/id?since={since}")
                r.raise_for_status()
        
            except requests.HTTPError:
                raise ValueError("Argument must be an integer or an ISO datetime string")

        items = r.json()["items"]   
        alerts = [Alert(a) for a in items]

        return alerts

    def searchAlerts(self, query):
        try:
            r = requests.get(f"https://data.food.gov.uk/food-alerts/id?search={query}")
            r.raise_for_status()

            items = r.json()["items"]   
            alerts = [Alert(a) for a in items]
        
        except requests.HTTPError:
            raise ValueError("Argument must be a valid search query string")

        return alerts

    def getAlert(self, ID):
        
        try:
            r = requests.get(f"https://data.food.gov.uk/food-alerts/id/{ID}")
            r.raise_for_status()

            alert = Alert(r.json()["items"][0])
        
        except requests.HTTPError:
            raise ValueError("Argument must be a valid alert ID")

        return alert
            