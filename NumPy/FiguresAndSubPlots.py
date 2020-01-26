import numpy as np
import matplotlib.pyplot as plt

my_first_figure = plt.figure("My first figure")
sub_plot1 = my_first_figure.add_subplot(2,3,1)
sub_plot6 = my_first_figure.add_subplot(2,3,6)
# k--- is for black colour
plt.plot(np.random.rand(50).cumsum(), 'k--')
#plt.show()

sub_plot2 = my_first_figure.add_subplot(2,3,2)
plt.plot(np.random.rand(50), 'go')
plt.show()
