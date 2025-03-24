
### 📌 **Brain Stroke Prediction**
**Predicting the likelihood of stroke based on patient health data using machine learning.**  

---

## 🚀 **Project Overview**
This project aims to predict the probability of stroke in individuals based on health metrics like **age, BMI, hypertension, heart disease, smoking status, and more**. It leverages **machine learning models** trained on a dataset of 15,304 records to enhance early detection and prevention strategies.

---

## 📂 **Dataset**
The dataset contains the following features:
- **Gender** (`Male`, `Female`)
- **Age** (in years)
- **Hypertension** (0 = No, 1 = Yes)
- **Heart Disease** (0 = No, 1 = Yes)
- **Ever Married** (`Yes`, `No`)
- **Work Type** (`Private`, `Self-employed`, etc.)
- **Residence Type** (`Urban`, `Rural`)
- **Average Glucose Level** (mg/dL)
- **BMI** (Body Mass Index)
- **Smoking Status** (`Never Smoked`, `Smokes`, etc.)
- **Stroke** (`0` = No, `1` = Yes) - Target Variable  

---

## ⚙ **Installation**
```bash
# Clone the repository
git clone https://github.com/your-username/brain-stroke-prediction.git

# Navigate to the project directory
cd brain-stroke-prediction

# Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate   # On Mac/Linux
myenv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🏗 **Data Preprocessing**
- **Handled missing values**  
- **Encoded categorical features** (Gender, Work Type, Smoking Status, etc.)  
- **Normalized numerical features** (Age, BMI, Glucose Level)  
- **Applied SMOTE** to balance the dataset  

---

## 🤖 **Machine Learning Models Used**
| Model | Accuracy | Precision | Recall | F1-Score |
|--------|-----------|------------|---------|----------|
| Logistic Regression | 95.45% | 27.2% | 2.2% | 4.1% |
| Random Forest | 95.49% | 40% | 5.9% | 10.3% |
| XGBoost | 95.42% | 40% | 8.9% | 14.6% |
| SVM | 95.62% | 0% | 0% | 0% |
| MLP Classifier | 95.32% | 32% | 5.9% | 10.0% |

✅ **Voting Classifier (Soft Voting)** was also implemented for improved performance.  

---

## 📊 **Feature Importance Analysis**
- **Age, BMI, and Glucose Level** showed a high correlation with stroke occurrence.  
- **Smoking status and hypertension** were secondary contributing factors.  
- **One-hot encoding** was applied to categorical variables like `work_type` and `residence_type`.

---

## 🖥 **Usage**
1. **Run the Flask App**  
   ```bash
   python app.py
   ```
2. **Make Predictions**  
   Open `http://127.0.0.1:5000/` in your browser and input patient details.  

---

## 📌 **Future Enhancements**
- Hyperparameter tuning for better model performance.  
- Deploying the model as an API for real-time predictions.  
- Integrating deep learning models for improved accuracy.  

---

## 📝 **Contributors**
- **Your Name** – Data Scientist  
- **Contributions** welcome! Feel free to submit a PR.  

---

## 📜 **License**
This project is open-source under the **MIT License**.  
