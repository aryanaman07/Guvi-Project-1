# Guvi-Project-1
# 📚 Problem Statement - 16: School Library Usage Dashboard

A data visualization project to monitor borrowing and return activity in a school library using Python, Pandas, Plotly, and Streamlit.

---

## 🚀 Features

- 📋 **Interactive Table**: View records with book title, borrower, and status.
- 📊 **Bar Chart**: Visualize most borrowed books.
- 📈 **Pie Chart**: See borrowed books by genre.
- 📌 **KPIs**:
  - Total borrowed books
  - Overdue book count
- 🎛️ **Filters**:
  - Borrow date range
  - Status (Borrowed, Returned, Overdue)
- 📁 Export filtered data as CSV

---

## 📂 Dataset

- **Rows**: 1000+
- **Fields**:  
  `BookID`, `Title`, `Genre`, `BorrowerName`, `BorrowDate`, `ReturnDate`, `Status`

The dataset is synthetically generated using `Faker` to simulate realistic library usage.

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas 📊
- Plotly 📈
- Streamlit ⚡
- Matplotlib + Seaborn (for Jupyter visuals)

---

## 📁 Project Structure

```plaintext
📁 Guvi-Project-1/
├── app.py                          # Main Streamlit app
├── school_library_dashboard.ipynb  # Jupyter Notebook version of the dashboard
├── school_library_usage_data.csv   # Synthetic dataset (1000+ rows)
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies (to be added)

```
## 🎬 Example
<img width="1919" height="923" alt="Screenshot 2025-08-01 124037" src="https://github.com/user-attachments/assets/0c1f0534-5c2c-4a4a-bd62-2d3ba160668c" />

<img width="1919" height="690" alt="Screenshot 2025-08-01 124102" src="https://github.com/user-attachments/assets/77fb7019-422f-4ed4-8463-e6c899d56f3f" />

<img width="1901" height="923" alt="Screenshot 2025-08-01 124325" src="https://github.com/user-attachments/assets/2479e73d-5d51-4446-859b-efe404ce304e" />



## 💻 How to Run

### 📌 Option 1: Jupyter Notebook

1. Clone the repo
2. Upload the .csv file to your Colab or local environment
3. Open `school_library_dashboard.ipynb`  
4. Run the notebook to see visuals and KPIs

### 📌 Option 2: Streamlit Dashboard

```bash
pip install -r requirements.txt
streamlit run app.py
