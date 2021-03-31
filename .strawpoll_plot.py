# INCOMPLETE - MAY NOT WORK CORRECTLY - DRAFT FILE
#
#
#
#
import matplotlib.pyplot as plt
# import StrawPoll_Scraper as scraper

import numpy as np
import pandas as pd


fig = plt.figure()
x = []
y = []

f = 'poll.csv'

with open(f, 'r') as fp:
	msft = pd.read_csv(fp, header=0, names=["Answer", "Votes"])

	for row in msft:
		x.append(str(row))
		y.append(str(row))



msft.plot(label='CSV DATA')
plt.xlabel('Answer')
plt.ylabel('# of Votes')
plt.title('StrawPoll_Plot')
plt.legend()
plt.show()
