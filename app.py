import streamlit as st
import model  # Import our model.py file

st.title("Student Pass/Fail Predictor")

st.write("Enter the student's average assignment score to predict if they will pass or fail the final exam.")

average_score = st.number_input("Average Assignment Score", min_value=0, max_value=100, value=70)

if st.button("Predict"):
    prediction = model.predict_pass_fail(average_score)
    if prediction == 1:
        st.success("The student is predicted to PASS the final exam.")
    else:
        st.error("The student is predicted to FAIL the final exam.")

st.sidebar.header("About")
st.sidebar.info(
    "This is a simple AI app to predict student pass/fail status. "
    "It uses a Logistic Regression model trained on synthetic data."
)
