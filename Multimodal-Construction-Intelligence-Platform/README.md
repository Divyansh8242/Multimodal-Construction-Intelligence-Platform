# 🏗️ Multimodal Construction Intelligence Platform
### *Skill Wallet Capstone Project 1 — Enterprise Full-Stack AI Application*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Google GenAI](https://img.shields.io/badge/Google%20GenAI-Gemini%202.5%20%2F%203.7-orange.svg)](https://ai.google.dev/)
[![OSHA & IS 456](https://img.shields.io/badge/Standards-OSHA%201926%20%7C%20IS%20456%3A2000-green.svg)](https://bis.gov.in/)

An enterprise-grade, multimodal AI platform designed for civil structural engineers, project managers, and occupational safety officers. The platform fuses computer vision, regulatory compliance reasoning, parametric financial estimation, and weather-aware site logistics into a production-ready Streamlit application.

---

## 🌟 Core Modules & Epics

### 1. 🛡️ Tab 1: Site Safety & PPE Audit (Epic 2)
- **Computer Vision Ingestion**: Accepts high-resolution drone/CCTV/mobile photos (JPG/PNG) or pre-packaged high-risk site benchmarks.
- **Multimodal Compliance Engine**: Audits worker gear under **OSHA 29 CFR 1926** and **Bureau of Indian Standards**:
  - Industrial Safety Helmets (*OSHA 1926.100 / IS 2925:1984*)
  - High-Visibility Retroreflective Vests (*OSHA 1926.201 / IS 15809:2017 Class 2*)
  - Steel-Toe Puncture-Resistant Boots (*OSHA 1926.96 / IS 15298:Part 2*)
  - Full-Body Fall Arrest Harnesses & Lanyards (*OSHA 1926.502 / IS 3521:1999 Class A*)
- **Actionable Outputs**:
  - `safety_score` (0–100) and overall compliance status pills.
  - Interactive PPE detection checklist with compliance percentages.
  - Environmental hazard breakdown with severity ratings (**Critical**, **High**, **Medium**, **Low**) and prescriptive engineering remedies.
  - Downloadable structured JSON safety audit report.

### 2. 🔬 Tab 2: Crack Diagnostics & Structural Integrity (Epic 2)
- **Forensic Concrete Defect Classification**: Identifies Hairline Cracks, Foundation Settlement, Structural Shear Cracks, Thermal Expansion, and Rebar Corrosion Spalling.
- **Quantitative Defect Metrics**:
  - Estimated crack width in millimeters (evaluated against **IS 456:2000 Cl. 35.3.2** thresholds: $\le 0.1$ mm for severe exposure, $\le 0.3$ mm for mild exposure).
  - Depth penetration profile into concrete cover and rebar core.
  - Structural risk index score (0–100).
- **Engineering Remediation Specifications**:
  - High-pressure structural epoxy resin injection (*ASTM C881 Type IV, Grade 1*).
  - Carbon Fiber Reinforced Polymer (CFRP) composite jacketing (*ACI 440.2R / IS 13920:2016*).
  - Rebar passivation and hydro-demolition (*ICRI 310.1R / IS 9077*).
  - Downloadable JSON and engineering repair specification report.

### 3. 📊 Tab 3: Planning & Real Estate Valuation (Epic 3)
- **Parametric Inputs**: Structure Archetype (High-Rise Residential, Grade-A Commercial, PEB Logistics Warehouse, Luxury Villas), Built-Up Area (sq. ft.), and Geographic Location Tiers (Mumbai MMR, Bengaluru, Delhi-NCR, Hyderabad, Pune, Tier 2 & 3 Hubs).
- **Financial & CapEx Dashboard**:
  - Total Estimated Project Budget formatted in **INR Crores & Lakhs**.
  - Cumulative CapEx Incurred to Date based on milestone completion slider (0% to 100%).
  - Current Asset Market Valuation incorporating stage-completion appreciation index.
- **Bill of Quantities (BOQ) Thumb Rules**:
  - TMT Structural Steel Tonnage ($3.8$ – $5.2$ kg/sq.ft. Fe 500D / Fe 550D).
  - Cement consumption ($0.35$ – $0.52$ bags/sq.ft., Metric Tonnes).
  - Milestone execution trajectory from Piling to Handover.
- **Pollinations AI 3D Architectural Rendering**:
  - Generates real-time architectural visualization prompts.
  - Streams dynamic 1280x720 conceptual renders with selectable architectural languages, lighting, and camera perspectives.

### 4. 🤖 Tab 4: Daily Site Assistant & Weather-Aware Advisory (Epic 5)
- **Dynamic Meteorological Matrix**: Weather selector for High Wind ($>40$ km/h), Heavy Monsoon ($>30$ mm/h), Extreme Heat ($>42^\circ\text{C}$), Dense Fog, and Optimal Conditions.
- **Automated Safety Advisories**:
  - Tower crane wind cutoff limits and jib weather-vaning protocols (*OSHA 1926.1412*).
  - Concrete curing protocols under **IS 456:2000 Clause 13.5** (minimum moist curing periods, chilled batching, evaporation mitigation).
  - Scaffolding evacuation, ground bearing checks, and electrical dewatering GFCI protocols.
- **Multi-Turn Civil Engineering Assistant**:
  - Interactive multi-turn chatbot powered by Gemini or built-in engineering simulation.
  - Maintains conversation history across tabs with domain expertise in IS codes and OSHA.

---

## 🚀 Quick Start Guide

### 1. Clone & Navigate
```bash
git clone https://github.com/your-username/multimodal-construction-intelligence.git
cd "multimodal-construction-intelligence"
```

### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Launch the Application
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🔑 AI Authentication & Demonstration Mode

The platform is designed with a **fail-safe dual execution mode**:
1. **Live Gemini Multimodal Mode**: Enter your Google Gemini API Key in the sidebar (or set `export GEMINI_API_KEY="your-key"`). Utilizes the official `google-genai` SDK with models like `gemini-2.5-flash` or `gemini-3.7-flash`.
2. **Demonstration Mode (Zero Key Required)**: If no key is entered, the platform operates seamlessly using authentic, pre-calibrated engineering benchmark datasets and simulations.

---

## ☁️ 1-Click Streamlit Community Cloud Deployment

1. Push this repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io).
3. Select your repository, set the main file path to `app.py`, and click **Deploy**.
4. *(Optional)* Add your `GEMINI_API_KEY` under **App Settings > Secrets**.

---

## 📁 Repository Directory Structure

```
Multimodal Construction Intelligence Platform/
├── .streamlit/
│   └── config.toml             # Custom theme configuration (Industrial slate & amber)
├── assets/
│   ├── sample_ppe.jpg          # Pre-packaged construction site photo for 1-click audit
│   └── sample_crack.jpg        # Pre-packaged concrete defect photo for 1-click diagnostics
├── modules/
│   ├── __init__.py
│   ├── gemini_service.py       # Official google-genai SDK wrapper & fallback handler
│   ├── safety_audit.py         # Tab 1: PPE compliance & site hazard audit
│   ├── crack_diagnostics.py    # Tab 2: Concrete crack & structural integrity diagnostics
│   ├── valuation_planner.py    # Tab 3: Planning, CapEx, INR valuation & Pollinations AI
│   ├── site_assistant.py       # Tab 4: Weather advisory & multi-turn assistant
│   └── demo_data.py            # Calibrated engineering simulation datasets
├── app.py                      # Main Streamlit application
├── requirements.txt            # Zero external DB dependencies
└── README.md                   # Complete capstone documentation
```

---

## 📜 Regulatory Standards Reference
- **OSHA 29 CFR 1926**: Safety and Health Regulations for Construction.
- **IS 456:2000**: Plain and Reinforced Concrete — Code of Practice.
- **IS 13920:2016**: Ductile Design and Detailing of Reinforced Concrete Structures Subject to Seismic Forces.
- **IS 2925:1984**: Specification for Industrial Safety Helmets.
- **IS 15809:2017**: High Visibility Warning Clothes.
- **IS 3521:1999**: Industrial Safety Belts and Harnesses.
- **ASTM C881**: Standard Specification for Epoxy-Resin-Base Bonding Systems for Concrete.
