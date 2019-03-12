# classifier-work
## Results of FIRST classifier on the tgss fits files 

Results obtained from the use of the [FIRST classifier](https://github.com/wathela/FIRST-CLASSIFIER) for the FR1 and FR2 ra dec value catalogs of tgss survey. 

The accuracy for the FR1 catalog is 77.73 % (164/211 sources)
The accuracy for the FR2 catalog is 47.86 % (56/117 sources)

From the FR2 catalog, it classifies many images as BENT (35/117)

Added the output csv files with results for FR1 and FR2. Also some of the cutouts used in classification - present in cutouts folder (obtained via link in the output csv) 

These results are obtained via the multi-source classification script which takes in csv file of ra dec values as input (created using to_csv script). The low accuracy values may have been due to the quality of cutout images.

Added the single source classification outputs where default sigma value is 3.0 in the classifier but we tried with sigma values 3.0, 4.0 and 5.0 

Seeing that the accuracy for the tgss FR1 and FR2 catalogs is not as expected, If we try to build our own classifier for tgss images, we may have the following issues:

1. The fits files contain multiple sources, and even the cutouts contain multiple sources in some cases.
2. The sources are not labelled. The labelling work needs expertise. 

We can get the cutouts from these images but labelling seems difficult.

