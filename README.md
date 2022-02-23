
- [Sentiment based product recommendation system](#sentiment-based-product-recommendation-system)
- [Heroku Deployment](#heroku-deployment)
  - [Getting Started](#getting-started)

# Sentiment based product recommendation system

- Use recommendation model to predict the top 20 products
- Use the dataset to pass the clean text review to the `tfidf` model pertaining to each product to `vectorize` them
- Use the vectors as input to the classification model for prediction
- Use the predicted sentiments to further refine the top 5 products based on the percentage positive reviews for each product.

# Heroku Deployment
[SBPRS - View Project in Action](https://capstone-sbprs-jay.herokuapp.com/)

## Getting Started
- Open the project link
- Enter a `username` which is present in the database.
- To find an existing user click on `Available Users`
- Copy the username for which you would like to see the product recommendations for and paste it in the home page field for `username` and hit `submit`

