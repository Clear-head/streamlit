import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import numpy as np


def dummy_data_day():
    region = ["경기도", "충청남도", "충청북도", "경상남도", "경상북도", "전라남도", "제주특별자치도", "강원특별자치도", "전북특별자치도"]
    data = {region[_]: [i for i in np.random.randint(1, 30, 7)] for _ in range(len(region))}
    now = datetime.date.today()
    date = [(now - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

    return pd.DataFrame(data, index=date)

def dummy_data_week():
    region = ["경기도", "충청남도", "충청북도", "경상남도", "경상북도", "전라남도", "제주특별자치도", "강원특별자치도", "전북특별자치도"]
    data = {region[_]: [i for i in np.random.randint(1, 30, 7)] for _ in range(len(region))}
    now = datetime.date.today()
    date = [(now - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

    return pd.DataFrame(data, index=date)


def dummy_data_month():
    region = ["경기도", "충청남도", "충청북도", "경상남도", "경상북도", "전라남도", "제주특별자치도", "강원특별자치도", "전북특별자치도"]
    data = {region[_]: [i for i in np.random.randint(1, 30, 12)] for _ in range(len(region))}
    now = datetime.date.today()
    date = [(now - datetime.timedelta(weeks=i*4)).strftime("%Y-%m") for i in range(12)]

    return pd.DataFrame(data, index=date)


def start_setup():
    df = pd.read_csv("./data/2019.csv")
    now = datetime.datetime.now().strftime("%Y-%m-%d")



def map_kakao():
    map_data = pd.DataFrame(
        np.random.randn(5, 1) / [20, 20] + [37.513122, 126.938526], 
        columns=['lat', 'lon']
    )
    st.map(map_data)
    


def draw_barchart(dataframe, x, y):

    fig = px.bar(
        dataframe,
        x=x,
        y=y
    )


def chart_col(appear_chart=None, accident_chart=None):
    appear, accident = st.columns(2)
    with appear:
        st.subheader("출몰 현황 차트(종합)")

        # st.plotly_chart(appear_chart)

    with accident:
        st.subheader("사고 현황 차트(종합)")
        #  st.plotly_chart(accident_chart)
    

def today_dash(fig=None):
    st.header("금일 현황")
    st.divider()

    appear, accident = st.columns(2)
    with appear:
        st.subheader("전국 출몰 현황 차트")

        # st.plotly_chart(appear_chart)

    with accident:
        st.subheader("전국 사고 현황 차트")
        #  st.plotly_chart(accident_chart)


def daily_dash(fig=None):
    st.header("일간 현황")
    st.divider()

    #   일주일 차트.
    chart_col()
    st.plotly_chart(
        px.bar(
            x=dummy_data_day().columns,
            y=[sum(dummy_data_day()[i]) for i in dummy_data_day()],
            template='plotly_dark'
        )
    )


def week_dash(fig=None):
    st.header("주간 현황")
    st.divider()


    #   월단위 차트
    chart_col()
    st.plotly_chart(
        px.bar(
            data_frame=dummy_data_week(),
            y=dummy_data_week().columns,
            x=dummy_data_week().index,
            template='plotly_dark'
        )
    )


def month_dash(fig=None):
    st.header("월간 현황")
    st.divider()

    #   1년 차트
    chart_col()
    st.plotly_chart(
        px.bar(
            data_frame=dummy_data_month(),
            y=dummy_data_month().columns,
            x=dummy_data_month().index,
            template='plotly_dark'
        )
    )


def total_dash(fig=None):
    st.header("종합 현황")
    st.divider()


    #   기준 필요
    chart_col()
    # st.plotly_chart(fig)


side = st.sidebar.selectbox(
    "현황",
    [
        "일간",
        "주간",
        "월간",
        "종합"
    ]
)


today_dash()

st.divider()

if side == "일간":
    daily_dash()
elif side == "주간":
    week_dash()
elif side == "월간":
    month_dash()
else:
    total_dash()

st.divider()

map_kakao()
