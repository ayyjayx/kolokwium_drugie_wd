# ZESTAW A

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cars.csv', header=0, sep=';')
waga = df[(df['Weight']<2200)]
HP = (df.groupby(['Model year', 'Horsepower'], as_index=False).mean().groupby('Model year')['Horsepower'].mean())
wykres = HP.plot.bar(legend=False, xlabel='Rok produkcji', ylabel='Średnia moc',
                     title='Średnia moc silnika w poszczególnych latach', color='g')
plt.savefig('wykres.png')
plt.show()
