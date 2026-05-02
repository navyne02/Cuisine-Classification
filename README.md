<div align="center">

# 🌍 Cuisine Classification Model

> *Teaching machines to taste the difference between Biryani and Pizza.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Algorithm](https://img.shields.io/badge/Algorithm-Random%20Forest-green?style=for-the-badge)](/)
[![Type](https://img.shields.io/badge/Task-Classification-purple?style=for-the-badge)](/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](/)

<br/>

```
🍛 Indian   🍕 Italian   🍣 Japanese   🥘 Chinese   🌮 Mexican
        🤖  ──────────────────────────────────── 🎯
        ML Model classifying cuisines with precision!
🍛 Indian   🍕 Italian   🍣 Japanese   🥘 Chinese   🌮 Mexican
```

</div>

---

## 🎯 Objective

> **Can a machine figure out what type of food a restaurant serves — just from numbers?**

This project builds a **Machine Learning classification model** that predicts a restaurant's **cuisine type** based on its operational features like cost, votes, city, and available services — no menu needed! 🍽️

---

## 🗂️ Project Structure

```
📦 Cuisine-Classification
 ┣ 📄 Dataset.csv           ← Raw restaurant data
 ┣ 🐍 task3 code.py         ← Classification pipeline & model
 ┣ 🖼️ Task3 output.png      ← Visual results & confusion matrix
 ┗ 📖 README.md             ← You're here!
```

---

## ⚙️ Features Used for Classification

The model learns to identify cuisine type from these restaurant attributes:

| Feature | Description | Type |
|---|---|---|
| 💰 **Average Cost for Two** | Spending level per visit | Numerical |
| 👥 **Votes** | Total number of user reviews | Numerical |
| 📊 **Price Range** | Budget / Mid / Premium category | Categorical |
| 📅 **Has Table Booking** | Reservation available? (Yes/No) | Binary |
| 🛵 **Has Online Delivery** | Delivers food online? (Yes/No) | Binary |
| 📍 **City** | Location of the restaurant | Categorical |

---

## 🤖 Model Used

<div align="center">

### 🌲 Random Forest Classifier

> An ensemble of decision trees that **votes** on the most likely cuisine — just like asking a panel of food critics!

| Property | Detail |
|---|---|
| Algorithm | Random Forest Classifier |
| Task | Multi-class Classification |
| Target Classes | Top 10 Cuisines |
| Handles Imbalance | ✅ Via class balancing |

</div>

---

## 🔬 Approach — Step by Step

```
 Raw Data ──► Clean ──► Simplify ──► Balance ──► Encode ──► Split ──► Train ──► 🎯 Predict
```

### Detailed Pipeline

**1. 🧹 Data Cleaning**
> Handled all missing values and removed inconsistent entries to ensure model reliability.

**2. 🍽️ Cuisine Simplification**
> Many restaurants list multiple cuisines (e.g., *"North Indian, Chinese, Fast Food"*). We extracted only the **primary cuisine** to keep the classification clean and focused.

**3. ⚖️ Handling Class Imbalance**
> Some cuisines had thousands of samples while others had just a few. We narrowed down to the **Top 10 most frequent cuisines** to prevent the model from being biased toward dominant categories.

**4. 🔢 Encoding Categorical Variables**
> Converted text-based features (City, Yes/No columns) into numeric format that the model can process.

**5. ✂️ Train-Test Split**
> Divided the dataset into training and testing sets to evaluate model performance on unseen data.

**6. 🌲 Model Training & Evaluation**
> Trained the Random Forest Classifier and measured accuracy, precision, recall, and F1-score.

---

## 📈 Results

<div align="center">

### 🏆 Classification Performance

| Metric | Score |
|---|---|
| 🎯 Algorithm | Random Forest Classifier |
| 🍽️ Classes Predicted | Top 10 Cuisines |
| 📊 Evaluation | Accuracy, Precision, Recall, F1 |

</div>

> 📌 See `Task3 output.png` in the repository for the full confusion matrix and classification report!

---

## 🍽️ Top 10 Cuisines Classified

```
 1. 🍛  North Indian        6. 🥘  Mughlai
 2. 🍕  Italian             7. 🍔  Fast Food
 3. 🍣  Chinese             8. 🥗  Cafe
 4. 🌮  Continental         9. 🍜  South Indian
 5. 🍱  Bakery             10. 🍰  Desserts
```

*(Actual cuisines depend on dataset distribution)*

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Run the Project

```bash
# Clone the repository
git clone https://github.com/navyne02/Cuisine-Classification.git

# Navigate into the project
cd Cuisine-Classification

# Run the classification model
python "task3 code.py"
```

---

## 🛠️ Tech Stack

<div align="center">

| Tool | Role |
|---|---|
| 🐍 Python | Core Language |
| 🐼 Pandas | Data Loading & Cleaning |
| 🔢 NumPy | Numerical Operations |
| 🤖 Scikit-Learn | ML Model & Evaluation |
| 📊 Matplotlib / Seaborn | Visualization & Confusion Matrix |

</div>

---

## 💡 Future Improvements

- [ ] 🌐 Build a **Streamlit web app** for live cuisine prediction
- [ ] 🔤 Use **restaurant name / menu keywords** as NLP features
- [ ] ⚖️ Apply **SMOTE** for better class imbalance handling
- [ ] 🧪 Compare with **XGBoost**, **SVM**, and **KNN** classifiers
- [ ] 🗺️ Add **geolocation heatmaps** to visualize cuisine hotspots by city
- [ ] 🚀 Deploy as a REST API using **FastAPI** or **Flask**

---

## 🔗 Related Projects

| Project | Description |
|---|---|
| 🍽️ [Predict-Restaurant-Ratings](https://github.com/navyne02/Predict-Restaurant-Ratings) | Predicts restaurant rating using Random Forest Regressor |

---

## 🤝 Contributing

Contributions are always welcome! Here's how:

1. 🍴 Fork the repository
2. 🌿 Create a new branch (`git checkout -b feature/your-feature`)
3. 💾 Commit your changes (`git commit -m 'Add your feature'`)
4. 📤 Push to the branch (`git push origin feature/your-feature`)
5. 🔁 Open a Pull Request

---

## 👨‍💻 Author

<div align="center">

**navyne02**

[![GitHub](https://img.shields.io/badge/GitHub-navyne02-black?style=for-the-badge&logo=github)](https://github.com/navyne02)

*"Classifying world cuisines, one decision tree at a time."* 🌍🍽️

</div>

---

<div align="center">

⭐ **Star this repo if it helped you!** ⭐

</div>
