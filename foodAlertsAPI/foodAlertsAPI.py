import requests
from foodAlertsAPI.Alert import Alert;

class foodAlertsAPI:

    # a negative limit value would return all entries
    def getAlerts(self, quantifier=None, params={}):
        """Gets alerts from the FSA Food Alerts API

        Args:
            quantifier: The quantifier can be an int n, in which case the function returns the last n
                        alerts. The quantifier can also be a date string in ISO format, in which case 
                        the function returns the alerts published since the given date.
        """

        # if quantifier is an int, then use the limit param
        try:
            limit = int(quantifier)
            r = requests.get(f"https://data.food.gov.uk/food-alerts/id?_limit={limit}", params=params)
            print(r.url)

        except ValueError:
            # if quantifier is not an int, try if it works as an iso datetime string
            try: 
                since = quantifier
                r = requests.get(f"https://data.food.gov.uk/food-alerts/id?since={since}", params=params)
                print(r.url)
                r.raise_for_status()
        
            except requests.HTTPError:
                raise ValueError("""Quantifier must be an integer or an ISO datetime string
            and params should be a valid string:string dictionary""")

        items = r.json()["items"]   
        alerts = [Alert(a) for a in items]

        return alerts
 
    def searchAlerts(self, query, params={}):

        try:
            r = requests.get(f"https://data.food.gov.uk/food-alerts/id?search={query}", params=params)
            r.raise_for_status()

            items = r.json()["items"]   
            alerts = [Alert(a) for a in items]
        
        except requests.HTTPError:
            raise ValueError("""Query must be a valid search query string 
        and params should be a valid string:string dictionary""")

        return alerts

    def getAlert(self, ID):
        
        try:
            r = requests.get(f"https://data.food.gov.uk/food-alerts/id/{ID}")
            r.raise_for_status()

            alert = Alert(r.json()["items"][0])
        
        except requests.HTTPError:
            raise ValueError("Argument must be a valid alert ID")

        return alert
            