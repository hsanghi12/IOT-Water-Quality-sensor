import streamlit as st

def app():
    st.title("FAQ · HydroPulse Sentinel")

    st.markdown("---")
    st.subheader("Did you know? Essential water quality facts")
    st.markdown(
        """
**What is pH?**  
pH measures how acidic or alkaline water is. A pH below 7 is acidic, above 7 is alkaline, and around 7 is neutral. HydroPulse Sentinel alerts operators when pH drifts more than 0.5 units from the local safe range because both acidic and alkaline extremes can corrode pipes or harm health.

**Why is turbidity important?**  
Turbidity tracks how cloudy the water is. High turbidity often means sediment, microbes, or pollution, so we pair it with microbial testing.

**Why monitor dissolved oxygen (DO)?**  
DO affects aquatic life and indicates organic pollution. A sharp drop may signal contamination from sewage or chemicals.
"""
    )

    st.markdown("---")
    st.subheader("Waterborne disease resources")
    st.markdown(
        """
- [WHO — Water-related diseases](https://www.who.int/news-room/fact-sheets/detail/drinking-water)
- [CDC — Healthy Water](https://www.cdc.gov/healthywater/)
- [UNICEF — Water, Sanitation & Hygiene (WASH)](https://www.unicef.org/wash)
"""
    )

    st.markdown("---")
    st.subheader("Frequently Asked Questions")
    st.markdown(
        """
**How does HydroPulse Sentinel track remote water bodies?**  
Each node labels readings by water type (groundwater, river, municipal, tank) and uploads to ThingSpeak so the central CatBoost model learns context-aware patterns.

**Can I check potability from my phone?**  
Yes, the dashboard updates in seconds and records any deviation from detection limits so you can take immediate action.

**Why does the model look at multiple parameters at once?**  
Water quality is multi-dimensional: low pH with high TDS may need buffering, while high turbidity may point to microbial blooms. CatBoost captures these correlations and reduces false alarms.
"""
    )

    st.markdown("---")
    st.subheader("SEO-ready image descriptions")
    st.markdown(
        """
HydroPulse Sentinel uses descriptive captions so search engines index the site for keywords like *water quality sensor*, *remote water monitoring*, *pH detection*, and *IoT drinking water safety*. Each image caption mentions the scenario, sensor, or test to boost discoverability.
"""
    )
