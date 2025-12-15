import streamlit as st
import numpy as np
import cv2
from PIL import Image
import math

# =========================================================
# 🌸 PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="✨ Cute Image Matrix Lab ✨",
    page_icon="💖",
    layout="wide"
)

# =========================================================
# 🎀 ROSE GOLD METALLIC THEME (GLOBAL)
# =========================================================
st.markdown("""
<style>
body {
    background-color: #f6e7e2;
}
.stApp {
    background: linear-gradient(135deg, #f6e7e2, #efd6d2);
}
h1, h2, h3 {
    color: #7a4a4f;
}
p, li {
    color: #5a3a3f;
    font-size: 17px;
}
.stButton>button {
    background: linear-gradient(90deg, #c89fa3, #e6bfc4);
    color: white;
    border-radius: 20px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
}
.stSlider > div {
    color: #7a4a4f;
}
.card {
    background-color: #fff5f3;
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 🌷 SIDEBAR ROSE GOLD THEME (TARO DI SINI 👇)
# =========================================================
st.markdown("""
<style>

/* Sidebar container */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f3d6cf, #efd0ca);
    border-right: 2px solid #e6bfc4;
}

/* Sidebar text */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: #6a3d40;
}

/* Radio button cards */
div[role="radiogroup"] label {
    background-color: #fff5f3;
    padding: 12px 16px;
    margin-bottom: 12px;
    border-radius: 22px;
    transition: all 0.25s ease;
    cursor: pointer;
}

/* Hover effect */
div[role="radiogroup"] label:hover {
    background-color: #f1c6c9;
    transform: translateX(4px);
}

