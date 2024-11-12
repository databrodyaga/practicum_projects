# Search for toxic comments on "Wikipedia Shop" using BERT

## Project Description
The online shop "Wikipedia Shop" is launching a new service. Now users can edit and complete product descriptions, just like in wiki communities. This means that customers are proposing their edits and commenting on the changes made by others. The shop needs an instrument to search for toxic comments and send them for moderation.

A model needs to be trained to classify comments as positive or negative. We have a dataset with labeled data on the toxicity of edits available.

Requirements for the model in terms of quality metric F1 - at least 0.75.

## Data Description

The data is located in the file toxic_comments.csv.  
The text column contains the comment text, and toxic is the target variable.

Specific steps to analyze and predict the data are outlined in the notebook.  

In this project the following aspects of **text machine learning** were worked on:      
- Introduction to text machine learning (text preprocessing and applying a classification task to it)   
- Vectorization of texts using BERT, TF-IDF, Word2Vec  
- Language representations