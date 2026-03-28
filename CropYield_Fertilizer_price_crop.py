from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import tkinter
import numpy as np
from tkinter import filedialog
import pandas as pd 
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import normalize
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.ensemble import RandomForestClassifier



main = tkinter.Tk()
main.title("Crop Yield Prediction for Fertilizer, Crop and Price")
main.geometry("1300x1200")


global filename
global X_train, X_test, y_train, y_test
global X,Y
global dataset
global le
global model
global ms, sc, rfc

def upload():
    global filename
    global dataset
    text.delete('1.0', END)
    filename = filedialog.askopenfilename(initialdir = "Dataset")
    pathlabel.config(text=filename)
    text.delete('1.0', END)
    text.insert(END,'CropYield dataset loaded\n')
    dataset = pd.read_csv(filename,encoding='unicode_escape')
    #crop = pd.read_csv("C:/Users/User/Desktop/python/Crop_recommendation.csv",encoding='unicode_escape')
    v=dataset.head()
    text.insert(END,str(dataset.head(10))+"\n")

def processDataset():
    global le
    global dataset
    global X_train, X_test, y_train, y_test
    global X,Y
    global ms, sc, rfc
    text.delete('1.0', END)
    le = LabelEncoder()

  

    X = dataset.drop(['label', 'Soil'], axis=1)
    y = dataset['label']



    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    ms = MinMaxScaler()
    sc = StandardScaler()
    X_train = ms.fit_transform(X_train)
    X_train = sc.fit_transform(X_train)

    X_test=ms.transform(X_test)
    X_test=sc.transform(X_test)
    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)
    text.insert(END,"\n\nTotal records found in dataset is : "+str(len(X))+"\n")
    text.insert(END,"all the data are trained with machine learning algorithm : "+str(X_train.shape[0])+"\n")
  


def trainModel():
    global model
    text.delete('1.0', END)
    global X_train, X_test, y_train, y_test
    global X,Y

    model = DecisionTreeRegressor(max_depth=100,random_state=0,max_leaf_nodes=20,max_features=5,splitter="random")
    model.fit(X,Y)
    predict = model.predict(X_test)
    mse = mean_squared_error(predict,y_test)
    rmse = np.sqrt(mse)/ 1000
    text.insert(END,"Training process completed\n")
    text.insert(END,"Decision Tree Machine Learning Algorithm Training RMSE Error Rate : "+str(rmse)+"\n\n")


