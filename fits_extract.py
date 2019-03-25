"""arg - fullpath to csv with urls"""

import pandas as pd
import wget
from scipy.misc import imread, imsave
import numpy as np
import matplotlib.pyplot as plt
import sys
from astropy.io import fits
from astropy.stats import sigma_clipped_stats

def plot_img(img, ra,dec):
    plt.figure()
    plt.title(str(ra)+'_'+str(dec))
    plt.imshow(img,cmap="gray")
    plt.colorbar()
    plt.grid(False)
    plt.savefig('fr1FITS/'+str(ra)+'_'+str(dec)+'.jpeg')
    plt.close()
    # plt.show()
    
def clip(data,lim):
    data[data<lim] = 0.0
    return data
    
def clean_crop_FITS(fname):
    hdu_list = fits.getdata(fname)
    image = np.squeeze(hdu_list)
    nan = np.isnan(image)
    image[nan] = 0
    sigma = 3.0
    
    mean, median, std = sigma_clipped_stats(image, sigma=sigma, iters=10)
    # Clip off n sigma points
    img_clip = clip(image,std*sigma)
    img_clip = img_clip[ 75:225, 75:225]
    
    minval, maxval = img_clip.min(),img_clip.max()
    norm = img_clip - minval
    img = norm*(1./(maxval-minval))
    
    return img
    
def readcsv(filename):
	df = pd.read_csv(filename)
	t=0
	print(df.shape[0])
	for cord in range(df.shape[0]):
		#print(ra)
		#print(dec)
		ra=df['RA'][cord]
		dec=df['DEC'][cord]
		url = df['URL'][cord]
		stringname='new/'+str(ra)+'_'+str(dec)+'.FITS'
		wget.download(url, stringname)
		cropped_fits = clean_crop_FITS(stringname)
		plot_img(cropped_fits,ra,dec)

if __name__ == '__main__':
	readcsv(sys.argv[1])
	
