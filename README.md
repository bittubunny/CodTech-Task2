# CodTech-Task2
 **Name**: Bharath Chelimalla
 **Company**: CODTECH IT SOLUTIONS
 **ID**: CT12WEUS
 **Domain**: Machine Learning
 **Duration**: December 2024 to March 2025

### Overview: Sentiment Analysis Using Deep Learning  

#### **Objective**  
This project aims to build a sentiment analysis model to classify movie reviews as either positive or negative. By leveraging deep learning techniques, the project explores text preprocessing, tokenization, and Convolutional Neural Networks (CNN) for accurate sentiment prediction.

#### **Dataset**  
 **Dataset Used**: IMDB Movie Reviews Dataset  
 **Description**: Contains 50,000 movie reviews labeled as "positive" or "negative". The reviews are evenly split between the two classes.  
 **Preprocessing**: Sentiment labels were mapped to binary values (1 for positive and 0 for negative).  
![Screenshot 2024-12-30 182720](https://github.com/user-attachments/assets/6cbf15c8-8fab-4f1b-9999-c9d22a5bbb99)

#### **Methodology**  

1. **Data Preprocessing**  
    **Text Tokenization**: Used Keras's `Tokenizer` to convert text into numerical sequences.  
    **Padding**: Applied padding to ensure all sequences have a uniform length (500 words).  

2. **Model Architecture**  
    **Embedding Layer**: Converts input words into dense vectors of fixed size for efficient representation.  
    **Convolutional Layer**: Captures local patterns in text using filters.  
    **Global Max Pooling**: Reduces dimensionality by selecting the most significant features.  
    **Dense Layer**: Learns higher-level representations.  
    **Output Layer**: Uses a sigmoid activation function to classify reviews as positive or negative.  

3. **Training**  
    Optimizer: Adam  
    Loss Function: Binary Crossentropy  
    Early Stopping: Monitors validation loss and stops training if performance does not improve for 3 consecutive epochs.  

4. **Evaluation**  
    The model was evaluated on a test set using metrics like accuracy and loss.  

#### **Results**  
 **Training Accuracy**: Achieved high accuracy during training and validation.  
 **Test Accuracy**: The model achieved a test accuracy of **89.24%**, demonstrating robust performance on unseen data.  

#### **Visualizations**  
 **Accuracy Plot**: Shows training and validation accuracy over epochs, indicating the model's learning progression.  
 **Loss Plot**: Highlights the reduction in training and validation loss, showcasing effective optimization.  
![Screenshot 2024-12-30 182648](https://github.com/user-attachments/assets/5f4f6ad2-247b-4fff-8f4d-571acda2448f)

#### **Features**  

1. **Dynamic Prediction**  
    Allows users to input custom reviews for sentiment prediction.  
    Provides the predicted sentiment along with the confidence score.  
![Screenshot 2024-12-30 182807](https://github.com/user-attachments/assets/7d50233c-f11b-4e74-bdf2-42cf7321be5e)

2. **Model Saving and Reloading**  
    The trained model and tokenizer are saved for future use.  
    Supports loading the model and tokenizer for prediction or further evaluation.  

#### **Conclusion**  
This project successfully demonstrates the application of deep learning for sentiment analysis. The CNN-based architecture effectively captures patterns in text, providing accurate predictions on movie reviews.  
