"""
Multimodal Construction Intelligence Platform - Demo & Simulation Engine
Provides realistic domain benchmarks adhering to OSHA 1926 and Bureau of Indian Standards (IS 456, IS 13920).
"""

from typing import Dict, Any, List


def get_demo_safety_data() -> Dict[str, Any]:
    """Returns structured OSHA / IS 456 safety audit data for demo mode."""
    return {
        "safety_score": 88,
        "overall_status": "Moderate Risk - Minor Non-Compliance Detected",
        "worker_count": 4,
        "compliant_workers": 3,
        "compliance_percentage": 75.0,
        "ppe_detection": [
            {
                "item": "Industrial Safety Helmets (Hard Hats)",
                "detected": True,
                "status": "Compliant",
                "count": 4,
                "required_count": 4,
                "compliance_rate": "100%",
                "standard": "OSHA 1926.100 / IS 2925:1984",
                "notes": "High-density polyethylene Type 1 Class E helmets equipped with chin straps worn by all active personnel."
            },
            {
                "item": "High-Visibility Safety Vests",
                "detected": True,
                "status": "Compliant",
                "count": 4,
                "required_count": 4,
                "compliance_rate": "100%",
                "standard": "OSHA 1926.201 / IS 15809:2017 Class 2",
                "notes": "Fluorescent orange/lime vests with reflective horizontal retroreflective stripes active."
            },
            {
                "item": "Steel-Toe Safety Footwear",
                "detected": True,
                "status": "Compliant",
                "count": 4,
                "required_count": 4,
                "compliance_rate": "100%",
                "standard": "OSHA 1926.96 / IS 15298:Part 2",
                "notes": "Heavy-duty anti-puncture steel toe construction work boots with non-slip outsoles verified."
            },
            {
                "item": "Full Body Fall Arrest Harnesses",
                "detected": True,
                "status": "Partial Non-Compliance",
                "count": 3,
                "required_count": 4,
                "compliance_rate": "75%",
                "standard": "OSHA 1926.502 / IS 3521:1999 Class A",
                "notes": "Three workers secured with shock-absorbing lanyards to anchorage lifeline; one worker on outer scaffolding tier lacks 100% tie-off."
            },
            {
                "item": "Eye & Heavy Duty Work Gloves",
                "detected": True,
                "status": "Compliant",
                "count": 4,
                "required_count": 4,
                "compliance_rate": "100%",
                "standard": "OSHA 1926.102 / IS 5983 / IS 6994",
                "notes": "Cut-resistant nitrile/leather gloves observed during rebar fabrication and tie-wire handling."
            }
        ],
        "site_hazards": [
            {
                "hazard": "Fall Protection Anchor Defect at Scaffolding Perimeter",
                "location": "Upper Level Scaffolding Bay 3 - North Elevation",
                "severity": "High",
                "standard_ref": "OSHA 1926.501(b)(1) & IS 3521 Cl 5.2",
                "impact": "Risk of high-elevation fall (>2.8m above working platform).",
                "corrective_remedies": "Mandate immediate 100% dual-lanyard tie-off to certified overhead static lifeline. Install toe-boards and mid-rails along incomplete scaffolding bay."
            },
            {
                "hazard": "Exposed Reinforcing Starter Bars Without Safety Impalement Caps",
                "location": "Column Cage Footing C-14 Area",
                "severity": "Medium",
                "standard_ref": "OSHA 1926.701(b) & IS 456 Cl 26.2",
                "impact": "Severe impalement hazard during movement around rebar cages.",
                "corrective_remedies": "Affix high-visibility OSHA-compliant steel-reinforced mushroom impalement protective caps over all projecting rebar dowels immediately."
            },
            {
                "hazard": "Housekeeping & Loose Tie-Wire Bundles on Deck",
                "location": "Slab Shuttering Deck Level 4",
                "severity": "Low",
                "standard_ref": "OSHA 1926.25(a) & National Building Code (NBC 2016)",
                "impact": "Tripping hazard and ankle sprain risk for workers carrying formwork panels.",
                "corrective_remedies": "Enforce 5S end-of-shift housekeeping protocol; consolidate scrap rebar, binding wire clippings, and nails into designated disposal bins."
            },
            {
                "hazard": "Scaffolding Diagonal Cross-Brace Locking Pin Missing",
                "location": "Modular Cuplock Tower Frame #2",
                "severity": "Critical",
                "standard_ref": "OSHA 1926.451(c)(2) & IS 4014 Part 2",
                "impact": "Potential structural instability or racking failure of staging tower under dynamic wind/concrete pour load.",
                "corrective_remedies": "Tag tower 'DO NOT USE' (Red Tag), insert drop-forged safety wedge pins, verify plumbness with spirit level, and re-certify scaffold before resuming pours."
            }
        ],
        "summary": "Overall site safety compliance demonstrates high baseline adherence for mandatory personal gear (Helmets, Vests, Steel-Toe Footwear). Critical corrective intervention is required for the unpinned scaffolding diagonal brace and perimeter tie-off anchor before continuing structural shuttering."
    }


