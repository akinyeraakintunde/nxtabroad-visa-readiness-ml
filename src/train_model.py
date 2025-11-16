# src/train_model.py

import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def build_pipeline(
    numeric_features,
    categorical_features
) -> Pipeline:
    # Preprocess numeric features
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    # Preprocess categorical features
    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    # Model
    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        n_jobs=-1
    )

    # Full pipeline
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", clf)
    ])

    return model


def main():
    data_path = os.path.join("data", "processed", "visa_readiness_data.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Dataset not found at {data_path}. "
            f"Run src/generate_synthetic_data.py first."
        )

    df = load_data(data_path)

    # Features and target
    target_col = "visa_readiness_class"
    X = df.drop(columns=[target_col, "applicant_id"])
    y = df[target_col]

    # Separate feature types
    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

    print("Numeric features:", numeric_features)
    print("Categorical features:", categorical_features)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = build_pipeline(numeric_features, categorical_features)

    print("Training model...")
    model.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = model.predict(X_test)

    print("\nClassification report:")
    print(classification_report(y_test, y_pred))

    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Save model
    os.makedirs("models", exist_ok=True)
    model_path = os.path.join("models", "visa_readiness_model.joblib")
    joblib.dump(model, model_path)
    print(f"\nSaved trained model to: {model_path}")


if __name__ == "__main__":
    main()

