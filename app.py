import os
import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

# Streamlit Page Config
st.set_page_config(
    page_title="MNIST Digit Predictor - 67102010174",
    page_icon="🔢",
    layout="centered"
)

st.title("🔢 MNIST Digit Predictor")
st.markdown("### Lab: Intro. ANN, MNIST Model + Deploy with Streamlit")
st.caption("👤 **ผู้พัฒนา:** นายวัชรพงศ์ มาลัง | **รหัสนิสิต:** 67102010174")

# Model Loading
model_path = '67102010174_mnist_model.keras'

@st.cache_resource
def load_model():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        model_path,
        os.path.join(script_dir, model_path),
        os.path.join(os.getcwd(), model_path)
    ]
    for p in candidates:
        if os.path.exists(p):
            return tf.keras.models.load_model(p)
    return None

model = load_model()

if model is None:
    st.error(f"❌ Model file '{model_path}' not found. Please ensure the model file is in the same directory.")
    st.stop()
else:
    st.sidebar.success(f"✅ โหลดโมเดล `{model_path}` เรียบร้อยแล้ว")

# Preprocessing Option in Sidebar
st.sidebar.header("⚙️ ตั้งค่าการประมวลผล")
auto_invert = st.sidebar.checkbox(
    "สลับสีภาพอัตโนมัติ (Invert Color)",
    value=True,
    help="แปลงภาพตัวเลขสีดำบนพื้นขาวให้เป็นตัวเลขสีขาวบนพื้นดำตามมาตรฐาน MNIST"
)

st.write("อัปโหลดรูปภาพตัวเลขลายมือเขียน (0 - 9) เพื่อให้โมเดลทำนาย:")

# File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Quick sample test button
script_dir = os.path.dirname(os.path.abspath(__file__))
sample_path = os.path.join(script_dir, "img_1.jpg")
if not uploaded_file and os.path.exists(sample_path):
    if st.button("🖼️ ทดสอบด้วยภาพตัวอย่าง img_1.jpg"):
        uploaded_file = sample_path

if uploaded_file is not None:
    try:
        if isinstance(uploaded_file, str):
            img = Image.open(uploaded_file)
        else:
            img = Image.open(uploaded_file)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🖼️ ภาพต้นฉบับ")
            st.image(img, caption='Uploaded Image', use_container_width=True)

        st.write("")
        st.write("🔄 กำลังประมวลผลและจำแนกตัวเลข...")

        # 1. Convert to grayscale
        gray_img = img.convert('L')

        # 2. Check and Invert if background is light/white
        img_np_raw = np.array(gray_img)
        if auto_invert and img_np_raw.mean() > 127:
            gray_img = ImageOps.invert(gray_img)

        # 3. Resize to 28x28 pixels
        img_resized = gray_img.resize((28, 28))

        with col2:
            st.subheader("🔍 ภาพขนาด 28x28 (Grayscale)")
            st.image(img_resized, caption='Processed 28x28', width=140)

        # 4. Convert to numpy array & Normalize pixel values to [0, 1]
        img_array = np.array(img_resized).astype("float32") / 255.0

        # 5. Reshape for model prediction (add batch dimension)
        img_array = img_array.reshape(1, 28, 28)

        # 6. Make a prediction
        prediction = model.predict(img_array)[0]

        # 7. Get the predicted digit and confidence
        predicted_digit = int(np.argmax(prediction))
        confidence = float(prediction[predicted_digit]) * 100

        st.divider()
        st.subheader("🎯 ผลการทำนาย")
        
        m_col1, m_col2 = st.columns([1, 2])
        with m_col1:
            st.metric(label="ตัวเลขที่ทำนายได้", value=str(predicted_digit))
            st.metric(label="ความมั่นใจ (Confidence)", value=f"{confidence:.2f}%")
        
        with m_col2:
            st.write("📊 **กราฟแสดงความน่าจะเป็น (Probability Distribution):**")
            chart_data = {str(i): float(prediction[i]) for i in range(10)}
            st.bar_chart(chart_data)

        st.success(f"🎉 โมเดลทำนายว่าภาพนี้คือตัวเลข: **{predicted_digit}** (ความแม่นยำ {confidence:.2f}%)")

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการทำนาย: {e}")
