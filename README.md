# Reddit-Flair-Detector

watch it in live action on https://reddit-flair-detector-final.herokuapp.com/

## In order to use this:

1. Enter a valid reddit url, submit it.
2. result.html will display the results.
3. Navigate to statistics section under the navigation bar to view statistics:
   
   3.1 Relation between the flairs their frequency and the year of post.
   
   3.2 Relation between total scores and different flairs.
   
   3.3 Relation between mean scores and different flairs.
   
   3.4 Relation between number of comments and different flairs.
   
   3.5 Relation between comments and hours when they were posted (comments).
   
   3.6 Relation between flairs and their occurence in dataset instance.

This is a flask based application hosted on Heroku server.

## Codebase

The entire code has been developed using Python programming language, utilizing it's powerful text processing and machine learning modules. The application has been developed using Flask framework and hosted on Heroku web server.

## Execution

To execute the application on localhost:
  1. set FLASK_APP = application.py
  2. flask run
  
## Description of files used is given below:
  1. templates folder contains all the web templates related to the flask application.
     
     1.1 index.html is home page of application.
     
     1.2 statistics.html contains statistics related to flairs.
     
     1.3 result.html predicts the appropiate flair based on the model.
     
  2. static folder contains all the static images related to flask application.
  3. redditmodelforflair.pkl is the machine learning model used to make flair predictions.
  4. cleaned_reddit_alphabetav5.csv is csv file containing combined features(title+url+comments).
  5. MongoDb collection folder contains the mongodb instance.
  6. requirements.txt specify the requirements for heroku server and list of libraries used.
  7. Procfile is the file required by the heroku server.
  8. fetch_data_from_reddit.ipynb gets data from reddit with fields as: flair, title, score, id, url, comms_num, created, body, author,      comments.
  9. reddit_combine_cols.ipynb combines features such as title, url, comments into one.
  10. reddit_stats.ipynb gives statistics on an instance of dataset (it can be viewed in ststistics menu under navigation bar on               application page).
  11. write_combined_features_stopwords_removed.ipynb removes all the STOPWORDS in the dataset using SPACY.
  12. randomforest_on_url.ipynb in this file classifier is applied on dataset using URL as the only feature.
  13. logistic_regression_applied_to_combined_features.ipynb in this file logistic regression is applied to the dataset taking                 (title+url+comments) as combined features and gives a maximum accuracy of 77.90%.
  14. random_forest_on_combined_features.ipynb in this file Random Forest is applied to the dataset taking (title+url+comments) as             combined features and gives accuracy of 74.37%. 
  15. application.py is the main file that runs the applicaton on flask.
  16. original_reddit_data.csv is the file that contains original raw data fetched from reddit.
  
## Predicted accuracies:  
  
1. Accuracy given by Random Forest Classifier is 74.372 on combined features when together url,title and comments are used as features.

2. Accuracy given by Logistic Regression is 77.90 on combined features when together url,title and comments are used as features.

3. Accuracy of Logistic Regression applied only to url as feature is 60.91.

4. Accuracy of Random Forest Classifier applied to url is 59.30.

## Approach I followed:

1. Fetch data from r/india subreddit.
2. Clean the data, combine features, remove stopwords using Spacy.
3. Train using combined features.
4. Apply the classifier.
5. Predict the flair

As evident from above I have used combined features url + title + comments as maximum accuracy is achieved using this. I too have used CountVectorizer for fitting purpose and LogisticRegression, RandomForest to classify the flair.

## Dependencies used are:

1. scikit-learn
2. nltk
3. Flask
4. praw
5. Numpy
6. pandas
7. spacy

## References

   https://mdbootstrap.com/education/bootstrap/