/* Selected state */
div[role="radiogroup"] input:checked + div {
    background: linear-gradient(90deg, #c89fa3, #e6bfc4);
    color: white;
    border-radius: 22px;
}

/* Hide radio safely */
div[role="radiogroup"] input {
    opacity: 0;
    position: absolute;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 📌 SIDEBAR NAVIGATION (SETELAH CSS)
# =========================================================
st.sidebar.markdown("## 🌷 Navigation")

page = st.sidebar.radio(
    "",
    ["🏠 Home", "🖼 Image Processing", "👩‍💻 Team Members"]
)


# =========================================================
# 🏠 HOME PAGE
# =========================================================
if page == "🏠 Home":

    st.markdown("""
    <div style="text-align:center; padding:30px;">
        <h1>💖 Image Magic Lab 💖</h1>
        <p style="font-size:20px;">
        Where <b>math</b>, <b>images</b>, and a little bit of ✨magic✨ meet.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>🌷 Welcome, Curious Human!</h2>
    <p>
    This app is not just about clicking buttons.  
    It's about <b>seeing math come alive</b> through images.
    </p>
    <p>
    Every movement, rotation, blur, and sharpen you see here  
    is controlled by <b>real matrices</b> and <b>convolution kernels</b>.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## ✨ What Kind of Magic Can You Do Here?")
    st.markdown("""
    <div class="card">
    <ul>
        <li>💫 Move images like sliding stickers (Translation)</li>
        <li>💫 Resize them like zooming in real life (Scaling)</li>
        <li>💫 Spin them around their own center (Rotation)</li>
        <li>💫 Stretch reality a little (Shearing)</li>
        <li>💫 Mirror the world (Reflection)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <ul>
        <li>🍓 Smooth images like applying soft makeup (Blur)</li>
        <li>🍓 Sharpen details like highlighter on cheekbones (Sharpen)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🧠 Behind the Scenes")
    st.markdown("""
    <div class="card">
    <p>
    Each pixel in an image has a position.  
    We gently tell those pixels where to move using matrices.
    </p>
    <p>
    Filters work differently — they <b>mix neighboring pixels together</b>  
    using tiny numerical recipes called kernels.
    </p>
    <p>
    No shortcuts. No magic tricks.  
    Just <b>math doing beautiful things</b> ✨
    </p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 🖼 IMAGE PROCESSING PAGE
# =========================================================
elif page == "🖼 Image Processing":
    st.markdown("<h1 style='text-align:center;'>🖼 Image Processing Playground</h1>", unsafe_allow_html=True)

    upload = st.file_uploader("📤 Upload an Image", type=["jpg", "png", "jpeg"])

    if upload:
        image = Image.open(upload)
        img = np.array(image)
        h, w = img.shape[:2]

        tab1, tab2 = st.tabs(["🎀 Geometric Transformations", "✨ Image Filters"])

        # -----------------------------
        # 🎀 GEOMETRIC TRANSFORMATIONS
        # -----------------------------
        with tab1:
            transform = st.selectbox(
                "Choose Transformation",
                ["Translation", "Scaling", "Rotation", "Shearing", "Reflection"]
            )

            if transform == "Translation":
                tx = st.slider("Move X", -200, 200, 0)
                ty = st.slider("Move Y", -200, 200, 0)
                M = np.float32([[1, 0, tx], [0, 1, ty]])

            elif transform == "Scaling":
                sx = st.slider("Scale X", 0.1, 3.0, 1.0)
                sy = st.slider("Scale Y", 0.1, 3.0, 1.0)
                M = np.float32([[sx, 0, 0], [0, sy, 0]])

            elif transform == "Rotation":
                angle = st.slider("Angle (degrees)", -180, 180, 0)
                rad = math.radians(angle)
                cos = math.cos(rad)
                sin = math.sin(rad)
                M = np.float32([[cos, -sin, w/2],
                                [sin,  cos, h/2]])

            elif transform == "Shearing":
                shx = st.slider("Shear X", -1.0, 1.0, 0.0)
                shy = st.slider("Shear Y", -1.0, 1.0, 0.0)
                M = np.float32([[1, shx, 0], [shy, 1, 0]])

            elif transform == "Reflection":
                axis = st.radio("Reflect Axis", ["X-axis", "Y-axis"])
                if axis == "X-axis":
                    M = np.float32([[1, 0, 0], [0, -1, h]])
                else:
                    M = np.float32([[-1, 0, w], [0, 1, 0]])

            result = cv2.warpAffine(img, M, (w, h))

            col1, col2 = st.columns(2)
            with col1:
                st.image(img, caption="Original Image", use_container_width=True)
            with col2:
                st.image(result, caption="Transformed Image", use_container_width=True)

        # -----------------------------
        # ✨ IMAGE FILTERS (CONVOLUTION)
        # -----------------------------
        with tab2:
            filter_type = st.selectbox("Choose Filter", ["Blur", "Sharpen"])

            if filter_type == "Blur":
                kernel = np.ones((3, 3)) / 9
            else:
                kernel = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])

            filtered = cv2.filter2D(img, -1, kernel)

            col1, col2 = st.columns(2)
            with col1:
                st.image(img, caption="Original Image", use_container_width=True)
            with col2:
                st.image(filtered, caption=f"{filter_type} Image", use_container_width=True)

# =========================================================
# 👩‍💻 TEAM PAGE
# =========================================================
else:
    st.markdown("""
    <div style="text-align:center; padding:30px;">
        <h1>👩‍💻 Meet the Brains Behind the Magic</h1>
        <p style="font-size:18px;">Two minds. One cute math project 💖</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .team-card {
        background-color: #fff5f3;
        padding: 25px;
        border-radius: 30px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.12);
        margin-top: -80px;
        text-align: center;
    }
    .team-img {
        border-radius: 50%;
        border: 6px solid #e6bfc4;
        width: 180px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("gitri.jpg", use_container_width=False)
        st.markdown("""
        <div class="team-card">
            <h3>🌼 Gita Triyani Siagian</h3>
            <p><b>Matrix & Image Processing Logic</b></p>
            <p>
            Turns mathematical formulas into moving, rotating,
            and transforming images.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("rosie.jpg", use_container_width=False)
        st.markdown("""
        <div class="team-card">
            <h3>🌸 Roshni Mythili</h3>
            <p><b>UI Design & Streamlit Layout</b></p>
            <p>
            Makes math feel soft, friendly, and visually enjoyable.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="margin-top:40px;">
    <h2>💖 How This App Comes to Life</h2>
    <p>
    You upload an image.  
    You choose what you want to do to it.
    </p>
    <p>
    Behind the scenes, matrices and convolution kernels
    quietly do their job — and the result appears instantly.
    </p>
    <p>
    Learning math doesn’t have to be scary.  
    Sometimes, it can be ✨cute✨.
    </p>
    </div>
    """, unsafe_allow_html=True)

