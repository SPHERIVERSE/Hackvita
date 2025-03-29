# Student Performance Predictor

This project uses AI to predict whether a student will pass or fail a final exam based on their average assignment score.

## Files:

* `data/student_data.csv`:  Synthetic dataset.
* `model.py`:     Python code for training and prediction.
* `app.py`:       Streamlit web application.
* `requirements.txt`: Python dependencies.

## How to Run:

1.  **Install Python:** Make sure you have Python 3.6 or later installed.
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Train the Model:**
    ```bash
    python model.py
    ```
4.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## Explanation:

The project uses a Logistic Regression model to classify students as Pass (1) or Fail (0). The model is trained on a synthetic dataset of average assignment scores.
