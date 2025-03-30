import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title='Perpetuity Calculator', layout='wide')
st.title("♾️ Perpetuity Investment Calculator")

st.sidebar.header('Enter your financial details')

annual_cashflow = st.sidebar.number_input("💵 Annual Cash Flow (PKR)", min_value=0.0, value=10000.0, step=1000.0)
interest_rate = st.sidebar.slider("📊 Annual Interest Rate (%)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
years_to_visualize = 50

if interest_rate > 0:
    perpetuity_value = annual_cashflow/(interest_rate/100)
    st.subheader("📌 Visual Representation")
    st.success(f"The present value of this perpetuity is: **PKR {perpetuity_value:,.2f}**")

    st.subheader("📈 Visual Representation")

    years = list(range(1, years_to_visualize + 1))
    cash_flow = [annual_cashflow] * years_to_visualize
    cumulative_cashflow = np.cumsum(cash_flow)


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=cash_flow, mode='lines', name='Cash Flow')) 

    fig.update_layout(
        title='Constant Perpetuity Cashflow Overtime',
        xaxis_title='Years',
        yaxis_title='Cashflow (PKR)',
        template='plotly_white'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.caption("♾️ This graph shows the first 50 years of cash flows to represent perpetuity visually.")
    st.caption("⚠️ It is important to note that this is a constant cash flow generation in equal interval of time but for unlimited time periods.")
else:
    st.warning("⚠️ Interest rate must be greater than 0 to calculate perpetuity value.")