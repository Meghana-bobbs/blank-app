import streamlit as st
import pandas as pd
import os

# --- Page Config ---
st.set_page_config(page_title="Team Task Snapshot", layout="wide")

# --- File Path ---
DATA_FILE = "team_tasks.xlsx"

# --- Initialize or Load Data ---
def load_data(sheet_name):
    if os.path.exists(DATA_FILE):
        return pd.read_excel(DATA_FILE, sheet_name=sheet_name)
    else:
        return pd.DataFrame({
            "Task": [""],
            "Status": [""],
            "PIC": [""],
            "Due Date": [""],
            "Done": [False],
        })

def save_data(priority_df, monthly_df, daily_df, followups_df):
    with pd.ExcelWriter(DATA_FILE) as writer:
        priority_df.to_excel(writer, sheet_name="Priority", index=False)
        monthly_df.to_excel(writer, sheet_name="Monthly", index=False)
        daily_df.to_excel(writer, sheet_name="Daily", index=False)
        followups_df.to_excel(writer, sheet_name="FollowUps", index=False)

# --- Load Data ---
df_priority = load_data("Priority")
df_monthly = load_data("Monthly")
df_daily = load_data("Daily")
df_followups = load_data("FollowUps")

# --- Custom CSS ---
st.markdown("""
    <style>
    body, .main, .block-container {
        background-color: #eafaf1 !important;
        color: #1c1c1c !important;
    }

    h1, h2, h3 {
        color: #1c1c1c !important;
        margin-top: 0.5rem;
    }

    .section-banner {
        background-color: #bdc3c7;  
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        font-weight: 600;
        font-size: 1.2rem;
    }

    .stDataEditor {
        background-color: transparent !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
    }

    .stDataEditor table {
        background-color: white !important;
        border-radius: 8px;
        overflow: hidden;
    }

    .stDataEditor table td {
        color: #1c1c1c !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Page Title ---
st.markdown("## 🫡 Task Dashboard")
st.markdown("Keep track of **what's happening this week**, monthly responsibilities, daily priorities, and ongoing follow-ups.")

# --- Layout ---

# Top Row
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-banner">📌 This Week\'s Priority</div>', unsafe_allow_html=True)
    df_priority = st.data_editor(df_priority, key="priority", num_rows="dynamic")

with col2:
    st.markdown('<div class="section-banner">📆 Monthly Duties</div>', unsafe_allow_html=True)
    df_monthly = st.data_editor(df_monthly, key="monthly", num_rows="dynamic")

# Bottom Row
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="section-banner">📅 Daily Priorities</div>', unsafe_allow_html=True)
    df_daily = st.data_editor(df_daily, key="daily", num_rows="dynamic")

with col4:
    st.markdown('<div class="section-banner">📝 Follow-Ups</div>', unsafe_allow_html=True)
    df_followups = st.data_editor(df_followups, key="followups", num_rows="dynamic")

# --- Save Button ---
if st.button("💾 Save All Changes"):
    save_data(df_priority, df_monthly, df_daily, df_followups)
    st.success("✅ Changes saved for everyone!")