def cropYieldPredict():
    global model
    global le
    global ms, sc, rfc
    crop_dict = {
    'rice': 1,'maize': 2,'jute': 3,'cotton': 4,'coconut': 5,'papaya': 6,'orange': 7,'apple': 8,'muskmelon': 9,'watermelon': 10,
    'grapes': 11,'mango': 12,'banana': 13,'pomegranate': 14,'lentil': 15,'blackgram': 16,'mungbean': 17,'mothbeans': 18,
    'pigeonpeas': 19,'kidneybeans': 20,'chickpea': 21,'coffee': 22
    }
    soil_dict = {
    'clay loams': 1,'maize': 2,'jute': 3,'cotton': 4,'coconut': 5,'papaya': 6,'orange': 7,'apple': 8,'muskmelon': 9,'watermelon': 10,
    'grapes': 11,'mango': 12,'banana': 13,'pomegranate': 14,'lentil': 15,'blackgram': 16,'mungbean': 17,'mothbeans': 18,
    'pigeonpeas': 19,'kidneybeans': 20,'chickpea': 21,'coffee': 22
    }
    dataset['crop_num']=dataset['label'].map(crop_dict)


    natural_fertilizers = {
    "rice": ["Compost", "Manure", "NPK Fertilizer"],"maize": ["Compost", "Manure", "NPK Fertilizer"],
    "jute": ["Organic Fertilizer", "NPK Fertilizer"],"cotton": ["Compost", "Manure", "NPK Fertilizer"],
    "coconut": ["Organic Fertilizer", "Palm Ash", "Fish Emulsion"],"papaya": ["Compost", "Manure", "Organic Fertilizer"],
    "orange": ["Compost", "Manure", "Citrus Fertilizer"],"apple": ["Compost", "Manure", "Fruit Tree Fertilizer"],
    "muskmelon": ["Compost", "Manure", "Melon Fertilizer"],"watermelon": ["Compost", "Manure", "Melon Fertilizer"],
    "grapes": ["Compost", "Manure", "Grape Vine Fertilizer"],"mango": ["Compost", "Manure", "Fruit Tree Fertilizer"],
    "banana": ["Compost", "Manure", "Banana Fertilizer"],"pomegranate": ["Compost", "Manure", "Fruit Tree Fertilizer"],
    "lentil": ["Compost", "Manure", "Legume Fertilizer"],"blackgram": ["Compost", "Manure", "Legume Fertilizer"],
    "mungbean": ["Compost", "Manure", "Legume Fertilizer"],"mothbeans": ["Compost", "Manure", "Legume Fertilizer"],
    "pigeonpeas": ["Compost", "Manure", "Legume Fertilizer"],"kidneybeans": ["Compost", "Manure", "Legume Fertilizer"],
    "chickpea": ["Compost", "Manure", "Legume Fertilizer"],"coffee": ["Compost", "Manure", "Coffee Plant Fertilizer"],
    # Add more crops and their suitable natural fertilizers here
    }

    price = {
    "rice": ["23,450 per Acer"],"maize": ["19,450 per Acer"],
    "jute": ["33,450 per Acer"],"cotton": ["19,250 per Acer"],
    "coconut": ["43,450 per Acer"],"papaya": ["12,47 per Acer"],
    "orange": ["53,450 per Acer"],"apple": ["29,450 per Acer"],
    "muskmelon": ["63,450 per Acer"],"watermelon": ["83,450 per Acer"],
    "grapes": ["73,450 per Acer"],"mango": ["73,450 per Acer"],
    "banana": ["83,450 per Acer"],"pomegranate": ["63,450 per Acer"],
    "lentil": ["93,450 per Acer"],"blackgram": ["53,450 per Acer"],
    "mungbean": ["13,450 per Acer"],"mothbeans": ["43,450 per Acer"],
    "pigeonpeas": ["23,450 per Acer"],"kidneybeans": ["33,450 per Acer"],
    "chickpea": ["33,450 per Acer"],"coffee": ["Compost", "23,450 per Acer"],
    # Add more crops and their suitable natural fertilizers here
    }
    
    text.delete('1.0', END)

    def recommendation(N, P, K, temperature, humidity, pH, rainfall):
    # Predict the crop as before
        features = np.array([[N, P, K, temperature, humidity, pH, rainfall]])
        transformed_features = ms.transform(features)
        transformed_features = sc.transform(transformed_features)
        predicted_crop = rfc.predict(transformed_features)[0]
    # Get the recommended natural fertilizers for the predicted crop from the dictionary
        recommended_fertilizers = natural_fertilizers.get(predicted_crop,[])
        cost = price.get(predicted_crop,[])
        return predicted_crop, recommended_fertilizers, cost
        if not recommended_fertilizers:
           recommended_fertilizers=["Unknown Crop"]
           cost =["0"]
        return predicted_crop,recommended_fertilizers, cost
    text.insert(END,str("prediction is started")+"\n")
    n=data.get()
    n1=data1.get()
    n2=data2.get()
    n3=data3.get()
    n4=data4.get()
    n5=data5.get()
    n6=data6.get()
    if(n1=="" or n2=="" or n== "" or n3=="" or n4=="" or n5== "" or n6== "" or not(n.isdigit()) or not(n1.isdigit()) or not(n2.isdigit()) or not(n3.isdigit()) or not(n4.isdigit()) or not(n5.isdigit()) or not(n6.isdigit())):
        text.insert(END,str("Please enter valid data only")+"\n")
    else:
        N = int(n)
        P = int(n1)
        K = int(n2)
        temperature = float(n3)
        humidity = float(n4)
        pH = float(n5)
        rainfall = float(n6)
        predicted_crop, recommended_fertilizers, price = recommendation(N, P, K, temperature, humidity, pH, rainfall)
        if predicted_crop != "Unknown Crop":
         print(f"{predicted_crop} is a best crop to be cultivated.")
         print(f"Suggested natural fertilizers for {predicted_crop}: {', '.join(recommended_fertilizers)}")
         print(f"Estimated Price for {predicted_crop}: {', '.join(price)}")
        else:
         print("Sorry, we are not able to recommend a proper crop for this environment.")
         text.insert(END,str("Sorry, we are not able to recommend a proper crop for this environment.")+"\n")

        text.insert(END,str(f"{predicted_crop} is a best crop to be cultivated.")+"\n")
        text.insert(END,str(f"Suggested natural fertilizers for {predicted_crop}: {', '.join(recommended_fertilizers)}")+"\n")
        text.insert(END,str(f"Estimated Price for {predicted_crop}: {', '.join(price)}")+"\n")
        text.insert(END,str("prediction is done")+"\n")
    

