import pandas as pd
import matplotlib.pyplot as plt


players = pd.read_csv("data/players.csv") #leggiamo i giocatori e capiamo cosa c'è dentro
country_counts = players['birthPlaceCountry'].value_counts() #contiamo i giocatori per nazione
top_countries = country_counts.head(10) #ne selezioniamo solo 10


plt.figure(figsize=(12,6))
plt.bar(top_countries.index, top_countries.values, color='skyblue')
plt.title("Top 10 nazioni dei giocatori")
plt.xlabel("Nazione")
plt.ylabel("Numero di giocatori")
plt.xticks(rotation=45)
plt.show()


plt.savefig("img/top_nazioni.png")
