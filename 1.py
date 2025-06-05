Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import streamlit as st   # 导入Streamlit并用st代表它


# 标题格式
st.markdown('# 学生档案')


st.markdown('## 基本信息')

st.markdown('##### 姓名： text1  |   班级：23级高本智能一班')
st.markdown('##### 姓名： text1  |   班级：23级高本智能一班')


#内容
st.header("text1:smiley:",anchor='text1')
st.text('word1')


st.header("text1:smiley:",anchor='text1')
st.text('word1')


st.header("text1:smiley:",anchor='text1')
st.text('word1')




st.subheader('')
st.metric(label="当前学期", value="大二 下学期")

st.subheader('学习情况')

c1, c2, c3 = st.columns(3)
c1.metric(label="当前周数", value="15/20", delta="-剩余5周")
c2.metric(label="text1", value="text1", delta="text1")
c3.metric(label="text1", value=None, delta="0", delta_color="off")

st.subheader('text1')
st.metric(label="text1", value="text1", delta="text1", label_visibility='hidden')




import pandas as pd   


data = {
    '1':[1],
    '2':[123],
    '3':[1232],
}
... index = pd.Series(['01月', '02月', '03月', '04月', '05月'], name='月份')
... # 根据上面创建的data和index，创建数据框
... df = pd.DataFrame(data, index=index)
... 
... st.subheader('表')
... st.table(df)
... 
... 
... 
... 
... st.subheader('Python代码展示')
... python_code = '''def hello():
...     print("你好，Streamlit！")
... '''
... 
... st.code(python_code, line_numbers=True)
... 
... st.subheader('Java代码展示')
... java_code = '''public class Hello {
...     public static void main(String[] args) {
...         System.out.println("你好！ Streamlit!");
...     }
... }
... '''
... 
... st.code(java_code, language='java',line_numbers=True)
... 
... st.subheader('JavaScript代码展示')
... javascript_code = '''<p id="demo"></p>
... <script>
...     document.getElementById("demo").innerHTML ="你好！ Streamlit!";
... </script>
... '''
... 
... st.code(javascript_code, language='javascript',line_numbers=True)
... 
... 
... 
... 
