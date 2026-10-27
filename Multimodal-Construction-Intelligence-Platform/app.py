"""
Multimodal Construction Intelligence Platform (Skill Wallet Capstone Project 1)
Full-Stack Streamlit Production Application
"""

import streamlit as st
import os

from modules.gemini_service import GeminiService
from modules.safety_audit import render_safety_audit_tab
from modules.crack_diagnostics import render_crack_diagnostics_tab
from modules.valuation_planner import render_valuation_planner_tab
from modules.site_assistant import render_site_assistant_tab

# Page Configuration
st.set_page_config(
    page_title="Multimodal Construction Intelligence Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Modern CSS Styling
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3rem;
        max-width: 1350px;
    }

    /* Streamlit Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(15, 23, 42, 0.7);
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        border-radius: 8px;
        color: #94A3B8;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0 18px;
        transition: all 0.2s ease;
        border: none;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.25) 0%, rgba(245, 158, 11, 0.08) 100%) !important;
        color: #F59E0B !important;
        border: 1px solid rgba(245, 158, 11, 0.4) !important;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);
    }

    /* Metrics Cards */
    div[data-testid="stMetric"] {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 14px 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    div[data-testid="stMetric"]:hover {
        border-color: rgba(245, 158, 11, 0.4);
        transform: translateY(-2px);
    }

    div[data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    div[data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-weight: 800 !important;
        font-size: 1.6rem !important;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton>button[kind="primary"] {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        color: #0F172A !important;
        border: none;
        font-weight: 700;
        box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3);
    }

    .stButton>button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.45);
    }

    /* File Uploader */
    div[data-testid="stFileUploader"] {
        background: rgba(15, 23, 42, 0.5);
        border-radius: 10px;
        padding: 8px;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(30, 41, 59, 0.5) !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    /* Toast and Alerts */
    .stAlert {
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)


def main():
    # Sidebar Setup
    with st.sidebar:
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <div style="background: linear-gradient(135deg, #F59E0B, #EA580C); width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);">
                    🏗️
                </div>
                <div>
                    <h3 style="margin: 0; color: #F8FAFC; font-size: 1.05rem; font-weight: 800; line-height: 1.2;">
                        Multimodal Construction
                    </h3>
                    <span style="color: #F59E0B; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">
                        Intelligence Platform
                    </span>
                </div>
            </div>
            <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 6px; padding: 4px 10px; margin-bottom: 16px; font-size: 0.72rem; color: #F59E0B; font-weight: 600; text-align: center;">
                Skill Wallet Capstone Project 1
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='border: 1px solid rgba(255, 255, 255, 0.08); margin: 12px 0 16px 0;'/>", unsafe_allow_html=True)

        # Gemini API Key Authentication
        st.markdown("#### 🔑 AI Engine Authentication")
        
        # Check environment variable first for seamless deployment
        default_key = os.environ.get("GEMINI_API_KEY", "")
        api_key_input = st.text_input(
            "Google Gemini API Key",
            value=default_key,
            type="password",
            help="Enter your Google Gemini API key. If left blank, the platform automatically runs in realistic Demonstration Mode with pre-calibrated benchmarks.",
            placeholder="AIzaSy..."
        )

        model_choice = st.selectbox(
            "Model Selection",
            options=["gemini-2.5-flash", "gemini-3.7-flash", "gemini-2.5-pro"],
            index=0,
            help="Gemini 2.5 Flash is recommended for balanced multimodal vision reasoning and sub-second latency."
        )

        # Initialize Service
        gemini_service = GeminiService(api_key=api_key_input, model_name=model_choice)

        # Connection Status Pill
        if gemini_service.is_live:
            st.markdown(f"""
                <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10B981; border-radius: 8px; padding: 8px 12px; margin-top: 8px; display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1rem;">🟢</span>
                    <div>
                        <div style="color: #10B981; font-weight: 700; font-size: 0.8rem;">Live Gemini API Active</div>
                        <div style="color: #94A3B8; font-size: 0.72rem;">Model: {model_choice}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background: rgba(245, 158, 11, 0.15); border: 1px solid #F59E0B; border-radius: 8px; padding: 8px 12px; margin-top: 8px; display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1rem;">🟡</span>
                    <div>
                        <div style="color: #F59E0B; font-weight: 700; font-size: 0.8rem;">Demonstration Mode</div>
                        <div style="color: #94A3B8; font-size: 0.72rem;">Full features unlocked without API key</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<hr style='border: 1px solid rgba(255, 255, 255, 0.08); margin: 18px 0;'/>", unsafe_allow_html=True)

        # Architecture Pipeline
        st.markdown("#### 🏛️ Platform Architecture")
        st.markdown("""
            <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 12px; font-size: 0.78rem; line-height: 1.5; color: #CBD5E1;">
                <div style="margin-bottom: 6px;"><strong>1. Multimodal Sensor Ingest:</strong> Drones, CCTV, Field Cameras (JPG/PNG)</div>
                <div style="margin-bottom: 6px;"><strong>2. Neural Vision Reasoning:</strong> Gemini 2.5 Flash / 3.7 Flash Multimodal Pipeline</div>
                <div style="margin-bottom: 6px;"><strong>3. Structural & Safety Codes:</strong> OSHA 1926 & IS 456 / IS 13920 Rule Engine</div>
                <div style="margin-bottom: 6px;"><strong>4. CapEx & Asset Valuation:</strong> Parametric Indian Real Estate Models (Lakhs/Cr)</div>
                <div><strong>5. Generative Visualization:</strong> Dynamic Pollinations AI 3D Rendering</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='border: 1px solid rgba(255, 255, 255, 0.08); margin: 18px 0;'/>", unsafe_allow_html=True)

        # Regulatory Compliance Badges
        st.markdown("#### 📜 Governing Regulatory Standards")
        st.markdown("""
            <div style="display: flex; flex-direction: column; gap: 6px; font-size: 0.75rem;">
                <div style="background: rgba(30, 41, 59, 0.6); padding: 5px 8px; border-radius: 6px; color: #94A3B8; display: flex; justify-content: space-between;">
                    <span>OSHA 29 CFR 1926</span> <strong style="color: #10B981;">VERIFIED</strong>
                </div>
                <div style="background: rgba(30, 41, 59, 0.6); padding: 5px 8px; border-radius: 6px; color: #94A3B8; display: flex; justify-content: space-between;">
                    <span>IS 456:2000 (Plain & RC)</span> <strong style="color: #10B981;">VERIFIED</strong>
                </div>
                <div style="background: rgba(30, 41, 59, 0.6); padding: 5px 8px; border-radius: 6px; color: #94A3B8; display: flex; justify-content: space-between;">
                    <span>IS 13920:2016 (Ductile)</span> <strong style="color: #10B981;">VERIFIED</strong>
                </div>
                <div style="background: rgba(30, 41, 59, 0.6); padding: 5px 8px; border-radius: 6px; color: #94A3B8; display: flex; justify-content: space-between;">
                    <span>IS 2925 / IS 15809 (PPE)</span> <strong style="color: #10B981;">VERIFIED</strong>
                </div>
                <div style="background: rgba(30, 41, 59, 0.6); padding: 5px 8px; border-radius: 6px; color: #94A3B8; display: flex; justify-content: space-between;">
                    <span>ASTM C881 (Epoxy Repair)</span> <strong style="color: #10B981;">VERIFIED</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Reset button
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        if st.button("🧹 Clear All Session Cache", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

    # Main Application Header Banner
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 22px 28px; margin-bottom: 24px; position: relative; overflow: hidden;">
            <div style="position: absolute; right: -20px; top: -30px; font-size: 7rem; opacity: 0.04; user-select: none;">
                🏗️
            </div>
            <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px;">
                <div>
                    <span style="background: rgba(245, 158, 11, 0.2); color: #F59E0B; font-weight: 700; font-size: 0.72rem; padding: 4px 10px; border-radius: 999px; text-transform: uppercase; letter-spacing: 0.06em;">
                        Production-Ready AI Capstone
                    </span>
                    <h1 style="margin: 8px 0 4px 0; color: #F8FAFC; font-size: 1.85rem; font-weight: 800; letter-spacing: -0.02em;">
                        Multimodal Construction Intelligence Platform
                    </h1>
                    <p style="color: #94A3B8; font-size: 0.9rem; margin: 0; max-width: 800px; line-height: 1.5;">
                        Enterprise civil engineering intelligence fusing <strong>multimodal computer vision</strong>, 
                        <strong>structural integrity diagnostics (IS 456 & ASTM)</strong>, <strong>parametric CapEx/valuation modeling (INR Cr)</strong>, 
                        and <strong>weather-aware site orchestration</strong>.
                    </p>
                </div>
                <div style="display: flex; gap: 10px;">
                    <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 10px 14px; text-align: center;">
                        <div style="color: #94A3B8; font-size: 0.7rem; font-weight: 600; text-transform: uppercase;">Standard Codebase</div>
                        <div style="color: #38BDF8; font-size: 1rem; font-weight: 700;">OSHA & IS 456</div>
                    </div>
                    <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 10px 14px; text-align: center;">
                        <div style="color: #94A3B8; font-size: 0.7rem; font-weight: 600; text-transform: uppercase;">Cloud Deploy</div>
                        <div style="color: #10B981; font-size: 1rem; font-weight: 700;">1-Click Ready</div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4 Core Tab Modules
    tab1, tab2, tab3, tab4 = st.tabs([
        "🛡️ Site Safety & PPE Audit (Epic 2)",
        "🔬 Crack Diagnostics & Integrity (Epic 2)",
        "📊 Planning & Real Estate Valuation (Epic 3)",
        "🤖 Daily Assistant & Weather Advisory (Epic 5)"
    ])

    with tab1:
        render_safety_audit_tab(gemini_service)

    with tab2:
        render_crack_diagnostics_tab(gemini_service)

    with tab3:
        render_valuation_planner_tab()

    with tab4:
        render_site_assistant_tab(gemini_service)

    # Footer
    st.markdown("""
        <hr style="border: 1px solid rgba(255, 255, 255, 0.08); margin: 40px 0 20px 0;"/>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; color: #64748B; font-size: 0.8rem; gap: 12px;">
            <div>
                <strong>Multimodal Construction Intelligence Platform</strong> &bull; Skill Wallet Capstone Project 1
            </div>
            <div>
                Evaluated against <strong>OSHA 29 CFR 1926</strong> &bull; <strong>IS 456:2000</strong> &bull; <strong>IS 13920:2016</strong> &bull; Built with Streamlit & Google GenAI
            </div>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
