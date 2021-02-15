# Personality Detection
Our main idea is to use image url and text from user profile and then passing it through image analysis model and text-analysis model to get the possibility of person being in personality traits from big 5 model namely: <ol> <li>Extraversion</li> <li>Agreeableness </li> <li>Conscientiousness </li> <li>Neuroticism </li> <li>Openness </li> </ol>

<p> For Text analysis part we are using pretrained <a href = "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3">bert model for preprocessing</a> and <a href= "https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-4_H-512_A-8/1">smaller bert</a> from tensorflow_hub using mean squared loss BinaryCrossentropy loss and AdamW optimizer. The overall accuracy of over model for predicting personality trait is about 50%<br> 

model wieghts link : https://drive.google.com/drive/folders/1U1fuZryj3R4rj6E7Umwbt9qefjMckCjA?usp=sharing
</p>

<p> For Image analysis part we are using custom convolution network trained using mean squared loss (regression loss) and adam optimizer. The overall accuracy of over model for predicting personality trait is about 80% <br>
Dataset pickle files link : https://drive.google.com/drive/folders/1U1fuZryj3R4rj6E7Umwbt9qefjMckCjA?usp=sharing
</p>

Training code for image analysis part is in personality_image.ipynb file you can directly open it in colab and run it.

## Testing Instruction

<ul>
  <li> run pip install -r requirements.txt </li>
  <li> run python configurator.py, it will prompt you for your linkedin username(email) and password </li>
  <li> Download the weights from https://drive.google.com/drive/folders/1r8rIBKtnzF91gaxSdjFyYLn3Du4hpiiE?usp=sharing and store it in the project directory </li>
  <li> run test.py like python test.py -u [linkedin user url]. Example: python test.py -u https://www.linkedin.com/in/sahil-nare-b96694179/</li>
</ul>

## Instruction for  text analsysis
<ul>
  <li>Run text_analsysis.pynb on colab</li>
  <li>Load model weights </li>
  
</ul>

## Sentiment analysis part
<p> Just run sentiment_analysis.ipynb. training data link : https://www.kaggle.com/cosmos98/twitter-and-reddit-sentimental-analysis-dataset <br>
   work in progress: model saving and inference code will be added soon and this will be automated with twitter scraper which scraps comments of users on twitter and gives sentiment of each comment. <p>
