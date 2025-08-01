import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load dataset
df = pd.read_csv('school_library_usage_data.csv', parse_dates=["BorrowDate", "ReturnDate"])

st.set_page_config(page_title="School Library Dashboard", layout="wide")

st.title("📚 School Library Usage Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("🔎 Filter Records")

# Date range
min_date = df['BorrowDate'].min()
max_date = df['BorrowDate'].max()

start_date, end_date = st.sidebar.date_input(
    "Select Borrow Date Range:",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Status filter
status_options = df['Status'].unique().tolist()
selected_status = st.sidebar.multiselect("Select Status:", status_options, default=status_options)

# --- Apply Filters ---
filtered_df = df[
    (df["BorrowDate"].dt.date >= start_date) &
    (df["BorrowDate"].dt.date <= end_date) &
    (df["Status"].isin(selected_status))
]

# --- KPIs ---
total_borrowed = len(filtered_df)
overdue_count = len(filtered_df[filtered_df["Status"] == "Overdue"])

col1, col2 = st.columns(2)
col1.metric("📦 Total Borrowed (Filtered)", total_borrowed)
col2.metric("⚠️ Overdue Count", overdue_count)

# --- Table ---
st.subheader("📋 Borrowing Table (Filtered)")
st.dataframe(filtered_df[["Title", "BorrowerName", "Status"]], use_container_width=True)

# --- Bar Chart: Most Borrowed Books ---
st.subheader("📊 Most Borrowed Books")
bar_data = filtered_df["Title"].value_counts().reset_index()
bar_data.columns = ["Title", "Borrow Count"]
fig_bar = px.bar(bar_data, x="Title", y="Borrow Count", color="Title", text="Borrow Count")
st.plotly_chart(fig_bar, use_container_width=True)

# --- Pie Chart: Genre Distribution ---
st.subheader("📈 Borrowed Books by Genre")
pie_data = filtered_df["Genre"].value_counts().reset_index()
pie_data.columns = ["Genre", "Count"]
fig_pie = px.pie(pie_data, values='Count', names='Genre', title='Genre Distribution')
st.plotly_chart(fig_pie, use_container_width=True)
