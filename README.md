# **7-Day Machine Learning with Python (Beginner → Practical Mastery)**

**Tools:**  Python, NumPy, pandas, Matplotlib, Seaborn, scikit-learn

**Workspace:** Google Colab (free cloud coding)

**Goal:** Go from zero to building real ML models in 1 week 🚀

---

## ⚙️ **Setup (Before Day 1)**

✅ Install Python or use **Google Colab** (recommended)

🖥️ Open [Google Colab](https://colab.research.google.com/) → New Notebook

📦 Install libraries:

```python
!pip install numpy pandas matplotlib seaborn scikit-learn

```

📂 Get free datasets:

- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Seaborn built-in datasets](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

---

## 📅 **WEEK PLAN OVERVIEW**

| Day | Topic | Mini Project |
| --- | --- | --- |
| 1 | Python Basics + Setup | Simple Calculator |
| 2 | NumPy Arrays | Student Score Stats |
| 3 | pandas Data Analysis | Clean & Summarize Data |
| 4 | Data Visualization | Iris Data Visualization |
| 5 | Regression Models | Predict House Prices |
| 6 | Classification Models | Predict Iris Species |
| 7 | Final Project | Student Grades Predictor |

---

## 🧩 **DAY 1 — Python & Setup Basics**

🎯 **Goal:** Understand Python syntax, libraries, and environment setup.

💡 **Learn:**

- Python basics: variables, loops, lists, functions
- Installing and importing libraries

📘 **Example:**

```python
numbers = [10, 20, 30]
avg = sum(numbers) / len(numbers)
print("Average:", avg)

```

🧠 **Mini Project:**

Create a **Simple Calculator** that adds, subtracts, multiplies, and divides two numbers.

✅ **Checklist:**

- [ ]  Learn Python basics
- [ ]  Install libraries
- [ ]  Test Colab environment

---

## 📊 **DAY 2 — NumPy for Numerical Computation**

🎯 **Goal:** Work with numerical data easily and fast.

💡 **Learn:**

- Arrays, slicing, matrix operations
- Basic stats: mean, sum, std

📘 **Example:**

```python
import numpy as np
scores = np.random.randint(50, 100, size=(10,))
print("Average score:", scores.mean())

```

🧠 **Mini Project:**

Simulate 100 student exam scores → find average, highest, and lowest scores.

✅ **Checklist:**

- [ ]  Learn array creation & slicing
- [ ]  Perform matrix operations
- [ ]  Use random data for practice

---

## 🧾 **DAY 3 — pandas for Data Handling**

🎯 **Goal:** Load, clean, and explore real datasets.

💡 **Learn:**

- Read CSV/Excel files
- Handle missing data
- Grouping, filtering

📘 **Example:**

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
print(df.head())
print(df.describe())

```

🧠 **Mini Project:**

Analyze restaurant tips dataset → find which day has highest average tips.

✅ **Checklist:**

- [ ]  Load data from CSV
- [ ]  Clean and filter
- [ ]  Summarize stats

---

## 📈 **DAY 4 — Data Visualization**

🎯 **Goal:** Understand and visualize data trends.

💡 **Learn:**

- Matplotlib basics
- Seaborn plots (scatter, bar, heatmap)

📘 **Example:**

```python
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("iris")
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
plt.show()

```

🧠 **Mini Project:**

Visualize iris dataset — compare petal/sepal length by species.

✅ **Checklist:**

- [ ]  Learn Seaborn plotting
- [ ]  Create scatter & heatmap
- [ ]  Interpret visual insights

---

## 🤖 **DAY 5 — Regression with scikit-learn**

🎯 **Goal:** Train a model to predict continuous values.

💡 **Learn:**

- Train/test split
- Linear Regression model
- Evaluate model performance

📘 **Example:**

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

data = load_diabetes()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
print("Accuracy:", model.score(X_test, y_test))

```

🧠 **Mini Project:**

Predict house prices using linear regression (Boston dataset or similar).

✅ **Checklist:**

- [ ]  Understand regression
- [ ]  Train model
- [ ]  Evaluate predictions

---

## 🧠 **DAY 6 — Classification Models**

🎯 **Goal:** Classify data into categories.

💡 **Learn:**

- Logistic Regression
- Decision Tree
- Accuracy metrics

📘 **Example:**

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier()
model.fit(X, y)
y_pred = model.predict(X)
print("Accuracy:", accuracy_score(y, y_pred))

```

🧠 **Mini Project:**

Classify iris flowers using Decision Tree and compare accuracy with KNN.

✅ **Checklist:**

- [ ]  Learn classification basics
- [ ]  Train Decision Tree model
- [ ]  Evaluate accuracy

---

## 🚀 **DAY 7 — Final Project: Student Grades Predictor**

🎯 **Goal:** Combine all skills — data, visualization, and ML model.

💡 **Learn:**

- End-to-end pipeline: clean → visualize → train → test → predict

📘 **Example:**

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'Hours':[1,2,3,4,5,6,7,8,9,10],
        'Scores':[35,40,50,55,65,70,75,80,85,95]}
df = pd.DataFrame(data)

X = df[['Hours']]
y = df['Scores']

model = LinearRegression()
model.fit(X, y)

print("Prediction for 6 hours study:", model.predict([[6]]))

```

✅ **Checklist:**

- [ ]  Load data
- [ ]  Visualize patterns
- [ ]  Train Linear Regression model
- [ ]  Predict new values
- [ ]  Present your results

---

## 🏁 **AFTER 7 DAYS YOU’LL BE ABLE TO:**

✅ Handle data with NumPy & pandas

✅ Visualize trends with Matplotlib & Seaborn

✅ Train & test ML models using scikit-learn

✅ Build small real-world ML projects

✅ Use datasets from Kaggle or Seaborn

✅ Run everything easily in Google Colab

---
