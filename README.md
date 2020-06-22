# FSA Food Alerts API Python Wrapper

This is a Python wrapper for the FSA Food Alerts API, created with the aim of making interactions with the API much simpler so developers can focus on processing and analysing the data it provides.

This Python 3 wrapper is created using the [requests](https://requests.readthedocs.io/en/master/) package. It abstracts the details of HTTP requests away so that the user can just interact with API data. Using the wrapper, developers can access data from the API by simply calling intuitive functions, such as `getAlerts()` or `searchAlerts()`.

These functions also parse the HTTP response, so the user can simply access the response data as Python objects. 

## Example

```python
yearAgo = (datetime.now() - timedelta(days=365)).isoformat()
alerts = f.getAlerts(yearAgo)   # getting alerts from the past year

allergenCounts = defaultdict(int)

for alert in alerts:
    allergens = alert.allergenLabels()  # convenience functions such as allergenLabels() make it easy to access attributes in a complex data structure
    for allergen in allergens:
        allergenCounts[allergen] += 1

# get the 10 most frequently occurring allergens
sortedAllergens = [(k, v) for k, v in sorted(allergenCounts.items(), key=lambda item: item[1], reverse=True)][:10]
totalAllergensCount = sum(v for k, v in sortedAllergens)

labels = [k for (k, v) in sortedAllergens]
sizes = [v/totalAllergensCount for k, v in sortedAllergens]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.set_title('10 Most Common Allergens in the Past Year')
ax1.title.set_position([.5, 1.075])
ax1.axis('equal')

plt.show()
```

The example above plots a pie chart of the 10 most frequently occurring allergens in alerts over the past year. The entirety of data acquisition and parsing has been accomplished using only `getAlerts()` and `allergenLabels()`, allowing for succinct and readable code. 