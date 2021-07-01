# Lost and Found Image Search
#### A web application that keeps track of missing belongings in a hotel. You lost something? Look here.

## Brief Introduction 📍
Losing possession in hotel or resort premises is a serious concern for many. The management also has to take care of these items and ensure that it is retrieved by their actual owner only. Our project aims to solve this hassle and pressure a person deals with to retrieve a lost object. The object can be lost anywhere, whether it be a hotel, hospital, restaurant, school, etc. For this project, our application focuses on the retrieval of lost objects from hotels premises. Our main motive is for better management of these lost items and to ease the process of finding a lost item.

## Process of the Project 👨‍🏫
Different hotel administrations have different ways of keeping track of the lost items and a common way was to protect those items in a storeroom until the owner comes asking for the item. Creating an online database through images and letting the users access the database from a similar image of the lost item is a great way of easing the process. Image retrieval was the main point of focus here. Choosing the best image retrieval method that is widely used and gives accurate result was necessary. After some thorough research, we found that VGG16 is a model that will help us give the most accurate results. Also, the web was a great medium to bring this project to life and create an interface for the users and hotel management. Thus, we made a portal to access the model with ease. For this project we have used a model **VGG 16** provided by **Keras**, it is 16 layers deep convolutional neural network. The model achieves 92.7% top 5 test accuracy in ImageNet which is a dataset of over 14 million images belonging to several 1000 classes. The default input size of the image for the VGG16 model is 224x 224 px with 3 channels for RGB Image.  Since images are unstructured data and we can’t directly train our model over those images. We converted these images into structured data and extracted their features. For that, we converted images into **NumPy** arrays and performed **Deep Feature Synthesis**. Deep feature synthesis stacks multiple transformation and aggregation operations to create features from data spread across many tables. Like most ideas in  machine learning, it’s a complex method built on a foundation of simple concepts. We made use of various modules for the making of our project like **Keras and TensorFlow** for building our deep learning models, **Matplotlib and pillow** for image preprocessing and importing them, **NumPy** for all the calculations and preprocessing and **Flask** to connect the model to our **web application**.

## File Description 📒
#### templates
Stores the HTML files<i>
- index.html - the home page of our app where we upload the image of lost item and retrieve the top 5 images that match the description
- upload.html - the upload page where we upload a new lost item found in the hotel by management</i>
#### static
Stores all the data that remains static irrespective of the instance you are building<i>
- feature - Stores the deep features of each image in a form of NumPy array
- image - image database of all the lost belongings
- uploaded - stores the query image once uploaded
- bg.png - background of the website
- style.css - styling of the website</i>
#### DeepFeatures.py
Call and instante our VGG16 model that helps in Deep Feature synthesis
#### SaveFeatures.py
Iterate through our database and save all the deep features extracted
#### Server.py
Retrieve top 5 lost objects and display on the web

## Tools and Technologies used 🛠
1. VGG16
2. Deep Features Synthesis
3. Flask
4. TensorFlow
5. Keras
6. Numpy
7. Javascript/HTML5/CSS3

## Snapshots 🖼
![Lost nd Found](https://user-images.githubusercontent.com/60514776/124169900-66519580-dac4-11eb-9a09-936e31a028f5.png)


## Contributors 👨‍💻
[Nikhil Kumar Parashar](https://github.com/NikhilKP631197)
<br>
[Anmol Bansal](https://github.com/anmolbansal7)

<p align = "center"><b>
Drop a star ⭐ if you find this project interesting!
  </b></p>
