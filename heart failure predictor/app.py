  
from flask import Flask,redirect,request,render_template,url_for
import pickle

app = Flask(__name__)
model=pickle.load(open('heartt.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        agee=request.form['age']
        anamia=request.form['anaemia']
        if anamia == 'yes':
            
            anamia=1
        else:
            anamia=0
        
        dia=request.form['diabetes']
        if dia== "yes":
            dia=1
        else:
            dia=0
        bp=request.form['high_blood_pressure']
        if bp == "yes":
            bp=1
        else:
            bp=0
        plate=request.form['platelets'] 
        creat=request.form['serum_creatinine']
        se=request.form['sex']
        if se == "male":
            se=1
        else:
            se=0
        
        smoke=request.form['smoking']
        if smoke == 'yes':
            smoke=1
        else:
            smoke=0
        
        prediction=model.predict([[agee,anamia,dia,bp,plate,creat,se,smoke]])
    
        if prediction == 1:
            return render_template('submit.html',pred=' There is high chance of heart failure')
        else:
            return render_template('index2.html',pred=' There is less chance of heart failure')
        


if __name__ == '__main__':
    app.run(debug=True)

