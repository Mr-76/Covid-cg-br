import json
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt

def convert_to_seconds(date_string):
    date = datetime.strptime(date_string, "%d/%m/%Y")
    seconds = (date - datetime(1970, 1, 1)).total_seconds()

    return seconds


with open("dados.json", "r") as f:
    data = json.load(f)

x = [x["Data"] for x in data]

for i in range(len(x)):
    seconds = convert_to_seconds(x[i])
    x[i] = seconds

y = [y["total_de_doses1_aplicadas"] for y in data]

x = np.array(x).reshape(-1, 1)
y = np.array(y)


model = LinearRegression()
model.fit(x, y)

new_date = [convert_to_seconds("30/3/2022")]
new_date = np.array(new_date).reshape(-1, 1)
prediction = model.predict(new_date)
print("Predicted value for {} is {}".format(new_date[0], prediction[0]))

