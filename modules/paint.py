import streamlit as st
import base64
import os

def _(zh, en, lang):
    return zh if lang == "中文" else en

def render(lang):
    st.header(_("为老虎队员化妆", "Paint the Tiger Face", lang))

    st.markdown(_(
        "使用颜色选择器与画笔工具在下方图像上绘制虎纹，点击“保存”即可下载到本地，然后请到展示页上传。",
        "Use the brush below to paint tiger stripes. Click 'Save' to download, then upload it in the showcase page.",
        lang
    ))

    image_path = "assets/tiger_reference.PNG"
    if os.path.exists(image_path):
        st.image(image_path, caption=_("\u793a\u4f8b\u56fe", "Example", lang), width=300)
    else:
        st.warning(_("无法找到 tiger_reference.png 图片", "Reference image not found.", lang))

    # 加载底图 base64
    with open("assets/paint_base_tiger.png", "rb") as f:
        base_img_data = base64.b64encode(f.read()).decode()
    base_img_url = f"data:image/png;base64,{base_img_data}"

    selected_color = st.color_picker(_("请选择画笔颜色", "Choose Brush Color", lang), "#ff9900")

    st.markdown("### 👇 点击下方图开始绘画")

    st.components.v1.html(f"""
    <html>
      <body style="text-align:center;">
        <input type="color" id="colorPicker" value="{selected_color}" style="margin-bottom:10px;">
        <br>
        <canvas id="tigerCanvas" width="400" height="500"
          style="border:1px solid #000;">
        </canvas>
        <br><br>
        <button onclick="clearCanvas()">🪜 清除</button>
        <button onclick="saveCanvas()">📏 保存图片</button>

        <script>
        const canvas = document.getElementById('tigerCanvas');
        const ctx = canvas.getContext('2d');
        const colorInput = document.getElementById('colorPicker');
        let drawing = false;

        const background = new Image();
        background.src = "{base_img_url}";
        background.onload = function () {{
            ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
        }};

        canvas.addEventListener('mousedown', function(e) {{
            drawing = true;
            ctx.beginPath();
            ctx.moveTo(e.offsetX, e.offsetY);
        }});
        canvas.addEventListener('mousemove', function(e) {{
            if (drawing) {{
                ctx.lineTo(e.offsetX, e.offsetY);
                ctx.strokeStyle = colorInput.value;
                ctx.lineWidth = 5;
                ctx.lineCap = 'round';
                ctx.stroke();
            }}
        }});
        canvas.addEventListener('mouseup', function(e) {{
            drawing = false;
        }});

        function clearCanvas() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
        }}

        function saveCanvas() {{
            const finalCanvas = document.createElement('canvas');
            finalCanvas.width = canvas.width;
            finalCanvas.height = canvas.height;
            const finalCtx = finalCanvas.getContext('2d');

            const finalBg = new Image();
            finalBg.src = "{base_img_url}";
            finalBg.onload = function () {{
                finalCtx.drawImage(finalBg, 0, 0, finalCanvas.width, finalCanvas.height);
                finalCtx.drawImage(canvas, 0, 0);

                const dataURL = finalCanvas.toDataURL('image/png');
                const a = document.createElement('a');
                a.href = dataURL;
                a.download = "tiger_paint.png";
                a.click();
                alert("🎉 已保存完整图片，请前往展示页上传！");
            }};
        }}
        </script>
      </body>
    </html>
    """, height=680)
