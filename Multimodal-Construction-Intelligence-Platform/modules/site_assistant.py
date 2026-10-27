"""
Multimodal Construction Intelligence Platform - Tab 4: Daily Site Assistant & Weather-Aware Advisory (Epic 5)
Weather Environmental Hazard Matrix & Multi-Turn Civil Engineering AI Assistant
"""

import streamlit as st
from datetime import datetime
from typing import Dict, Any, List

from modules.gemini_service import GeminiService


WEATHER_ADVISORIES = {
    "High Wind (>40 km/h)": {
        "badge_color": "#EF4444",
        "icon": "💨",
        "status": "CRITICAL WIND ALERT - HIGH ELEVATION PROTOCOL ACTIVE",
        "crane_protocol": "SUSPEND ALL TOWER CRANE HOISTING IMMEDIATELY. Release slew brake to permit free weather-vaning of the jib (OSHA 1926.1412 / IS 456). Ground all suspended skips.",
        "scaffolding_protocol": "Evacuate personnel from scaffolding tiers above Level 4. Inspect tie-backs, anchor wall anchors, and remove debris or formwork panels prone to becoming wind-borne projectiles.",
        "curing_concreting": "Halt large horizontal flatwork concrete pours (slabs) unless protected by windbreaks. High evaporation rates induce severe early plastic shrinkage cracking (>1.0 kg/m²/hr evaporation rate).",
        "electrical_safety": "Secure high-voltage temporary distribution cables; inspect perimeter floodlighting poles and temporary mast fixtures."
    },
    "Heavy Rain / Monsoon (>30 mm/h)": {
        "badge_color": "#38BDF8",
        "icon": "🌧️",
        "status": "SEVERE MONSOON & DEWATERING PROTOCOL ACTIVE",
        "crane_protocol": "Operate cranes only with non-slip rigging. Exercise extreme caution regarding decreased ground bearing pressure under outriggers; check timber/steel spreader pad integrity.",
        "scaffolding_protocol": "Slip and fall hazard. No work on wet staging without fall-arrest harnesses. Inspect base sole plates on muddy or saturated subgrade for differential settlement.",
        "curing_concreting": "STOP ALL ACTIVE CONCRETE POURS. Fresh unhardened concrete exposed to heavy rain suffers severe surface water-cement ratio dilution and loss of strength. Cover active decks with waterproof tarpaulins.",
        "electrical_safety": "Turn off power to flooded zones. Ensure 100% of portable tools operate via Ground Fault Circuit Interrupters (GFCI) or 30mA Residual Current Circuit Breakers (RCCB - IS 732)."
    },
    "Extreme Heatwave (>42°C / 108°F)": {
        "badge_color": "#F97316",
        "icon": "☀️",
        "status": "THERMAL STRESS & HOT WEATHER CONCRETING PROTOCOL ACTIVE",
        "crane_protocol": "Operator cabin air conditioning check mandatory. Restrict long crane shifts; enforce 15-minute cool-down breaks every 2 hours to avoid operator fatigue.",
        "scaffolding_protocol": "Metal scaffolding pipes reach >55°C. Cut-resistant thermally insulated leather gloves mandatory for all staging crews. Provide shaded resting stations.",
        "curing_concreting": "MANDATORY HOT-WEATHER CONCRETING (IS 456 Cl. 13.5 & ACI 305R): Batch concrete with chilled water or shaved ice to maintain fresh temperature <32°C. Extend wet burlap curing to minimum 14 days.",
        "electrical_safety": "Inspect generator and transformer enclosures for thermal overheating; ensure continuous forced ventilation around mobile power packs."
    },
    "Dense Fog & Low Visibility (<100m)": {
        "badge_color": "#A855F7",
        "icon": "🌫️",
        "status": "REDUCED VISIBILITY BLIND-LIFT RESTRICTIONS ACTIVE",
        "crane_protocol": "MANDATORY BLIND-LIFT PROCEDURES: Crane hoist moves permitted ONLY with dedicated two-way radio signalmen equipped with lighted signal wands (OSHA 1926.1419).",
        "scaffolding_protocol": "High-visibility reflective Class 3 retroreflective vests mandatory for all deck workers. Activate perimeter warning strobes.",
        "curing_concreting": "High ambient relative humidity retards initial concrete setting time. Delay power floating and shuttering strike-off until needle penetration resistance confirms final set.",
        "electrical_safety": "Ensure all site access roads, vehicle paths, and stair towers maintain minimum 50 lux illumination."
    },
    "Normal / Favorable (24°C, Mild Breeze)": {
        "badge_color": "#10B981",
        "icon": "⛅",
        "status": "OPTIMAL STRUCTURAL EXECUTION CONDITIONS",
        "crane_protocol": "Full lifting operations authorized under standard daily crane log inspection and pre-lift checks.",
        "scaffolding_protocol": "Standard OSHA 1926 fall protection; 100% tie-off above 1.8 meters.",
        "curing_concreting": "Standard moist curing conforming to IS 456:2000 Cl. 13.5 (minimum 7 days for OPC, 10 days for mineral-admixture blended cement).",
        "electrical_safety": "Routine daily electrical panel maintenance and earth pit resistance checks."
    }
}


