from flask import Flask,redirect,request,render_template,url_for
import pickle

app = Flask(__name__)
model=pickle.load(open('model_tr.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        gender=request.form['gender']
        if gender == 'male':
            
            gender=1
        else:
            gender=0
        age=request.form['age']
        Hypertension=request.form['hypertension']
        if Hypertension== "yes":
            Hypertension=1
        else:
            Hypertension=0
        heart_disease=request.form['heart_disease']
        if heart_disease == "yes":
            heart_disease=1
        else:
            heart_disease=0
        marry=request.form['ever_married']
        if marry == "yes":
            marry=1
        else:
            marry=0
        
        Residence_type=request.form['Residence_type']
        if Residence_type == 'urban':
            Residence_type=1
        else:
            Residence_type=0
        glu=request.form['avg_glucose_level']
        bmi=request.form['bmi']
        smoke=request.form['smoking_status']
        if smoke == "formerly smoked":
            smoke=0
        elif smoke == "never smoked":
            smoke=1
        elif smoke == "smokes":
            smoke=2
        else:
            smoke=3
        prediction=model.predict([[gender,age,Hypertension,heart_disease,marry,Residence_type,glu,bmi,smoke]])
    
        if prediction == 1:
            return render_template('submit.html',pred=' There is chance of stroke')
        else:
            return render_template('index2.html',pred=' There is no chance of stroke')
        


if __name__ == '__main__':
    app.run(debug=True)