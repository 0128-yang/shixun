import streamlit as st
import numpy as np  
import pandas as pd

st.set_page_config(
    page_title="南宁动物园",
    page_icon="🏆"
)





#侧边选项卡
page = st.sidebar.radio("选择页面", ["首页", "员工档案", "园内一瞥","附近美食", "招聘个人信息简历投稿"])

if page == "首页":
    st.title("南宁动物园：城市绿洲中的自然奇趣王国")
    tab1, tab2, tab3 = st.tabs(["门口一览", "五香胡", "熊猫馆"])

    with tab1:
        
        images=['https://n.sinaimg.cn/sinacn10/90/w1000h690/20180831/d4e3-hinpmnq5016932.jpg']
        st.image(images)

    with tab2:
        images=['https://qcloud.dpfile.com/pc/W4kkyyVqV3Ja6kh8a4qZ0i6BN58AzN-9zJ6onbaIrVfM_zlUQkigoY3vIRTvq8gJ.jpg']
        st.image(images)

    with tab3:
       images=['https://b0.bdstatic.com/20dfdc462bfeef2c9f379482134cfe73.jpg']
       st.image(images)


    st.text("""
南宁动物园，全称南宁市动物园，位于广西壮族自治区首府南宁市西乡塘区大学东路73号，是一座集动物保护、科普教育、休闲娱乐、科研繁育于一体的综合性城市动物园。作为国家4A级旅游景区和全国科普教育基地，它不仅承载着野生动物迁地保护的重要职能，更是南宁市民亲子游玩、亲近自然的首选目的地。以下从历史沿革、园区布局、特色展区、科普功能、服务设施及游览建议等方面，为您展开详细介绍。

一、历史沿革：从植物园到现代化动物园
南宁动物园的前身可追溯至1973年成立的南宁市植物园，1975年正式转型为动物园并向公众开放。经过近50年的发展，园区从最初的简单笼舍逐步升级为现代化生态展区：

20世纪80年代：引入大熊猫、亚洲象等珍稀动物，成为广西首个大型动物园。

2005年：完成首次大规模改造，新增热带雨林馆、海豚馆等特色展区。

2010年至今：持续优化动物福利，推行“沉浸式展区”设计，如仿自然生态的“熊猫苑”“长臂猿岛”等。

如今，南宁动物园占地约42公顷，饲养动物超250种、数量逾3000只（头），年接待游客量突破200万人次。

二、园区布局：四大主题区域
动物园按功能划分为动物展区、游乐区、科普区、休闲服务区，游客可沿导览图有序参观。

1. 动物展区
珍稀动物馆

大熊猫苑：居住着来自四川的国宝大熊猫，场馆模拟高山竹林环境，配备空调和专属保育团队。

亚洲象园：东南亚风格场馆，游客可观看大象洗澡、喷水等自然行为展示。

灵长类动物区：包括金丝猴、长臂猿、黑猩猩等，设有攀爬架和树冠走廊。

猛兽谷
白虎、非洲狮、东北虎等生活在仿原生态的山谷中，通过玻璃幕墙安全观赏。

鸟语林
开放式天网内放养孔雀、火烈鸟、犀鸟等，可近距离观察鸟类飞翔。

两栖爬行馆
展出缅甸蟒、鳄龟、变色龙等，配有温湿度控制系统。

2. 加勒比水上世界（季节性开放）
南宁动物园的招牌游乐项目，占地3万平方米，包含：

超级造浪池：人工海浪体验。

彩虹滑道：6条并列滑道，适合亲子互动。

儿童水寨：迷你滑梯和喷水设施。

3. 科普教育区
动物科普馆：通过标本、AR互动屏幕展示生物多样性。

志愿者讲解站：节假日提供免费导览，适合学生团体。

4. 休闲服务区
餐饮：园区内设快餐店、咖啡厅，提供广西特色小吃如老友粉、五色糯米饭。

纪念品商店：出售动物玩偶、文创产品。

三、明星动物与特色体验
1. 不容错过的“动物明星”
“明明”和“阳阳”：两只大熊猫，以憨态可掬的吃竹姿势圈粉无数。

亚洲象“波波”：擅长用鼻子卷起游客投喂的水果（需在饲养员指导下进行）。

白虎“雷霆”：罕见的白化孟加拉虎，威严与美丽并存。

2. 特色互动项目
动物投喂：

长颈鹿投喂（10元/次，提供专用树叶）。

环尾狐猴岛（可进入展区与温顺的狐猴互动）。

行为展示：

海狮表演（每日11:00、15:00两场）。

大象趣味运动会（踢足球、吹口琴等）。

四、科普保护：不止于观赏
南宁动物园积极参与全球濒危物种保护计划（如华南虎繁育），并开展多项公众教育活动：

研学课程：针对中小学生设计“夜探动物园”“动物保育员体验”等活动。

公益宣传：设立“拒绝动物表演”“抵制非法野生动物贸易”展板。

五、实用游览信息
1. 门票与开放时间
门票：成人50元，儿童/学生/老人25元（需证件）。

加勒比水世界：夏季单独售票，约100元/人。

开放时间：

旺季（4-10月）7:30-17:30，淡季（11-3月）8:00-17:00。

2. 交通指南
地铁：1号线“动物园站”C出口直达。

公交：4路、33路、604路等至“动物园站”。

自驾：停车场收费5元/小时，周末建议早到。

3. 游览贴士
最佳时段：上午动物较活跃，避开正午高温。

必备物品：防晒帽、驱蚊液、舒适运动鞋。

禁忌：勿拍打玻璃、勿投喂自带食物。

结语：人与自然和谐共处的典范
南宁动物园通过科学的场馆设计、丰富的互动项目和扎实的保育工作，让游客在欢乐中感受生命之美。无论是家庭出游、科普学习，还是摄影爱好者的创作，这里都能满足您的期待。计划行程前，建议关注官方公众号获取最新活动资讯，让您的游览更加充实！ 🦁🐼🌿""")

    
elif page == "员工档案":
    st.markdown('# 员工档案——芙蓉王源😇')

    st.markdown('# 😃基本信息')

    st.markdown('''# 姓名: *芙蓉王源😁*
    #### 班级: *23级练习生一班😉*
    #### 学号: *9527😇*''')


    # 创建一个为基本信息的标题，并指定锚点为基本信息
    st.header('兴趣:smiley:', anchor='text!')
    st.markdown('### :red[游戏] 🎮, :blue[游泳]🏊︎ ,:orange[唱跳]🎤 , :green[篮球]🏀')

    #调用指标类展示元素metric
    st.subheader('')
    st.metric(label="当前学期", value="大二 下学期")
    st.subheader('学习情况')

    c1, c2, c3 = st.columns(3)
    c1.metric(label="当前周数", value="15/20", delta="剩余5周")
    c2.metric(label="四六级进度", value="1/2", delta="已过四级")
    c3.metric(label="人生进度", value="20/100", delta="未来可期")

    #对于箭头的表示通过在内容前使用+或-进行展示
    st.metric(label="-心情状态",value="心情状态",delta="愉悦",label_visibility='visible')

    # Streamlit课程进度部分
    st.header('Streamlit课程进度')
    st.progress(0.2, text="Streamlit课程进度") # 此处设置参数为20%



    data = {
       '课程': ['高等数学', '大学英语', 'C语言程序设计'],
       '期末达标分数': [90,101,97],
       '状态': ['***通过***','***通过***','***补考***'], 
       '难度': ['***中等***','***简单***','***困难***']
    }

    ###-------------------------------------------
    # 字体样式提示
    #st.markdown('*斜体文本*')
    #st.markdown(' 斜体文本 ')
    #st.markdown('**斜体文本**')
    #st.markdown('_*斜体文本 ')
    #st.markdown('**斜体文本***')
    #st.markdown('_* 斜体文本 ')
    ###-------------------------------------------

    index = pd.Series(['1','2','3'], name='') 
    # 根据上面创建的data和index，创建数据框 
    df = pd.DataFrame(data, index=index) 

    st.subheader('课程日志')
    st.table(df)
    #使用datatrame可以增加用户对数据的处理，此处使用table表示仅进行展示

    # 创建一个代码块，用于展示python_code的内容
    # line_numbers=True 表示显示代码行数
    # language为None，即该代码块无法满足高亮
    st.subheader('Python代码展示')
    python_code = '''def hello():
        print('你好，Streamlit！')'''

    st.code(python_code, line_numbers=True)

    st.subheader('java代码展示')
    java_code = '''public class Hello {
        public static void main(String[] args) {
            System.out.println('你好！ Streamlit！');
        }
    }'''

    st.code(java_code, language='java',line_numbers=True)

    st.subheader('JavaScript代码展示')
    javascript_code = '''<p id="demo"></p>
    <script>
        document.getElementById('demo').innerHTML ='你好！ Streamlit！';
    </script>'''

    st.code(javascript_code, language='javascript',line_numbers=True)



