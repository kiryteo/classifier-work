from astropy.io import fits

#fits_filename = '3C68-2.SP2B.PBCOR_22_064_03aug2012_16s_lta.FITS'
#fits_filename = '1120+143.SP2B.PBCOR.FITS'
#fits_filename = '0022+002.SP2B.PBCOR_22_044_28aug2012_lta.FITS'

fits_filename = '00015-00130E.fits'

hd = fits.open(fits_filename)
#hd.info()

data0 = hd[0].data

#print(data0)
data = hd[1].data

cols = hd[1].columns
#cols.info()

#print(data)

for i in range(len(data)):
    print(data[i]['FLDNAME'], data[i]['RA'], data[i]['DEC'])