def render_site_assistant_tab(gemini_service: GeminiService):
    """Renders the Daily Site Assistant & Weather-Aware Advisory interface."""
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #F59E0B; font-weight: 700; display: flex; align-items: center; gap: 10px;">
                <span>🤖</span> Daily Site Assistant & Weather Advisory (Epic 5)
            </h2>
            <p style="color: #94A3B8; margin-top: 4px; font-size: 0.95rem;">
                Dynamic environmental hazard warnings calibrated to real-time meteorological conditions paired with a 
                <strong>Multi-Turn Civil Engineering Intelligence Chatbot</strong> powered by IS codes & OSHA standards.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Weather Selector & Dynamic Advisory Panel
    st.markdown("""
        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px; margin-bottom: 20px;">
            <h4 style="margin: 0 0 12px 0; color: #F8FAFC; font-size: 1rem;">🌦️ Environmental Telemetry & Weather Condition Selector</h4>
    """, unsafe_allow_html=True)

    col_w1, col_w2 = st.columns([1, 2])
    with col_w1:
        weather_condition = st.selectbox(
            "Active Site Weather Condition",
            options=list(WEATHER_ADVISORIES.keys()),
            index=0,  # High wind default demonstrates high-impact dynamic safety rules
            key="selected_weather_condition"
        )
    with col_w2:
        st.caption("Selecting weather condition automatically reconfigures crane load cutoffs, concrete curing protocols (IS 456:2000 Cl. 13.5), and safety mitigation triggers.")

    advisory = WEATHER_ADVISORIES[weather_condition]
    badge_c = advisory["badge_color"]

    st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid {badge_c}; border-radius: 10px; padding: 14px 18px; margin-top: 12px;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                <span style="font-size: 1.5rem;">{advisory['icon']}</span>
                <span style="background: {badge_c}; color: #0F172A; font-weight: 800; font-size: 0.75rem; padding: 3px 8px; border-radius: 4px;">
                    {advisory['status']}
                </span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px; font-size: 0.85rem;">
                <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 6px; border-left: 3px solid #F59E0B;">
                    <strong style="color: #F59E0B;">🏗️ Tower Crane Protocol:</strong>
                    <p style="margin: 4px 0 0 0; color: #CBD5E1;">{advisory['crane_protocol']}</p>
                </div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 6px; border-left: 3px solid #10B981;">
                    <strong style="color: #10B981;">🧪 Concrete Curing Protocol:</strong>
                    <p style="margin: 4px 0 0 0; color: #CBD5E1;">{advisory['curing_concreting']}</p>
                </div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 6px; border-left: 3px solid #38BDF8;">
                    <strong style="color: #38BDF8;">🪜 Scaffolding & Edge Safety:</strong>
                    <p style="margin: 4px 0 0 0; color: #CBD5E1;">{advisory['scaffolding_protocol']}</p>
                </div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 6px; border-left: 3px solid #EF4444;">
                    <strong style="color: #EF4444;">⚡ Electrical & Dewatering:</strong>
                    <p style="margin: 4px 0 0 0; color: #CBD5E1;">{advisory['electrical_safety']}</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Multi-Turn Construction Engineering Chatbot
    st.markdown("""
        <div style="margin: 24px 0 12px 0; display: flex; justify-content: space-between; align-items: center;">
            <h3 style="margin: 0; color: #F8FAFC; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                <span>💬</span> Construction Engineering AI Resident Assistant
            </h3>
        </div>
    """, unsafe_allow_html=True)

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = [
            {
                "role": "model",
                "content": "👋 Greetings! I am your Multimodal Construction Intelligence Assistant. I am specialized in Bureau of Indian Standards (IS 456, IS 13920, IS 1893), OSHA 1926 site safety protocols, and daily site logistics. How can I assist your site operations today?"
            }
        ]

    # Quick Suggestion Chips
    st.markdown("<p style='font-size: 0.8rem; color: #94A3B8; margin-bottom: 6px;'>💡 Quick Engineering Queries:</p>", unsafe_allow_html=True)
    q_col1, q_col2, q_col3 = st.columns(3)
    preset_query = None

    with q_col1:
        if st.button("🧪 Minimum Curing for OPC vs PPC under IS 456?", use_container_width=True):
            preset_query = "What is the minimum curing period for OPC vs PPC under IS 456:2000 Clause 13.5 in current weather?"
    with q_col2:
        if st.button("🏗️ Tower Crane Wind Cutoff Rules (OSHA)", use_container_width=True):
            preset_query = "Explain tower crane shutdown and weather-vaning wind limits under OSHA 1926.1412."
    with q_col3:
        if st.button("📐 Estimate Steel Tonnage for 80,000 sq ft RCC Tower", use_container_width=True):
            preset_query = "How do I calculate steel rebar tonnage and cement consumption for an 80,000 sq ft residential G+20 tower?"

    # Chat Container
    chat_container = st.container()

    with chat_container:
        for msg in st.session_state["chat_history"]:
            with st.chat_message(msg["role"], avatar="👷" if msg["role"] == "user" else "🏗️"):
                st.markdown(msg["content"])

    # Chat Input
    user_input = st.chat_input("Ask about IS codes, OSHA rules, mix design, shuttering strike-off, or weather safety...")

    active_prompt = preset_query if preset_query else user_input

    if active_prompt:
        # Append User Message
        st.session_state["chat_history"].append({"role": "user", "content": active_prompt})

        with st.chat_message("user", avatar="👷"):
            st.markdown(active_prompt)

        with st.chat_message("model", avatar="🏗️"):
            with st.spinner("Formulating civil engineering guidance..."):
                response_text, is_live_chat = gemini_service.chat_construction_assistant(
                    prompt=active_prompt,
                    history=st.session_state["chat_history"][:-1],
                    weather_condition=weather_condition
                )
                st.markdown(response_text)

        # Append Model Message
        st.session_state["chat_history"].append({"role": "model", "content": response_text})

    # Clear Chat Button
    c_btn1, c_btn2 = st.columns([1, 4])
    with c_btn1:
        if st.button("🗑️ Reset Chat History", key="btn_clear_chat", use_container_width=True):
            st.session_state["chat_history"] = [
                {
                    "role": "model",
                    "content": "👋 Greetings! I am your Multimodal Construction Intelligence Assistant. I am specialized in Bureau of Indian Standards (IS 456, IS 13920, IS 1893), OSHA 1926 site safety protocols, and daily site logistics. How can I assist your site operations today?"
                }
            ]
            st.rerun()
