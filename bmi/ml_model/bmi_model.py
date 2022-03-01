from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
import pickle
import joblib

# 로드 및 전처리
data = pd.read_csv("bmi/static/data/bmi.csv")
df = data
le = LabelEncoder()
df["gender"] = le.fit_transform(df["Gender"])

df["Height"] = df["Height"] / 100
df["Weight"] = df["Weight"] / 100

X = df.drop(["Index", "Gender"], axis="columns")
y = df["Index"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)


# train  kneighborclassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# 저장
saved_model = pickle.dumps(model)
from_pickled = pickle.loads(saved_model)
from_pickled.predict(X)
joblib.dump(model, "bmi/ml_model/bmi_model.pkl")
