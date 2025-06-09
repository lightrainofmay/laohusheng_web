import streamlit as st
import streamlit.components.v1 as components
import base64
import json

def _(zh, en, lang):
    return zh if lang == "中文" else en

def render(lang="中文"):
    st.header(_("🥁 羊皮鼓练习", "🥁 Learn the Yangpi Drum", lang))

    st.subheader(_("🔊 节奏示范", "🔊 Rhythm Demo", lang))
    st.audio("assets/yangpi_demo.wav", format="audio/wav")

    st.markdown(_(
        "请聆听上方示范节奏，然后点击下方羊皮鼓图片模拟打鼓！",
        "Listen to the demo above and tap the drum image below to simulate drumming!", lang
    ))

    st.subheader(_("👐 鼓点互动", "👐 Drum Along", lang))

    # 读取音频和图片
    with open("assets/drum_hit.wav", "rb") as f:
        drum_audio_b64 = base64.b64encode(f.read()).decode()
    audio_src = f"data:audio/wav;base64,{drum_audio_b64}"

    with open("assets/yangpigu.png", "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()
    img_src = f"data:image/png;base64,{img_b64}"

    # 嵌入 HTML+JS
    components.html(f"""
    <html>
      <body style="text-align:center;">
        <img id="drumImg" src="{img_src}" alt="羊皮鼓" style="width:200px;cursor:pointer;" />
        <p id="status" style="font-size:18px;">速度: -</p>
        <p id="intervalsDisplay" style="font-size:14px;color:#666;"></p>
        <audio id="drumSound" src="{audio_src}"></audio>

        <script>
          let lastClick = null;
          const intervals = [];

          const img = document.getElementById("drumImg");
          const status = document.getElementById("status");
          const display = document.getElementById("intervalsDisplay");
          const sound = document.getElementById("drumSound");

          img.addEventListener("click", () => {{
            const now = Date.now();
            if (lastClick) {{
              const interval = now - lastClick;
              intervals.push(interval);
              if (intervals.length > 5) intervals.shift();

              const avg = intervals.reduce((a, b) => a + b, 0) / intervals.length;
              let speed = "慢速";
              if (avg < 400) speed = "快速";
              else if (avg < 800) speed = "中速";

              status.innerText = `速度: ${{speed}}（${{avg.toFixed(0)}}ms）`;
              display.innerText = "你的节奏间隔: " + JSON.stringify(intervals);
            }}
            lastClick = now;
            sound.currentTime = 0;
            sound.play();
          }});
        </script>
      </body>
    </html>
    """, height=400)

    st.markdown("---")
    st.subheader(_("🎯 节奏评分", "🎯 Rhythm Scoring", lang))

    # 示例节奏间隔（毫秒）
    demo_intervals = [500, 500, 500, 500, 500]

    user_input = st.text_input(_("请输入你的节奏数组", "Enter your rhythm intervals array", lang),
                               placeholder="[480, 520, 500, 510, 530]")

    if user_input:
        try:
            user_intervals = json.loads(user_input)
            if not isinstance(user_intervals, list) or not all(isinstance(i, (int, float)) for i in user_intervals):
                raise ValueError("必须是数字组成的数组")

            if len(user_intervals) != len(demo_intervals):
                st.error(_("节奏数量不一致，请尝试打 5 次鼓", "Mismatch: Try hitting the drum 5 times", lang))
            else:
                errors = [abs(u - d) for u, d in zip(user_intervals, demo_intervals)]
                avg_error = sum(errors) / len(errors)
                score = max(0, 100 - avg_error * 0.1)  # 每超出 10ms 扣 1 分
                st.success(_("你的评分为", "Your score is", lang) + f"：{score:.1f} 分")
        except Exception as e:
            st.error(_("输入格式有误，请使用如：[500, 520, 480] 的数组", "Invalid format, use e.g. [500, 520, 480]", lang))