import pandas as pd
import numpy as np

name = input("What is your name? :")
if name == "mouad":
  print("nta fruiti rigel rohek")
else:
  print(f"Hello, {name}!")

data = {
    'Name': ['John', 'Emma', 'Alex', 'Sarah'],
    'Age': [28, 24, 32, 27],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

df = pd.DataFrame(data)
print("Basic DataFrame:\n", df)