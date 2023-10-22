import pickle
import streamlit as st
import numpy as np

model_file = pickle.load(open('notebook/model.pkl', 'rb'))

def pred_output(user_input):
    model_input = np.array(user_input)
    ypred = model_file.predict(model_input.reshape(1, -1))
    return ypred[0]

def main():
    st.title("SURVIVAL OF THE FITTEST")
    st.write(
        "This app predicts the survival of a passenger on the Titanic based on their information. "
        "Please enter the following details to make a prediction."
    )

    st.subheader("Passenger Information")

    passenger_class = st.selectbox("Passenger Class", (1, 2, 3))

    sex = st.radio("Sex", ("Male", "Female"))

    age = st.number_input("Age", value=20, min_value=0, max_value=100)

    sibsp = st.number_input("Number of Siblings/Spouses Aboard", value=0, min_value=0, max_value=10)

    parch = st.number_input("Number of Parents/Children Aboard", value=0, min_value=0, max_value=10)

    fare = st.number_input("Fare", value=50, min_value=0, max_value=1000)

    embarked = st.selectbox(
        "Port of Embarkation",
        ("Cherbourg (C)", "Queenstown (Q)", "Southampton (S)")
    )

    if embarked == "Cherbourg (C)":
        embarked = 0
    elif embarked == "Queenstown (Q)":
        embarked = 1
    elif embarked == "Southampton (S)":
        embarked = 2

    if st.button('Predict'):
        user_input = [passenger_class, 0 if sex == "Male" else 1, age, sibsp, parch, fare, embarked]
        prediction = pred_output(user_input)

        result = "Survived :)" if prediction == 1 else "Not Survived :("

        st.subheader("Prediction Result")
        st.success(result)

if __name__ == '__main__':
    main()


# SEX - Male=0 Female=1
# Embarked - C=Cherbourg Q=Queentown S=Southampton