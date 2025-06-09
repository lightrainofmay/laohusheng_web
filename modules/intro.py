import streamlit as st
import pandas as pd

def _(zh, en, lang):
    return zh if lang == "中文" else en

def render(lang):
    st.header(_("老虎笙的历史与文化", "History & Culture", lang))

    # 🎨 图文两栏排版
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(
            "assets/tiger_sheng_photo.png",
            caption=_("双柏县老虎笙演出", "Tiger Sheng Performance in Shuangbai", lang),
            
        )

    with col2:
        st.markdown(_(
            """
            老虎笙（跳虎节）是云南楚雄州双柏县彝族“倮倮人”世代传承的民间祭祀舞蹈，核心体现为“供虎”“敬虎”的仪式性表演。
            每年农历正月初八至十五举行，象征着对虎神的崇拜与祈福。

            据《中国民族民间舞蹈集成》和小麦地冲村老虎笙协会资料记载，老虎笙起源于古老的虎图腾信仰，
            是彝族供奉虎神、敬畏自然的宗教表达。彝族人自称“虎子孙”，视虎为祖先与保护神。

            跳虎节逐日递增“虎”的数量，初八为三虎，至十三日增至八虎，节日气氛逐步推向高潮。
            正月十五为“送虎日”，白天“虎队”走村入户祝福贺年，由“朵西”（山神）诵吉语祈福驱邪；
            晚上村民集中跳舞至深夜，由“道人”（虎首）率众将“虎”送至村外“叫魂子”梁子处，仪式圆满落幕。

            相传跳虎节源于一段古老故事：勇敢青年苗阿保在正月初八击鼓赶走猛虎，最终化为守护石虎。
            村民为纪念他而创作“老虎笙”，年年传承不断。

            小麦地冲村位于云南省楚雄州双柏县法脿镇，由上村（小麦地冲）与下村（半坡）组成，两村相距500余米。
            全村126户，常住人口600余人，多数为彝族，少数为汉族。

            村中彝族自称“倮倮”，“倮”在彝语中意为“虎”，“倮倮族”即“虎族”，体现其世代崇虎的文化传统。
            据村中老人苗自有回忆，村子原名“玉米村”，最早居住为“苗”姓彝族，后有“杨”“李”姓迁入，因广泛种植小麦，遂更名为“小麦地冲村”。

            跳虎节舞队结构严谨，分工明确：
            - 道人（虎首）：披羊皮，手持挂葫芦的竹杆，负责指挥；
            - 山神（朵西）：头戴笠帽，右手铜铃，左手香束，送福祈安；
            - 老虎（共8只）：身披虎皮、头戴虎面，绘虎纹，动作威武；
            - 猫（2只）：身着短装，脸绘胡须线，灵巧收礼；
            - 鼓手（4人）：持羊皮鼓，全程伴奏。

            今日跳虎节不仅延续了民族记忆，更是国家级非物质文化遗产的鲜活体现。
            """,
            """
            Tiger Sheng (also called the Tiger Festival) is a ritual dance inherited by the Yi people of Shuangbai County in Chuxiong, Yunnan.
            Held annually from the 8th to the 15th day of the first lunar month, it symbolizes respect and worship for the tiger deity.

            According to the *Anthology of Chinese Folk Dances* and the Xiaomaidichong Village Tiger Sheng Association, the dance originates from ancient tiger totem beliefs,
            serving as a spiritual offering to nature and ancestral spirits. The Yi people refer to themselves as “descendants of the tiger.”

            The festival adds one tiger per day—starting with three on the 8th, reaching eight by the 13th. On the 15th, the “Sending off the Tigers” ceremony takes place:
            during the day, tiger dancers visit homes with blessings delivered by the “Duoxi” (mountain god), and at night,
            the “Taoist leader” leads the final ritual by escorting the tigers to the “Jiaohunzi” mountain ridge.

            A local legend tells of a young man named Miao Abao who bravely drove away two tigers with a goatskin drum and turned into a stone tiger.
            In his honor, the villagers created Tiger Sheng, performed yearly ever since.

            Xiaomaidichong Village is located in Fapiao Town, Shuangbai County, with two sections—Upper and Lower Village—separated by 500 meters.
            The village has 126 households and over 600 residents, mostly of Yi ethnicity.

            The local Yi call themselves “Luoluo,” meaning “Tiger People” in the Yi language, reflecting their ancestral tiger worship.
            The village was once named “Corn Village” and later renamed after extensive wheat cultivation.

            Festival roles are clearly defined:
            - Taoist Leader: wears goatskin and holds a gourd-topped bamboo staff to lead;
            - Mountain Gods: hold incense and bells to deliver blessings;
            - Tigers (8): dressed in tiger costumes with painted stripes;
            - Cats (2): nimble helpers with whisker-painted faces, collecting gifts;
            - Drummers (4): play goatskin drums throughout the event.

            Today, Tiger Sheng is not only a cultural memory but also a vibrant expression of national intangible heritage.
            """,
            lang
        ))

    st.markdown("---")
    show_festival_schedule(lang)
    st.markdown("---")
    show_role_costumes(lang)

