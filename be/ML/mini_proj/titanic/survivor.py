import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
import joblib

# Load the Titanic dataset
@st.cache
def load_data():
    df = pd.read_csv('train.csv')
    return df

df = load_data()

# Feature Engineering
def feature_engineering(df):
    # Create a binary 'HasCabin' column based on 'Cabin' data
    df['HasCabin'] = df['Cabin'].notna().astype(int)

    # Fill missing 'Age' values with the median age
    df['Age'].fillna(df['Age'].median(), inplace=True)

    return df

df = feature_engineering(df)

# Train a logistic regression model
X = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'HasCabin']]
y = df['Survived']

X = pd.get_dummies(X, columns=['Sex'], drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Save the trained model to a file using joblib
model_filename = 'logistic_regression_model.joblib'
joblib.dump(model, model_filename)

# Evaluate the model on the testing set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Streamlit UI
st.title('Titanic Survival Prediction Model')
st.write('Model accuracy:', accuracy)

st.subheader('Predict the survival of a new passenger:')
age = st.number_input('Age:')
sex = st.selectbox('Sex:', ['Male', 'Female'])
pclass = st.selectbox('Pclass:', ['1st class', '2nd class', '3rd class'])

# Preprocess the new_passenger dataframe to handle missing values
new_passenger = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex],
    'Age': [age],
    'SibSp': [0],  # Initialize with zero, you can adjust this based on data
    'Parch': [0],  # Initialize with zero, you can adjust this based on data
    'HasCabin': [0]  # Initialize with zero, you can adjust this based on data
})

# One-hot encode the 'Sex' column
new_passenger = pd.get_dummies(new_passenger, columns=['Sex'], drop_first=True)

# Make sure 'Sex_male' and 'Sex_Female' columns are present
if 'Sex_Female' not in new_passenger:
    new_passenger['Sex_Female'] = 0
if 'Sex_male' not in new_passenger:
    new_passenger['Sex_male'] = 0

# Reorder columns to match the order during model training
new_passenger = new_passenger[['Pclass', 'Sex_Female', 'Sex_male', 'Age', 'SibSp', 'Parch', 'HasCabin']]

# Predict the survival of the new passenger
survival_prediction = model.predict_proba(new_passenger)[:, 1][0]

# Display the survival prediction
st.write('Survival prediction:', f'{survival_prediction * 100:.2f}%')

# Add a button to save the trained model
if st.button('Save Model'):
    st.write('Saving the trained model...')
    st.write(f'Model saved to {model_filename}')


