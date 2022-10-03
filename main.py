import streamlit as st
import numpy as np 
import pandas as pd
import requests
import json
import time


st.title("返品了解書作成ツール")
st.text_input("出版社")
st.checkbox("チェック")

#st.write("プレグレスバーの表示")


#latest_interation = st.empty()
#bar = st.progress(0)

#for i in range(100):
#    latest_interation.text(f'interation{i+1}')
#    bar.progress(i + 1)
#    time.sleep(0.1)



text = st.sidebar.text_input('ISBN01')
xmin=st.sidebar.number_input('冊数：',0,100,0)


endpoint = "https://api.openbd.jp/v1/get"

headers= {
    
}
params={
    "isbn": text
}

result = requests.get(endpoint, headers=headers, params=params)

res = result.json()


a1 = res[0]["onix"]["DescriptiveDetail"]["TitleDetail"]["TitleElement"]["TitleText"]["content"]#タイトル
a2 = res[0]["onix"]["ProductSupply"]["SupplyDetail"]["Price"][0]["PriceAmount"]#価格

df = pd.DataFrame({'ISBN': [text,],
                   'タイトル': [a1],
                   '価格': [a2],
                   '冊数': [xmin],
                   })
st.subheader('テスト結果')

st.dataframe(df)