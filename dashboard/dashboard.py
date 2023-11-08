import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')


def create_byworkingday_df(df):
    byworkingday_df = df.groupby(
        by="workingday").instant.nunique().reset_index()

    return byworkingday_df


def create_byweathersit_df(df):
    byweathersit_df = df.groupby(
        by="weathersit").instant.nunique().reset_index()

    return byweathersit_df


# Load cleaned data
all_df = pd.read_csv("dashboard/all_data.csv")

# # Menyiapkan berbagai dataframe
byworkingday_df = create_byworkingday_df(all_df)
byweathersit_df = create_byweathersit_df(all_df)

st.header('Bike Sharing Dashboard :bicyclist:')
st.subheader('Cyclist Demographics')

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))

    colors = ["#D3D3D3", "#72BCD4"]

    sns.barplot(
        y="instant",
        x="workingday",
        data=byworkingday_df.sort_values(by="instant", ascending=False),
        palette=colors,
        ax=ax,
        hue="instant"
    )
    ax.set_title("Number of Users by Working Day", loc="center", fontsize=50)
    ax.set_ylabel("Users", fontsize=30)
    ax.set_xlabel("Working Day", fontsize=30)
    ax.tick_params(axis='x', labelsize=50)
    ax.tick_params(axis='y', labelsize=50)
    st.pyplot(fig)

    # textcol1 = '''Based on documentation from https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset, the number 1 indicates a working day or weekday, and 0 represents weekends and holidays.
    # '''
    # st.markdown(textcol1)


with col2:
    fig, ax = plt.subplots(figsize=(20, 10))

    colors = ["#D3D3D3", "#D3D3D3", "#72BCD4"]

    sns.barplot(
        y="instant",
        x="weathersit",
        data=byweathersit_df.sort_values(by="instant", ascending=False),
        palette=colors,
        ax=ax,
        hue="instant"
    )
    ax.set_title("Number of Users by Weathersit", loc="center", fontsize=50)
    ax.set_ylabel("Users", fontsize=30)
    ax.set_xlabel("Weathersit", fontsize=30)
    ax.tick_params(axis='x', labelsize=50)
    ax.tick_params(axis='y', labelsize=50)
    st.pyplot(fig)

    # textcol2 = '''Based on documentation from https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset there are 4 weather categories, here is the explanation:

    # 1: Clear, Few clouds, Partly cloudy, Partly cloudy
    # 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    # 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    # 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
    # '''
    # st.markdown(textcol2)

st.markdown("Created by mluthfifrd")
