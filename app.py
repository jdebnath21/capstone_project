# Importing required libraries

from crypt import methods
from distutils.log import error
from flask import Flask, render_template, request, redirect, url_for
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

# Import the model library
import model

# Initialize Flask
app = Flask(__name__)

# Defining root path
@app.route('/')
def home():
    return  render_template('index.html')


@app.route('/products', methods=['POST'])
def recommendProduct():
    """Product Recommender"""

    # Get username
    username = str(request.form.get('username'))

    # Getting the final recommendations
    finalRecommendation = model.sentimentProductRecommendation(username)

    # Validating output type
    if type(finalRecommendation) != list:
        return render_template('index.html', error=finalRecommendation)

    # Converting finalRecommendation to a dataframe
    recommendations = pd.DataFrame(finalRecommendation, columns = ['Product', 'Positive Percentage'])

    # Creating a HTML table from Dataframe
    recommendation_tabular = [recommendations.to_html(classes=recommendations)]

    # table definitions
    title_tabular = ['NAN', 'Top five product recommendation for User : {} are'.format(username)]

    # Passing the results
    return render_template('index.html', productsTable = recommendation_tabular, titles = title_tabular)


@app.route('/users', methods=['GET'])
def allUsers():

    # get users from the recommendation model itself
    usernames = list(model.recommendation_model.index)

    # userlist to Dataframe
    usernamesdf = pd.DataFrame(usernames, columns=['List of Users'])

    # Render Dataframe to HTML Table
    usernames_tabular = [usernamesdf.to_html(classes='username')]

    # Table view
    title_tabular = ['NAN', 'List of all users in the system']

    # Render the page
    return render_template('allusernames.html', userTable = usernames_tabular, titles=title_tabular)

if __name__ == "__main__":
    app.run(debug=True)