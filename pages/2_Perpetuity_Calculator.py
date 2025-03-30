import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title='Perpetuity Calculator', layout='wide')
st.title("♾️ Perpetuity Investment Calculator")

st.sidebar.header('Enter your financial details')

annual_cashflow = st.sidebar.number_input("💵 Annual Cash Flow (PKR)", min_value=0.0, value=10000.0, step=1000.0)
interest_rate = st.sidebar.slider("📊 Annual Interest Rate (%)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
years_to_visualize = st.sidebar.slider("📆 Visualize for how many years (optional)", min_value=1, max_value=60, value=20)

if interest_rate > 0:
    perpetuity_value = annual_cashflow/(interest_rate/100)
    st.subheader("📌 Visual Representation")
    st.success(f"The present value of this perpetuity is: **PKR {perpetuity_value:,.2f}**")

    st.subheader("📈 Visual Representation")

    years = list(range(1, years_to_visualize + 1))
    cash_flow = [annual_cashflow] * years_to_visualize
    cumulative_cashflow = np.cumsum(cash_flow)


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=cash_flow, name='Cash Flow'))
    fig.add_trace(go.Bar(x=years, y=cumulative_cashflow, name='Cumulative Cash Recieved'))

    fig.update_layout(
        title='Estimated Perpetuity Cashflow',
        xaxis_title='Years',
        yaxis_title='Cashflow (PKR)',
        template='plotly_white'
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("⚠️ Interest rate must be greater than 0 to calculate perpetuity value.")