data = np.array(np.arange(25).reshape(5,5))

index = pd.date_range('20200201', periods=5)

dataFrame = pd.DataFrame(data, index = index, columns = list('ABCDE'))

# E can be printed before A. Order can be manupulated. dataFrame takes first parameter as index
print(dataFrame.loc[index[1:3],['E','A']])
# Can select one element also
print(dataFrame.loc['2020-02-03',['B','D']][1])
# describe function describes the function. There is a option to pass the precision. CumSum sums every value of the matrix. 
# append creates a new matrix. To read a excel file pd.read_excel and to write to a csv use .to_csv
# group by function is same as sql. ,groupBy('Department')
    