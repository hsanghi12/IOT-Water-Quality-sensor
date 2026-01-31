import streamlit as st

def app():
    # Intro paragraph with no italics
    st.markdown(
        """
        <span style="font-size:1.2em;font-weight:bold;">Harshit Sanghi</span>, 
        a 16-year-old student from Step by Step School, Noida, isn't just tinkering with tech—he is building **HydroPulse Sentinel** to deliver safer water globally.<br><br>
        Inspired by unsafe water in remote parts of India, he developed this IoT-powered system that monitors water quality live and sends alerts before families drink. Driven by purpose, curiosity, and (passion to serve the duniya), Harshit proves that innovation has no age.
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    # Machine Learning Model Info (no italics, bold model names)
    st.markdown("""
    <span style="font-weight:bold;">About Machine Learning Models in Water Quality Prediction:</span><br>
    In the world of machine learning, several models are commonly used for prediction tasks:
    <ul>
      <li><b>Logistic Regression</b>: Great for simple binary classification problems.</li>
      <li><b>Random Forests</b>: Ensemble models that combine many decision trees for robust predictions.</li>
      <li><b>Support Vector Machines (SVM)</b>: Effective for high-dimensional data and classification.</li>
      <li><b>Neural Networks</b>: Powerful for complex, non-linear relationships in data.</li>
      <li><b>CatBoost</b>: A cutting-edge gradient boosting algorithm, excellent for handling categorical features and complex patterns.</li>
    </ul>
    <br>
    While many systems rely on basic models like logistic regression or random forests, 
    HydroPulse Sentinel harnesses the power of <b>CatBoost</b>, a state-of-the-art algorithm built for performance and accuracy. 
    The model is tested with stratified samples from borewell, river, and municipal tap sources so it generalizes across **different water types**. 
    This ensures faster insights, smarter predictions, and truly actionable alerts.
    <br><br>
    """, unsafe_allow_html=True)

    # Image
    image1 = "ab.webp"  # Replace with your image path or URL
    st.image(image1, caption="“Like water through pipes, ML flows through data to power AI and Deep Learning.” ", width=350)

    st.markdown("---")
    st.subheader("Developer story & research partners")
    st.markdown(
        """
Harshit is a coder, designer, and field observer. He coded the CatBoost pipeline, documented sensor calibration routines, and continues field visits to remote places to validate the data. HydroPulse Sentinel partners with research organizations such as the **Central Water Commission**, **WaterAid India**, **World Resources Institute (WRI)**, and **the Delhi Jal Board Academy** to co-create intervention kits and publish actionable datasets.
"""
    )

    st.markdown("---")
    st.subheader("Compliance & Credentials")
    st.markdown(
        """
This initiative maintains a **Delhi Jal Board Certificate** for potable water testing and follows WHO guidelines on drinking water quality. The certificate ensures calibration accuracy and proper field sampling documentation.
"""
    )

    st.markdown("---")
    st.image(
        "drinking.png",
        caption="A person drinking clean water at home — the HydroPulse Sentinel promise.",
        use_column_width=True,
    )


    # Typing animation with aqua blue preserved
    st.markdown(
        """
        <style>
        @keyframes typing {
            0% { width: 0 }
            80% { width: 27ch }
            90% { width: 27ch }
            100% { width: 0 }
        }
        @keyframes blink {
            50% { border-color: transparent }
        }
        .typing-demo {
            width: 27ch;
            animation: typing 12s steps(27) infinite, blink .5s step-end infinite alternate;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid #00c6ff;
            font-size: 2.5em;
            font-weight: normal;
            color: #00c6ff;
            letter-spacing:2px;
            margin: 0 auto;
            display: block;
            text-align: center;
        }
        </style>
        <div style="text-align:center; margin-top:30px; width:100%;">
            <span class="typing-demo">EVERY DROP HOLDS A HOPE</span>
        </div>
        """,
        unsafe_allow_html=True
    )
