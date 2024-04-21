import matplotlib.pyplot as plt
import random as rnd

x = [0]     # lista x z wprowadzonym x pocz�tkowym x_0 = 0
y = [0]     # lista y z wprowadzonym y pocz�tkowym y_0 = 0
for i in range(1, 10000):
    random_number = rnd.random()    #liczba rzeczywista z przedzia�u [0;1)
    # je�li wylosowana liczba zawiera si� w [0;0.895652), to wybierany jest pierwszy uk�ad r�wna�
    if random_number < 0.895652:         
        x.append(0.787879 * x[i - 1] - 0.424242 * y[i - 1] + 1.758647)
        y.append(0.242424 * x[i - 1] + 0.859848 * y[i - 1] + 1.408065)
    # je�li wylosowana liczba zawiera si� w [0.895652;0.947826), to wybierany jest drugi uk�ad r�wna�
    elif random_number < 0.947826:
        x.append(-0.121212 * x[i - 1] + 0.257576 * y[i - 1] - 6.721654)
        y.append(0.151515 * x[i - 1] + 0.053030 * y[i - 1] + 1.377236)
    # je�li wylosowana liczba zawiera si� w [0.947826;1), to wybierany jest trzeci uk�ad r�wna�
    else:
        x.append(0.181818 * x[i - 1] - 0.136364 * y[i - 1] + 6.086107)
        y.append(0.090909 * x[i - 1] + 0.181818 * y[i - 1] + 1.568035)
plt.plot(x, y, ".", markersize=1)      #rozmiar punktu wielko�ci 1
plt.show()
