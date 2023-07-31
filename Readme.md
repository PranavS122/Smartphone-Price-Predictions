<html>
<body>
<h1>Smartphone Price Predictor</h1>
<p>This is a machine learning project that predicts the price of a mobile phone based on its specifications. The data was scraped from the E-commerce website Flipkart, and the project is implemented on Streamlit.</p>
<h2>You can check out the Deployed app here</h2>
<p>[Link to the app](https://smartphone-price-predictions.onrender.com)</p>
<h2>Installation</h2>
<p>To run this project on your local machine, you need to install the following libraries:</p>
<ul>
<li>requests</li>
<li>beautifulsoup4</li>
<li>pandas</li>
<li>numpy</li>
<li>scikit-learn</li>
<li>flask</li>
<li>streamlit</li>
</ul>
<p>You can install them using pip:</p>
<code>pip install requests beautifulsoup4 pandas numpy scikit-learn flask streamlit</code>
<h2>Usage</h2>
<p>To use this app, you can run the <code>app.py</code> file using the command:</p>
<code>streamlit run app.py</code>
<p>This will open a Streamlit app in your browser where you can enter the specifications of the mobile phone and get a price prediction.</p>
<h2>Data</h2>
<p>The raw data for this project is in the file <code>Flipkart_results(1).csv</code>. This data was preprocessed using the <code>Preprocessing.ipynb</code> Jupyter Notebook, which generated the processed data in the file <code>mobile_df.pkl</code>.</p>
<p>The Exploratory Data Analysis (EDA) was done in the <code>EDA on mobile data.ipynb</code> Jupyter Notebook. The machine learning models were trained in the <code>Models.ipynb</code> Jupyter Notebook, which uses the processed data to train and save the best model in <code>pipe.pkl</code>.</p>
<h2>Model Selection</h2>
<p>The following machine learning models were used to train and evaluate the best model for price prediction:</p>
<ul>
<li>Linear regression</li>
<li>Ridge</li>
<li>Lasso</li>
<li>KNN-regressor</li>
<li>SVM</li>
<li>Decision trees</li>
<li>Extra trees</li>
<li>Random Forest</li>
<li>Ada Boost</li>
<li>XG-Boost</li>
<li>Voting regressor</li>
<li>Stacking regressor</li>
</ul>
<p>The best model for this project was the Random Forest model, which achieved an accuracy of 92%.</p>
<h2>Contributing</h2>
<p>If you want to contribute to this project, feel free to open an issue or pull request on the GitHub repository.</p>
<h2>Conclusion</h2>
<p>In conclusion, our mobile price predictor project utilizes machine learning algorithms to predict the prices of new mobile phone models based on their specifications. We scrapped the data for this project from the popular e-commerce website, Flipkart, and preprocessed it using Python libraries such as Beautifulsoup, Pandas, and Numpy. We used the Scikit-learn library to build and train our predictive models, which included Linear Regression, Ridge, Lasso, KNN-Regressor, SVM, Decision Trees, Extra Trees, Random Forest, Ada Boost, XG-Boost, Voting, and Stacking Regressor.</p>
<p>After thorough evaluation, we found that the Random Forest model was the best performer with an accuracy of 92%. We developed the project using Streamlit, a popular Python library for building web applications, and created a pipeline model that is capable of predicting the prices of new mobile phone models based on their specifications.</p>
<p>This project has the potential to be extended to include more models and more data sources.</p>
<p>Thank you for your interest in my project!</p>
</body>
</html>
