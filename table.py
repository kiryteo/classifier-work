"""script to get csv file for Fieldname
RA Dec values from FITS table and create"""

import csv
from astropy.io import fits

fits_filename = 'first_14dec17.fits'

hd = fits.open(fits_filename)
#hd.info()

data0 = hd[0].data

data = hd[1].data

cols = hd[1].columns
#cols.info()

#print(cols[1])

fields = ['FLDNAME', 'RA', 'DEC']
with open('FIRST_catalog_ra_dec.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for i in range(len(data['FLDNAME'])):
        values_row = []
        values_row.append(data['FLDNAME'][i])
        values_row.append(data['RA'][i])
        values_row.append(data['DEC'][i])
        csvwriter.writerow(values_row)
    csvfile.close()
