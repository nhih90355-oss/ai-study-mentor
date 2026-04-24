import streamlit as st
import random

st.set_page_config(page_title='AI Study Mentor', page_icon='🧠', layout='wide')

st.markdown('''
<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");
html, body, [class*='css'] {font-family:'Poppins',sans-serif; color:#1f2937;}
.stApp {
 background: radial-gradient(circle at top left,#fde2e4 0%,transparent 35%),
             radial-gradient(circle at bottom right,#dbeafe 0%,transparent 35%),
             linear-gradient(135deg,#fffafc,#f8fafc,#eef2ff);
}
h1,h2,h3,p,label,div,span {color:#1f2937 !important;}
.card{background:rgba(255,255,255,.78); border:1px solid rgba(255,255,255,.7); padding:20px; border-radius:18px; box-shadow:0 10px 25px rgba(0,0,0,.06); margin-bottom:18px;}
.stButton>button{background:#6366f1; color:white; border:none; border-radius:12px; font-weight:700; padding:.6rem 1rem;}
.stButton>button:hover{background:#4f46e5;}
input, textarea {color:#111827 !important; background:#ffffff !important;}
.stSelectbox div[data-baseweb='select'], .stSlider {color:#111827 !important;}
.block-container{padding-top:2rem;}
.title{font-size:52px; font-weight:800; text-align:center; margin-bottom:.2rem;}
.subtitle{text-align:center; color:#475569 !important; margin-bottom:1.5rem;}
</style>
''', unsafe_allow_html=True)

st.sidebar.title('📌 Menu')
menu = st.sidebar.radio('Chọn chức năng',['🏠 Trang chính','📊 Phân tích','📈 Tiến trình'])
st.markdown("""
<div style="
padding:70px 20px;
text-align:center;
border-radius:25px;
background: linear-gradient(135deg,#6366f1,#a855f7,#ec4899);
color:white;
margin-bottom:40px;
box-shadow:0 20px 50px rgba(0,0,0,0.15);
">

<h1 style="font-size:60px; margin-bottom:10px;">
🌿 AI Study Mentor
</h1>

<p style="font-size:22px; opacity:0.9;">
Biến việc học thành hệ thống có chiến lược 🚀
</p>

</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style="padding:60px 20px; text-align:center; border-radius:20px;
background: linear-gradient(135deg,#6366f1,#a855f7);
color:white; margin-bottom:30px; box-shadow:0 10px 30px rgba(0,0,0,0.1);">

    <h1 style="font-size:52px; margin-bottom:10px;">🌿 AI Study Mentor</h1>

    <p style="font-size:20px; opacity:0.9;">
        Trợ lý học tập thông minh giúp bạn tăng điểm nhanh chóng 🚀
    </p>

</div>
""", unsafe_allow_html=True)
# luôn khai báo biến trước để tránh lỗi nhảy giao diện
st.markdown("## 🧾 Thông tin học tập")
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    ten = st.text_input('👤 Tên')
    diem = st.slider('📊 Điểm hiện tại',0.0,10.0,5.0)
    mucTieu = st.slider('🎯 Mục tiêu',0.0,10.0,8.0)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    mon = st.selectbox('📚 Môn yếu',['Toán','Văn','Anh'])
    tamLy = st.selectbox('🧠 Tâm trạng',['😞 Stress','😐 Bình thường','😄 Tích cực'])
    gioHoc = st.selectbox('⏰ Thời gian học',['1h','2h','3h+'])
    st.markdown('</div>', unsafe_allow_html=True)

def ai_mentor(d,name,target,time,mood,subject):
    gap = target-d
    rs = f'🎯 {name}, AI phân tích:\n\n'
    if gap>0:
        rs += f'📉 Bạn còn thiếu {gap:.1f} điểm\n'
        tips = {'Toán':'📘 Luyện đề + ôn công thức','Văn':'📝 Viết đoạn văn mỗi ngày','Anh':'🌍 Học từ vựng + nghe'}
        rs += tips[subject] + '\n'
        if mood=='😞 Stress': rs += '💡 Nghỉ 10 phút rồi học tiếp\n'
    else:
        rs += '🏆 Bạn đã đạt mục tiêu!'
    return rs

if menu=='📊 Phân tích':
    if st.button('🚀 Phân tích'):
        if ten.strip():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.write(ai_mentor(diem,ten,mucTieu,gioHoc,tamLy,mon))
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning('Nhập tên!')

if menu=='📈 Tiến trình':
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    progress = diem/mucTieu if mucTieu else 0
    st.progress(min(progress,1.0))
    st.write(f'Bạn đạt {progress*100:.1f}% mục tiêu')
    st.markdown('</div>', unsafe_allow_html=True)

if menu=='🏠 Trang chính':
    st.info('🎯 ' + random.choice(['Giải 5 bài Toán','Học 20 từ vựng','Ôn 1 chương']))

st.markdown("## 🤖 Chat với AI (Link ChatGPT)")

# Tạo hộp chat dẫn đến ChatGPT
if st.button("Mở ChatGPT trên web"):
    st.markdown("[Nhấn vào đây để chat với AI](https://chat.openai.com/)  🔗", unsafe_allow_html=True)
