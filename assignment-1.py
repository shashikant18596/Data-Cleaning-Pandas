import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', 'Swiss Air']})
flight_number=df['FlightNumber']
flight_number.fillna(0,inplace=True)
flight_number = flight_number.astype('int')
for i in range(len(flight_number)):
    if flight_number[i] == 0:
        flight_number[i]= flight_number[i-1]+10
print(flight_number)
df['FlightNumber']= flight_number
print(df)

df[['From','To']]= df['From_To'].str.split("_",expand=True)
df.drop(['From_To'],axis=1,inplace=True)
print(df)
df=df[['From','To','FlightNumber','RecentDelays','Airline']]
print(df)
df['From'] = df['From'].str.capitalize()
df['To'] = df['To'].str.capitalize()
print(df)


Delays=pd.DataFrame(df['RecentDelays'].to_list(),columns=['delays-1','delays-2','delays-3'])
print(Delays)




                   
               
               
               
               






