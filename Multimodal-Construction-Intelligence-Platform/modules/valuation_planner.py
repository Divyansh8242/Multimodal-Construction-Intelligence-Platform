"""
Multimodal Construction Intelligence Platform - Tab 3: Planning & Real Estate Valuation (Epic 3)
Budgeting, CapEx Tracking, Indian Market Valuation (Lakhs/Crores), BOQ Metrics & Pollinations AI 3D Rendering
"""

import streamlit as st
import urllib.parse
import random
from typing import Dict, Any, Tuple


# Indian Construction Benchmarks (Cost per Sq. Ft. in INR)
STRUCTURE_BENCHMARKS = {
    "Residential High-Rise (G+25)": {
        "base_cost_sqft": 3200,
        "steel_kg_sqft": 4.2,      # kg TMT steel per sqft
        "cement_bags_sqft": 0.44,   # 50kg bags per sqft
        "land_multiplier": 1.45,
        "completion_premium": 1.25,
        "description": "RCC Framed tower with shear walls, M30/M40 grade concrete, dual basements."
    },
    "Commercial Grade-A Office Park": {
        "base_cost_sqft": 3900,
        "steel_kg_sqft": 4.8,
        "cement_bags_sqft": 0.48,
        "land_multiplier": 1.65,
        "completion_premium": 1.30,
        "description": "Large span post-tensioned slabs, unitized double-glazed curtain wall façade, LEED Gold standards."
    },
    "Industrial Logistics Warehouse": {
        "base_cost_sqft": 2100,
        "steel_kg_sqft": 3.0,
        "cement_bags_sqft": 0.35,
        "land_multiplier": 1.15,
        "completion_premium": 1.15,
        "description": "Pre-Engineered Building (PEB) steel portal frames, FM2 high-tolerance laser screed flooring."
    },
    "Luxury Residential Villa Gated Enclave": {
        "base_cost_sqft": 4500,
        "steel_kg_sqft": 4.0,
        "cement_bags_sqft": 0.50,
        "land_multiplier": 1.55,
        "completion_premium": 1.35,
        "description": "Custom reinforced concrete structure, Italian marble finishes, VRV HVAC, smart automation."
    },
    "Mixed-Use Urban Transit Hub (Retail + Office)": {
        "base_cost_sqft": 4200,
        "steel_kg_sqft": 5.2,
        "cement_bags_sqft": 0.52,
        "land_multiplier": 1.80,
        "completion_premium": 1.35,
        "description": "Multi-tier commercial podium with composite steel-concrete columns and high-capacity elevators."
    }
}

LOCATION_TIERS = {
    "Tier 1: Mumbai MMR": {"cost_factor": 1.35, "land_factor": 2.80, "avg_selling_sqft": 22000},
    "Tier 1: Bengaluru (Whitefield/ORR)": {"cost_factor": 1.15, "land_factor": 1.85, "avg_selling_sqft": 10500},
    "Tier 1: Delhi-NCR (Gurugram/Noida)": {"cost_factor": 1.20, "land_factor": 2.10, "avg_selling_sqft": 12500},
    "Tier 1: Hyderabad (HITEC City/Gachibowli)": {"cost_factor": 1.10, "land_factor": 1.70, "avg_selling_sqft": 9200},
    "Tier 1: Pune (Kharadi/Hinjawadi)": {"cost_factor": 1.08, "land_factor": 1.60, "avg_selling_sqft": 8500},
    "Tier 2: Ahmedabad / GIFT City": {"cost_factor": 1.00, "land_factor": 1.35, "avg_selling_sqft": 6500},
    "Tier 2: Jaipur / Chandigarh / Kochi": {"cost_factor": 0.95, "land_factor": 1.25, "avg_selling_sqft": 5800},
    "Tier 3: Emerging Industrial Growth Hubs": {"cost_factor": 0.88, "land_factor": 1.10, "avg_selling_sqft": 4200}
}


def format_inr(amount_rupees: float) -> Tuple[str, str]:
    """Formats rupees into Lakhs and Crores with Indian numbering."""
    crores = amount_rupees / 10000000.0
    lakhs = amount_rupees / 100000.0

    if crores >= 1.0:
        cr_str = f"₹{crores:,.2f} Cr"
        full_str = f"₹{crores:,.2f} Crores ({lakhs:,.1f} Lakhs)"
    else:
        cr_str = f"₹{lakhs:,.2f} L"
        full_str = f"₹{lakhs:,.2f} Lakhs"

    return cr_str, full_str


