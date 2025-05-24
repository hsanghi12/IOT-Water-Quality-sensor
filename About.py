import streamlit as st

def app():
    # Theme-friendly intro paragraph
    st.markdown(
        """
        <span style="font-size:1.2em;font-weight:bold;">Harshit Sanghi</span>, 
        <span style="font-style:italic;">
        a 16-year-old student from Step by Step School, Noida, isn't just tinkering with tech—he's using it to save lives.<br><br>
        Moved by the unsafe water conditions in rural India, he developed <b>AquaSentinel</b>, an IoT-powered system that monitors water quality in real time.<br><br>
        Driven by <span style='font-style:italic;'>purpose</span>, <span style='font-style:italic;'>curiosity</span>, and 
        <span style='font-style:italic;'>दिल से देश के लिए कुछ करने का जुनून</span>, 
        Harshit is proving that <span style='font-style:italic;'>innovation has no age</span>.
        </span>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    # Machine Learning Model Info (with bold headings for each model)
    st.markdown("""
    <span style="font-weight:bold;">About Machine Learning Models in Water Quality Prediction:</span><br>
    <span style="font-style:italic;">
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
    <i>AquaSentinel harnesses the power of <b>CatBoost</b></i>, a state-of-the-art algorithm built for performance and accuracy. 
    This model excels at handling complex data patterns like those in water quality parameters—pH, turbidity, TDS, and conductivity. 
    The result? <i>Faster insights, smarter predictions, and truly actionable alerts.</i>
    <br><br>
    </span>
    """, unsafe_allow_html=True)

    # Image (use your own local path or URL)
    image1 = "ab.webp"  # Update with correct path if needed
    st.image(image1, caption="“Like water through pipes, ML flows through data to power AI and Deep Learning.” ", width=350)

    # Typing animation for theme-safe text
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
            border-right: 3px solid var(--primary-color);
            font-size: 2.5em;
            font-weight: normal;
            font-style: italic;
            color: var(--primary-color);
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
