"""
Multimodal Construction Intelligence Platform - Tab 2: Crack Diagnostics & Structural Integrity (Epic 2)
Forensic Concrete Defect Classification & Remediation Engineering Module
"""

import streamlit as st
import json
import os
from datetime import datetime
from PIL import Image
import io

from modules.gemini_service import GeminiService


def render_crack_diagnostics_tab(gemini_service: GeminiService):
    """Renders the complete Crack Diagnostics & Structural Integrity interface."""
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #F59E0B; font-weight: 700; display: flex; align-items: center; gap: 10px;">
                <span>🔬</span> Crack Diagnostics & Structural Integrity (Epic 2)
            </h2>
            <p style="color: #94A3B8; margin-top: 4px; font-size: 0.95rem;">
                Multimodal forensic engineering inspection of concrete structural distress, rebar spalling, and crack width metrics 
                evaluated against <strong>IS 456:2000 Clause 35.3.2</strong>, <strong>IS 13920</strong>, and <strong>ASTM C881 / ACI 224</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_upload, col_preview = st.columns([1, 1], gap="large")

    with col_upload:
        st.markdown("""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
                <h4 style="margin: 0 0 10px 0; color: #F8FAFC; font-size: 1rem;">🧱 Ingest Concrete Surface Imagery</h4>
                <p style="color: #94A3B8; font-size: 0.85rem; margin-bottom: 12px;">
                    Upload close-up imagery of beams, columns, slab soffits, retaining walls, or masonry facades.
                </p>
            </div>
        """, unsafe_allow_html=True)

        uploaded_crack = st.file_uploader(
            "Upload Concrete Surface Photo (JPG, JPEG, PNG)",
            type=["jpg", "jpeg", "png"],
            key="crack_file_uploader",
            help="High-contrast close-up photos yield the most accurate crack width and depth estimation."
        )

        sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "sample_crack.jpg")
        c1, c2 = st.columns([1, 1])
        with c1:
            use_sample = st.button("🚀 Load Sample Structural Defect Photo", key="btn_load_sample_crack", use_container_width=True)
        with c2:
            clear_crack = st.button("🔄 Reset Image", key="btn_clear_crack", use_container_width=True)

        if clear_crack:
            if "crack_image_bytes" in st.session_state:
                del st.session_state["crack_image_bytes"]
            if "crack_result" in st.session_state:
                del st.session_state["crack_result"]
            st.rerun()

        active_image = None
        active_mime = "image/jpeg"

        if use_sample and os.path.exists(sample_path):
            with open(sample_path, "rb") as f:
                st.session_state["crack_image_bytes"] = f.read()
            st.session_state["crack_mime"] = "image/jpeg"
            st.toast("Loaded pre-packaged concrete structural shear sample photo!", icon="✅")

        if uploaded_crack is not None:
            st.session_state["crack_image_bytes"] = uploaded_crack.getvalue()
            st.session_state["crack_mime"] = uploaded_crack.type

        if "crack_image_bytes" in st.session_state:
            active_image = Image.open(io.BytesIO(st.session_state["crack_image_bytes"]))
            active_mime = st.session_state.get("crack_mime", "image/jpeg")

    with col_preview:
        if active_image:
            st.image(active_image, caption="Active Concrete Defect Inspection Frame", use_container_width=True)
            run_diag_btn = st.button("🧪 Run Multimodal Forensic Diagnostics", type="primary", use_container_width=True, key="btn_run_crack_diagnostics")
        else:
            st.markdown("""
                <div style="height: 280px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: rgba(15, 23, 42, 0.6); border: 2px dashed rgba(255, 255, 255, 0.15); border-radius: 12px; text-align: center; padding: 20px;">
                    <span style="font-size: 2.5rem; margin-bottom: 8px;">🧱</span>
                    <h4 style="color: #CBD5E1; margin: 0 0 6px 0;">No Defect Image Loaded</h4>
                    <p style="color: #64748B; font-size: 0.85rem; max-width: 300px; margin: 0;">
                        Upload a photo or click <strong>'Load Sample Structural Defect Photo'</strong> to classify cracks, evaluate width, and formulate repair specifications.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            run_diag_btn = False

    # Execute Diagnostics
    if run_diag_btn and "crack_image_bytes" in st.session_state:
        with st.spinner("Analyzing concrete microstructure, crack propagation vectors, and rebar corrosion profiles..."):
            result, is_live, err_msg = gemini_service.analyze_crack_diagnostics(
                st.session_state["crack_image_bytes"],
                mime_type=active_mime
            )
            st.session_state["crack_result"] = result
            st.session_state["crack_is_live"] = is_live
            st.session_state["crack_err_msg"] = err_msg
            st.session_state["crack_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Render Results
    if "crack_result" in st.session_state:
        result = st.session_state["crack_result"]
        is_live = st.session_state.get("crack_is_live", False)
        err_msg = st.session_state.get("crack_err_msg", None)
        timestamp = st.session_state.get("crack_timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        st.markdown("<hr style='border: 1px solid rgba(255, 255, 255, 0.1); margin: 24px 0;'/>", unsafe_allow_html=True)

        if err_msg:
            st.info(f"ℹ️ {err_msg}")

        defect_type = result.get("defect_type", "Structural Crack")
        severity = result.get("severity_level", "Moderate")
        urgency = result.get("urgency", "Moderate Urgency")
        width_mm = result.get("estimated_width_mm", 0.0)
        depth_mm = result.get("crack_depth_mm", 0.0)
        risk_score = result.get("structural_risk_score", 50)
        element = result.get("affected_element", "Reinforced Concrete Element")
        cost_est = result.get("estimated_repair_cost_inr", "₹50,000 - ₹1,00,000")
        repair_time = result.get("estimated_remedy_time_days", "3 - 5 Days")

        # Color token by severity
        if severity == "Critical":
            accent_color = "#EF4444"
            accent_bg = "rgba(239, 68, 68, 0.15)"
            sev_pill = "🔴 CRITICAL STRUCTURAL DEFECT"
        elif severity == "High":
            accent_color = "#F97316"
            accent_bg = "rgba(249, 115, 22, 0.15)"
            sev_pill = "🟠 HIGH STRUCTURAL DEFECT"
        elif severity == "Moderate":
            accent_color = "#F59E0B"
            accent_bg = "rgba(245, 158, 11, 0.15)"
            sev_pill = "🟡 MODERATE DISTRESS"
        else:
            accent_color = "#10B981"
            accent_bg = "rgba(16, 185, 129, 0.15)"
            sev_pill = "🟢 COSMETIC / MINOR DEFECT"

        # Executive Diagnostic Header
        st.markdown(f"""
            <div style="background: {accent_bg}; border: 1px solid {accent_color}; border-radius: 14px; padding: 18px 24px; margin-bottom: 24px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px;">
                <div>
                    <span style="background: {accent_color}; color: #0F172A; font-weight: 700; font-size: 0.75rem; padding: 4px 10px; border-radius: 999px; text-transform: uppercase; letter-spacing: 0.05em;">
                        {sev_pill}
                    </span>
                    <h3 style="margin: 8px 0 0 0; color: #F8FAFC; font-size: 1.4rem;">{defect_type}</h3>
                    <p style="color: #94A3B8; font-size: 0.85rem; margin: 4px 0 0 0;">
                        Target Element: <strong style="color: #38BDF8;">{element}</strong> &bull; Urgency: <strong style="color: {accent_color};">{urgency}</strong>
                    </p>
                </div>
                <div style="text-align: right; display: flex; align-items: baseline; gap: 6px;">
                    <div>
                        <div style="font-size: 0.8rem; color: #94A3B8; text-transform: uppercase;">Structural Risk Index</div>
                        <span style="font-size: 3rem; font-weight: 800; color: {accent_color}; line-height: 1;">{risk_score}</span>
                        <span style="font-size: 1.2rem; color: #64748B; font-weight: 600;">/100</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 4 Metric Cards
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        with col_m1:
            st.metric("Estimated Crack Width", f"{width_mm} mm", help="Permissible under IS 456: <= 0.1mm (severe), <= 0.3mm (mild)")
        with col_m2:
            st.metric("Estimated Penetration", f"{depth_mm} mm", help="Crack depth relative to nominal rebar concrete cover")
        with col_m3:
            st.metric("Estimated Remediation Cost", cost_est)
        with col_m4:
            st.metric("Remediation Timeline", repair_time)

        # IS 456 Code Compliance Callout
        code_violation = result.get("is_code_violation", "")
        if code_violation:
            st.markdown(f"""
                <div style="background: rgba(15, 23, 42, 0.8); border-left: 4px solid #38BDF8; border-radius: 6px; padding: 12px 16px; margin: 16px 0;">
                    <strong style="color: #38BDF8; font-size: 0.9rem;">📐 IS 456:2000 Clause 35.3.2 Regulatory Assessment:</strong>
                    <p style="color: #CBD5E1; font-size: 0.85rem; margin: 4px 0 0 0;">{code_violation}</p>
                </div>
            """, unsafe_allow_html=True)

        # Columns: Root Causes & Remediation Protocols
        c_causes, c_remedies = st.columns([1, 1], gap="large")

        with c_causes:
            st.markdown("""
                <h3 style="color: #F8FAFC; font-size: 1.15rem; margin: 16px 0 12px 0; display: flex; align-items: center; gap: 8px;">
                    <span>🔍</span> Forensic Engineering Root Causes
                </h3>
            """, unsafe_allow_html=True)

            causes = result.get("root_causes", [])
            for i, c in enumerate(causes):
                st.markdown(f"""
                    <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; display: flex; gap: 12px;">
                        <span style="background: rgba(245, 158, 11, 0.2); color: #F59E0B; font-weight: 700; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; flex-shrink: 0;">
                            {i+1}
                        </span>
                        <div style="color: #E2E8F0; font-size: 0.88rem; line-height: 1.5;">{c}</div>
                    </div>
                """, unsafe_allow_html=True)

            depth_desc = result.get("depth_profile", "")
            if depth_desc:
                st.markdown(f"""
                    <div style="background: rgba(30, 41, 59, 0.5); border: 1px dashed rgba(255, 255, 255, 0.15); border-radius: 8px; padding: 12px; margin-top: 14px;">
                        <span style="font-size: 0.8rem; color: #94A3B8; text-transform: uppercase; font-weight: 600;">Depth & Trajectory Profile:</span>
                        <p style="color: #CBD5E1; font-size: 0.85rem; margin: 4px 0 0 0;">{depth_desc}</p>
                    </div>
                """, unsafe_allow_html=True)

        with c_remedies:
            st.markdown("""
                <h3 style="color: #F8FAFC; font-size: 1.15rem; margin: 16px 0 12px 0; display: flex; align-items: center; gap: 8px;">
                    <span>🛠️</span> Recommended Engineering Remediation Specifications
                </h3>
            """, unsafe_allow_html=True)

            repairs = result.get("recommended_repairs", [])
            for rep in repairs:
                st.markdown(f"""
                    <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-left: 4px solid #10B981; border-radius: 8px; padding: 14px; margin-bottom: 12px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="color: #10B981; font-weight: 700; font-size: 0.8rem; text-transform: uppercase;">
                                {rep.get('stage', 'Remediation Step')}
                            </span>
                            <span style="color: #38BDF8; font-size: 0.75rem; background: rgba(56, 189, 248, 0.1); padding: 2px 6px; border-radius: 4px;">
                                {rep.get('standards', 'IS / ASTM')}
                            </span>
                        </div>
                        <h5 style="color: #F8FAFC; margin: 0 0 6px 0; font-size: 0.95rem;">{rep.get('action', 'Action')}</h5>
                        <p style="color: #94A3B8; font-size: 0.83rem; margin: 0; line-height: 1.45;">
                            {rep.get('specification', '')}
                        </p>
                    </div>
                """, unsafe_allow_html=True)

            mon_proto = result.get("monitoring_protocol", "")
            if mon_proto:
                st.markdown(f"""
                    <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 10px 14px; margin-top: 10px;">
                        <strong style="color: #F59E0B; font-size: 0.85rem;">📡 Post-Remediation Monitoring Protocol:</strong>
                        <p style="color: #CBD5E1; font-size: 0.82rem; margin: 4px 0 0 0;">{mon_proto}</p>
                    </div>
                """, unsafe_allow_html=True)

        # Download Report
        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
        report_payload = {
            "platform": "Multimodal Construction Intelligence Platform",
            "module": "Crack Diagnostics & Structural Integrity (Epic 2)",
            "inspection_timestamp": timestamp,
            "governing_standards": ["IS 456:2000 Cl. 35.3.2", "IS 13920:2016", "ASTM C881", "ACI 224.1R", "ICRI 310.1R"],
            "diagnostic_findings": result
        }
        json_str = json.dumps(report_payload, indent=2)

        col_d1, col_d2 = st.columns([1, 2])
        with col_d1:
            st.download_button(
                label="📥 Download Structural Diagnostic Report (JSON)",
                data=json_str,
                file_name=f"Concrete_Structural_Diagnostics_IS456_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        with col_d2:
            st.caption("Forensic structural engineering specification ready for tender packaging, structural peer reviews, and contractor remediation.")
