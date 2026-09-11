import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา (Brainrot Edition)")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี (มี 5 ข้อ)
for i in range(1, 6):
    key = f"ans{i}_val"
    if key not in st.session_state:
        st.session_state[key] = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    for i in range(1, 6):
        st.session_state[f"ans{i}_val"] = ""
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog) แสดงผลลัพธ์
# ----------------------------------------------------
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

    if score == 5:
        st.success("🎉 ว้าววว คุณเก่งมาก! สมเป็นเซียน Brainrot!")
    elif score >= 1:
        st.info("🎈 คุณพยายามอีกนิดนะ!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง (ตั้งไว้ที่ 45 วินาที)
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(45 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# ----------------------------------------------------
# 3. ช่องรับคำตอบพร้อมรูปประกอบแต่ละตัวละคร
# ----------------------------------------------------

# ข้อ 1: Tung tung sahur
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Tung_Tung_Tung_Sahur.jpg/800px-Tung_Tung_Tung_Sahur.jpg", width=200)
ans1 = st.text_input(
    "ข้อ 1: T _ n g  t _ n g  s _ h u r 🔔",
    value=st.session_state.ans1_val,
)

st.divider()

# ข้อ 2: Bombardiro crocodillo
st.image("https://example.com/bombardiro_crocodillo.jpg", width=200)
ans2 = st.text_input(
    "ข้อ 2: B _ m b a r d _ r o  c r _ c o d _ l l o 🐊",
    value=st.session_state.ans2_val,
)

st.divider()

# ข้อ 3: Brr brr patapim
st.image("https://example.com/brr_brr_patapim.jpg", width=200)
ans3 = st.text_input(
    "ข้อ 3: B _ r  b _ r  p a t _ p _ m 🐧",
    value=st.session_state.ans3_val,
)

st.divider()

# ข้อ 4: Tralalero tralala
st.image("https://example.com/tralalero_tralala.jpg", width=200)
ans4 = st.text_input(
    "ข้อ 4: T r _ l a l _ r o  t r _ l a l a 🎶",
    value=st.session_state.ans4_val,
)

st.divider()

# ข้อ 5: Capuchino assassino
st.image("https://example.com/capuchino_assassino.jpg", width=200)
ans5 = st.text_input(
    "ข้อ 5: C _ p u c h _ n o  a s s _ s s i n o ☕",
    value=st.session_state.ans5_val,
)

# อัปเดตค่าล่าสุดเข้า session_state
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)

st.divider()
st.write("กลุ่มที่ 7")

