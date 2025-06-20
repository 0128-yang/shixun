# 第八章/explore_data.py
import pandas as pd

# 设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)
# 读取数据集，并指定字符编码为gbk，防止中文报错
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')

# 输出数据框的前5行
print(penguin_df.head())



# 第八章/data_preprocess.py
import pandas as pd


# 设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)
# 读取数据集，并指定字符编码为gbk，防止中文报错
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')
# 删除缺失值所在的行
penguin_df.dropna(inplace=True)
# 定义企鹅的种类为目标输出变量
output = penguin_df['企鹅的种类']
# 将去除年份列不作为特征列
# 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
# 对特征列进行独热编码
features = pd.get_dummies(features)
# 将目标输出变量，进行转换为离散数值表示
output_codes, output_uniques = pd.factorize(output)


print('下面是去重后，目标输出变量的数据：')
print(output_uniques)
print('下面是独热编码后，特征列的数据：')
print(features.head())




# 第八章/generate_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 读取数据集，并指定字符编码为gbk，防止中文报错
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')
# 删除缺失值所在的行
penguin_df.dropna(inplace=True)
# 定义企鹅的种类为目标输出变量
output = penguin_df['企鹅的种类']
# 将去除年份列不作为特征列
# 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
# 对特征列进行独热编码
features = pd.get_dummies(features)
# 将目标输出变量，进行转换为离散数值表示
output_codes, output_uniques = pd.factorize(output)

# 从features和output_codes 这两个数组中划分数据集为训练集和测试集。
# 训练集为80%，测试集为20%（1-80%）
# 返回的x_train和 y_train为划分得到的训练集特征和标签。
# x_test和y_test为划分得到的测试集特征和标签。
# 这里标签和目标输出变量是一个意思

x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

# 构建一个随机森林分类器
rfc = RandomForestClassifier()

# 使用训练集数据x_train和y_train来拟合(训练)模型。
rfc.fit(x_train, y_train)

# 用训练好的模型rfc对测试集数据x_test进行预测，预测结果存储在y_pred中
y_pred = rfc.predict(x_test)

# 计算测试集上模型的预测准确率。
# 方法是使用accuracy_score方法，比对真实标签y_test和预测标签y_pred
# 返回预测正确的样本占全部样本的比例，即准确率。
score = accuracy_score(y_test, y_pred)
print(f'该模型的准确率是：{score}')



# 第八章/save_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle  # 用来保存模型和output_uniques变量


# 读取数据集，并指定字符编码为gbk，防止中文报错
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')
# 删除缺失值所在的行
penguin_df.dropna(inplace=True)
# 定义企鹅的种类为目标输出变量
output = penguin_df['企鹅的种类']
# 将去除年份列不作为特征列
# 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
# 对特征列进行独热编码
features = pd.get_dummies(features)
# 将目标输出变量，进行转换为离散数值表示
output_codes, output_uniques = pd.factorize(output)

# 从features和output_codes 这两个数组中划分数据集为训练集和测试集。
# 训练集为80%，测试集为20%（1-80%）
# 返回的x_train和 y_train为划分得到的训练集特征和标签。
# x_test和y_test为划分得到的测试集特征和标签。
# 这里标签和目标输出变量是一个意思

x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

# 构建一个随机森林分类器
rfc = RandomForestClassifier()

# 使用训练集数据x_train和y_train来拟合(训练)模型。
rfc.fit(x_train, y_train)

# 用训练好的模型rfc对测试集数据x_test进行预测，预测结果存储在y_pred中
y_pred = rfc.predict(x_test)

# 计算测试集上模型的预测准确率。
# 方法是使用accuracy_score方法，比对真实标签y_test和预测标签y_pred
# 返回预测正确的样本占全部样本的比例，即准确率。
score = accuracy_score(y_pred, y_test)

# 使用with语句，简化文件操作
# open()函数和'wb'参数用于创建并写入字节流
# pickle.dump()方法将模型对象转成字节流
with open('rfc_model.pkl', 'wb') as f:
    pickle.dump(rfc, f)

# 同上
# 将映射变量写入文件中
with open('output_uniques.pkl', 'wb') as f:
    pickle.dump(output_uniques, f)

print('保存成功，已生成相关文件。')



import streamlit as st
import pickle
import pandas as pd


# 加载模型（只需加载一次）
@st.cache_resource  # 使用缓存避免重复加载
def load_model():
    with open('rfc_model.pkl', 'rb') as f:
        rfc_model = pickle.load(f)
    with open('output_uniques.pkl', 'rb') as f:
        output_uniques_map = pickle.load(f)
    return rfc_model, output_uniques_map

rfc_model, output_uniques_map = load_model()

# 侧边栏导航
with st.sidebar:
    st.image('images/rigth_logo.png', width=100)
    st.title('请选择页面')
    page = st.selectbox("请选择页面", ["简介页面", "预测分类页面"], label_visibility='collapsed')

if page == "简介页面":
    st.title("企鹅分类器 :penguin:")
    st.header('数据集介绍')
    st.markdown("""帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集...""")
    st.header('三种企鹅的卡通图像')
    st.image('images/penguins.png')

elif page == "预测分类页面":
    st.header("预测企鹅分类")
    st.markdown("输入6个信息，预测企鹅物种：")

    col_form, _, col_logo = st.columns([3, 1, 2])
    
    with col_form:
        with st.form('user_inputs'):
            island = st.selectbox(
                '企鹅栖息的岛屿', 
                options=['托尔森岛', '比斯科群岛', '德里姆岛'],
                key="island_selectbox"
            )
            sex = st.selectbox('性别', options=['雄性', '雌性'], key="sex_selectbox")
            bill_length = st.number_input('喙的长度（毫米）', min_value=0.0, key="bill_length")
            bill_depth = st.number_input('喙的深度（毫米）', min_value=0.0, key="bill_depth")
            flipper_length = st.number_input('翅膀的长度（毫米）', min_value=0.0, key="flipper_length")
            body_mass = st.number_input('身体质量（克）', min_value=0.0, key="body_mass")
            submitted = st.form_submit_button('预测分类')

    # 数据预处理
    island_map = {
        '比斯科群岛': (0, 0, 1),
        '德里姆岛': (0, 1, 0),
        '托尔森岛': (1, 0, 0)
    }
    island_dream, island_torgerson, island_biscoe = island_map.get(island, (0, 0, 0))
    sex_male = 1 if sex == '雄性' else 0
    sex_female = 1 if sex == '雌性' else 0

    format_data = [
        bill_length, bill_depth, flipper_length, body_mass,
        island_dream, island_torgerson, island_biscoe, sex_female, sex_male
    ]

    # 预测逻辑
    if submitted:
        format_data_df = pd.DataFrame(data=[format_data], columns=rfc_model.feature_names_in_)
        predict_result_code = rfc_model.predict(format_data_df)
        predict_result_species = output_uniques_map[predict_result_code][0]
        
        st.success(f'预测结果：**{predict_result_species}**')
        with col_logo:
            st.image(f'images/{predict_result_species}.png', width=300)
