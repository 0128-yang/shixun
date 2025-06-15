
import streamlit as st # 导入Streamlit并用st代表它
import numpy as np #导入numpy库调用表格内容
import pandas as pd #导入pandas库调用表格内容
st.set_page_config(layout="wide")

st.markdown('<p class="main-title">个人简历编辑器</p>', unsafe_allow_html=True)
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
        'age': '2',
        'phone': '',
        'bio': '',
        'avatar': None
    }

# 创建两列
col1, col2 = st.columns([1,2])

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

