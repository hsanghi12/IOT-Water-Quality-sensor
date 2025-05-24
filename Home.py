import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AquaSentinel",
    page_icon="💧",
    layout="wide",
)

# Main app function
def app():
    # Title and header
    st.title("Where Clean Water Was a Dream, AquaSentinel Makes It Reality 💧")

    # Introductory text
    intro = """
Imagine waking up every morning unsure if the water in your glass could harm your family. Not because you live in a desert, but because the very groundwater beneath your village carries hidden threats—high TDS, dangerous acidity, and unseen pollutants.

This is not imagination. This is the daily truth for thousands of families in rural Gurugram, Haryana—and across many parts of India.
"""
    st.markdown(intro)

    # Highlight section
    st.markdown("---")
    st.subheader("AquaSentinel: Your Silent Guardian")
    st.markdown(
        """
Not just another fancy gadget, **यह एक शांत रक्षक है**—a humble, powerful device built with love, tech, and a lot of heart. It's a smart, AI-powered IoT-based system that monitors water quality in real time using sensors that detect **pH**, **turbidity**, **dissolved oxygen**, **conductivity**, and **TDS**. Think of it as a digital watchdog for your drinking water, alerting you before danger knocks.

**Key features:**
- **Real-time monitoring**: Instant data upload via ThingSpeak.
- **Remote access**: View readings on any smartphone.
- **Early warnings**: Alerts before a crisis.
- **Affordable & scalable**: Designed for every village.
"""
    )

    # Technology stack
    st.subheader("How It Works")
    tech = {
        "Microcontroller": "NodeMCU",
        "Connectivity": "Wi-Fi / ThingSpeak",
        "Sensors": ["pH", "Turbidity", "Dissolved Oxygen", "Conductivity", "TDS"],
        "Power": "Solar / Battery Backup"
    }

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Hardware Components**")
        for k, v in tech.items():
            if isinstance(v, list):
                st.write(f"- **{k}**: {', '.join(v)}")
            else:
                st.write(f"- **{k}**: {v}")

    with col2:
        st.write("**Field Trial Highlights**")
        st.write("- Site 1: Borderline safe water.")
        st.write("- Site 2: Acid levels at hazardous limits.")
        st.write("- Site 3: High dissolved solids detected.")

    # Call to action
    st.markdown("---")
    st.subheader("Join the Mission")
    st.markdown(
        """
Driven by *purpose*, *curiosity*, and **दिल से देश के लिए कुछ करने का जुनून**, we dream of placing AquaSentinel in every village: schools, health centers, and anganwadi. With just a bit of funding and a lot of **josh**, we can turn this dream into reality.

> **क्या आप हिस्सा बनना चाहें گے इस मिशन का?**
"""
    )

    # Image gallery at the bottom
    st.markdown("---")
    st.subheader("Gallery: AquaSentinel in Action 📸")
    # Replace these GitHub raw URLs with your own image links
    images = [
        "Picture 1.jpg",
        "UN016418.jpg.jpg",
        "Picture 3.jpg",
        "Harshit Sanghi Poster Template 36x48_page-0001.jpg",
    ]
    captions = [
        "Field deployment in rural Haryana",
        "Real-time readings on smartphone",
        "Sensor array hard at work",
        "Community engagement workshop",
    ]

    cols = st.columns(4)
    for idx, col in enumerate(cols):
        col.image(images[idx], caption=captions[idx], use_column_width=True)

if __name__ == "__main__":
    app()




