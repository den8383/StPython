import pandas as pd
x = [('Gause', 1777),
    ('Pascal', 1623),
    ('Turing',1912),
    ('Bernoull', 1700),
    ('Fourier', 1768),
    ('Maxwell', 1831)]
df = pd.DataFrame(data=x, columns=['Name','BirthYear'])
print(df)
print(df['BirthYear'].sum())
print(df['BirthYear'].mean())
print(df.query("BirthYear < 1800"))
