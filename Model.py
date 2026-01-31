import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from catboost import CatBoostClassifier


def load_model():
    model = CatBoostClassifier()
    model.load_model("catboost_model.cbm")
    return model


def gauge_chart(title, value, min_val, max_val, unit):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": f"{title} ({unit})", "font": {"size": 18}},
            gauge={
                "axis": {"range": [min_val, max_val], "tickwidth": 1, "tickcolor": "#333"},
                "bar": {"color": "#2980b9", "thickness": 0.35},
                "steps": [
                    {"range": [min_val, (max_val - min_val) * 0.4 + min_val], "color": "#c0392b"},
                    {"range": [(max_val - min_val) * 0.4 + min_val, (max_val - min_val) * 0.75 + min_val], "color": "#f1c40f"},
                    {"range": [(max_val - min_val) * 0.75 + min_val, max_val], "color": "#27ae60"},
                ],
                "threshold": {
                    "line": {"color": "#8e44ad", "width": 4},
                    "thickness": 0.75,
                    "value": value,
                },
            },
            number={"font": {"size": 24}},
        )
    )
    fig.update_layout(
        margin={"t": 40, "b": 0, "l": 0, "r": 0},
        height=260,
        width=320,
        paper_bgcolor="lightgreen",
        font={"color": "#1a1a1a"},
    )
    return fig


def app():
    st.title("💧 Water Potability Prediction Model")
    st.write("Check potability of water by entering values below; the gauges mirror the dashboard meters so you can visualize each parameter live.")

    detection_table = pd.DataFrame(
        [
            {"Parameter": "pH", "Range": "0.0 – 14.0", "Detection Limit": "0.01", "Unit": "pH"},
            {"Parameter": "Turbidity", "Range": "0 – 1000", "Detection Limit": "0.1", "Unit": "NTU"},
            {"Parameter": "TDS", "Range": "0 – 2000", "Detection Limit": "1", "Unit": "ppm"},
            {"Parameter": "Conductivity", "Range": "0 – 2000", "Detection Limit": "0.5", "Unit": "μS/cm"},
        ]
    )
    st.subheader("Detection Limits & Safe Ranges")
    st.table(detection_table)

    gauge_section = st.container()

    ph_col, turb_col = st.columns(2)
    solids_col, cond_col = st.columns(2)
    ph = ph_col.number_input("pH", min_value=0.0, max_value=14.0, step=0.1, value=7.0)
    turbidity = turb_col.number_input("Turbidity (NTU)", min_value=0.0, value=5.0)
    solids = solids_col.number_input("Solids (ppm)", min_value=0.0, value=200.0)
    conductivity = cond_col.number_input("Conductivity (μS/cm)", min_value=0.0, value=250.0)

    st.markdown(
        """
**Why these parameters matter:**  
- pH: Below 6.5 is acidic, above 8.5 is alkaline—both extremes damage pipes or signal contamination.  
- Turbidity: Cloudy water suggests suspended particles, microbes, or pollution, so filtration is advised.  
- Solids/conductivity: Values above 1500 ppm/μS may indicate salinity or industrial discharge requiring treatment.
"""
    )

    with gauge_section:
        st.subheader("Live meter dashboard")
        gauge_columns = st.columns(2)
        parameter_values = [
            ("pH", ph, 0, 14, "pH"),
            ("Turbidity", turbidity, 0, 1000, "NTU"),
            ("TDS", solids, 0, 2000, "ppm"),
            ("Conductivity", conductivity, 0, 2000, "μS/cm"),
        ]
        for idx, (name, val, min_val, max_val, unit) in enumerate(parameter_values):
            col = gauge_columns[idx % 2]
            fig = gauge_chart(name, val, min_val, max_val, unit)
            col.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
**pH insights:** Water with pH below 6.5 usually has acid rain influence, dissolved CO2, or industrial runoff. pH above 8.5 often signals mineral-rich sources, alkaline soils, or treatment chemicals.
"""
    )
    if ph < 6.5:
        st.info("Lower pH indicates acidity from dissolved carbon dioxide, organic acids, or potential pollution; buffering may help.")
    elif ph > 8.5:
        st.info("Higher pH often comes from mineral-rich rocks (calcium/magnesium) or added treatment chemicals like lime.")
    else:
        st.success("pH is within the neutral range; it likely reflects balanced natural groundwater or properly treated supply.")

    model = load_model()
    features = np.array([[ph, turbidity, solids, conductivity]])
    prediction = model.predict(features)
    st.write("Values used for prediction:", dict(pH=ph, Turbidity=round(turbidity, 2), Solids=round(solids, 2), Conductivity=round(conductivity, 2)))
    if prediction[0] == 1:
        st.success("✅ The water is **potable**.")
    else:
        st.error("❌ The water is **not potable**.")
    if ph < 6.5 or ph > 8.5:
        st.warning("pH is outside the recommended drinking range (6.5-8.5). Consider buffering.")
    if turbidity > 5:
        st.info("Turbidity is above 5 NTU: clarify with filtration before relying on this source.")
    if conductivity > 1500:
        st.warning("Conductivity/TDS is high; stronger treatment such as reverse osmosis may be needed.")
