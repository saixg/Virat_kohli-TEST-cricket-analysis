import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# Page configuration
# -----------------------------------
st.set_page_config(
    page_title="Virat Kohli – Test Career Analysis",
    layout="wide"
)

st.title("🏏 Virat Kohli – Test Career Struggle Analysis")

st.markdown("""
This application analyzes **when and why Virat Kohli struggled in Test cricket**  
using **ball-by-ball data**, **clean statistics**, and **cricket logic**.

⚠️ This is **explanatory analysis**, not prediction.
""")

# -----------------------------------
# Load data
# -----------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/kohli_test_ball_by_ball.csv")

df = load_data()

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.header("Filters")

career_filter = st.sidebar.multiselect(
    "Career Phase",
    options=df["career_phase"].dropna().unique(),
    default=df["career_phase"].dropna().unique()
)

df = df[df["career_phase"].isin(career_filter)]

# -----------------------------------
# Helper function for dismissal rate
# -----------------------------------
def dismissal_rate_plot(group_col, title, labels=None):
    stats = df.groupby(group_col).agg(
        balls=("dismissal", "count"),
        dismissals=("dismissal", "sum")
    )
    stats["rate"] = stats["dismissals"] / stats["balls"]

    fig, ax = plt.subplots()
    stats["rate"].plot(kind="bar", ax=ax)

    ax.set_title(title)
    ax.set_ylabel("Dismissal Rate")

    if labels:
        ax.set_xticklabels(labels, rotation=0)

    st.pyplot(fig)

# ===================================
# SECTION 1: Early Phase Vulnerability
# ===================================
st.header("1️⃣ Early Phase Vulnerability")

df["early_phase"] = (df["over"] <= 10).astype(int)

dismissal_rate_plot(
    "early_phase",
    "Dismissal Rate: Early Phase vs Settled Phase",
    labels=["Settled Phase", "Early Phase"]
)

st.markdown("""
**Insight**  
Virat Kohli’s dismissal rate is higher in the **first 10 overs** of an innings.
This suggests vulnerability before settling, especially against fresh bowlers
and early movement.
""")

# ===================================
# SECTION 2: Ball Age (New vs Old Ball)
# ===================================
st.header("2️⃣ Ball Age Impact")

df["ball_age"] = pd.cut(
    df["over"],
    bins=[0, 15, 40, 200],
    labels=["New Ball", "Middle Overs", "Old Ball"]
)

dismissal_rate_plot(
    "ball_age",
    "Dismissal Rate by Ball Age"
)

st.markdown("""
**Insight**  
The **new ball** phase carries the highest dismissal risk, confirming the impact
of seam and swing. Elevated risk later reflects fatigue and match pressure rather
than technique alone.
""")

# ===================================
# SECTION 3: Pace vs Spin
# ===================================
st.header("3️⃣ Pace vs Spin")

dismissal_rate_plot(
    "is_pace",
    "Dismissal Rate: Pace vs Spin",
    labels=["Spin", "Pace"]
)

st.markdown("""
**Insight**  
Dismissals occur more frequently against **pace** than spin. Speed, bounce,
and lateral movement posed a greater challenge than turn-based bowling.
""")

# ===================================
# SECTION 4: Dismissal Types
# ===================================
st.header("4️⃣ Dismissal Type Distribution")

dismissal_dist = (
    df[df["dismissal"] == 1]["dismissal_type"]
    .value_counts()
    .head(6)
)

fig, ax = plt.subplots()
dismissal_dist.plot(kind="bar", ax=ax)
ax.set_title("Most Common Dismissal Types")
ax.set_ylabel("Count")
st.pyplot(fig)

st.markdown("""
**Insight**  
A large proportion of dismissals occur via **catches**, particularly behind the wicket.
This supports the narrative of persistent challenges outside off stump.
""")

# ===================================
# SECTION 5: Match Pressure (Innings)
# ===================================
st.header("5️⃣ Match Pressure & Innings")

dismissal_rate_plot(
    "innings",
    "Dismissal Rate by Innings"
)

st.markdown("""
**Insight**  
Higher dismissal rates in later innings suggest **fatigue, deteriorating pitch
conditions, and pressure**, rather than isolated technical issues.
""")

# ===================================
# FINAL CONCLUSION
# ===================================
st.header("📌 Final Conclusion")

st.markdown("""
Virat Kohli’s Test struggles were **not caused by a single technical flaw**.

The data shows:
- Increased vulnerability in **early phases** against pace
- Elevated risk with the **new ball**
- Greater dismissals under **pressure and fatigue**
- Persistent exposure **outside off stump**

Together, these patterns indicate a **contextual and physical decline** rather
than a fundamental batting weakness.

This aligns with how elite performance analysts interpret late-career downturns.
""")

st.markdown("---")
st.markdown("📊 *Built using ball-by-ball Test match data and cricket-driven analysis.*")
