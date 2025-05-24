import streamlit as st
def app():
   st.markdown("""***Harshit Sanghi***, a *16-year-old* student from *Step by Step School, Noida*, isn't just tinkering with tech—he's using it to **save lives**.  

Moved by the unsafe water conditions in rural India, he developed **AquaSentinel**, an *IoT-powered* system that monitors water quality in real time.  

Driven by *purpose*, *curiosity*, and **दिल से देश के लिए कुछ करने का जुनून**, Harshit is proving that **innovation has no age**.
""")
   st.write("")
   st.write("")
   st.write("")
   st.markdown("""
   <b>About Machine Learning Models in Water Quality Prediction:</b><br>
   In the world of machine learning, several models are commonly used for prediction tasks:
   <ul>
     <li><b>Logistic Regression</b>: Great for simple binary classification problems.</li>
     <li><b>Random Forests</b>: Ensemble models that combine many decision trees for robust predictions.</li>
     <li><b>Support Vector Machines (SVM)</b>: Effective for high-dimensional data and classification.</li>
     <li><b>Neural Networks</b>: Powerful for complex, non-linear relationships in data.</li>
     <li><b>CatBoost</b>: A cutting-edge gradient boosting algorithm, excellent for handling categorical features and complex patterns.</li>
   </ul>
   <br>
   While many systems rely on basic models like logistic regression or random forests, <b>AquaSentinel harnesses the power of <span style='color:#1976d2;'>CatBoost</span></b>, a state-of-the-art algorithm built for performance and accuracy. This model excels at handling complex data patterns like those in water quality parameters—pH, turbidity, TDS, and conductivity. The result? <b>Faster insights, smarter predictions, and truly actionable alerts.</b>
   <br><br>
   Learn more at: <a href="https://www.aquasentinel.in" target="_blank" style="color:#0072ff;font-weight:bold;">AquaSentinel Website</a>
   """, unsafe_allow_html=True)

   # Images in a row
    # Replace with your image path or URL  # Replace with your image path or URL
   image1 = "ab.webp"  # Replace with your image path or URL
   st.image(image1, caption="AquaSentinel in action", use_column_width=True)

  

   # Water is Life with typing effect
   st.markdown(
       """
       <style>
       .typing-demo {
           width: 15ch;
           animation: typing 2.5s steps(15), blink .5s step-end infinite alternate;
           white-space: nowrap;
           overflow: hidden;
           border-right: 3px solid #00c6ff;
           font-size: 2em;
           font-weight: bold;
           background: linear-gradient(90deg, #00c6ff, #43e97b);
           -webkit-background-clip: text;
           -webkit-text-fill-color: transparent;
           text-shadow: 2px 2px 8px #b3e0ff;
           letter-spacing:2px;
           margin: 0 auto;
           display: block;
           text-align: center;
       }
       @keyframes typing {
           from { width: 0 }
           to { width: 15ch }
       }
       @keyframes blink {
           50% { border-color: transparent }
       }
       </style>
       <div style="text-align:center; margin-top:30px;">
           <span class="typing-demo">WATER IS LIFE</span>
       </div>
       """,
       unsafe_allow_html=True
   )

   # Enhanced introduction with bold and effects
   st.markdown(
       """
       <style>
       .intro-name {
           font-size: 2em;
           font-weight: 900;
           color: #0072ff;
           letter-spacing: 1px;
           text-shadow: 1px 1px 8px #b3e0ff;
           display: inline-block;
       }
       .intro-age {
           color: #ff6f61;
           font-weight: bold;
           font-size: 1.1em;
       }
       .intro-school {
           color: #388e3c;
           font-style: italic;
           font-weight: bold;
       }
       .intro-key {
           color: #ffb300;
           font-weight: bold;
           font-size: 1.1em;
       }
       .intro-hindi {
           color: #e53935;
           font-weight: bold;
           font-size: 1.1em;
       }
       </style>
       <span class="intro-name">Harshit Sanghi</span>, <span class="intro-age">a 16-year-old</span> student from <span class="intro-school">Step by Step School, Noida</span>, isn't just tinkering with tech—he's using it to <span class="intro-key">save lives</span>.<br><br>
       Moved by the unsafe water conditions in rural India, he developed <span class="intro-key">AquaSentinel</span>, an <span class="intro-key">IoT-powered</span> system that monitors water quality in real time.<br><br>
       Driven by <span class="intro-key">purpose</span>, <span class="intro-key">curiosity</span>, and <span class="intro-hindi">दिल से देश के लिए कुछ करने का जुनून</span>, Harshit is proving that <span class="intro-key">innovation has no age</span>.
       """,
       unsafe_allow_html=True
   )
   st.write("")
   st.write("")
   st.write("")
   st.markdown("""
   <b>About Machine Learning Models in Water Quality Prediction:</b><br>
   In the world of machine learning, several models are commonly used for prediction tasks:
   <ul>
     <li><b>Logistic Regression</b>: Great for simple binary classification problems.</li>
     <li><b>Random Forests</b>: Ensemble models that combine many decision trees for robust predictions.</li>
     <li><b>Support Vector Machines (SVM)</b>: Effective for high-dimensional data and classification.</li>
     <li><b>Neural Networks</b>: Powerful for complex, non-linear relationships in data.</li>
     <li><b>CatBoost</b>: A cutting-edge gradient boosting algorithm, excellent for handling categorical features and complex patterns.</li>
   </ul>
   <br>
   While many systems rely on basic models like logistic regression or random forests, <b>AquaSentinel harnesses the power of <span style='color:#1976d2;'>CatBoost</span></b>, a state-of-the-art algorithm built for performance and accuracy. This model excels at handling complex data patterns like those in water quality parameters—pH, turbidity, TDS, and conductivity. The result? <b>Faster insights, smarter predictions, and truly actionable alerts.</b>
   <br><br>
   Learn more at: <a href="https://www.aquasentinel.in" target="_blank" style="color:#0072ff;font-weight:bold;">AquaSentinel Website</a>
   """, unsafe_allow_html=True)

   # Smaller image
   image1 = "ab.webp"  # Replace with your image path or URL
   st.markdown(
       f'<div style="text-align:center;"><img src="{image1}" width="300" style="border-radius:12px;box-shadow:0 4px 16px #b3e0ff;" alt="AquaSentinel in action"/><div style="font-size:1em;color:#0072ff;font-weight:bold;">AquaSentinel in action</div></div>',
       unsafe_allow_html=True
   )

   # Water is Life with continuous typing effect
   st.markdown(
       """
       <style>
       @keyframes typing {
           0% { width: 0 }
           70% { width: 15ch }
           80% { width: 15ch }
           90% { width: 0 }
           100% { width: 0 }
       }
       @keyframes blink {
           50% { border-color: transparent }
       }
       .typing-demo {
           width: 15ch;
           animation: typing 4s steps(15) infinite, blink .5s step-end infinite alternate;
           white-space: nowrap;
           overflow: hidden;
           border-right: 3px solid #00c6ff;
           font-size: 2em;
           font-weight: bold;
           background: linear-gradient(90deg, #00c6ff, #43e97b);
           -webkit-background-clip: text;
           -webkit-text-fill-color: transparent;
           text-shadow: 2px 2px 8px #b3e0ff;
           letter-spacing:2px;
           margin: 0 auto;
           display: block;
           text-align: center;
       }
       </style>
       <div style="text-align:center; margin-top:30px;">
           <span class="typing-demo">WATER IS LIFE</span>
       </div>
       """,
       unsafe_allow_html=True
   )