def render_valuation_planner_tab():
    """Renders the Planning, Real Estate Valuation & 3D Pollinations AI interface."""
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #F59E0B; font-weight: 700; display: flex; align-items: center; gap: 10px;">
                <span>📊</span> Planning, CapEx & Real Estate Valuation (Epic 3)
            </h2>
            <p style="color: #94A3B8; margin-top: 4px; font-size: 0.95rem;">
                Parametric civil engineering cost estimation, CapEx drawdown schedules, Indian market asset valuation (INR Lakhs/Crores), 
                material bill of quantities (BOQ), and <strong>Pollinations AI 3D Architectural Rendering</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Top Configuration Section
    st.markdown("""
        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px; margin-bottom: 20px;">
            <h4 style="margin: 0 0 12px 0; color: #F8FAFC; font-size: 1rem;">📐 Project Specifications & Geographic Parameters</h4>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.2, 1, 1])

    with col1:
        structure_type = st.selectbox(
            "Structure Archetype",
            options=list(STRUCTURE_BENCHMARKS.keys()),
            index=0,
            help="Select structural configuration to calibrate civil engineering thumb rules and finishes."
        )

    with col2:
        location_tier = st.selectbox(
            "Geographic Location & City Tier",
            options=list(LOCATION_TIERS.keys()),
            index=1,  # Bengaluru default
            help="Calibrates regional material cartage, labor indexes, and land market value."
        )

    with col3:
        built_up_sqft = st.number_input(
            "Built-Up Area (Sq. Ft.)",
            min_value=5000,
            max_value=2500000,
            value=75000,
            step=5000,
            help="Total gross construction built-up area (BUA) including super-built amenities."
        )

    # Completion slider
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    completion_pct = st.slider(
        "Construction Milestone Completion Stage (%)",
        min_value=0,
        max_value=100,
        value=55,
        step=5,
        help="Current physical project progress on site."
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Computational Engine
    struct_meta = STRUCTURE_BENCHMARKS[structure_type]
    loc_meta = LOCATION_TIERS[location_tier]

    # Effective construction rate per sq ft
    effective_rate_sqft = struct_meta["base_cost_sqft"] * loc_meta["cost_factor"]
    total_construction_budget = effective_rate_sqft * built_up_sqft

    # Land & approvals component
    land_component_sqft = struct_meta["base_cost_sqft"] * loc_meta["land_factor"] * 0.75
    total_land_budget = land_component_sqft * built_up_sqft
    total_project_cost = total_construction_budget + total_land_budget

    # CapEx incurred to date (100% of land + % of construction)
    capex_incurred = total_land_budget + (total_construction_budget * (completion_pct / 100.0))

    # Market Asset Valuation (incorporates stage appreciation index)
    # Stage appreciation factor: builds up as completion nears 100%
    stage_appreciation = 1.0 + (0.35 * (completion_pct / 100.0) ** 1.3)
    base_market_rate_sqft = loc_meta["avg_selling_sqft"]
    current_asset_valuation = built_up_sqft * base_market_rate_sqft * (0.65 + 0.35 * (completion_pct / 100.0))

    # BOQ Material Estimations
    total_steel_kg = built_up_sqft * struct_meta["steel_kg_sqft"]
    total_steel_tonnes = total_steel_kg / 1000.0
    total_cement_bags = built_up_sqft * struct_meta["cement_bags_sqft"]
    total_cement_tonnes = (total_cement_bags * 50) / 1000.0

    # Format values
    tot_cost_cr, tot_cost_full = format_inr(total_project_cost)
    capex_cr, capex_full = format_inr(capex_incurred)
    val_cr, val_full = format_inr(current_asset_valuation)

    # Render Metric Dashboards
    st.markdown("""
        <h3 style="color: #F8FAFC; font-size: 1.15rem; margin: 18px 0 12px 0; display: flex; align-items: center; gap: 8px;">
            <span>💰</span> Financial Metrics & Capital Expenditure Breakdown
        </h3>
    """, unsafe_allow_html=True)

    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    with f_col1:
        st.metric(
            label="Total Project Budget",
            value=tot_cost_cr,
            help=f"Total estimated project capital cost: {tot_cost_full}"
        )
    with f_col2:
        st.metric(
            label="CapEx Incurred to Date",
            value=capex_cr,
            help=f"Cumulative capital expenditure deployed: {capex_full}"
        )
    with f_col3:
        st.metric(
            label="Current Asset Market Value",
            value=val_cr,
            delta=f"+{round((current_asset_valuation / max(total_project_cost, 1) - 1) * 100, 1)}% Return",
            help=f"Current valuation based on {location_tier} market benchmarks: {val_full}"
        )
    with f_col4:
        st.metric(
            label="Effective Unit Rate",
            value=f"₹{int(effective_rate_sqft):,} / sq.ft",
            help="Direct civil & MEP construction cost per square foot"
        )

    # BOQ Material Requirements
    st.markdown("""
        <h3 style="color: #F8FAFC; font-size: 1.15rem; margin: 20px 0 12px 0; display: flex; align-items: center; gap: 8px;">
            <span>🏗️</span> Bill of Quantities (BOQ) - Core Structural Materials (IS 456 Thumb Rules)
        </h3>
    """, unsafe_allow_html=True)

    b_col1, b_col2, b_col3, b_col4 = st.columns(4)
    with b_col1:
        st.metric(
            label="TMT Steel Requirement",
            value=f"{total_steel_tonnes:,.1f} MT",
            help=f"Estimated based on {struct_meta['steel_kg_sqft']} kg/sq.ft. (Fe 500D / Fe 550D)"
        )
    with b_col2:
        st.metric(
            label="Cement Quantity (Bags)",
            value=f"{int(total_cement_bags):,} Bags",
            help="Standard 50kg bags (OPC 53 / PPC)"
        )
    with b_col3:
        st.metric(
            label="Cement Tonnage",
            value=f"{total_cement_tonnes:,.1f} MT",
            help=f"Total bulk cement equivalent tonnage: {total_cement_tonnes:,.1f} metric tonnes"
        )
    with b_col4:
        st.metric(
            label="Physical Progress",
            value=f"{completion_pct}%",
            delta=f"{100 - completion_pct}% Remaining",
            delta_color="off"
        )

    # Milestone Progress Bar & Stage Breakdown
    st.markdown(f"""
        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px; margin: 20px 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 600; color: #F8FAFC; font-size: 0.95rem;">Milestone Execution Trajectory:</span>
                <span style="font-weight: 700; color: #F59E0B; font-size: 1rem;">{completion_pct}% Completed</span>
            </div>
            <div style="height: 12px; background: rgba(15, 23, 42, 0.8); border-radius: 999px; overflow: hidden; position: relative;">
                <div style="height: 100%; width: {completion_pct}%; background: linear-gradient(90deg, #F59E0B 0%, #10B981 100%); border-radius: 999px; transition: width 0.4s ease;"></div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); margin-top: 10px; font-size: 0.75rem; color: #94A3B8; text-align: center;">
                <div>0-15%: Piling & Raft</div>
                <div>15-45%: RCC Superstructure</div>
                <div>45-70%: Masonry & MEP</div>
                <div>70-90%: Façade & Finishes</div>
                <div>90-100%: OC & Handover</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Module 3B: Pollinations AI 3D Architectural Rendering Generator
    st.markdown("<hr style='border: 1px solid rgba(255, 255, 255, 0.1); margin: 30px 0;'/>", unsafe_allow_html=True)
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <h3 style="margin: 0; color: #F59E0B; font-weight: 700; display: flex; align-items: center; gap: 10px;">
                <span>🏛️</span> Conceptual 3D Architectural Rendering (Pollinations AI)
            </h3>
            <p style="color: #94A3B8; margin-top: 4px; font-size: 0.9rem;">
                Real-time generative architectural visualization synthesised dynamically from your project archetype, urban typology, and lighting preferences.
            </p>
        </div>
    """, unsafe_allow_html=True)

    render_col1, render_col2 = st.columns([1, 1], gap="large")

    with render_col1:
        st.markdown("""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
                <h4 style="margin: 0 0 10px 0; color: #F8FAFC; font-size: 1rem;">🎨 Visual Rendering Parameters</h4>
        """, unsafe_allow_html=True)

        arch_style = st.selectbox(
            "Architectural Design Language",
            options=[
                "Biophilic Green Eco-Architecture with Hanging Sky Gardens",
                "Parametric Double-Glazed Curtain Wall High-Rise",
                "Contemporary Indian Vernacular with Terracotta Jali Screens",
                "Monolithic Minimalist Exposed Board-Formed Concrete",
                "Futuristic Carbon-Neutral Mass Timber & Steel Hybrid",
                "Luxury Neo-Classical Portico & Italian Travertine Stone"
            ],
            index=0
        )

        lighting_cond = st.selectbox(
            "Atmospheric Lighting & Horizon",
            options=[
                "Dramatic Golden Hour Sunset with Volumetric Sunlight",
                "Crisp Blue Sky Architectural Daylight at Noon",
                "Blue Hour Twilight with Illuminated Interior Workspaces",
                "Misty Atmospheric Morning Fog with Diffused Ambient Light"
            ],
            index=0
        )

        camera_perspective = st.selectbox(
            "Camera Viewpoint & Framing",
            options=[
                "Dramatic Low-Angle Street View Looking Up at Towers",
                "Wide-Angle Drone Aerial Masterplan Perspective",
                "Cinematic Eye-Level Pedestrian Plaza Angle",
                "Isometric 3D Architectural Model Presentation Cutaway"
            ],
            index=0
        )

        custom_prompt_addon = st.text_input(
            "Additional Architectural Feature Tags",
            value="ultra realistic, 8k architectural photography, architectural digest feature, Octane Render, hyper-detailed",
            help="Append custom descriptors to refine texture, glass reflection, and urban context."
        )

        if "render_seed" not in st.session_state:
            st.session_state["render_seed"] = random.randint(1000, 999999)

        c_gen1, c_gen2 = st.columns([1, 1])
        with c_gen1:
            gen_btn = st.button("✨ Generate 3D Architectural Render", type="primary", use_container_width=True)
        with c_gen2:
            reroll_btn = st.button("🎲 Re-Roll New Seed", use_container_width=True)

        if reroll_btn:
            st.session_state["render_seed"] = random.randint(1000, 999999)
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

        # Synthesize Prompt
        base_prompt = (
            f"A masterpiece architectural visualization of a {built_up_sqft:,} sq ft {structure_type} in {location_tier.split(':')[1].strip() if ':' in location_tier else location_tier}, "
            f"styled in {arch_style}, {lighting_cond}, {camera_perspective}, {custom_prompt_addon}"
        )

        st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 12px; margin-top: 10px;">
                <span style="font-size: 0.75rem; color: #38BDF8; font-weight: 700; text-transform: uppercase;">Synthesized Pollinations AI Prompt:</span>
                <p style="color: #CBD5E1; font-size: 0.8rem; margin: 4px 0 0 0; line-height: 1.4;">{base_prompt}</p>
            </div>
        """, unsafe_allow_html=True)

    with render_col2:
        encoded_prompt = urllib.parse.quote(base_prompt)
        current_seed = st.session_state.get("render_seed", 42819)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1280&height=720&nologo=true&seed={current_seed}"

        st.markdown("""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h4 style="margin: 0; color: #F8FAFC; font-size: 1rem;">🖼️ Conceptual 3D Model Rendering</h4>
                    <span style="background: rgba(245, 158, 11, 0.2); color: #F59E0B; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 6px;">
                        Seed #{current_seed}
                    </span>
                </div>
        """, unsafe_allow_html=True)

        try:
            st.image(
                image_url,
                caption=f"Pollinations AI Architectural Concept: {structure_type} ({arch_style})",
                use_container_width=True
            )
            st.markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
                    <a href="{image_url}" target="_blank" style="color: #38BDF8; text-decoration: none; font-size: 0.85rem; font-weight: 600;">
                        🔗 Open Full-Resolution High-Definition Render (1280x720) ↗
                    </a>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Could not load Pollinations render: {e}")

        st.markdown("</div>", unsafe_allow_html=True)
