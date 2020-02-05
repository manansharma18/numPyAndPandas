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
The difference between serie and nd array is that series automatically aligns data based on labels. thus you can write computation without thinking about the labels. 

Value in dataframe is derived from the value in the dictonary and the indexes are the keys of the dictonary. There can be list in dictonary and dictonary in list

if you use dataframe.T then transposed dataframe is returned and if you use np.transpose(dataframe) then ndarray is returned. 

dataframe.fillna('0'): Fills every NaN value with 0. 
dataframs.fillna({0 : 1 , 5 : 1.2 }) : Fills NaN in 0 row with 1 and in row 5 with 1,2. 
dataframe.fillna(method = 'ffill') fills NaN with the previous value in the column. 
print(dataFrame.dropna()) // drops rows with NaN
print(dataFrame.dropna(axis = 1)) // drops columns with NaN
dataFrame.duplicated() // returns true if the rows are duplicate
dataFrame.drop_duplicated(['column 1'])// drop the duplicate values in column 1
dataFrame.drop_duplicated()//drop the duplicate rows
.read_csv() : Will read the csv file

Graphs can be added in two ways 
Object oriented and functional method

In object oriented ploting you generate an empty plot and then poplulate it with figures, labels and values. 
%matplotlib inline will plot graphs inline. 
