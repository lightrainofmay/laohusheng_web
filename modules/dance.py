import streamlit as st

def _(zh, en, lang):
    return zh if lang == "中文" else en

def render(lang):
    st.header(_("舞蹈结构与动作教学", "Dance Demonstration", lang))

    animations = [
        {
            "file": "assets/tiger_tiptoe.mp4",
            "title": _("老虎垫脚", "Tiger Tiptoeing", lang),
            "desc": _(
                "虎者垫脚前行，模拟潜行状态，象征谨慎与警觉。",
                "Tiger moves on tiptoe, imitating stealth—symbolizing alertness and caution.",
                lang
            )
        },
        {
            "file": "assets/tiger_door.mp4",
            "title": _("老虎开门", "Tiger Opening the Door", lang),
            "desc": _(
                "双掌推出如开门状，配合身体侧转，寓意探路迎福。",
                "Both paws push outward like opening a door while turning—symbolizing path-clearing and blessing.",
                lang
            )
        },
        {
            "file": "assets/tiger_bridge.mp4",
            "title": _("老虎搭桥", "Tiger Forming a Bridge", lang),
            "desc": _(
                "一虎抬起前掌搭在另一虎脚背上，象征信任与支撑。",
                "One tiger lifts its front paw and rests it on another tiger’s foot—symbolizing trust and support.",
                lang
            )
        },
        {
            "file": "assets/tiger_kiss.mp4",
            "title": _("老虎亲嘴", "Tiger Kissing", lang),
            "desc": _(
                "两虎面对面，前掌相对，左右扭动，象征钦慕物件。",
                "Two tigers face each other, bow slightly and touch paws—symbolizing intimacy and unity.",
                lang
            )
        },
        {
            "file": "assets/tiger_wipe_ass.mp4",
            "title": _("老虎擦屁股", "Tiger Butt Rubbing", lang),
            "desc": _(
                "两虎背对背站立，臀部相互摩擦，动作滑稽，象征亲密友善、群体融合。",
                "Two tigers stand back-to-back and rub their hips together in a playful motion—symbolizing intimacy, friendliness, and social bonding.",
                lang
            )
        }

    ]


    for anim in animations:
        st.markdown(f"### {anim['title']}")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.video(anim["file"])
        with col2:
            st.markdown(anim["desc"])
        st.markdown("---")