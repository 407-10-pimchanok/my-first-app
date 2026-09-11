import base64
import time
import requests
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา (Brainrot Edition)")

# 1. ลิงก์รูปภาพตัวละคร (ดึงและแปลงเป็น Base64 ป้องกันจอดำ)
IMAGE_URLS = [
    "https://spacebar.th/storage/tung-tung-tung-tung-sahur-meme-SPACEBAR-Hero.jpg",
    "https://preview.redd.it/can-someone-tell-me-what-does-even-this-meme-mean-p-s-its-v0-jt4yf9hiznte1.jpeg?auto=webp&s=5544ec2f38d636dbb0ffb6f2fbd65cfb2bd8fb76",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_xVOnSByH2i1XjJp78iInU5S4S_LSoo4Rtg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhInHqWSoG5i5t3Mst0S5a0O9zH22J2l0q_g&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6s5wE4k8Wv5z-O9M1xXvR2A-x8XkL4u4Zfg&s",
]


@st.cache_data
def get_base64_image(url):
    """ฟังก์ชันดึงรูปภาพและแปลงเป็น Base64 เพื่อป้องกันการเกิดจอดำ"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            encoded = base64.b64encode(response.content).decode()
            return f"data:image/jpeg;base64,{encoded}"
    except Exception:
        pass
    return url


def render_image(url, width=250):
    """ฟังก์ชันแสดงผลรูปภาพผ่าน HTML"""
    img_data = get_base64_image(url)
    st.markdown(
        f'<img src="{img_data}" width="{width}" style="border-radius: 8px; margin-bottom: 10px;">',
        unsafe_allow_html=True,
    )


# 2. กำหนดค่าเริ่มต้นใน session_state
for i in range(1, 6):
    key = f"ans{i}_val"
    if key not in st.session_state:
        st.session_state[key] = ""


def reset_game():
    for i in range(1, 6):
        st.session_state[f"ans{i}_val"] = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0
    answers = [
        (ans1, "tung tung sahur", "ข้อ 1"),
        (ans2, "bombardiro crocodillo", "ข้อ 2"),
        (ans3, "brr brr patapim", "ข้อ 3"),
        (ans4, "tralalero tralala", "ข้อ 4"),
        (ans5, "capuchino assassino", "ข้อ 5"),
    ]

    for user_ans, correct_ans, label in answers:
        u_clean = user_ans.strip().lower()
        if u_clean == correct_ans:
            st.success(f"✅ {label}: ถูกต้อง ({correct_ans})")
            score += 1
        else:
            st.error(f"❌ {label}: ยังไม่ถูกต้อง (คุณตอบ '{u_clean}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} / 5 คะแนน")


# ปุ่มเริ่มเกม
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# ตัวนับเวลา
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(45 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# ----------------------------------------------------
# 3. แสดงรูปภาพและช่องรับคำตอบ
# ----------------------------------------------------

# ข้อ 1
render_image(IMAGE_URLS[0], width=250)
ans1 = st.text_input(
    "ข้อ 1: T _ n g  t _ n g  s _ h u r 🔔", value=st.session_state.ans1_val
)
st.divider()

# ข้อ 2
render_image(IMAGE_URLS[1], width=250)
ans2 = st.text_input(
    "ข้อ 2: B _ m b a r d _ r o  c r _ c o d _ l l o 🐊",
    value=st.session_state.ans2_val,
)
st.divider()

# ข้อ 3
render_image(IMAGE_URLS[2], width=250)
ans3 = st.text_input(
    "ข้อ 3: B _ r  b _ r  p a t _ p _ m 🐧", value=st.session_state.ans3_val
)
st.divider()

# ข้อ 4
render_image(IMAGE_URLS[3], width=250)
ans4 = st.text_input(
    "ข้อ 4: T r _ l a l _ r o  t r _ l a l a 🎶",
    value=st.session_state.ans4_val,
)
st.divider()

# ข้อ 5
render_image(IMAGE_URLS[4], width=250)
ans5 = st.text_input(
    "ข้อ 5: C _ p u c h _ n o  a s s _ s s i n o ☕",
    value=st.session_state.ans5_val,
)

# บันทึกค่า
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5

# ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()
    time.sleep(1)
    st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)

st.divider()
st.write("นางสาวพิมพ์ชนก กาไชย เลขที่ 10 ม.4/7")
