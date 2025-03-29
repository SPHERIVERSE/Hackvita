import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

def train_model():
    """Trains the Logistic Regression model."""

    # Load the data
    data = pd.read_csv('data/student_data.csv')

    # Prepare the data
    X = data[['AverageScore']]  # Features
    y = data['PassOrFail']      # Target

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # 80% train, 20% test

    # Create and train the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save the model
    with open('models/model.pkl', 'wb') as file:
        pickle.dump(model, file)

    print("Model trained and saved!")

def predict_pass_fail(average_score):
    """Loads the trained model and predicts Pass/Fail."""

    # Load the model
    with open('models/model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Make the prediction
    prediction = model.predict([[average_score]])[0]  # [[ ]] is important!

    return prediction  # Returns 1 for Pass, 0 for Fail

if __name__ == '__main__':
    train_model()  # Train the model when the script is run directly
