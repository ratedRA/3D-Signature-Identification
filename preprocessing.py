import os
import codecs
from collections import Counter
from myhull import make_hull, initial
import csv	

csv_file = open('features.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['vertices', 'aera', 'volume', 'user'])

def make_dataset():

	direct = "Signatures/"
	files = os.listdir(direct)

	users = [direct + user for user in files]
	#print(users)

	for user in users:
		vertices, volume, area = make_hull(user)
		print(vertices, area, volume)

		label = user.split('_')
		label = label[0].split('/')[1]
		print(label)

		csv_writer.writerow([vertices, area, volume, label])
	csv_file.close()

make_dataset()
