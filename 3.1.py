import streamlit as st
st.set_page_config(layout="wide")

st.set_page_config(page_title='简易播放器', page_icon='🎶')

# 在内存中初始化一个ind,当内存中没有'ind'的时候，才初始化
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 图片数组-歌曲

image_obj = [{
        'url': 'https://p1.music.126.net/-xMsNLpquZTmMZlIztTgHg==/109951165953469081.jpg?param=230y230',
        'music':'https://music.163.com/song/media/outer/url?id=1842728629.mp3',
        '歌名': '如果呢',
        '歌手':' ### 郑泽润' 
    }, {
        'url': 'https://p1.music.126.net/CSjhWIv08-c2-M9PY1tLHQ==/109951170980089869.jpg',
        'music':'https://music.163.com/song/media/outer/url?id=2704506819.mp3',
        '歌名': '龙卷风',
         '歌手':' ### 赵乃吉'
    }, {
        'url': 'https://p1.music.126.net/cpoUinrExafBHL5Nv5iDHQ==/109951166361218466.jpg',
        'music':'https://music.163.com/song/media/outer/url?id=29769315.mp3',
        '歌名': '晴天',
        '歌手':' ### 刘瑞琪'
    }]


music_arr=['https://music.163.com/song/media/outer/url?id=1842728629.mp3',
           'https://music.163.com/song/media/outer/url?id=2704506819.mp3',
           'https://music.163.com/song/media/outer/url?id=29769315.mp3'
           ]


def nextImg():
    # 点击下一首按钮要做的事
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_obj)


def lastImg():
    # 点击上一首按钮要做的事
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_obj)
    

   
st.subheader(':🎶: 音乐播放器')
a1, a2 = st.columns([1,2])
with a1:
    # 读取图片IMG
     st.image(image_obj[st.session_state['ind']]['url'])
         
with a2:
    #歌曲名称
    music_name=image_obj[st.session_state['ind']]['歌名']
    st.title(music_name)
    st.markdown('  ')
    
    b1, b2 = st.columns([1,3])
    with b1:
         st.markdown('### 歌手 :')
    with b2:
         #输入歌手名字
        st.markdown( image_obj[st.session_state['ind']]['歌手'])
        st.markdown('')
    st.markdown('  ')
   
    c1, c2 = st.columns(2)
    with c1:
        st.button('上一首',on_click=lastImg, use_container_width=True)
    with c2:
        st.button('下一首',on_click=nextImg, use_container_width=True)
        
# 读取音频URL
audio_file = 'https://music.163.com/song/media/outer/url?id=1842728629.mp3'

st.subheader('播放音频')
st.audio(image_obj[st.session_state['ind']]['music'])


st.title('MV')
#video_file='https://www.bilibili.com/video/BV1d4411N7zD/?spm_id_from=333.337.search-card.all.click'
#st.video(video_file)




import streamlit.components.v1 as components

# B站视频URL
bilibili_url = "https://www.bilibili.com/video/BV1bM4y1c7G2/?spm_id_from=333.337.search-card.all.click"

# 提取BV号
bv_id = bilibili_url.split("/")[-1].split("?")[0]

# 构建嵌入代码
embed_code = f"""
<iframe src="https://player.bilibili.com/player.html?bvid={bv_id}&high_quality=1" 
width="800" height="450" frameborder="0" allowfullscreen></iframe>
"""

# 显示嵌入视频

components.html(embed_code, height=450)
