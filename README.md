
- [Sentiment based product recommendation system outline](#sentiment-based-product-recommendation-system-outline)
- [Deliverables Expected](#deliverables-expected)
- [Folder structure](#folder-structure)
- [Heroku Deployment](#heroku-deployment)
  - [Getting Started](#getting-started)

# Sentiment based product recommendation system outline

- Use recommendation model to predict the top 20 products
- Use the dataset to pass the clean text review to the `tfidf` model pertaining to each product to `vectorize` them
- Use the vectors as input to the classification model for prediction
- Use the predicted sentiments to further refine the top 5 products based on the percentage positive reviews for each product.

# Deliverables Expected

- [ ] Task 1:Data Cleaning and Pre-Processing
    - [ ] Performed all data quality checks and addressed all data quality issues in the right way (especially the missing value treatment). Provided a clear explanation for missing value removal or imputation
    - [ ] Provided a well-commented explanation for each step of data processing
    - [ ] Dropped the variables that were not relevant for the project with a well-commented explanation for each step. Converted all variables to correct datatypes
- [ ] Task 2: Text Pre-Processing
    - [ ] Explored all the relevant text preprocessing steps after cleaning the data set. Provided well-commented reasons for every step that was performed in text preprocessing
- [ ] Task 3: Feature Extraction
    - [ ] Divided the data into training and testing parts
    - [ ] Converted the text to features using the best-suited vectorizer (bag-of-words, TD-IDF, Word2Vec, etc.) for the ML model for sentiment analysis
- [ ] Task 4: Model Building
    - [ ] Built at least 3 ML models and did the comparative analysis on why one model is better than the other three models
    - [ ] Checked whether the data is imbalanced or not and took the necessary steps. If necessary then did the hyperparameter tuning also
    - [ ] Selected one out of the 3 models based on performance for predicting the sentiments based on the text and title of the reviews. Provided detailed reasons for selecting the model
- [ ] Task 5: Building the Recomemndation System
    - [ ] Split the data set into train and test data set for the recommendation system
    - [ ] Built at least two types of recommendation systems: user-based and item-based recommendation systems
    - [ ] Evaluated both the types of recommendation systems and selected one based on performance. Provided detailed reasons for selecting the recommendation system
- [ ] Task 6: Recommendation of Top 20 Products to a Specified User
    - [ ] Recommended the top 20 products for the username selected by the user based on the recommendation system built
- [ ] Task 7: Fine-Tuning the Recommendation System and Recommendation of Top 5 Products
    - [ ] Predicted the sentiment (positive or negative) of all the reviews in the train data set of the top 20 recommended products for a user. For each of the 20 products recommended, found the percentage of positive sentiments for all the reviews of each product. Filtered out the top 5 products with the highest percentage of positive reviews
- [ ] Task 8: Deployment Using Flask and Heroku
    - [ ] Deployed the end-to-end web application using Flask and Heroku. You need to only include one ML model and one recommendation system to deploy the model
    - [ ] You need to:
        - [ ] Take the username as input, and
        - [ ] Create a submit button, and once you press the submit button, it should recommend the 5 products based on the username entered.

# Folder structure

1. `/data` contains the `clean_reviews.csv` dataset which has been created post text cleaning and processing.
2. `/model` contains the pre-packaged models for `TF-IDF`, `Clssification Logisitic Regression` and `Recommendation` _pickle_ files respectively.
3. `/static` contains all static assets related to the Web Page in terms of the CSS file definitions and Images etc.
4. `/templates` contains all the `html` files required for the deployment of the project
5. `./*ipynb` files contain the actual Jupyter Notebooks used for building this project.
6. `./constants.py` this contains all constants that are referenced within the project either within `model.py` or `app.py`
7. `./Procfile` contains the entry point information for Heroku
8. `./requirements.txt` defines the pre-requisites and necessary packages that need to be installed for this project to work. _NB: There are more packages required to run the actual notebooks hence if there is a need to run / evaluate the notebooks then those missing packages need to be installed as well._
9. `./runtime.txt` defines the Python runtime needed for execution.

# Heroku Deployment
[SBPRS - View Project in Action](https://capstone-sbprs-jay.herokuapp.com/)

## Getting Started
- Open the project link
- Enter a `username` which is present in the database.
- To find an existing user click on `Available Users`
- Copy the username for which you would like to see the product recommendations for and paste it in the home page field for `username` and hit `submit`

