import streamlit as st
def app():
   # Simple, bold headlines and italic supporting text
   st.markdown(
       """
       <span style="font-size:1.2em;font-weight:bold;color:#111;">Harshit Sanghi</span>, <span style="font-style:italic;color:#111;">a 16-year-old student from Step by Step School, Noida, isn't just tinkering with tech—he's using it to save lives.<br><br>
       Moved by the unsafe water conditions in rural India, he developed <b>AquaSentinel</b>, an IoT-powered system that monitors water quality in real time.<br><br>
       Driven by <span style='font-style:italic;'>purpose</span>, <span style='font-style:italic;'>curiosity</span>, and <span style='font-style:italic;'>दिल से देश के लिए कुछ करने का जुनून</span>, Harshit is proving that <span style='font-style:italic;'>innovation has no age</span>.</span>
       """,
       unsafe_allow_html=True
   )
   st.write("")
   st.write("")
   st.write("")
   st.markdown("""
   <span style="font-weight:bold;color:#111;">About Machine Learning Models in Water Quality Prediction:</span><br>
   <span style="font-style:italic;color:#111;">
   In the world of machine learning, several models are commonly used for prediction tasks:
   <ul>
     <li><i>Logistic Regression</i>: Great for simple binary classification problems.</li>
     <li><i>Random Forests</i>: Ensemble models that combine many decision trees for robust predictions.</li>
     <li><i>Support Vector Machines (SVM)</i>: Effective for high-dimensional data and classification.</li>
     <li><i>Neural Networks</i>: Powerful for complex, non-linear relationships in data.</li>
     <li><i>CatBoost</i>: A cutting-edge gradient boosting algorithm, excellent for handling categorical features and complex patterns.</li>
   </ul>
   <br>
   While many systems rely on basic models like logistic regression or random forests, <i>AquaSentinel harnesses the power of CatBoost</i>, a state-of-the-art algorithm built for performance and accuracy. This model excels at handling complex data patterns like those in water quality parameters—pH, turbidity, TDS, and conductivity. The result? <i>Faster insights, smarter predictions, and truly actionable alerts.</i>
   <br><br>
   Learn more at: <a href=\"https://www.aquasentinel.in\" target=\"_blank\" style=\"font-weight:bold;color:#111;\">AquaSentinel Website</a>
   </span>
   """, unsafe_allow_html=True)

   # Bigger image, use st.image for compatibility
   image1 = "ab.webp"  # Replace with your image path or URL
   st.image(image1, caption="AquaSentinel in action", width=350)

   # Typing effect: EVERY DROP HOLDS A HOPE (aqua blue, types out fully, larger and slower)
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
           font-style: italic;
           color: #00c6ff;
           background: none;
           -webkit-background-clip: unset;
           -webkit-text-fill-color: unset;
           text-shadow: none;
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
