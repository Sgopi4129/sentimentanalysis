# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/py
# import numpy as np
#
# b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b)
#
# print(b[0,1,1])
# b[:,1,:]=[[9,9],[8,8]]
# print(np.zeros((2,3,3,2)))
# print(np.ones((4,2,2),dtype='int32'))
# print(np.full((2,2),99,dtype='float32'))
# print(np.full_like(b.shape,4))
# print(np.full_like(b,4))
# print(np.random.rand(4,2))
# print(np.random.rand(4,2,3))
# print(np.random.random_sample(b.shape))
# print(np.random.randint(-4,8,size=(3,3)))
# print(np.identity((5),dtype='int32'))
#
# arr=np.array([[1,2,3]])
# r1=np.repeat(arr,3,axis=0)
# print(r1)
#
# a=np.array([1,2,3])
# b=a.copy()
# b[0]=100
# print(a)
#
# a=np.array([1,2,3,4])
# print(a)
#
# a+=2
# print(a)
# a-=2
# print(a)

# print(a*2)
# print(a/2)
# print(np.sin(a))


# /*pandsa libraries*/

import pandas as pd
import numpy as np
# list1=['g','e','e','k','s']
# res=pd.Series(list1)
# print(res)


# data=np.array(['g','e','e','k','s'])
# ser=pd.Series(data,index=[11,12,13,14,15])
# print(ser)
#
# dict1={
#     'Geeks':10,
#     'for':40,
#     'geeks':30
# }
#
# dictresult=pd.Series(dict1)
# print(dictresult)