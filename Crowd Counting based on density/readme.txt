The project is done on google colab and the notebooks are downloaded and kept in the same folder
1) crowd_npy_gen		-- file used to covert .mat file to .npy
2) crowdcounting_pa_s		-- file trained and tested on part A dataset consisting of high density images
3) crowdcounting_pb_s		-- file trained and tested on part B dataset consisting of high density images
4) crowdcounting_both_s		-- file trained and tested on both part A and part B dataset consisting of high density images

The project is done on the Shanghaitech dataset which has been developed by the authors of our chosen paper. It consists of 1198 annotated images for 330,165 peoples.\\
It divides in two parts:  
Part A - 482 images crawled from the internet
Part B - 716 images taken from the streets of Shanghai
Both parts further divided into Train data containing ground-truth in .mat files and crowd images in .jpg format. Test data containing ground-truth in .mat files and crowd images in .jpg format.
Once the dataset is collected and we loaded it to the program, we have made few modifications to the dataset.

The dataset was placed in google drive and path has to be specified in the notebooks. Dataset can be collected by requesting the authors 