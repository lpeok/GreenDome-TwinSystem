import   进口 streamlit as   作为 st
import   进口 numpy as   作为 np   导入numpy为np
import plotly.graph_objects as go导入 plotly.graph_objects 模块作为 go 。
from scipy.interpolate import griddatafrom scipy.interpolate   插入 导入 griddata

# 1. 页面基本配置
st.set_page_config(page_title="绿动穹顶数字孪生台", layout="wide")st.set_page_config(page_title="Green Dome Digital Twin Platform"“绿穹顶数字孪生平台”, layout="wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide"   "wide")

# --- 核心算法：数字孪生温场渲染函数 ---
def render_digital_twin_heatmap(sensor_values):def 绘制数字孪生热图（
    """   """
    根据5个传感器点位计算全域温场   """   """
    sensor_values:    """[sensor_values: [upper left, upper right, lower left, lower right, center]左上, 右上, 左下, 右下, 中心]" " " [sensor_values: [upper left, upper right, lower left, lower right, center] upper left, upper right, lower left, lower right, center]
    """   """   """
    grid_z = griddata(传感器值， (网格_x， 网格_y)， 方法='三次插# 定义温室物理空间坐标 (单位: 米)
    # 假设温室为 10m x 20m
    points = np.array([   Points = np.array([
        [0, 20],   # S1: 左上
        [10, 20],  # S2: 右上
        [0, 0],    # S3: 左下
        [10, 0],   # S4: 右下
        [5, 10]    # S5: 中心
    ])
    
    # 构建高分辨率计算网格 (Meshgrid)
    grid_x, grid_y = np.mgrid[0:10:50j, 0:20:100j]grid_x, grid_y = np.mgrid[0:10:50j, 0:20:100j]grid_x, grid_y = np.mgrid[0:10:50j, 0:20:100j] 等同于 grid_x, grid_y = np.mgrid[0:10:50j, 0:20：100j]

grid_x, grid_y = np.mgrid[0:10:50j, 0:20:100j]  # grid_x 和 grid_y 分grid_x, grid_y = np.mgrid[0:10:50j, 0:20:100j]  # grid_x 和 grid_y 分别是 50 行 100 列的网格坐标
    
    # 执行空间插值算法 (Cubic)
    grid_z = griddata(points, sensor_values, (grid_x, grid_y), method='cubic')   colorscale =’Jet’,   colorscale =’Jet’,
    # 填充边缘空值
    grid_z = np.nan_to_num(grid_z, nan=np.mean(sensor_values))grid_z = np.nan_to_num(grid_z, nan=np.mean(sensor_values))  # 将 grid_z 中的 NaN 值替换为 sensor_values 的均值grid_z = np.nan_to_num(grid_z, nan=np.mean(sensor_values))  # Replace NaN values in grid_z with the mean of sensor_values

    # 使用 Plotly 构建 3D 表面图
    fig = go.Figure(data=[
        go.Surface(
            x=grid_x, y=grid_y, z=grid_z,x = 网格 x 坐标，y = 网格 y 坐标，z = 网格 z 坐标
            colorscale='Jet',   colorscale =’Jet’,
            colorbar=dict(title="温度 ℃"),colorbar=dict(title="Temperature ℃"),
            contours={"z": {"show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show"   "show": True   真正的, "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color"   "color": "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"   "white"}}   模式 = '标记 文 ，
        )   模式 = '标记 文 ，
    ])

    # 叠加传感器物理位置标记
    fig.add_trace(go.Scatter3d(fig.add_trace(go.Scatter3d(  # fig 添加一个三维散点图的轨迹
        x=points[:, 0], y=points[:, 1], z=sensor_values,x = 点的横坐标，y = 点的纵坐标，z = 传感器值
        mode='markers+text',   模式 = '标记 文 ，
        marker=dict(size=6, color='black', symbol='diamond')['S1', 'S2', 'S3', 'S4', '中心']   模式 = '标记 文 ，,标记 = dict(大小 = 6， 颜色 =
        text=['S1', 'S2', 'S3', 'S4', 'Center'],['S1', 'S2', 'S3', 'S4', '中心']
        name='物理节点'
    )   xaxis_title='Width (m)',)['S1', 'S2', 'S3', 'S4', '中心']['S1', 'S2', 'S3', 'S4', '中心']

    # 布局优化   xaxis_title='Width (m)',
    fig.update_layout(
        scene=dict(   现场= dict (
            xaxis_title='宽度 (m)',   xaxis_title='Width (m)',
            yaxis_title='长度 (m)',   yaxis_title='Length (m)',
            zaxis_title='温度 (℃)',纵横x"： 1, "y": 2, "z"： 0.5}
            aspectratio=dict(x=1, y=2, z=0.5)纵横x"： 1, "y": 2, "z"： 0.5}
        ),
        margin=dict(l=0, r=0, b=0, t=30),边距 = dict(左 = 0， 右 = 0， 底 = 0， 顶 = 30)
        height=700   身高= 700
    )
    return fig   返回图

# --- 主程序界面 ---
st.title("绿动穹顶 | 数字孪生全域监控大脑")

# 侧边栏模拟传感器数据输入
st.sidebar.header("传感器实时数据模拟")st.sidebar.header("📡 Real-time Sensor Data Simulation")
s1 = st.sidebar.slider("S1-左上 (℃)", 15.0, 45.0, 22.0)
s2 = st.sidebar.slider("S2-右上 (℃)", 15.0, 45.0, 28.0)s2 = st.sidebar.slider("S2-右上 (℃)", 15.0, 45.0, 28.0)
s3 = st.sidebar.slider("S3-左下 (℃)", 15.0, 45.0, 24.0)s3 = st.sidebar.slider("S3-左下（℃）"， 15.0, 45.0， 24.0)
s4 = st.sidebar.slider("S4-右下 (℃)", 15.0, 45.0, 26.0)s4 = st.sidebar.slider("S4-右下 (℃)", 15.0, 45.0, 26.0)
s5 = st.sidebar.slider("S5-中心 (℃)", 15.0, 45.0, 32.0)s5 = st.sidebar.slider("S5 - 中心（℃）", 15.0， 45.0, 32.0)

# 渲染热力云图
fig = render_digital_twin_heatmap([s1, s2, s3, s4, s5])fig = render_digital_twin_heatmap([s1, s2, s3, s4, s5])  # fig 等于 render_digital_twin_heatmap 函数对 [s1, s2, s3, s4, s5]
st.plotly_chart(fig, use_container_width=True)st.plotly_chart(fig, use_container_width=True)

这段代码使用 Streamlit 库中的 plotly_chart 函数来展示一个图表（figThis piece of code uses the `plotly_chart` function from the Streamlit library to display a chart (fig).

st.info("拖动左侧滑块模拟环境变化，3D数字孪生模型将实时计算并映射温场差异。")
