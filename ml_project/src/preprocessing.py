from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd

def preprocess_data(df):
    
    # Encode tarVget
    #df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

    # Fill missing values
    num_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(include='object').columns

    df[num_cols] = SimpleImputer(strategy='mean').fit_transform(df[num_cols])
    df[cat_cols] = df[cat_cols].fillna('Unknown')

    # Encode categorical
    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("loan_status", axis=1)
    y = df["loan_status"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y, test_size=0.2, random_state=42), scaler
