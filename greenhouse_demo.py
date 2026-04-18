import streamlit as st
import pandas as pd
import time

# --- 页面配置 ---
st.set_page_config(page_title="绿动穹顶 - 智慧温室数字孪生系统", layout="wide", page_icon="🌿")

# --- 页面标题 ---
st.title("🌿 “绿动穹顶”智慧温室 - 核心决策演示平台")
st.markdown("合肥工业大学 | 基于数字孪生与气象预判的主动式节能方案演示")
st.markdown("---")

# --- 侧边栏：模拟环境输入 ---
st.sidebar.header("🎛️ 感知层数据模拟面板")
st.sidebar.markdown("拖动滑块模拟传感器实时数据与气象预报：")

T_in = st.sidebar.slider("🌡️ 室内实时温度 (℃)", 15.0, 45.0, 33.0, step=0.5)
T_out = st.sidebar.slider("☁️ 未来1h室外预测温度 (℃)", 10.0, 40.0, 22.0, step=0.5)
S_current = st.sidebar.slider("💧 土壤当前湿度 (%)", 20.0, 80.0, 40.0, step=1.0)
EC_current = st.sidebar.slider("🧪 土壤当前EC值 (mS/cm)", 0.5, 3.0, 1.2, step=0.1)

st.sidebar.markdown("---")
st.sidebar.header("⚙️ 算法内部阈值设定")
T_set = st.sidebar.number_input("目标室温 (℃)", value=26.0)
delta = st.sidebar.number_input("自然换热温差阈值 (δ)", value=5.0)
S_threshold = st.sidebar.number_input("目标土壤湿度 (%)", value=55.0)
EC_target = st.sidebar.number_input("目标EC值 (mS/cm)", value=2.0)

# --- 核心算法处理 ---

# 1. 气象对冲降温决策
cooling_strategy = "正常待机"
ac_status = "关闭"
window_status = "关闭"
shade_status = "0% (收起)"
energy_mode = "🟢 节能"

if T_in > T_set:
    # 判断是否具备自然降温条件：室外温度 < 室内温度 - 换热阈值
    if T_out < (T_in - delta):
        cooling_strategy = "♻️ 主动节能模式：气象对冲被动降温"
        ac_status = "🚫 强制封锁 (关闭)"
        window_status = "✅ 100% 开启 (自然对流)"
        shade_status = "✅ 50% 展开 (遮蔽辐射)"
        energy_mode = "🟢 极低能耗"
    else:
        cooling_strategy = "⚡ 传统调控模式：主动设备制冷"
        ac_status = "✅ 开启 (高功率运行)"
        window_status = "关闭"
        shade_status = "关闭"
        energy_mode = "🔴 高能耗"

# 2. 水肥一体化决策
delta_S = max(0, S_threshold - S_current)
delta_EC = max(0, EC_target - EC_current)
alpha, beta = 2.0, 5.0 # 调节系数
Q_irrigation = round((alpha * delta_S) + (beta * delta_EC), 2)

pump_status = "关闭"
if Q_irrigation > 0:
    pump_status = f"✅ 开启 (精准加注: {Q_irrigation} L)"

# --- 主界面展示区 ---

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 实时环境状态")
    m1, m2, m3 = st.columns(3)
    m1.metric(label="室内温度", value=f"{T_in} ℃", delta=f"{round(T_in - T_set, 1)} ℃ (距目标)")
    m2.metric(label="室外预测", value=f"{T_out} ℃")
    m3.metric(label="内外温差", value=f"{round(T_in - T_out, 1)} ℃")
    
    st.markdown("##### 💡 气象对冲决策引擎")
    st.info(f"**当前策略：** {cooling_strategy}")
    
    # 虚拟设备状态面板
    st.markdown("**执行器实时状态：**")
    st.code(f"""
    [ 主控系统指令下发 ]
    ▶ 空调系统 : {ac_status}
    ▶ 顶侧天窗 : {window_status}
    ▶ 遮阳网幕 : {shade_status}
    ▶ 系统能效 : {energy_mode}
    """, language="markdown")

with col2:
    st.subheader("🌱 水肥一体化按需供给")
    m4, m5 = st.columns(2)
    m4.metric(label="土壤湿度缺口", value=f"{delta_S} %", delta="-需补水", delta_color="inverse")
    m5.metric(label="土壤EC值缺口", value=f"{round(delta_EC, 2)} mS/cm", delta="-需补肥", delta_color="inverse")
    
    st.markdown("##### 💧 资源精准调度方案")
    if Q_irrigation > 0:
        st.success(f"**模型推演结果：** 计算出综合水肥投放量为 **{Q_irrigation} L**")
    else:
        st.success("**模型推演结果：** 当前土壤水肥充沛，无需灌溉，**避免盲目作业导致的资源浪费**。")
        
    st.markdown("**水泵与施肥机状态：**")
    st.code(f"""
    [ 水肥一体机指令 ]
    ▶ 灌溉水泵 : {pump_status}
    """, language="markdown")

# --- 底部数据趋势模拟图 (增强科技感) ---
st.markdown("---")
st.subheader("📈 系统能耗对比推演 (传统模式 vs 气象对冲)")

# 生成模拟图表数据
chart_data = pd.DataFrame({
    '传统模式能耗 (kW·h)': [5.0, 5.2, 5.5, 5.1, 5.0, 5.3, 5.4],
    '绿动穹顶能耗 (kW·h)': [5.0, 3.8, 1.2, 1.0, 1.1, 2.5, 3.9]  # 模拟中间时段触发了被动降温
}, index=['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'])

st.line_chart(chart_data)

st.caption("注：图表展示在正午高温时段，若满足气象对冲条件，本系统强制封锁空调并调用天窗/遮阳网，能耗出现显著断崖式下降。")