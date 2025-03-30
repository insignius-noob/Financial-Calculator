import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

#Menu
st.set_page_config(page_title='Finance Calculator', layout='wide')


# st.set_page_config(page_title="Annuity Calculator", layout="wide")
st.title("📈 Annuity Investment Calculator")
st.sidebar.header("Enter your investment details")
initial_investment = st.sidebar.number_input("💵 Initial Investment Amount", min_value=0.0, value=50000.0, step=10000.0)
monthly_contribution = st.sidebar.number_input("📥 Monthly Contribution", min_value=0.0, value=10000.0, step=1000.0)
interest_rate = st.sidebar.slider("📊 Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
years = st.sidebar.slider("📆 Number of Years", min_value=1, max_value=60, value=20)


def calculate_annuity(initial_investment, monthly_contribution, interest_rate, years):
    months = years * 12
    monthly_rate = interest_rate/12/100 
    values = [] #storing money after each month
    amount = initial_investment
    for month in range(months):
        amount = amount * (1 + monthly_rate)
        amount = amount + monthly_contribution
        values.append(amount)
    return values


values = calculate_annuity(initial_investment, monthly_contribution, interest_rate, years)
months = list(range(1, years *12 + 1))

st.subheader("📌 Visual Representation")
st.success(f"After {years} years, your investment will grow to: **PKR {values[-1]:,.2f}**")

#Annuity Graph
fig = go.Figure()
fig.add_trace(go.Scatter(x=months, y = values, mode = 'lines', name = 'Annuity'))
fig.update_layout(
    title = 'Investment growth over time',
    xaxis_title = 'Months',
    yaxis_title = 'Future Value (PKR)',
    template = 'plotly_white'
)
st.plotly_chart(fig, use_container_width = True)