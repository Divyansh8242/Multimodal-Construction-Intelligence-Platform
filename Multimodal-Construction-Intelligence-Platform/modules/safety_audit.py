"""
Multimodal Construction Intelligence Platform - Tab 1: Site Safety & PPE Audit (Epic 2)
OSHA 1926 & IS 456 Compliance Inspection Module
"""

import streamlit as st
import json
import os
import time
from datetime import datetime
from PIL import Image
import io

from modules.gemini_service import GeminiService


def render_safety_audit_tab(gemini_service: GeminiService):
    """Renders the complete Site Safety & PPE Audit interface."""
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #F59E0B; font-weight: 700; display: flex; align-items: center; gap: 10px;">
                <span>🛡️</span> Site Safety & PPE Compliance Audit (Epic 2)
            </h2>
            <p style="color: #94A3B8; margin-top: 4px; font-size: 0.95rem;">
                Automated computer vision auditing for construction personal protective equipment (PPE) and environmental site hazards under 
                <strong>OSHA 29 CFR 1926</strong> and <strong>Bureau of Indian Standards (IS 2925, IS 15809, IS 3521, IS 456)</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_upload, col_preview = st.columns([1, 1], gap="large")

    with col_upload:
        st.markdown("""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
                <h4 style="margin: 0 0 10px 0; color: #F8FAFC; font-size: 1rem;">📷 Ingest Construction Site Imagery</h4>
                <p style="color: #94A3B8; font-size: 0.85rem; margin-bottom: 12px;">
                    Upload high-resolution inspection photos from drone telemetry, CCTV, or field mobile cameras.
                </p>
            </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Upload Site Photo (JPG, JPEG, PNG)",
            type=["jpg", "jpeg", "png"],
            key="safety_file_uploader",
            help="Supported formats: JPG, JPEG, PNG (Max 50MB)"
        )

        # Sample image selector
        sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "sample_ppe.jpg")
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            use_sample = st.button("🚀 Load Sample High-Risk Site Photo", key="btn_load_sample_ppe", use_container_width=True)
        with col_btn2:
            clear_img = st.button("🔄 Reset Image", key="btn_clear_ppe", use_container_width=True)

        if clear_img:
            if "ppe_image_bytes" in st.session_state:
                del st.session_state["ppe_image_bytes"]
            if "safety_result" in st.session_state:
                del st.session_state["safety_result"]
            st.rerun()

        # Handle active image
        active_image = None
        active_mime = "image/jpeg"

        if use_sample and os.path.exists(sample_path):
            with open(sample_path, "rb") as f:
                st.session_state["ppe_image_bytes"] = f.read()
            st.session_state["ppe_mime"] = "image/jpeg"
            st.toast("Loaded pre-packaged construction site sample photo!", icon="✅")

        if uploaded_file is not None:
            st.session_state["ppe_image_bytes"] = uploaded_file.getvalue()
            st.session_state["ppe_mime"] = uploaded_file.type

        if "ppe_image_bytes" in st.session_state:
            active_image = Image.open(io.BytesIO(st.session_state["ppe_image_bytes"]))
            active_mime = st.session_state.get("ppe_mime", "image/jpeg")

    with col_preview:
        if active_image:
            st.image(active_image, caption="Active Site Inspection Snapshot", use_container_width=True)
            run_audit_btn = st.button("🔍 Run Multimodal Safety Audit", type="primary", use_container_width=True, key="btn_run_safety_audit")
        else:
            st.markdown("""
                <div style="height: 280px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: rgba(15, 23, 42, 0.6); border: 2px dashed rgba(255, 255, 255, 0.15); border-radius: 12px; text-align: center; padding: 20px;">
                    <span style="font-size: 2.5rem; margin-bottom: 8px;">🏗️</span>
                    <h4 style="color: #CBD5E1; margin: 0 0 6px 0;">No Site Image Loaded</h4>
                    <p style="color: #64748B; font-size: 0.85rem; max-width: 300px; margin: 0;">
                        Upload a photo or click <strong>'Load Sample High-Risk Site Photo'</strong> to trigger automated OSHA & IS 456 compliance inspection.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            run_audit_btn = False

    # Execute Audit
    if run_audit_btn and "ppe_image_bytes" in st.session_state:
        with st.spinner("Analyzing worker PPE compliance and inspecting site hazards with Gemini Vision Intelligence..."):
            result, is_live, err_msg = gemini_service.analyze_site_safety(
                st.session_state["ppe_image_bytes"],
                mime_type=active_mime
            )
            st.session_state["safety_result"] = result
            st.session_state["safety_is_live"] = is_live
            st.session_state["safety_err_msg"] = err_msg
            st.session_state["safety_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Render Results if available
    if "safety_result" in st.session_state:
        result = st.session_state["safety_result"]
        is_live = st.session_state.get("safety_is_live", False)
        err_msg = st.session_state.get("safety_err_msg", None)
        timestamp = st.session_state.get("safety_timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        st.markdown("<hr style='border: 1px solid rgba(255, 255, 255, 0.1); margin: 24px 0;'/>", unsafe_allow_html=True)

        if err_msg:
            st.info(f"ℹ️ {err_msg}")

        # Top Executive Header & Score Card
        safety_score = result.get("safety_score", 0)
        overall_status = result.get("overall_status", "Unknown")
        worker_count = result.get("worker_count", 0)
        compliant_workers = result.get("compliant_workers", 0)
        compliance_pct = result.get("compliance_percentage", round((compliant_workers / max(worker_count, 1)) * 100, 1))
        hazards = result.get("site_hazards", [])

        # Color token by score
        if safety_score >= 85:
            score_color = "#10B981"  # Emerald
            score_bg = "rgba(16, 185, 129, 0.15)"
            status_badge = "🟢 COMPLIANT / MINIMAL RISK"
        elif safety_score >= 65:
            score_color = "#F59E0B"  # Amber
            score_bg = "rgba(245, 158, 11, 0.15)"
            status_badge = "🟡 MODERATE RISK DETECTED"
        else:
            score_color = "#EF4444"  # Crimson
            score_bg = "rgba(239, 68, 68, 0.15)"
            status_badge = "🔴 HIGH RISK / VIOLATIONS ACTIVE"

        # Metric Banner
        st.markdown(f"""
            <div style="background: {score_bg}; border: 1px solid {score_color}; border-radius: 14px; padding: 18px 24px; margin-bottom: 24px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px;">
                <div>
                    <span style="background: {score_color}; color: #0F172A; font-weight: 700; font-size: 0.75rem; padding: 4px 10px; border-radius: 999px; text-transform: uppercase; letter-spacing: 0.05em;">
                        {status_badge}
                    </span>
                    <h3 style="margin: 8px 0 0 0; color: #F8FAFC; font-size: 1.4rem;">{overall_status}</h3>
                    <p style="color: #94A3B8; font-size: 0.85rem; margin: 4px 0 0 0;">
                        Audit Timestamp: {timestamp} &bull; Engine: {"🟢 Live Gemini Multimodal Flash" if is_live else "🟡 Standard AI Simulation Engine"}
                    </p>
                </div>
                <div style="text-align: right; display: flex; align-items: baseline; gap: 6px;">
                    <span style="font-size: 3.2rem; font-weight: 800; color: {score_color}; line-height: 1;">{safety_score}</span>
                    <span style="font-size: 1.2rem; color: #64748B; font-weight: 600;">/100</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 4 Key Metric Cards
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        with m_col1:
            st.metric("Total Workers Detected", f"{worker_count} Personnel")
        with m_col2:
            st.metric("Fully Compliant Personnel", f"{compliant_workers} / {worker_count}")
        with m_col3:
            st.metric("PPE Compliance Rate", f"{compliance_pct}%")
        with m_col4:
            st.metric("Identified Site Hazards", f"{len(hazards)} Active", delta=-len(hazards), delta_color="inverse")

        # Two Column Layout: PPE Checklist & Hazard Breakdown
        col_ppe, col_hazards = st.columns([1, 1], gap="large")

        with col_ppe:
            st.markdown("""
                <h3 style="color: #F8FAFC; font-size: 1.15rem; margin: 20px 0 12px 0; display: flex; align-items: center; gap: 8px;">
                    <span>📋</span> Mandatory PPE Detection Checklist
                </h3>
            """, unsafe_allow_html=True)

            ppe_items = result.get("ppe_detection", [])
            for item in ppe_items:
                status = item.get("status", "Unknown")
                is_ok = status == "Compliant"
                is_part = "Partial" in status
                badge_color = "#10B981" if is_ok else ("#F59E0B" if is_part else "#EF4444")
                icon = "✅" if is_ok else ("⚠️" if is_part else "❌")

                st.markdown(f"""
                    <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-left: 4px solid {badge_color}; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div style="font-weight: 600; color: #F8FAFC; font-size: 0.95rem;">
                                {icon} {item.get('item', 'PPE Item')}
                            </div>
                            <span style="background: rgba(255,255,255,0.08); color: {badge_color}; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 6px;">
                                {status} ({item.get('compliance_rate', 'N/A')})
                            </span>
                        </div>
                        <div style="margin-top: 6px; font-size: 0.8rem; color: #94A3B8;">
                            <strong>Standard:</strong> <span style="color: #38BDF8;">{item.get('standard', 'OSHA / IS Code')}</span>
                        </div>
                        <div style="margin-top: 4px; font-size: 0.8rem; color: #CBD5E1;">
                            {item.get('notes', '')}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        with col_hazards:
            st.markdown("""
                <h3 style="color: #F8FAFC; font-size: 1.15rem; margin: 20px 0 12px 0; display: flex; align-items: center; gap: 8px;">
                    <span>⚠️</span> Identified Site Hazards & Engineering Remedies
                </h3>
            """, unsafe_allow_html=True)

            if not hazards:
                st.success("No critical environmental or procedural hazards detected in this snapshot.")
            else:
                for idx, h in enumerate(hazards):
                    sev = h.get("severity", "Medium")
                    if sev == "Critical":
                        s_color = "#EF4444"
                        s_pill = "🔴 CRITICAL"
                    elif sev == "High":
                        s_color = "#F97316"
                        s_pill = "🟠 HIGH"
                    elif sev == "Medium":
                        s_color = "#F59E0B"
                        s_pill = "🟡 MEDIUM"
                    else:
                        s_color = "#10B981"
                        s_pill = "🟢 LOW"

                    with st.expander(f"{s_pill} - {h.get('hazard', 'Hazard Item')} ({h.get('location', 'Site Location')})", expanded=(idx < 2)):
                        st.markdown(f"""
                            <div style="font-size: 0.85rem; line-height: 1.5;">
                                <p style="margin: 0 0 6px 0;"><strong>Regulatory Standard Reference:</strong> <span style="color: #38BDF8;">{h.get('standard_ref', 'OSHA 1926 / IS 456')}</span></p>
                                <p style="margin: 0 0 6px 0;"><strong>Safety Impact:</strong> <span style="color: #E2E8F0;">{h.get('impact', 'Potential injury or hazard.')}</span></p>
                                <div style="background: rgba(15, 23, 42, 0.7); border-radius: 6px; padding: 10px; margin-top: 8px; border-left: 3px solid {s_color};">
                                    <strong style="color: {s_color};">Mandatory Corrective Action:</strong>
                                    <p style="margin: 4px 0 0 0; color: #CBD5E1;">{h.get('corrective_remedies', 'Implement corrective procedures.')}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

        # Executive Summary Callout
        summary_text = result.get("summary", "")
        if summary_text:
            st.markdown(f"""
                <div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 14px 18px; margin-top: 16px;">
                    <h5 style="color: #F8FAFC; margin: 0 0 6px 0; font-size: 0.95rem;">📌 Chief Safety Auditor Synthesis</h5>
                    <p style="color: #94A3B8; font-size: 0.88rem; margin: 0; line-height: 1.5;">
                        {summary_text}
                    </p>
                </div>
            """, unsafe_allow_html=True)

        # Downloadable JSON report
        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
        report_payload = {
            "platform": "Multimodal Construction Intelligence Platform",
            "module": "Site Safety & PPE Compliance Audit (Epic 2)",
            "audit_timestamp": timestamp,
            "standards_evaluated": ["OSHA 29 CFR 1926", "IS 2925:1984", "IS 15809:2017", "IS 15298", "IS 3521:1999", "IS 456:2000"],
            "inspection_results": result
        }
        json_str = json.dumps(report_payload, indent=2)
        
        col_d1, col_d2 = st.columns([1, 2])
        with col_d1:
            st.download_button(
                label="📥 Download Structured JSON Safety Report",
                data=json_str,
                file_name=f"Construction_Safety_Audit_OSHA_IS456_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        with col_d2:
            st.caption("Includes full JSON payload, timestamp verification, OSHA/IS regulatory citations, and actionable engineering corrective remedies.")
