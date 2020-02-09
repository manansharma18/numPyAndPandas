import scipy 
from scipy.stats import spearmanr
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from pylab import rcParams
from scipy.stats import chi2_contingency
#%matplotlib inline
rcParams['figure.figsize'] = 14, 7
plt.style.use('seaborn-whitegrid')

address = '/Users/manansharma/Documents/Python/Business Requirement Data Science/mtcars.csv'
cars = pd.read_csv(address)
cars.column = ['car_name','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

#filtered_csv = pd.read_csv(address, usecols = ['car_name','mpg','cyl','disp','hp'])
#print(filtered_csv)
#print(cars.head())
#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

#sb.pairplot(cars)
#plt.show()

mpg = cars['mpg']
cyl = cars['cyl']
disp = cars['disp']
hp = cars['hp']

spearman_coeff, p_Value = spearmanr(mpg,cyl)

print('The value of spearman co-efficient and P value is %0.3f %0.3f' % (spearman_coeff, p_Value) )

#spearman_coeff, p_Value = spearmanr(disp,hp)
#print('The value of spearman co-efficient and P value is %0.3f %0.3f' % (spearman_coeff, p_Value) )
#sb.pairplot(mpg)
#plt.show()


table = pd.crosstab(cyl,mpg)
chi2, p , dof,expected = chi2_contingency(table.values)
#print(table)
print('chi and pvalue is %0.3f and %0.3f' %(chi2,p))


