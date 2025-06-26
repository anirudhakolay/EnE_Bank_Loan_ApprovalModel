from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model
from src.predict import predict
import numpy as np

def main():
    df = load_data("data/loan_data.csv")
    (X_train, X_test, y_train, y_test), scaler = preprocess_data(df)
    
    model = build_model()
    model = train_model(model, X_train, y_train)
    
    acc, report = evaluate_model(model, X_test, y_test)
    print(f"Accuracy: {acc:.2f}")
    print(report)
    
    # Example prediction
    sample_input = X_test[0].reshape(1, -1)
    pred = predict(model, sample_input)
    print("Sample Prediction:", "Approved" if pred[0] == 1 else "Rejected")

if __name__ == "__main__":
    main()