def get_demo_crack_data() -> Dict[str, Any]:
    """Returns structured structural diagnostics and crack integrity evaluation."""
    return {
        "defect_type": "Structural Shear Crack & Rebar Spalling",
        "severity_level": "Critical",
        "urgency": "High Urgency - Remediate Within 7 Days",
        "estimated_width_mm": 4.2,
        "crack_depth_mm": 42.0,
        "depth_profile": "Full-depth shear trajectory penetrating past core cover into primary longitudinal rebar zone.",
        "structural_risk_score": 86,
        "affected_element": "Reinforced Concrete Column-Beam Joint (RCC Frame)",
        "is_code_violation": "Exceeds IS 456:2000 Cl. 35.3.2 maximum permissible surface crack width (0.1 mm for severe exposure, 0.3 mm for mild exposure).",
        "root_causes": [
            "Excessive diagonal tension shear stress exceeding nominal concrete shear strength (Tc) under concentrated gravity/lateral cyclic loads.",
            "Depassivation of reinforcing steel bars induced by atmospheric carbonation and chloride penetration through porous cover.",
            "Volumetric expansion of corroding iron oxide (2.5x - 4x initial rebar volume) generating bursting tensile stresses and concrete cover spalling.",
            "Insufficient or widely spaced transverse shear stirrups at the critical plastic hinge zone (contrary to IS 13920:2016 ductile detailing)."
        ],
        "recommended_repairs": [
            {
                "stage": "Step 1: Emergency Shoring & Load Relief",
                "action": "Immediate Hydraulic Shoring",
                "specification": "Install adjustable hydraulic Acrow props (min 150 kN load capacity) under adjacent floor beams to relieve live and dead load from the distressed column prior to repair.",
                "standards": "IS 456:2000 / BS 5975 Temporary Works Code"
            },
            {
                "stage": "Step 2: Concrete Delamination Removal & Rebar Passivation",
                "action": "Hydro-Demolition & Anti-Corrosion Treatment",
                "specification": "Chisel/pneumatically chip cracked and carbonated concrete to at least 25mm behind exposed rebars. Sandblast rebar to Sa 2.5 profile. Apply zinc-rich epoxy primer (ASTM A775 / IS 9077) and migratory corrosion inhibitor.",
                "standards": "ICRI Guideline No. 310.1R / IS 9077"
            },
            {
                "stage": "Step 3: Structural Crack Injection",
                "action": "High-Pressure Structural Epoxy Resin Injection",
                "specification": "Seal crack perimeter with epoxy surface sealer; install mechanical injection ports at 150mm spacing along the 45-degree shear trace. Pressure-inject ultra-low viscosity structural epoxy resin (ASTM C881 Type IV, Grade 1) from bottom to top until refusal.",
                "standards": "ASTM C881 / ACI 224.1R"
            },
            {
                "stage": "Step 4: Structural Strengthening",
                "action": "Carbon Fiber Reinforced Polymer (CFRP) Composite Jacket",
                "specification": "Wrap joint region with 2 layers of bidirectional CFRP fabric (300 g/m², tensile strength >3400 MPa) saturated with high-modulus epoxy matrix to restore and enhance nominal shear capacity by 35%.",
                "standards": "ACI 440.2R / IS 13920 Ductile Detailing Provisions"
            }
        ],
        "monitoring_protocol": "Install calibrated vibrating-wire crack displacement tell-tale gauges with automated wireless data logging for 90 days post-cure.",
        "estimated_repair_cost_inr": "₹1,85,000 - ₹2,50,000",
        "estimated_remedy_time_days": "5 - 7 Days"
    }


