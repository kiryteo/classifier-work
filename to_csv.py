"""script to convert fri, frii
ra dec catalog files to csv"""

import csv

with open('friicat_radec_1') as file:
    fr = file.readlines()

fields = ['RA', 'DEC']

with open('f1.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    for each in fr:
        each = each.strip()
        ra = each.split(' ')[1]
        dec = each.split(' ')[2]
        final_row = []
        final_row.append(ra)
        final_row.append(dec)
        csvwriter.writerow(final_row)


