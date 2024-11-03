# import pandas as pd
#
# list1=['Geeks','For','Geeks','is','portal','for','Geeks']
# print(pd.DataFrame(list1))
# i=1
# while(i<=70):
#     print('*',end=' ')
#     i+=1
# print(' ')
# data={'Name':['harry','tom','holand','dome'],
#       'Age':[45,39,23,22]}
# print(pd.DataFrame(data))
#
# print(' ')
# datac={
#     'Name':['Jai','Princi','Gaurav','Anuj'],
#     'Age':[27,24,22,32],
#     'Address':['Delhi','Kanpur','Allahabad','Kann'],
#     'Qualification':['Msc','MA','MCA','Phd']
# }
# df=pd.DataFrame(datac)
# print(df[['Name','Qualification']])
#
# import  pandas as pd
# data=pd.read_csv("nba.csv",index_col='Name')
# first=data.loc["Avery Bradley"]
# second=data.loc["R.J Hunter"]
# print(first,'\n\n\n',second)
# import numpy as np
# import pandas as pd
#
# index=['a','b','c','d','e']
# column=['A','B','C','D','E']
#
# df=pd.DataFrame(np.random.rand(5,5),index=index,columns=column)
# print(df)
#
# print('\n\n The reindex is started :\n',df.reindex(['b','c','d','e','j']))

import numpy as np
import pandas as pd


dictionary={
    'Name':['Rohith','Mouli','Naveen','Sravan'],
    'designation':['Bank employee','Professor','Software developer','Constructor']
}
data=pd.DataFrame(dictionary,index=['a','b','c','d'],columns=['Name','designation'])
print(data)