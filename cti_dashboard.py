import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

st.set_page_config(page_title="YMCA CTI Dashboard", layout="wide")

# ----------------------
# Title and Introduction
# ----------------------
st.title("Cyber Threat Intelligence in Nonprofits")
st.subheader("YMCA Norfolk Case Study – Organisation Sponsored Project")
st.markdown("""
This interactive dashboard presents insights from a qualitative research project exploring how YMCA Norfolk, a nonprofit organisation, manages Cyber Threat Intelligence (CTI).
The project identifies challenges, thematic patterns, and practical recommendations tailored for the nonprofit sector.
""")

# -----------------------------
# Section 1: Research Objectives
# -----------------------------
st.header("1. Research Objectives")
with st.expander("Click to view objectives"):
    st.markdown("""
    - Identify what CTI data is collected, stored, and used.
    - Examine the tools and workflows used for CTI.
    - Discover barriers such as data overload and limited expertise.
    - Understand staff perspectives and ethical concerns.
    - Design a practical CTI framework for nonprofits.
    """)

# -----------------------------
# Section 2: Data Sources
# -----------------------------
st.header("2. Data Sources and Methodology")
data_sources = ["Firewall Logs", "Email Security Alerts", "Interview Transcripts", "Audit Reports"]
st.multiselect("Data sources used in research:", data_sources, default=data_sources)

st.markdown("""
Qualitative case study approach following Yin (2018). Data included semi-structured interviews, log inspections, and coding in NVivo to uncover themes.
""")

# -----------------------------
# Section 3: Key Challenges
# -----------------------------
st.header("3. Key Challenges Identified")
challenges = {
    "Alert Overload": 80,
    "Tool Fragmentation": 60,
    "Low Awareness": 70,
    "Ethical Resistance": 50,
}
fig, ax = plt.subplots()
ax.bar(challenges.keys(), challenges.values(), color='skyblue')
ax.set_ylabel('Severity (0–100)')
ax.set_title('CTI Challenges at YMCA Norfolk')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# -----------------------------
# Section 4: Thematic Word Cloud
# -----------------------------
st.header("4. Thematic Analysis")
with st.expander("Generated Word Cloud of Themes"):
    text = "alert overload awareness training logs ethics culture blame security automation"
    wordcloud = WordCloud(width=800, height=300, background_color='white').generate(text)
    fig_wc, ax_wc = plt.subplots()
    ax_wc.imshow(wordcloud, interpolation='bilinear')
    ax_wc.axis("off")
    plt.tight_layout()
    st.pyplot(fig_wc)

# -----------------------------
# Section 5: Mock Log Data with Filtering
# -----------------------------
st.header("5. Mock Log Data (for Testing CTI Tools)")
np.random.seed(42)
mock_data = pd.DataFrame({
    "Timestamp": pd.date_range("2025-06-01", periods=100, freq="h"),
    "Source_IP": np.random.choice(["192.168.1.1", "10.0.0.5", "172.16.0.9", "203.0.113.4"], size=100),
    "Destination_Port": np.random.choice([22, 80, 443, 3389], size=100),
    "Event_Type": np.random.choice(["Failed Login", "Malware Alert", "Phishing Attempt", "Firewall Block"], size=100),
    "Severity": np.random.randint(1, 5, size=100),
    "Is_Internal": np.random.choice([True, False], size=100)
})

selected_event = st.selectbox("Filter by Event Type:", options=mock_data["Event_Type"].unique())
filtered_data = mock_data[mock_data["Event_Type"] == selected_event]
st.dataframe(filtered_data)

# -----------------------------
# Section 6: Recommendations
# -----------------------------
st.header("6. Recommendations")
with st.expander("1. Use Automated Triage (e.g. Microsoft Sentinel)"):
    st.markdown("Reduce manual alert processing using automation tools.")
with st.expander("2. Centralise Log Views"):
    st.markdown("Combine tools like Defender and Elastic Stack for a unified dashboard.")
with st.expander("3. Cybersecurity Training Modules"):
    st.markdown("Quarterly, scenario-based training for all staff.")
with st.expander("4. CTI Steering Committee"):
    st.markdown("Form a cross-department group to manage and advocate for CTI.")

# -----------------------------
# Section 7: Ethical Considerations
# -----------------------------
st.header("7. Ethical Considerations")
st.markdown("""
- No personal data used; logs anonymised.
- Ethics clearance granted by UEA Business Research Ethics Committee.
- NDA signed with YMCA Norfolk.
- Reflexivity and boundary management respected throughout.
""")

# -----------------------------
# Section 8: Future Work
# -----------------------------
st.header("8. Next Steps")
st.markdown("""
- Finalise thematic coding in NVivo.
- Develop a lightweight CTI framework.
- Present findings to YMCA Norfolk leadership.
- Complete final report and erase data per NDA.
""")

st.success("✅ Dashboard Complete – Interactive Streamlit version ready!")
