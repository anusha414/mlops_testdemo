import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Configure MLflow
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("experiment1")

# Load data
df = pd.read_csv("student_scores.csv")

# Features and target
X = df[["Hours_Studied"]]
y = df["Pass"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Start MLflow run
with mlflow.start_run():

    # Log parameters
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("random_state", 42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)

    # Log metric
    mlflow.log_metric("accuracy", accuracy)

    # Save model
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model"
    )
    print("Model logged to MLflow successfully")
