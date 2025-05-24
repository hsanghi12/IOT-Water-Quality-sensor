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
   image1 = "path/to/your/image1.jpg"  # Replace with your image path or URL
   image2 = "path/to/your/image2.jpg"  # Replace with your image path or URL
   col1, col2 = st.columns(2)
   with col1:
       st.image(image1, caption="AquaSentinel in action", use_column_width=True)
   with col2:
       st.image(image2, caption="Clean water for all", use_column_width=True)

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
