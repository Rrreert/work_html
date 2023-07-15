import streamlit as st
import streamlit.components.v1 as components
import glob

st.set_page_config(layout="wide")


def set_background():
    page_bg_img = '''
    <style>
    .css-1avcm0n {background: rgb(14, 17, 23, 0)}
    .css-18ni7ap {background: rgb(255, 255, 255, 0)}
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    .css-18e3th9 {padding: 0 1rem 1rem}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background()

files_name = glob.glob('documents/*')
files_dic = {}
for item in files_name:
    files_dic[item.split('\\')[-1]] = item

col1, col2, col3 = st.columns([0.5, 2, 7.5])
with col2:
    name = st.selectbox('请选择需要预览的文件 👇', files_dic.keys())

with open(files_dic[name], encoding='utf8') as fp:
    text = fp.read()
components.html(text, scrolling=True, height=800)
