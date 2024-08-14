import streamlit as st
import pickle as pkl
import numpy as np

# Loading the trained model
model = pkl.load(open('MIPML.pkl', 'rb'))  

# Streamlit app layout
st.title('Insurance Premium Prediction')


age = st.number_input('Age', min_value=0, max_value=120, value=30)
sex = st.selectbox('Sex', options=['Female', 'Male'], index=0)
bmi = st.number_input('BMI', min_value=0.0, max_value=50.0, value=25.0, step=0.1)
children = st.number_input('Number of Children', min_value=0, max_value=10, value=0)
smoker = st.selectbox('Smoker', options=['No', 'Yes'], index=0)
region = st.selectbox('Region', options=['Southeast', 'Southwest', 'Northeast', 'Northwest'], index=0)

# Convert categorical inputs to numerical values using if-else
if sex == 'Female':
    sex = 0
else:
    sex = 1

if smoker == 'No':
    smoker = 0
else:
    smoker = 1

if region == 'Southeast':
    region = 0
elif region == 'Southwest':
    region = 1
elif region == 'Northeast':
    region = 2
else:
    region = 3

# Prepare input data for prediction
input_data = (age, sex, bmi, children, smoker, region)
input_data_array = np.asarray(input_data).reshape(1, -1)

# Button to trigger prediction
if st.button('Predict'):
    # Predict insurance premium using the model
    insurance_premium = model.predict(input_data_array)[0]

    # Display the result
    st.write(f'Predicted Insurance Premium: ${insurance_premium:.2f}')
