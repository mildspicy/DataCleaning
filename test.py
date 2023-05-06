import pandas

pd = pandas.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a','b','c'])
print(pd)
print('________________________________')
pd = pd.loc[(pd['a'] == 1)]
print(pd)
