import streamlit as st
import plotly.express as px
import pandas as pd
from numerize.numerize import numerize
from query import *
st.set_page_config(page_title="sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
)
st.title(":bar_chart: Diary Product Selling Website")
st.subheader("created by Ashutosh Mishra :smiling_imp:")
st.video("sudha_milk.mp4.mp4")

st.header("6 Products Available:-")

st.subheader("1) Sudha Peda")
st.image("download.jfif", caption="Fig:- Peda")
st.text("Peda is a sweet from the Indian subcontinent, usually prepared in thick, semi-soft pieces.")

st.subheader("2) Full Cream Milk")
st.image("milk.jfif", caption="Fig:- Full Cream Milk")
st.text("Milk is a pale liquid produced by the mammary glands of mammals.")

st.subheader("3) Sudha Gold")
st.image("goldmilk.jfif", caption="Fig:- Gold Milk")
st.text("Milk is a pale liquid produced by the mammary glands of mammals..")

st.subheader("4) Kalakand")
st.image("kalakand.jfif",caption="Fig:- Kalakand")
st.text("Kalakand is a sweet from the Indian subcontinent, usually prepared in thick, semi-soft pieces.")

st.subheader("5) Butter")
st.image("butter.jfif", caption="Fig:- Butter")
st.text("Pasteurized Sudha Butter meets the FSSAI standards for the respective type of milk")

st.subheader("6) Ghee")
st.image("ghee.jfif", caption="Fig:- Ghee")
st.text("Ghee is prepared by simmering butter, which is churned from cream, and removing the liquid residue.")

st.markdown("---")

result = view_all_data()
df=pd.DataFrame(result,columns=["product_id","product_name","price","date_of_expiry","quantity_available"])

st.sidebar.image("data/logo.jpg",caption="SUDHA INDIA")

st.sidebar.header("Please Filter")
product_name = st.sidebar.multiselect(
    "Select product_name",
    options=df["product_name"].unique(),
    default=df["product_name"].unique()
)
df_selection=df.query(
    "product_name==@product_name"
)
st.dataframe(df_selection)

st.header("Put Your Order Below:point_down:")

classdata1 = st.selectbox("Sudha Peda : ",("Quantity",0,1,2,3,4,5,6,7,8,9,10))

classdata2 = st.selectbox("Full Cream Milk : ",("Quantity",0,1,2,3,4,5,6,7,8,9,"Max(10)"))

classdata3 = st.selectbox("Sudha Gold : ",("Quantity",0,1,2,3,4,5,6,7,8,9,"Max(10)"))

classdata4 = st.selectbox("Kalakand : ",("Quantity",0,1,2,3,4,5,6,7,8,9,"Max(10)"))

classdata5 = st.selectbox("Butter : ",("Quantity",0,1,2,3,4,5,6,7,8,9,"Max(10)"))

classdata6 = st.selectbox("Ghee : ",("Quantity",0,1,2,3,4,5,6,7,8,9,"Max(10)"))


button = st.button("Confirm Order")
st.header("Your Order Details are:-")
if button :
    st.markdown(f"""            
    Sudha Peda : {classdata1}
    Full Cream Milk : {classdata2} 
    Sudha Gold : {classdata3}
    Kalakand : {classdata4}
    Butter : {classdata5}
    Ghee : {classdata6}""")