# 🔢 Lab: Intro. ANN, MNIST Model + Deploy with Streamlit

**วิชา:** CP461 Intro to Computer Vision  
**ผู้จัดทำ:** นายวัชรพงศ์ มาลัง  
**รหัสนิสิต:** 67102010174  

---

## 📌 ลิงก์สำคัญ (Important Links)
- **Google Sheets (NN-Random-w_67102010174):** [https://docs.google.com/spreadsheets/d/1BHw4WhmwJAYRmXCtsbq00YODmssfhJqjghRKug22YDw/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1BHw4WhmwJAYRmXCtsbq00YODmssfhJqjghRKug22YDw/edit?usp=sharing)
- **GitHub Repository:** [https://github.com/Watcharaphong09/week6-ANN-MNIST-Deploy-67102010174](https://github.com/Watcharaphong09/week6-ANN-MNIST-Deploy-67102010174)
- **Streamlit Web App:** [https://week6-ann-mnist-deploy-67102010174.streamlit.app](https://week6-ann-mnist-deploy-67102010174.streamlit.app)

---

## 📁 โครงสร้างโฟลเดอร์ส่งงาน (Folder Structure)
```
week6-ANN-MNIST-Deploy-67102010174/
├── Intro-ANN-MNIST-67102010174.ipynb   # โน้ตบุ๊กทดลองและเทรนโมเดล (รันผลลัพธ์ครบทุกเซลล์)
├── app.py                              # ซอร์สโค้ด Streamlit Web App
├── 67102010174_mnist_model.keras       # โมเดล Keras ที่ผ่านการเทรน
├── requirements.txt                    # รายการ Library สำหรับรันและ Deploy
├── img_1.jpg                           # ภาพตัวอย่างสำหรับทดสอบโมเดล (ตัวเลข 2)
└── README.md                           # คำอธิบายรายละเอียดโปรเจกต์
```

---

## 🧠 สรุปสถาปัตยกรรมโมเดลและผลการประเมิน (Model Architecture & Performance)
1. **โครงสร้างโมเดล (Artificial Neural Network - ANN):**
   - **Input Layer:** `Input(shape=(28, 28))`
   - **Flatten Layer:** แปลงภาพ 28x28 เป็นเวกเตอร์ 784 มิติ
   - **Hidden Layer:** `Dense(128, activation='relu')`
   - **Output Layer:** `Dense(10, activation='softmax')`
2. **การคอมไพล์ (Compile):**
   - Optimizer: `Adam`
   - Loss Function: `sparse_categorical_crossentropy`
   - Metrics: `accuracy`
3. **ผลการเทรน (5 Epochs):**
   - **Test Accuracy:** **97.32%**
   - **Test Loss:** **0.0813**
4. **การทดสอบกับภาพภายนอก (`img_1.jpg`):**
   - โมเดลทำนายได้ตัวเลข: **2** (ความมั่นใจ 99.99%)

---

## 🚀 วิธีการรันบนเครื่อง Local (Run Locally)
1. ติดตั้ง Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. รันแอปพลิเคชัน Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## ☁️ วิธีการ Deploy บน Streamlit Cloud
1. อัปโหลดไฟล์ทั้งหมดขึ้น GitHub Repository (`Watcharaphong09/week6-ANN-MNIST-Deploy-67102010174`)
2. เข้าสู่ระบบที่ [https://share.streamlit.io](https://share.streamlit.io) ด้วยบัญชี GitHub
3. เลือก Repository, Branch (`main`), และ Main file path (`app.py`)
4. ในส่วน **Advanced settings**, แนะนำเลือก Python Version เป็น **3.11**
5. กดปุ่ม **Deploy!**