def get_demo_chat_response(prompt: str, weather_condition: str) -> str:
    """Provides smart civil engineering responses for demonstration mode."""
    p_lower = prompt.lower()
    
    if "curing" in p_lower:
        return (
            "### 🏗️ Concrete Curing Engineering Protocols (IS 456:2000 Cl. 13.5)\n\n"
            "According to **IS 456:2000 Clause 13.5**, curing requirements depend on cement type and ambient environmental conditions:\n\n"
            "1. **Ordinary Portland Cement (OPC 43/53 Grade)**:\n"
            "   - **Standard Moist Curing Period**: Minimum **7 days** under normal ambient conditions.\n"
            "   - **Hot & Dry Weather / Low Humidity**: Minimum **10 days** (extends to 14 days when mineral admixtures like Fly Ash or GGBS are incorporated).\n\n"
            "2. **Portland Pozzolana Cement (PPC) / Slag Cement (PSC)**:\n"
            "   - Minimum **10 days** under normal conditions, and **14 days** under hot/dry weather due to slower secondary pozzolanic reaction kinetics.\n\n"
            f"3. **Weather Alert Adjustment ({weather_condition})**:\n"
            "   - Apply continuous wet hessian/burlap wrapping or liquid membrane-forming curing compounds conforming to **ASTM C309**. Never allow alternating wetting and drying cycles as this induces severe micro-cracking and loss of compressive strength."
        )
    elif "crane" in p_lower or "wind" in p_lower:
        return (
            "### 🚨 Tower Crane Operation Protocols Under Wind Speeds (OSHA 1926.1412 / IS 456)\n\n"
            "1. **Maximum Operational Wind Limit**: Standard tower cranes must cease lifting operations when sustained wind speeds exceed **38 km/h (24 mph or 10.5 m/s)**.\n"
            "2. **Critical Shutdown Threshold**: At **50 km/h (31 mph or 14 m/s)**, all loads must be grounded, the trolley brought to minimum radius, and the hook hoisted to upper limit.\n"
            "3. **Out-of-Service Weather-Vaning**: When winds exceed 60 km/h, the slew brake **MUST be released** to allow the jib to freely weather-vane with the wind, preventing catastrophic structural mast buckling.\n"
            "4. **Anemometer Mandate**: Electronic cup anemometers mounted at the jib apex must feed continuous real-time telemetry to the operator cabin console with visual/audible alarms set at 80% of rated threshold."
        )
    elif "steel" in p_lower or "tonnage" in p_lower or "bom" in p_lower:
        return (
            "### 📐 Structural Steel & Cement BOQ Estimation Rules of Thumb (IS Codes)\n\n"
            "For standard Reinforced Cement Concrete (RCC) framed structures, civil engineering thumb rules estimate:\n\n"
            "- **High-Rise Residential (G+15 to G+30)**: **3.8 to 4.5 kg of TMT steel per sq. ft.** of built-up area (Fe 500D or Fe 550D conforming to IS 1786).\n"
            "- **Commercial / Office Parks (Large Span Beams)**: **4.5 to 5.5 kg of steel per sq. ft.** to accommodate longer column-free spans.\n"
            "- **Industrial PEB / Warehouses**: **2.8 to 3.5 kg/sq.ft.** for sub-structure & foundations + structural hollow sections.\n"
            "- **Cement Consumption**: Approx. **0.40 to 0.45 bags (50kg each)** per sq. ft. of built-up area (accounting for M25/M30 grades for slabs, columns, and foundations).\n\n"
            "💡 *Tip: For ductile seismic detailing under IS 13920:2016 (Zone III, IV, V), increase joint stirrup tonnage by approximately 6-8%.*"
        )
    else:
        return (
            f"### 👷 Construction Intelligence Advisory\n\n"
            f"**Site Environmental State**: Current operational condition set to **{weather_condition}**.\n\n"
            f"Regarding your query on *'{prompt[:60]}...'*, here are key engineering recommendations:\n\n"
            "1. **Quality & Standard Compliance**: Align structural execution with **IS 456:2000** (Plain and Reinforced Concrete) and **IS 13920:2016** (Ductile Detailing).\n"
            "2. **Occupational Safety Mandate**: Ensure all workers adhere to **OSHA 1926 Subpart M** (Fall Protection) and **IS 3521** for scaffolding anchorages.\n"
            "3. **Site Monitoring**: Implement non-destructive testing (NDT)—such as Ultrasonic Pulse Velocity (UPV - IS 13311 Part 1) and Rebound Hammer testing—if concrete compaction or honeycomb voids are suspected.\n\n"
            "Feel free to ask for specific mix designs (M20-M50), shuttering strike-off timelines, or structural repair procedures!"
        )
