import streamlit as st # 导入Streamlit并用st代表它





###-------------------------------------------------------------------------------







###----------------------------------------------------------------------------------
###  模块③
###  多媒体内容展示，包含图片展示，音频展示，视频播放器
###----------------------------------------------------------------------------------


###-------------------------------------------
# 图片网址
images = ["https://eskipaper.com/images/mountains-1.jpg",
          "https://wallpaperaccess.com/full/1167990.jpg",
          "https://wallpapercave.com/wp/D3r6gVH.jpg"]


###-------------------------------------------
st.subheader("一些风景图片")
st.image(images)



import streamlit as st


###-------------------------------------------

# 读取音频URL
audio_file = 'https://music.163.com/song/media/outer/url?id=28263184.mp3'

###-------------------------------------------

st.subheader('播放音频')
st.audio(audio_file)








import streamlit as st
from streamlit.components.v1 import html



# 自定义CSS样式
st.markdown("""
<style>
    /* 主标题样式 */
    .main-title {
        font-size: 2.5rem;
        text-align: center;
        color: #00a1d6;
        margin-bottom: 1.5rem;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    
    /* 自定义按钮样式 */
    .custom-btn {
        background-color: white !important;
        color: black !important;
        border: 2px solid #ff4b4b !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: bold !important;
        transition: all 0.3s !important;
        width: 100% !important;
    }
    .custom-btn:hover {
        background-color: #fff0f0 !important;
        transform: scale(1.05) !important;
    }
    
    /* 视频容器样式 */
    .video-container {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }
    
    /* 当前播放信息样式 */
    .current-playing {
        font-size: 1.1rem;
        text-align: center;
        padding: 0.5rem;
        background-color: #f8f9fa;
        border-radius: 8px;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 美化后的主标题
st.markdown('<p class="main-title">🎬 B站视频播放器</p>', unsafe_allow_html=True)

# B站视频数据
video_data = {
    "视频1 - 高山风景视频": "BV1ST411E7wb",  
    "视频2 - 这大概就是美到窒息的感觉吧": "BV13A4y1Z7m2",
    "视频3 - 仿佛来到了童话里的世界~": "BV1co7Bz6Ehp",
    "视频4 - 日落后的二十分钟，被称为蓝调时刻": "BV1gLB4YwEXH",  
    "视频5 - 久在樊笼里，复得返自然": "BV1exrdYZEfM",
    "视频6 - 这是地理课本里的峡湾地貌 也是我国唯一没有的地貌": "BV1d9f4YoEwV"
}

# 获取视频列表和当前索引
video_list = list(video_data.values())
current_index = st.session_state.get("current_index", 0)

# 处理导航按钮点击
def navigate(direction):
    if direction == "prev":
        st.session_state.current_index = (current_index - 1) % len(video_list)
    elif direction == "next":
        st.session_state.current_index = (current_index + 1) % len(video_list)
    st.session_state.current_video = video_list[st.session_state.current_index]
    st.rerun()

# 获取当前BV号
current_bv = st.session_state.get("current_video", video_list[current_index])

# 创建容器放置视频和按钮
with st.container():
    # 视频选择下拉菜单
    selected_title = st.selectbox(
        "选择视频",
        options=list(video_data.keys()),
        index=current_index,
        key="video_selector"
    )
    
    # 如果下拉菜单选择变化，更新当前视频
    if selected_title != list(video_data.keys())[current_index]:
        st.session_state.current_index = list(video_data.keys()).index(selected_title)
        st.session_state.current_video = video_data[selected_title]
        st.rerun()
    
    # B站播放器HTML模板
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    bili_player = f"""
    <div style="margin:10px 0">
        <iframe 
            width="100%" 
            height="500" 
            src="//player.bilibili.com/player.html?bvid={current_bv}&page=1&high_quality=1&volume=0.3" 
            scrolling="no" 
            frameborder="no" 
            allowfullscreen="true">
        </iframe>
    </div>
    """
    html(bili_player, height=520)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 创建导航按钮（优化后的样式和布局）
    col1, col2, col3 = st.columns([1, 1, 4])  # 调整比例
    with col1:
        if st.button("◀ 上一个", key="prev_btn", help="播放上一个视频"):
            navigate("prev")
    with col2:
        if st.button("下一个 ▶", key="next_btn", help="播放下一个视频"):
            navigate("next")
    
    # 显示当前视频标题
    current_title = list(video_data.keys())[current_index]
    st.markdown(f'<div class="current-playing">🎥 当前播放: <strong>{current_title}</strong></div>', unsafe_allow_html=True)




# 添加页脚
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>© 2025 个人网页制作演示 | CPU180 版本号：0.6.12.4</p>
</div>
""", unsafe_allow_html=True)
