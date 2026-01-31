import streamlit as st

def app():
    st.title("HydroPulse Sentinel — Measuring Every Drop Before It Reaches You")

    intro = """
Every community, especially remote places, deserves a live sense of its water health before it hits a tap or bottle. HydroPulse Sentinel is an IoT + AI observatory that continuously measures **pH**, **turbidity**, **dissolved oxygen**, **conductivity**, and **TDS** from borewells, tanks, and surface sources to keep families informed.
"""
    st.markdown(intro)

    st.markdown("---")
    st.subheader("HydroPulse Sentinel at a Glance")
    st.markdown(
        """
Not just another gadget—HydroPulse Sentinel is the digital watchtower for your water supply. Every synthetic droplet is tracked with care, and the system learns from **groundwater, surface water, and municipal taps** by testing sample profiles as part of the model retraining pipeline.

**Key features:**
- **Real-time monitoring**: Instant ThingSpeak uploads keep a remote command center synced.
- **Remote access**: Caregivers can view trendlines from any smartphone or desktop.
- **Threshold watch**: Smart rules highlight approaching trouble long before it becomes a crisis.
- **Affordable & scalable**: Sensor kits, solar power, and open data make deployments sustainable.
"""
    )

    st.subheader("HydroPulse Sentinel Logo")
    st.image("logo.png", caption="HydroPulse Sentinel emblem", use_column_width=False)

    st.markdown("---")
    st.subheader("System Snapshot & Purpose")
    st.markdown(
        """
**Clean water deficit**: Over 2.2 billion people globally still lack safely managed drinking water, and roughly **29% of India’s population** (≈430 million people) consumes water that fails the WHO basic quality norms.  
**Contaminated water**: An estimated **844 million people** lack safe drinking water at home, so HydroPulse Sentinel highlights that nearly **11% of the world population** still relies on contaminated sources.  
**SDG alignment**: This project supports **SDG 6 — Clean Water and Sanitation**, the United Nations goal to ensure availability and sustainable management of water for all.  
**Trusted references**: [WHO Drinking Water fact sheet](https://www.who.int/news-room/fact-sheets/detail/drinking-water), [UN-Water updates](https://www.unwater.org), and [Delhi Jal Board initiatives](https://www.delhijalboard.nic.in) repeatedly highlight the need for monitoring in remote places.
"""
    )

    st.subheader("How the system works")
    st.markdown(
        """
1. HydroPulse Sentinel nodes sample **groundwater, rivers, municipal taps, and tanks** so every water chemistry is seen; the hardware labels each source.
2. Sensors stream live values (pH, turbidity, DO, conductivity, TDS) to ThingSpeak, where CatBoost compares the new signal to historical baselines from those same water types.
3. The model evaluates potability, updates contamination scores, and the dashboard shows meters and detection limits so caretakers know when thresholds are reached.
4. When any reading nears or exceeds its detection limit, the system pushes alerts, catalogs signal strength, and recommends actions (filtration, buffering, or municipal escalation), keeping the loop tight from field data to response.
"""
    )

    st.markdown("---")
    st.subheader("Sensor Table, Detection Limits & Shelf Life")
    st.markdown(
        """
| Parameter         | Typical Range     | Detection Limit | Unit   | Shelf Life (typical)                     |
|------------------|-------------------|-----------------|--------|------------------------------------------|
| pH               | 0.0 – 14.0        | 0.01            | pH     | 12 months (replace membrane annually)    |
| Turbidity        | 0 – 1000          | 0.1             | NTU    | 18 months (optical surface recalibration)|
| Dissolved Oxygen | 0 – 20            | 0.1             | mg/L   | 12 months (electrode maintenance)        |
| Conductivity     | 0 – 2000          | 0.5             | uS/cm | 24 months (sealed chip, recalibrate)     |
| TDS              | 0 – 2000          | 1               | ppm    | 24 months (combined probe recalibration) |
| Temperature      | 0 – 100           | 0.1             | C      | 36 months (digital sensors stay stable)  |
"""
    )

    st.subheader("Algorithm and Testing Improvements")
    st.markdown(
        """
HydroPulse Sentinel uses a CatBoost classifier tuned on stratified folds from **borewell, river, and municipal tap** samples so the detector does not overspecialize on a single water type. The retraining pipeline injects seasonal variance and noise to catch spikes, and the Model page contrasts live predictions with historical baselines from each source.
        """
    )

    st.subheader("Alerts & Monitoring")
    st.markdown(
        """
Early alerts are now powered by **threshold watch rules** that flag any parameter growing toward the highest measured limits. Alerts include the water type, parameter, and the confidence of the CatBoost prediction for the crew to act on.
        """
    )

    st.markdown("---")
    st.subheader("Search Engine Optimization & Mission Reach")
    st.markdown(
        """
Search engine optimization (SEO) helps HydroPulse Sentinel show up for searches such as *water quality sensor*, *remote water monitoring*, *IoT drinking water safety*, and *pH detection in tanks*. The copy balances keywords with storytelling about remote places so that when someone searches the duniya for safer water, this page is discoverable.
"""
    )

    st.markdown("---")
    st.subheader("Join the mission")
    st.markdown(
        """
Driven by purpose, curiosity, and a passion to serve the duniya (world), we aim to place HydroPulse Sentinel kits near remote water sources, schools, and health centers. Every grant of time, technology, or attention expands our remote monitoring grid and helps those communities see clearer water quality data.
"""
    )

    st.subheader("Field Trials & Storytelling")
    st.markdown(
        """
The project has tracked remote places from Gurugram’s arid outskirts to rain-fed uplands. Field logs flagged:  
- Site 1: Safe yet fluctuating pH after monsoon floods.  
- Site 2: Acidic groundwater needing buffering.  
- Site 3: High dissolved solids after nearby industrial discharge.
        """
    )

    st.markdown("---")
    st.subheader("Gallery: HydroPulse Sentinel in Action 📸")
    images = [
        "Picture 1.jpg",
        "UN016418.jpg.jpg",
        "Picture 3.jpg",
        "Harshit Sanghi Poster Template 36x48_page-0001.jpg",
    ]
    captions = [
        "Every measured pour becomes an actionable signal for clean drinking water monitoring.",
        "Remote communities are watching their taps in real time with HydroPulse Sentinel sensors.",
        "Water quality is data-backed, not just intuition—turbidity, pH, and TDS are tracked continuously.",
        "Graphs that once worried now narrate confidence for water safety researchers."
    ]
    cols = st.columns(4)
    for idx, col in enumerate(cols):
        col.image(images[idx], caption=captions[idx], use_column_width=True)

if __name__ == "__main__":
    app()
