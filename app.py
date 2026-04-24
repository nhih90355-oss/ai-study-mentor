import streamlit as st
import random

# ===== CONFIG =====
st.set_page_config(page_title="AI Study Mentor", page_icon="🧠", layout="wide")

# ===== STYLE (RESPONSIVE + DỄ NHÌN) =====
st.markdown("""
<style>

/* FIX CHỮ */
h1, h2, h3, label {
    color: #ffffff !important;
}

p {
    color: #cbd5e1 !important;
}

/* HOVER CARD */
.card {
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}
</style>

/* FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: #f8fafc !important;
}

/* BACKGROUND */
.stApp {
    background: radial-gradient(circle at 20% 20%, #4f46e5, transparent 40%),
                radial-gradient(circle at 80% 80%, #9333ea, transparent 40%),
                linear-gradient(135deg, #020617, #0f172a);
}

/* TITLE */
.title {
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(90deg, #f472b6, #fb923c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* LABEL */
label {
    color: #ffffff !important;
    font-weight: 600;
}

/* INPUT */
input, textarea {
    background-color: rgba(255,255,255,0.25) !important;
    color: #ffffff !important;
}

/* SELECT */
.stSelectbox div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.25) !important;
    color: #ffffff !important;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #f97316, #ec4899);
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: bold;
}

/* MOBILE FIX */
@media (max-width: 768px) {
    .title {
        font-size: 28px;
    }
}

</style>
""", unsafe_allow_html=True)

# ===== TITLE =====
st.sidebar.title("📌 Menu")

menu = st.sidebar.radio("Chọn chức năng", [
    "🏠 Trang chính",
    "📊 Phân tích",
    "📈 Tiến trình"
])
st.markdown("### 🏫 Trường PTDTNT THPT Đam San")
st.markdown("""
<div style="text-align:center; padding: 30px 0;">
    <h1 style="font-size:50px; background: linear-gradient(90deg,#f472b6,#fb923c);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
        🌿 AI Study Mentor
    </h1>
    <p style="color:#cbd5e1; font-size:18px;">
        Trợ lý học tập thông minh giúp bạn đạt mục tiêu nhanh hơn 🚀
    </p>
</div>
""", unsafe_allow_html=True)

# ===== RESPONSIVE LAYOUT =====
if menu == "🏠 Trang chính":
    col1, col2 = st.columns([1,1], gap="large")
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    ten = st.text_input("👤 Tên")
    diem = st.slider("📊 Điểm hiện tại", 0.0, 10.0, 5.0)
    mucTieu = st.slider("🎯 Mục tiêu", 0.0, 10.0, 8.0)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    mon = st.selectbox("📚 Môn yếu", ["Toán", "Văn", "Anh"])
    tamLy = st.selectbox("🧠 Tâm trạng", ["😞 Stress", "😐 Bình thường", "😄 Tích cực"])
    gioHoc = st.selectbox("⏰ Thời gian học", ["1h", "2h", "3h+"])

    st.markdown('</div>', unsafe_allow_html=True)

# ===== AI =====
def ai_mentor(d, name, target, time, mood, subject):
    result = f"🎯 {name}, AI phân tích:\n\n"
    gap = target - d

    if gap > 0:
        result += f"📉 Bạn còn thiếu {gap:.1f} điểm\n"

        if subject == "Toán":
            result += "📘 Luyện đề + học lại công thức\n"
        elif subject == "Văn":
            result += "📝 Viết mỗi ngày + học dẫn chứng\n"
        else:
            result += "🌍 Học từ vựng + nghe\n"

        if mood == "😞 Stress":
            result += "💡 Nghỉ ngắn rồi học tiếp\n"

    else:
        result += "🏆 Bạn đã đạt mục tiêu!"

    return result

# ===== BUTTON =====
if menu == "📊 Phân tích":
    if st.button("🚀 Phân tích"):
    if ten == "":
        st.warning("Nhập tên!")
    else:
        kq = ai_mentor(diem, ten, mucTieu, gioHoc, tamLy, mon)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📊 Kết quả")
        st.write(kq)
        st.markdown('</div>', unsafe_allow_html=True)

# ===== DASHBOARD =====
st.markdown('<div class="card">', unsafe_allow_html=True)
progress = diem / mucTieu if mucTieu > 0 else 0
st.progress(min(progress, 1.0))
st.write(f"Bạn đạt {progress*100:.1f}% mục tiêu")
st.markdown('</div>', unsafe_allow_html=True)

# ===== CHALLENGE =====
challenge = ["Giải 5 bài Toán", "Học 20 từ vựng", "Ôn 1 chương"]
st.info("🎯 " + random.choice(challenge))

st.markdown("## 🤖 Chat với AI (Link ChatGPT)")

# Tạo hộp chat dẫn đến ChatGPT
if st.button("Mở ChatGPT trên web"):
    st.markdown("[Nhấn vào đây để chat với AI](https://chat.openai.com/)  🔗", unsafe_allow_html=True)
