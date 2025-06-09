import streamlit as st
from config import LANGUAGES, MENU
from modules import intro, dance, drum, paint, qa, showcase

st.set_page_config(page_title="老虎笙 Tiger Sheng 教学网页", layout="wide")

# 初始化语言状态
if "lang" not in st.session_state:
    st.session_state.lang = LANGUAGES[0]

# 左侧栏语言选择
lang = st.sidebar.selectbox("选择语言 / Choose Language", LANGUAGES)
st.session_state.lang = lang

# 左侧栏导航菜单
page = st.sidebar.radio("导航 Navigation", list(MENU.keys()))
selected_page = MENU[page]

# 路由模块调用
if selected_page == "intro":
    intro.render(lang)
elif selected_page == "dance":
    dance.render(lang)
elif selected_page == "drum":
    drum.render(lang)
elif selected_page == "paint":
    paint.render(lang)
elif selected_page == "qa":
    qa.render(lang)
elif selected_page == "showcase":
    showcase.render(lang)
elif selected_page == "home":
    col1, col2 = st.columns([3, 1])

    with col1:
        if lang == "中文":
            st.title("🐯 云南彝族“老虎笙”的故事")
            st.image("assets/home.png", width=400)
            st.markdown("欢迎来到老虎笙课程主页！请选择左侧菜单浏览各模块内容。")
            st.markdown("---")
            st.markdown("""
            <div style='font-size:14px; color: #555; line-height: 1.6;'>
                <strong>制作者：</strong> 张怡，奎卓然，李欣欣，李妍妍，李亚辉<br>
                <strong>指导教师：</strong> 周晓宇
            </div>
            """, unsafe_allow_html=True)
        else:
            st.title("🐯 The story of Tiger Sheng")
            st.image("assets/home.png", width=400)
            st.markdown("Welcome to the Tiger Sheng course homepage! Use the left menu to explore modules.")
            st.markdown("---")
            st.markdown("""
            <div style='font-size:14px; color: #555; line-height: 1.6;'>
                <strong>Created by:</strong> Zhang Yi, Kui Zhuoran, Li xinxin, Li Yanyan, Li Yahui<br>
                <strong>Instructor:</strong> Zhou Xiaoyu
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='text-align: right; line-height: 1.2;'>
            <span style='font-size:18px; font-weight:600;'>楚雄师范学院语言文化学院</span><br>
            <span style='font-size:16px; font-style: italic; color:#444;'>CXNU School of Language and Culture</span><br>
            <span style='font-size:16px; color:gray;'>笃学尚行  扬美崇善</span>
        </div>
        """, unsafe_allow_html=True)