#import libraries
import pickle 
from flask import Flask, request, render_template 
  
# Flask constructor
app = Flask(__name__, template_folder = 'template')   
  
#Load saved model
model = pickle.load(open('model.pkl','rb'))

#set home page as calculator page
@app.route('/')
def home():
    return render_template('home.html')

#initialize prediction class
@app.route('/', methods = ['POST'])
def predict_class():
    
    #Get feature inputs from form requests
    #convert strings inputs to float type
    latitude = float(request.form.get("latitude"))

    longitude = float(request.form.get("longitude")) 
    
    bright_ti4 = float(request.form.get("bright_ti4"))
     
    scan = float(request.form.get("scan"))
    
    track = float(request.form.get("track"))
    
    bright_ti5 = float(request.form.get("bright_ti5"))
    
    frp = float(request.form.get("frp"))
    
    #Place each feature into it's corresponding position 
    final_features = [[latitude, longitude, bright_ti4, scan, track,	bright_ti5,	frp]]
    
    #create prediction
    prediction = model.predict(final_features)
    
    #get output value
    output = prediction[0]
    
    #display conditions for each class
    if output == 'h':
        return render_template('home.html', prediction_text = 'Confidence Level: High')
    elif output == 'l':
        return render_template('home.html', prediction_text = 'Confidence Level: Low')
    elif output == 'n':
        return render_template('home.html', prediction_text = 'Confidence Level: Nominal')


#run app
if __name__ == "__main__":
    app.run(debug=True)