import matplotlib.pyplot as plt
from matplotlib import colors
import csv
from math import log10

bins=200
d = []
with open("C:/dev/geiger/geiger_20191228_201419.txt") as f:
	r = csv.reader(f, delimiter='\t')
	for row in r:
		v = float(row[2])
		#v = round(v/100,0)
		v = v/1000000
		if(v > 0):
			d.append(v)
print(len(d))
print(sum(d)/len(d))

dd = []
for v in d:
	dd.append(log10(v))
	
fig, axs = plt.subplots(1, 1, tight_layout = True)
N, bins, patches = axs.hist(dd, bins = bins)
fracs = N / N.max()
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
	color = plt.cm.viridis(norm(thisfrac))
	thispatch.set_facecolor(color)
axs.hist(dd, bins=bins, density=True)
plt.xlim(1, max(dd))
plt.title("Log10 Count Interval, Counts = " + str(len(d)))

plt.show()