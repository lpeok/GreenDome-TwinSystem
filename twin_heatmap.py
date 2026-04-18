import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata

# 1. 页面基本配置
st.set_page_config(page_title="绿动穹顶数字孪生台", layout="wide")

# --- 核心算法：数字孪生温场渲染函数 ---
def render_digital_twin_heatmap(sensor_values):
    """
    根据5个传感器点位计算全域温场
    sensor_values: [左上, 右上, 左下, 右下, 中心]
    """
    # 定义温室物理空间坐标 (单位: 米)
    # 假设温室为 10m x 20m
    points = np.array([
        [0, 20],   # S1: 左上
        [10, 20],  # S2: 右上
        [0, 0],    # S3: 左下
        [10, 0],   # S4: 右下
        [5, 10]    # S5: 中心
    ])
    
    # 构建高分辨率计算网格 (Meshgrid)
    grid_x, grid_y = np.mgrid[0:10:50j, 0:20:100j]
    
    # 执行空间插值算法 (Cubic)
    grid_z = griddata(points, sensor_values, (grid_x, grid_y), method='cubic')
    # 填充边缘空值
    grid_z = np.nan_to_num(grid_z, nan=np.mean(sensor_values))

    # 使用 Plotly 构建 3D 表面图
    fig = go.Figure(data=[
        go.Surface(
            x=grid_x, y=grid_y, z=grid_z,
            colorscale='Jet',
            colorbar=dict(title="温度 ℃"),
            contours={"z": {"show": True, "color": "white"}}
        )
    ])

    # 叠加传感器物理位置标记
    fig.add_trace(go.Scatter3d(
        x=points[:, 0], y=points[:, 1], z=sensor_values,
        mode='markers+text',
        marker=dict(size=6, color='black', symbol='diamond'),
        text=['S1', 'S2', 'S3', 'S4', 'Center'],
        name='物理节点'
    ))

    # 布局优化
    fig.update_layout(
        scene=dict(
            xaxis_title='宽度 (m)',
            yaxis_title='长度 (m)',
            zaxis_title='温度 (℃)',
            aspectratio=dict(x=1, y=2, z=0.5)
        ),
        margin=dict(l=0, r=0, b=0, t=30),
        height=700
    )
    return fig

# --- 主程序界面 ---
st.title(" 绿动穹顶 | 数字孪生全域监控大脑")

# 侧边栏模拟传感器数据输入
st.sidebar.header(" 传感器实时数据模拟")
s1 = st.sidebar.slider("S1-左上 (℃)", 15.0, 45.0, 22.0)
s2 = st.sidebar.slider("S2-右上 (℃)", 15.0, 45.0, 28.0)
s3 = st.sidebar.slider("S3-左下 (℃)", 15.0, 45.0, 24.0)
s4 = st.sidebar.slider("S4-右下 (℃)", 15.0, 45.0, 26.0)
s5 = st.sidebar.slider("S5-中心 (℃)", 15.0, 45.0, 32.0)

# 渲染热力云图
fig = render_digital_twin_heatmap([s1, s2, s3, s4, s5])
st.plotly_chart(fig, use_container_width=True)

st.info(" 提示：拖动左侧滑块模拟环境变化，3D数字孪生模型将实时重新计算并映射温场差异。")