elif page =="园内一瞥":
    st.markdown('<p class="main-title">图片展示模块</p>', unsafe_allow_html=True)



    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 图片网址
    images = ["https://wallpaperaccess.com/full/1414728.jpg",
              "https://wallpaperaccess.com/full/1167990.jpg",
              "https://wallpapercave.com/wp/D3r6gVH.jpg"]


    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    st.subheader("一些风景图片")
    st.image(images)



    import streamlit as st


    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # 读取音频URL
    audio_file = 'https://music.163.com/song/media/outer/url?id=28263184.mp3'

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    st.subheader('播放音频')
    st.audio(audio_file)






    ###-------------------------------------------
    # 视频播放器代码块

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

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # B站视频数据
    video_data = {
        "视频1 - 高山风景视频": "BV1ST411E7wb",  
        "视频2 - 这大概就是美到窒息的感觉吧": "BV13A4y1Z7m2",
        "视频3 - 仿佛来到了童话里的世界~": "BV1co7Bz6Ehp",
        "视频4 - 日落后的二十分钟，被称为蓝调时刻": "BV1gLB4YwEXH",  
        "视频5 - 久在樊笼里，复得返自然": "BV1exrdYZEfM",
        "视频6 - 这是地理课本里的峡湾地貌 也是我国唯一没有的地貌": "BV1d9f4YoEwV"
    }

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


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
    st.markdown(f'🎥 **当前播放: {current_title}**')
        