def close():
    main.destroy()

font = ('times', 16, 'bold')
title = Label(main, text='Crop Yield Prediction for Fertilizer, Crop and Price')
title.config(bg='#8E44AD', fg='#F4D03F')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 14, 'bold')
upload = Button(main, text="Upload Crop Dataset", command=upload)
upload.place(x=700,y=100)
upload.config(font=font1)  

pathlabel = Label(main)
pathlabel.config(bg='DarkOrange1', fg='white')  
pathlabel.config(font=font1)           
#pathlabel.place(x=700,y=100)

processButton = Button(main, text="Preprocess Dataset", command=processDataset)
processButton.place(x=700,y=150)
processButton.config(font=font1) 

'''mlButton = Button(main, text="Train Machine Learning Algorithm", command=trainModel)
mlButton.place(x=700,y=200)
mlButton.config(font=font1)  temperature, humidity, pH, rainfall'''
data=StringVar()
data1=StringVar()
data2=StringVar()
data3=StringVar()
data4=StringVar()
data5=StringVar()
data6=StringVar()

user_name = Label(main, text = "N").place(x=700,y=200)
N_val = Entry(main, textvariable=data, width = 30).place(x = 780,y = 200)

p = Label(main, text = "P").place(x=700,y=230)
P_val = Entry(main, textvariable=data1, width = 30).place(x = 780,y = 230)

k = Label(main, text = "K").place(x=700,y=260)
k_val = Entry(main, textvariable=data2, width = 30).place(x = 780,y = 260)

t = Label(main, text = "temperature").place(x=700,y=290)
t_val = Entry(main, textvariable=data3, width = 30).place(x = 780,y = 290)

h = Label(main, text = "humidity").place(x=700,y=320)
h_val = Entry(main, textvariable=data4, width = 30).place(x = 780,y = 320)
ph = Label(main, text = "pH").place(x=700,y=350)
ph_val = Entry(main, textvariable=data5, width = 30).place(x = 780,y = 350)
ra = Label(main, text = "rainfall").place(x=700,y=380)
ra_val = Entry(main, textvariable=data6, width = 30).place(x = 780,y = 380)

predictButton = Button(main, text="Upload Test Data & Predict Yield", command=cropYieldPredict)
predictButton.place(x=700,y=410)
predictButton.config(font=font1)

closeButton = Button(main, text="Close", command=close)
closeButton.place(x=700,y=460)
closeButton.config(font=font1)


font1 = ('times', 12, 'bold')
text=Text(main,height=30,width=80)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=100)
text.config(font=font1)


main.config(bg='skyblue')
main.mainloop()
