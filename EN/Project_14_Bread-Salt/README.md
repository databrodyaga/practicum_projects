# Definition of age for customers at "Hleb-Sol" store

## Project Description
The online supermarket «Xleb-Sol» is implementing a computer vision system to process customer images. Image fixation in the checkout area will help determine the age of customers, allowing:  
- Analysis of purchases and suggesting products that may interest customers within this age group;  
- Monitoring the honesty of cashiers when selling alcohol.

A model is required to be built that can identify an approximate age from a photo. A dataset containing images of people with their ages is available. The metric for quality will be MAE (Mean Absolute Error).

Recommendations:  
- The loss function does not necessarily need to be MAE. Neural networks typically use MSE as the loss function and train faster.  
- Quality on validation set improves, but the model becomes over-trained. Do not rush to change the model. Typically, neural networks with a large number of layers become over-trained.

A convolutional neural network must be built and trained on the dataset containing photos of people. The target value is MAE on the test set not greater than 8.  
On the [dataset paper](https://inria.hal.science/hal-01677892/document), which we will work with, the MAE was 5.4. A good result would be an MAE less than 7.

## Data Description
The data is taken from the website [ChaLearn Looking at People](http://chalearnlap.cvc.uab.es/dataset/26/description/).  
One directory of all images (/final_files) and a CSV file labels.csv with two columns: file_name and real_age.
Extracting data from the directory can be done using the method [ImageDataGenerator](https://keras.io/preprocessing/image/) — flow_from_dataframe(dataframe, directory, ...).

The specific steps for analyzing and predicting the data are described in the notebook.  

In this project, the following aspects of **Computer Vision** have been implemented:  
- Introduction to computer vision (solving simple computer vision problems using pre-trained neural networks and Keras libraries)  
- Fully connected networks  
- Convolutional networks