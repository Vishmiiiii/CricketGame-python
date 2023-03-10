import pandas as pd
print()
print("             WELCOME TO T20 CRICKET MATCH !!!")
print()
print("These are the teams that will be playing in this tournament")
print()
print("              ----------SRI LANKA----------")
GroupAteam1=[['Dasun Shanaka-captain',30],['Avishka Fernando',23],['Bhanuka Rajapaksa',29],['Pathum Nissanka',23],['Dinesh Chandimal',31],['Dhananjaya de Silva',30],['Wanindu Hasaranga',24],['Chamika Karunaratne',25],['Maheesh Theekshana',21],['Binura Fernando',26],['Lahiru Kumara',24]]


df1 = pd.DataFrame(GroupAteam1,columns=['Name','Age'])
df1.to_csv("GroupAteam1.csv",index=False)
print(df1)

print()
print("              ----------BANGLADESH----------")
GroupAteam2=[['Mahmudullah-Captain',35],['Liton Das',27],['Mohammad Naim',22],['Nurul Hasan',27],['Mushfiqur Rahim',34],['Mahedi Hasan',26],['Shakib Al Hasan',34],['Afif Hossain',22],['Shamim Hossain',21],['Mohammad Saifuddin',24],['Soumya Sarkar',28]]
df2 = pd.DataFrame(GroupAteam2,columns=['Name','Age'])
df2.to_csv("GroupAteam2.csv",index=False)
print(df2)

print()
print("              ----------PAKISTAN----------")
GroupAteam3=[['Babar Azam-Captain',27],['Asif Ali',30],['Shoaib Malik',39],['Fakhar Zaman',31],['Haider Ali',21],['Mohammad Rizwan',29],['Sarfaraz Ahmed',34],['Shadab Khan',23],['Mohammad Hafeez',41],['Mohammad Nawaz',27],['Khushdil Shah',26]]
df3 = pd.DataFrame(GroupAteam3,columns=['Name','Age'])
df3.to_csv("GroupAteam3.csv",index=False)
print(df3)

print()
print("              ----------AUSTRALIA----------")
GroupAteam4=[['Aaron Finch-Captain',34],['Steven Smith',32],['David Warner',34],['Josh Inglis',	26],['Matthew Wade',33],['Ashton Agar',	28],['Mitchell Marsh',29],['Glenn Maxwell',33],['Marcus Stoinis',32],['Dan Christian',38],['Daniel Sams',28]]
df4 = pd.DataFrame(GroupAteam4,columns=['Name','Age'])
df4.to_csv("GroupAteam4.csv",index=False)
print(df4)

print()
print("              ----------NEW ZEALAND----------")
GroupBteam1=[['Temba Bavuma-Captain',31],['Reeza Hendricks',32],['Aiden Markram',27],['David Miller',32],['Rassie van der Dussen',32],['Quinton de Kock',28],['Heinrich Klaasen',30],['Wiaan Mulder',23],['Dwaine Pretorius',32],['George Linde',29],['Andile Phehlukwayo',25]]

df5 = pd.DataFrame(GroupBteam1,columns=['Name','Age'])
df5.to_csv("GroupBteam1.csv",index=False)
print(df5)

print()
print("              ----------ENGLAND----------")
GroupBteam2=[['Eoin Morgan-Captain',35],['Liam Livingstone',28],['Dawid Malan',34],['Jason Roy',31],['Liam Dawson',31],['James Vince',30],['Jonny Bairstow',32],['Sam Billings',30],['Jos Buttler',31],['Moeen Ali',34],['Tom Curran',26]]
df6 = pd.DataFrame(GroupBteam2,columns=['Name','Age'])
df6.to_csv("GroupBteam2.csv",index=False)
print(df6)

print()
print("              ----------SOUTH AFRICA----------")
GroupBteam3=[['Kane Williamson-Captain',31],['Mark Chapman',27],['Martin Guptill',35],['Devon Conway',30],['Glenn Phillips',24],['Tim Seifert',26],['Todd Astle',35],['Daryl Mitchell',30],['James Neesham',31],['Mitchell Santner',29],['Tim Southee',32]]
df7 = pd.DataFrame(GroupBteam3,columns=['Name','Age'])
df7.to_csv("GroupBteam3.csv",index=False)
print(df7)

print()
print("              ----------INDIA----------")
GroupBteam4=[['Virat Kohli-Captain',32],['Rohit Sharma',34],['KL Rahul',29],['Suryakumar Yadav',31],['Shreyas Iyer',26],['Ishan Kishan',23],['Rishabh Pant',24],['Ravindra Jadeja',32],['Axar Patel',27],['Hardik Pandya',28],['Shardul Thakur',29]]
df8 = pd.DataFrame(GroupBteam4,columns=['Name','Age'])
df8.to_csv("GroupBteam4.csv",index=False)
print(df8)
