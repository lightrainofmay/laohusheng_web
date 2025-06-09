# modules/showcase.py

import streamlit as st
import os
import shutil
from datetime import datetime

def _(zh, en, lang):
    return zh if lang == "中文" else en

def render(lang):
    st.header(_("📺 上传你的老虎笙表演", "📺 Upload Your Tiger Sheng Performance", lang))

    uploaded_video = st.file_uploader(
        _("请上传你的舞蹈视频 (MP4)", "Upload your dance video (MP4)", lang),
        type="mp4",
        key="video_uploader"
    )

    if uploaded_video:
        st.video(uploaded_video)
        st.success(_("视频上传成功！", "Upload successful!", lang))

    st.markdown("---")
    st.subheader(_("🖼️ 上传你的绘画作品", "🖼️ Upload Your Drawing", lang))

    uploaded_image = st.file_uploader(
        _("请上传你绘制的图片 (PNG/JPG)", "Upload your painted image (PNG/JPG)", lang),
        type=["png", "jpg", "jpeg"],
        key="image_uploader"
    )

    if uploaded_image:
        upload_folder = "user_uploads"
        os.makedirs(upload_folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = os.path.join(upload_folder, f"user_paint_{timestamp}_{uploaded_image.name}")
        with open(save_path, "wb") as f:
            f.write(uploaded_image.read())

        st.success(_("图片上传成功！", "Image uploaded successfully!", lang))

    st.markdown("---")
    st.subheader(_("🎨 学生作品展示", "🎨 Student Artwork Showcase", lang))

    upload_folder = "user_uploads"
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    image_files = sorted(
        [f for f in os.listdir(upload_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))],
        reverse=True
    )

    if not image_files:
        st.info(_("暂无作品，快来上传吧！", "No artwork yet. Upload yours now!", lang))
        return

    cols = st.columns(3)
    for idx, filename in enumerate(image_files):
        img_path = os.path.join(upload_folder, filename)
        with cols[idx % 3]:
            st.image(img_path, caption=filename, width=250)