# Importing necessary libraries

import pandas as pd
import pickle

# Import the constants

import constants

# Loading Recommendation System Model
recommendation_model = pickle.load(open(constants.RECOMMENDATION_MODEL, 'rb'))

# Loading the TfIDF vectorizer Model
tfidf_vectorizer = pickle.load(open(constants.TFIDF_VECTORIZER, 'rb'))

# Loading the Sentiment Classifier Model
sentiment_classifier = pickle.load(open(constants.SENTIMENT_CLASSIFIER_PATH, 'rb'))

# Loading the cleanReview Dataset
clean_review_df = pd.read_csv(constants.PRODUCT_REVIEW_MAPPING)

# probability threshold
probability_threshold = constants.PROBABILITY_THRESHOLD

def sentimentProductRecommendation(username):
    """Input is the username and output is a list of 5 top recommended products"""
    
    # Get top 20 product recommendations
    try:
        top20 = (recommendation_model
                .loc[username]
                .sort_values(ascending=False)[:20])
    except KeyError:
        # Unable to find username
        errorMessage = "ERROR: Unable to find username {}, as this user does not exist in the system!\n\
                        Please try again from the list of Available Users".format(username)
        
        return errorMessage
    
    # Temporary dictionary to store the percentage positive
    recommendationPercentPositive = {}
    
    # Iterating over all the recommendations
    for product in top20.index:
        
        # mapping out the reviewText from the cleanReview
        filterReviews = (clean_review_df
                        [clean_review_df.name == product]
                        .reviews_text)
        # print(filterReviews)
        
        # using tfidf vectorizer to transform the text
        vectorizedReviews = tfidf_vectorizer.transform(filterReviews)
        
        # Getting the sentiment from the transformed text
        sentimentProbability = sentiment_classifier.predict_proba(vectorizedReviews).T[1]
        
        # using the probability threshold metric
        reviewSentiment = [1 if value>probability_threshold else 0 for value in sentimentProbability]
        # print(reviewSentiment)
        
        # Calculating the percentage positive reviews
        percentPositive = round((sum(reviewSentiment) / len(reviewSentiment))*100, 2)
        # print(percentPositive)
        
        # Adding data into the dictionary
        recommendationPercentPositive[product] = percentPositive
        
    # sorting the dictionary based on percentages
    sortedByPositivePercentage = dict(sorted(recommendationPercentPositive.items(),
                                        key=lambda x : x[1],
                                        reverse=True))

    # Sorting the recommendations to predict top 5
    # finalRecommendations = list(sortedByPositivePercentage.keys())[:5]

    finalRecommendations = list(sortedByPositivePercentage.items())[:5]
    
    # Return the final recommendations
    return finalRecommendations