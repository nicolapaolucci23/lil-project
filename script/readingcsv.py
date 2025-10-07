import pandas as pd

players = pd.read_csv("data/players.csv") #leggiamo i giocatori e capiamo cosa c'è dentro
# print(players.head())
# print(players.columns)

# # Leggi teams
# teams = pd.read_csv("data/teams.csv") #leggiamo le squadre e capiamo cosa c'è dentro 
# print(teams.head())
# print(teams.columns)

# #players['dateOfBirth'] = pd.to_datetime(players['dateOfBirth']) #convertiamo in dattetime per poter filtrare
# #argentinianp = players[
#     (players["birthPlaceCountry"].str.lower() == "argentina") & #voglio sapeere gli argentini nati dal 2000 in su
#     (players["dateOfBirth"] > "1999-12-31")
# ]

# print(argentinianp)

country_counts = players['birthPlaceCountry'].value_counts()
# rint(country_counts)

# englandplayers=players[
#      (players["birthPlaceCountry"].str.lower() == "england") #& 
#      #(players["dateOfBirth"] > "1999-12-31")
#  ]
# print(englandplayers)

