import http.client

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/tennis-t2/en/schedules/2016-07-06/results.xml?api_key=avt52c5das7kngnh5xe7t554")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))