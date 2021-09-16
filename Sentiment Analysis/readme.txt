The program uses Jupyter notebook and python file . 
The report is given as Project_Report.pdf
Please install Jupyter notebook and open the .ipynb file using the Jupyter application and the same can be used to run both type of files.
Kindly enter below for any missing packages
!pip install <package name>
Kindly unzip the Finalproject.zip and keep all the files as extracted in the same folder.
Once the notebooks are open please click on "Cell" tab and select "Run All"
The program will load and each output can be viewed as scrolled down

For the final output the Sentimentprediction.ipynb file is to be run

All other files are supporting files created for the project.
Details are given further below:

The over all project has below phases:
1) Data collection and corpus formation
2) Training on supervised model
3) Sentiment Analysis on our dataset


* Dataset generation is done using youtubeapi.py in Youtube Comments folder, by inputing the video id's and TwitterDataCollection.ipynb for collecting tweets related to candidates.
  Sentiown.ipynb is used to filter our youtube comments and segregate it for each candidates.
  Once the segregation is done it the both datasets were manually combined to form Trumpall.csv and Bidenall.csv

The train and test dataset can be downloaded from https://ai.stanford.edu/~amaas/data/sentiment/
Include the train and test data set folder in the same path ./ (as the python file)
* Training is done on IMDB reviews which are supervised, the related files are train folder, test folder, train.pkl. test.pkl and imdbReview.py
  imdbReview.py uses data set in train and test folder to generate train.pkl and test.pkl.
  The train.pkl and test.pkl genrated is used in customPolarity.py to predict sentiment of any new comments sent and return polarity.

* Sentimentprediction.ipynb is the file to be run to see the final output.
  


  