elif page == "附近美食":
    restaurants = pd.DataFrame({
    "餐厅名称": ["舒记老友粉", "天福香老友粉", "三品王牛肉粉", "姜胖胖自助烤肉", "牛扒大亨西餐厅","素宴·蔬食(素食自助餐厅科德店)","隆江猪脚饭(衡阳店)","尝回家猪脚饭·烧卤·白切(友爱店)","乐观面屋(东盟店)","重庆江湖拌面","三兄弟小龙虾馆","苏格里岛自助海鲜烤肉","吉布鲁牛排海鲜自助(南宁江南万达店)","鹿客臻鲜·海鲜烤肉自助餐厅(蓝鲸世界店)","今邕烧烤(园湖店)","舌战烧烤酒馆(三街两巷店)","亿口香龙虾","炙爱烧烤(万秀店)","夏朗蛋糕(城市花园店)","卡卡米苏·生日蛋糕(西乡塘店)","盛记顺德高佬猪杂粥店","南宁市雲菌瑶酒楼","啫啫村-生料啫啫煲(埌西店)"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐","自助","堂食","堂食","粉","粉","小吃","自助","自助","自助","烧烤","烧烤","小吃","烧烤","糕点","糕点","粥","自助","堂食"],
    "评分": [4.4, 4.1,  4.9, 4.3,4.6,4.7,4.4,4.5,4.2,4.7,4.6,4.6,4.5,4.3,4.8,4.6,4.3,4.2,4.6,4.7,4.4,4.2,4.7],
    "人均消费(元)": [15, 15, 20, 60, 80,30,30,39,21,20,103,78,80,90,123,90,120,89,68,134,15,200,34],
    "营业时间": ["6:00-22:00","5:00-23:00","10:00-23:00","12:00-24:00","17:00-20:30","10:30-20:00","9:00-19:00","9:00-20:00","9:00-20:00","12:00-23:00","12:00-23:00","12:300-23:00","12:00-23:00","17:00-23:00","17:00-02:00","17:00-02:00","12:300-23:00","12:300-23:00","17:30-22:00","7:30-22:00","7:30-22:00","7:30-22:00","7:30-22:00"],
    "latitude": [22.809728,22.822481,22.838432,22.789523,22.808867,22.848224,22.831269,22.839999,22.689112,22.810435,22.756756,22.813919,22.790188,22.769671,22.826847,22.813768,22.845349,22.789165,22.808243,22.688017,22.819031,22.798990,22.805077],
    "longitude": [108.324614,108.387910,108.262110,108.313493,108.326838,108.257296,108.310691,108.309224,108.267817,108.284216,108.332567,108.321484,108.312827,108.306724,108.339396,108.320656,108.315969,108.318908,108.370764,108.300288,108.343062,108.378891,108.368414]
    })

    

    st.markdown('### 门店详细数据（仅展示评分大于4.5的店铺）')

    #仅展示评分大于4.5的店
    high_rating = restaurants[restaurants["评分"] >= 4.5]
    # 显示表格（可排序、搜索）
    st.dataframe(high_rating[["餐厅名称", "类型", "评分", "人均消费(元)","营业时间"]])




    st.markdown("### 人均消费数据")

    st.bar_chart(restaurants.set_index("餐厅名称")["人均消费(元)"])


    st.markdown('### 门店评分数据（仅展示评分大于4.5的店铺）')

    # 设置餐厅名称为索引（X轴）
    data_for_chart = restaurants.set_index("餐厅名称")["评分"]

    # 绘制面积图
    st.area_chart(data_for_chart)

    # 绘制折线图
    st.markdown('### 价格走势折线图')

    data = {
        '月份': ['一月', '二月', '三月', '四月', '五月', '六月', 
               '七月', '八月', '九月', '十月', '十一月', '十二月'],
        '书记老友粉': [15, 18, 14, 17, 19, 31, 22, 13, 17, 13, 11, 21],
        '天福香老友粉': [18, 16, 21, 24, 45, 21, 12, 24, 26, 16, 18, 25],
        '三品王牛肉粉': [23, 21, 34, 23, 25, 35, 53, 27, 21, 24, 32, 14],
        '姜胖胖自助烤肉': [115, 145, 95, 122, 165, 116, 131, 151, 125, 99, 123, 156],
        '乐观面屋(东盟店)': [27, 25, 34, 35, 21, 41, 12, 35, 23, 34, 28, 45]
    }

    df = pd.DataFrame(data)
    df.index = pd.RangeIndex(start=1, stop=13, name='序号')  # 更规范的设置索引方式

    st.line_chart(df, x='月份')
     

    import pydeck as pdk


    ###-------------------------------------------------------------------------------
    ### 腾讯地图模块(正在完善中)
    ### 点击显示功能尚未实现


    import streamlit.components.v1 as components


    # API配置
    TENCENT_API_KEY = "7QTBZ-NDMLM-GAQ6N-6YN54-XVWL2-5WFQS"




    # 确保列名正确 - 直接使用数据中的实际列名
    required_columns = {
        'name': '餐厅名称',
        'category': '类型',
        'rating': '评分',
        'price': '人均消费(元)',
        'hours': '营业时间',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    # 检查所有必要列是否存在
    missing_cols = [col for col in required_columns.values() if col not in restaurants.columns]
    if missing_cols:
        st.error(f"数据中缺少必要列: {missing_cols}")
        st.stop()

    # 重命名列以匹配地图代码中的预期字段名
    restaurants = restaurants.rename(columns={
        '餐厅名称': 'name',
        '类型': 'category',
        '评分': 'rating',
        '人均消费(元)': 'price',
        '营业时间': 'hours'
    })

    # 确保经纬度是数值类型
    restaurants['latitude'] = pd.to_numeric(restaurants['latitude'], errors='coerce')
    restaurants['longitude'] = pd.to_numeric(restaurants['longitude'], errors='coerce')

    # 移除无效坐标
    restaurants = restaurants.dropna(subset=['latitude', 'longitude'])

    # 显示处理后的数据供检查
    #st.write("处理后的餐厅数据:", restaurants.head())

    # 然后使用之前提供的地图HTML代码
    # 注意确保TENCENT_API_KEY已正确设置

    #地图参数设置（调用腾讯定位服务API）
    map_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://map.qq.com/api/gljs?v=2.exp&key={TENCENT_API_KEY}"></script>
        <style>
            #map-container {{
                width: 100%;
                height: 500px;
                margin: 0;
                padding: 0;
                position: relative;
            }}
            #map {{
                width: 100%;
                height: 100%;
            }}
            .info-window {{
                min-width: 200px;
                padding: 10px;
                font-family: Arial, sans-serif;
            }}
            .info-window h3 {{
                margin: 0 0 8px 0;
                font-size: 16px;
                color: #333;
            }}
            .info-window p {{
                margin: 4px 0;
                font-size: 14px;
                color: #666;
            }}
            #loading {{
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(255,255,255,0.8);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 1000;
            }}
        </style>
    </head>
    <body>
        <div id="map-container">
            <div id="loading">地图加载中...</div>
            <div id="map"></div>
        </div>
        <script>
            // 更健壮的数据处理
            function processRestaurantData(data) {{
                return data.map(restaurant => {{
                    return {{
                        id: restaurant.id || Math.random().toString(36).substr(2, 9),
                        name: restaurant.name || '未知餐厅',
                        category: restaurant.category || '未知类型',
                        rating: restaurant.rating || '无评分',
                        price: restaurant.price || '未知',
                        hours: restaurant.hours || '未知',
                        latitude: Number(restaurant.latitude),
                        longitude: Number(restaurant.longitude)
                    }};
                }}).filter(restaurant => 
                    !isNaN(restaurant.latitude) && 
                    !isNaN(restaurant.longitude) &&
                    Math.abs(restaurant.latitude) <= 90 &&
                    Math.abs(restaurant.longitude) <= 180
                );
            }}
            
            // 初始化地图
            function initMap() {{
                try {{
                    // 隐藏加载提示
                    document.getElementById('loading').style.display = 'none';
                    
                    // 处理数据
                    var rawData = {restaurants.to_json(orient='records', force_ascii=False)};
                    var restaurantData = processRestaurantData(rawData);
                    
                    if (restaurantData.length === 0) {{
                        throw new Error('没有有效的餐厅位置数据');
                    }}
                    
                    // 计算中心点
                    var centerLat = restaurantData.reduce((sum, r) => sum + r.latitude, 0) / restaurantData.length;
                    var centerLng = restaurantData.reduce((sum, r) => sum + r.longitude, 0) / restaurantData.length;
                    
                    // 创建地图
                    var map = new TMap.Map(document.getElementById('map'), {{
                        center: new TMap.LatLng(centerLat, centerLng),
                        zoom: 12,
                        mapStyleId: "style1"
                    }});
                    
                    // 创建标记
                    var markerLayer = new TMap.MultiMarker({{
                        map: map,
                        styles: {{
                            default: new TMap.MarkerStyle({{
                                width: 25,
                                height: 35,
                                anchor: {{ x: 12, y: 35 }},
                                src: "https://mapapi.qq.com/web/lbs/javascriptGL/demo/img/markerDefault.png"
                            }})
                        }},
                        geometries: restaurantData.map(r => ({{
                            id: r.id,
                            styleId: "default",
                            position: new TMap.LatLng(r.latitude, r.longitude),
                            properties: {{
                                name: r.name,
                                category: r.category,
                                rating: r.rating,
                                price: r.price,
                                hours: r.hours
                            }}
                        }}))
                    }});
                    
                    // 信息窗口
                    var infoWindow = new TMap.InfoWindow({{
                        map: map,
                        enableCustom: true,
                        offset: {{ x: 0, y: -35 }}
                    }});
                    
                    // 点击事件
                    markerLayer.on("click", function(evt) {{
                        var props = evt.geometry.properties;
                        infoWindow.setContent(
                            '<div class="info-window">' +
                            '<h3>' + props.name + '</h3>' +
                            '<p><b>类型:</b> ' + props.category + '</p>' +
                            '<p><b>评分:</b> ' + props.rating + '</p>' +
                            '<p><b>人均:</b> ' + props.price + '</p>' +
                            '<p><b>营业时间:</b> ' + props.hours + '</p>' +
                            '</div>'
                        );
                        infoWindow.setPosition(evt.geometry.position);
                        infoWindow.open();
                    }});
                    
                }} catch (error) {{
                    console.error('地图初始化错误:', error);
                    document.getElementById('loading').innerHTML = 
                        '<div style="color:red;padding:20px;text-align:center">' +
                        '<h3>地图加载失败</h3>' +
                        '<p>' + error.message + '</p>' +
                        '</div>';
                }}
            }}
            
            // 检查API是否加载
            function checkAPI() {{
                if (typeof TMap !== 'undefined') {{
                    initMap();
                }} else {{
                    setTimeout(checkAPI, 100);
                }}
            }}
            
            // 文档加载后执行
            document.addEventListener('DOMContentLoaded', function() {{
                checkAPI();
            }});
        </script>
    </body>
    </html>
    """

    # 显示地图
    st.title("🍜 南宁餐厅地图（腾讯卫星图）")
    components.html(map_html, height=600)



    

else :
    st.markdown('<p class="main-title">个人简历</p>', unsafe_allow_html=True)


    from datetime import datetime
    from PIL import Image
    import io


    # 初始化session state
    if 'resume_data' not in st.session_state:
        st.session_state.resume_data = {
            'name': '',
            'gender': '',
            'email': '',
            'birth_date': '',
            'work_location': '',
            'position': '',
            'age': '',
            'phone': '',
            'bio': '',
            'avatar': None
        }

    # 创建两列
    col1, col2 = st.columns(2)

    with col1:
        st.header("个人信息表单", divider="rainbow")
        
        # 表单输入
        with st.form("resume_form"):
            # 头像上传
            uploaded_file = st.file_uploader("上传头像（最大200MB，支持JPG,JEPG,PNG格式）", type=['jpg', 'jpeg', 'png'])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                image.thumbnail((200, 200))
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                st.session_state.resume_data['avatar'] = img_byte_arr.getvalue()
            
            st.session_state.resume_data['name'] = st.text_input("姓名*(必填)", st.session_state.resume_data['name'])
            st.session_state.resume_data['gender'] = st.selectbox("性别*(必填)", ["", "男", "女"], 
                                                              index=0 if not st.session_state.resume_data['gender'] else ["男", "女"].index(st.session_state.resume_data['gender']))
            st.session_state.resume_data['email'] = st.text_input("邮箱*(必填)", st.session_state.resume_data['email'])
            
            # 日期输入
            birth_date = st.date_input("出生日期*", 
                                     value=datetime.strptime(st.session_state.resume_data['birth_date'], "%Y-%m-%d").date() 
                                     if st.session_state.resume_data['birth_date'] else None,
                                     min_value=datetime(1900, 1, 1),
                                     max_value=datetime.now())
            st.session_state.resume_data['birth_date'] = birth_date.strftime("%Y-%m-%d") if birth_date else ""
            
            st.session_state.resume_data['work_location'] = st.text_input("家庭住址", st.session_state.resume_data['work_location'])
            st.session_state.resume_data['position'] = st.text_input("当前身份（如学生）*(必填)", st.session_state.resume_data['position'])
            
            # 计算年龄
            if st.session_state.resume_data['birth_date']:
                birth_year = datetime.strptime(st.session_state.resume_data['birth_date'], "%Y-%m-%d").year
                current_year = datetime.now().year
                st.session_state.resume_data['age'] = str(current_year - birth_year)
            else:
                st.session_state.resume_data['age'] = ""
            
            st.session_state.resume_data['phone'] = st.text_input("联系电话", st.session_state.resume_data['phone'], placeholder="010-0000-0001")
            st.session_state.resume_data['bio'] = st.text_area("个人简介", st.session_state.resume_data['bio'], 
                                                            placeholder="请简要介绍自己...", height=150)
            
            submitted = st.form_submit_button("更新简历", use_container_width=True)
            if submitted:
                if not st.session_state.resume_data['name'] or not st.session_state.resume_data['gender'] or not st.session_state.resume_data['email'] or not st.session_state.resume_data['birth_date'] or not st.session_state.resume_data['position']:
                    st.error("请填写所有带*号的必填项")

    with col2:
        st.header("简历预览", divider="rainbow")
        
        # 简历样式
        st.markdown("""
        <style>
        .resume-box {
            border: 1px solid #e0e0e0;
            padding: 25px;
            border-radius: 15px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .resume-header {
            border-bottom: 2px solid #4a6fa5;
            margin-bottom: 20px;
            padding-bottom: 15px;
        }
        .empty-field {
            color: #999999;
            font-style: italic;
        }
        .section-title {
            color: #4a6fa5;
            font-weight: bold;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # 简历内容
        with st.container():
            st.markdown('<div class="resume-box">', unsafe_allow_html=True)
            
            # 头部信息
            col_header1, col_header2 = st.columns([1, 3])
            with col_header1:
                if st.session_state.resume_data['avatar']:
                    st.image(Image.open(io.BytesIO(st.session_state.resume_data['avatar'])), width=100)
                else:
                    st.image(Image.new('RGB', (100, 100), color='lightgray'), width=100)
            
            # 基本信息
            st.markdown('<p class="section-title">基本信息</p>', unsafe_allow_html=True)
            cols = st.columns(2)
            with cols[0]:
                st.text(f"年龄: {st.session_state.resume_data['age'] or '未填写'}")
                st.text(f"性别: {st.session_state.resume_data['gender'] or '未填写'}")
            with cols[1]:
                st.text(f"邮箱: {st.session_state.resume_data['email'] or '未填写'}")
                st.text(f"电话: {st.session_state.resume_data['phone'] or '010-0000-0001'}")
            
            st.divider()
            
            # 个人信息
            st.markdown('<p class="section-title">个人信息</p>', unsafe_allow_html=True)
            cols = st.columns(2)
            with cols[0]:
                st.text(f"出生日期: {st.session_state.resume_data['birth_date'] or '未填写'}")
            with cols[1]:
                st.text(f"工作地点: {st.session_state.resume_data['work_location'] or '未填写'}")
            
            st.divider()
            
            # 个人简介
            st.markdown('<p class="section-title">个人简介</p>', unsafe_allow_html=True)
            st.text(st.session_state.resume_data['bio'] or "请简要介绍自己...")
            
            st.markdown('</div>', unsafe_allow_html=True)