def show_festival_schedule(lang):
    st.subheader(_("📅 老虎笙节庆活动时间线", "📅 Tiger Sheng Festival Schedule", lang))

    data = {
        _( "日期", "Date", lang): [
            "正月初八", "正月初九", "正月初十", "正月十一", "正月十二", "正月十三", "正月十四", "正月十五"
        ],
        _("活动内容", "Activity", lang): [
            _("晚上开始跳三虎（跳三组“老虎”）", "Night: Dance with three tiger roles", lang),
            _("跳四虎（四组“老虎”上场）", "Four tigers join the performance", lang),
            _("跳五虎，活动增多", "Five tiger teams dance, events expand", lang),
            _("跳六虎，加入拜山神、绕村拜户", "Six tiger teams, pray to mountain gods, visit homes", lang),
            _("跳七虎，并演绎农事劳动等内容", "Seven tigers, act out farming scenes", lang),
            _("预演八虎，为高潮铺垫", "Preview of eight-tiger dance, pre-climax performance", lang),
            _("八虎正式登场，舞蹈达到高潮", "Eight tigers officially perform; dance reaches climax", lang),
            _("送虎归山，舞蹈节庆圆满结束", "Send tiger spirits to the mountains; festival ends", lang)
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

def show_role_costumes(lang):
    st.subheader(_("🎭 角色与服饰一览", "🎭 Characters & Costumes Overview", lang))

    roles = [
        {
            "name": _("道人(虎首)", "Taoist Leader ('Tiger Head')", lang),
            "image": "assets/daoren.png",
            "desc": _("穿深色长衫，手持系葫芦的竹竿，象征指挥角色",
                      "Wears a long dark robe, holds a bamboo stick with a gourd tied on top, symbolizes the team leader", lang)
        },
        {
            "name": _("山神（2位）", "Mountain Gods (x2)", lang),
            "image": "assets/shanshen.png",
            "desc": _("戴尖顶笠帽，灰色斗篷，右手铜铃，左手香束",
                      "Wears a pointed straw hat and gray cape, holds a bronze bell and incense stick", lang)
        },
        {
            "name": _("老虎（8只）", "Tigers (x8)", lang),
            "image": "assets/tiger.png",
            "desc": _("棕色短衣短裤，虎皮披肩，虎耳头套，画虎纹，表现严肃",
                      "Brown short outfit with tiger pelt shoulder cover, tiger-ear headgear, painted tiger stripes, serious expression", lang)
        },
        {
            "name": _("猫（2只）", "Cats (x2)", lang),
            "image": "assets/mao.png",
            "desc": _("短衣长裤，披羊皮坎肩，脸部绘胡须线，动作灵活",
                      "Short top and pants, sheepskin vest, whisker-painted face, agile actions", lang)
        }
    ]

    for role in roles:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(role["image"], caption=role["name"])
        with col2:
            st.markdown(f"**{role['name']}**")
            st.markdown(role["desc"])
        st.markdown("---")