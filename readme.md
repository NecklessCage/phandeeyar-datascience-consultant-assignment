# News Data Analysis and Classification

This project scrapes 50 news articles from each of Irrawaddy, Eleven, DVB, Mizzima and The Voice, totalling 250 articles. The data is cleaned. EDA, topic modelling, string querying and document classification (statistical and neural network) are performed.

1. Webscraping
    - Notebooks 0irrawaddy.ipynb, 1eleven.ipynb, 2dvb.ipynb, 3mizzima.ipynb and 4thevoice.ipynb fetch articles from the respective websites. The urls, titles and article bodies are saved in `data/*.json`.
    - All sites require trasversing 1 layer to get at least 50 articles. The landing page main menu is used to go in deeper for more articles.
    - Each site has a different html and css structure. The details are seen in the code.

2. Cleaning and Tokenization
    - The data is cleaned for common dirty characters, unicode/ascii issues and whitespace issues. Syllable segmentation and word segmentation are performed and saved in `data/clean` and `data/clean_wb`.

3. EDA
    - Preliminary analysis is performed on both titles and bodies of the articles.

4. Topic Modelling
    - Gensim module is used for LDA topic modelling on word-level documents. Number of topics and passes can be adjusted for better relevancy of topics.

5. String Query
    - LSI-based method from Gensim is used for string querying. The LDA model from the previous step is used.

6. Document Classifiers
    - Word segmented data is vectorized using TFIDF.
    - Logistic regression is used as statistical classifier and as a baseline model.
    - Simple perceptron is used as neural network document classifier.
