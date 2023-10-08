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

name_dic = {
    "youtube.html": "youtube评论文本分析",
    "modelPred.html": "房价预测",
    "Store.html": "商店销量预测",
    "water-bottle-images-classification-cnn-resnet50.html": "图像分类",
    "ICH.html": "医学二分类",
    "ICR.html": "ICR二分类",
    "HouseClean.html": "房源数据清洗",
    "DBSCAN.html": "船舶航迹聚类",
    "Korea.html": "韩国房价数据挖掘",
    "HouseRec.html": "房源推荐模型",
    "TDM.html": "血糖预测",
    "DBSCAN_model.html": "船舶航迹预测",
    "Laying.html": "下蛋率数据挖掘",
    "FIT5196.html": "房源选择决策研究",
    "主题分类.html": "B站评论主题分类（需稍加等待加载）",
    "主题分类_youtube.html": "油管评论主题分类",
    "DDOS.html": "DDOS攻击分类预测",
}
files_name = glob.glob('documents/*')
files_dic = {}
for item in files_name:
    files_dic[name_dic[item.split('/')[-1]]] = item

col1, col2, col3 = st.columns([0.5, 2, 7.5])
with col2:
    name = st.selectbox('请选择需要预览的文件 👇', files_dic.keys())

with open(files_dic[name], encoding='utf8') as fp:
    text = fp.read()
components.html(text, scrolling=True, height=800)
