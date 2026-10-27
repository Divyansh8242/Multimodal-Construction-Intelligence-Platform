"""
Multimodal Construction Intelligence Platform - Gemini AI Service
Powered by official Google GenAI SDK (google-genai) with automated fallback to demonstration mode.
"""

import os
import json
import re
from typing import Dict, Any, Optional, List, Tuple
from PIL import Image
import io

from modules.demo_data import (
    get_demo_safety_data,
    get_demo_crack_data,
    get_demo_chat_response
)

# Attempt official Google GenAI SDK import
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


def clean_json_response(raw_text: str) -> Dict[str, Any]:
    """Extracts and parses JSON object from Gemini markdown response."""
    # Remove markdown code fences if present
    cleaned = raw_text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()

    # Search for first { and last }
    start_idx = cleaned.find('{')
    end_idx = cleaned.rfind('}')
    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        cleaned = cleaned[start_idx:end_idx + 1]

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as err:
        # Fallback: attempt regex extraction or raise
        raise ValueError(f"Could not parse valid JSON from AI response: {str(err)}\nRaw: {raw_text[:200]}")


class GeminiService:
    """Enterprise wrapper for multimodal construction analysis."""

    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-2.5-flash"):
        self.api_key = api_key.strip() if api_key and api_key.strip() else None
        self.model_name = model_name
        self.client = None

        if self.api_key and GENAI_AVAILABLE:
            try:
                self.client = genai.Client(api_key=self.api_key)
            except Exception as e:
                self.client = None
                print(f"[GeminiService] Client init failed: {e}")

    @property
    def is_live(self) -> bool:
        """Returns True if a valid client is configured with an API key."""
        return bool(self.client and self.api_key)

    def analyze_site_safety(self, image_bytes: bytes, mime_type: str = "image/jpeg") -> Tuple[Dict[str, Any], bool, Optional[str]]:
        """
        Multimodal audit of construction site photos for worker PPE compliance under OSHA & IS 456.
        Returns: (result_dict, is_live_result, error_or_info_message)
        """
        if not self.is_live:
            return get_demo_safety_data(), False, "Running in Demonstration Mode (No active API key provided)"

        prompt = """
You are a Principal Construction Safety Auditor and Civil Structural Engineer certified under OSHA (29 CFR 1926) and Bureau of Indian Standards (IS 456:2000, IS 2925, IS 15809, IS 15298, IS 3521).

Analyze the attached construction site image for worker Personal Protective Equipment (PPE) compliance and environmental site hazards.

CRITICAL REQUIREMENT: Output your analysis STRICTLY as a single valid JSON object with NO surrounding markdown commentary, adhering exactly to this schema:
{
  "safety_score": <integer from 0 to 100 based on overall compliance and severity of hazards>,
  "overall_status": "<One of: 'Fully Compliant', 'Moderate Risk - Minor Non-Compliance', 'High Risk - Safety Violations Present', 'Critical Hazard - Immediate Halt Required'>",
  "worker_count": <estimated number of workers visible in the scene, minimum 1>,
  "compliant_workers": <estimated number of workers equipped with all mandatory safety gear>,
  "compliance_percentage": <percentage float between 0.0 and 100.0>,
  "ppe_detection": [
    {
      "item": "<Item name e.g., 'Industrial Safety Helmets (Hard Hats)', 'High-Visibility Safety Vests', 'Steel-Toe Footwear', 'Full-Body Fall Arrest Harnesses', 'Eye & Hearing Protection'>",
      "detected": <true or false>,
      "status": "<'Compliant', 'Partial Non-Compliance', or 'Missing / Not Detected'>",
      "count": <number of workers observed with this item>,
      "required_count": <number of workers requiring this item>,
      "compliance_rate": "<e.g. '100%' or '66%'>",
      "standard": "<OSHA and/or IS standard ref e.g. 'OSHA 1926.100 / IS 2925'>",
      "notes": "<Brief engineering observation on quality, fit, or condition>"
    }
  ],
  "site_hazards": [
    {
      "hazard": "<Specific hazard name e.g., 'Unprotected Deck Perimeter', 'Missing Rebar Impalement Caps', 'Scaffolding Tie-off Missing'>",
      "location": "<Visual location in image e.g., 'Foreground Column Cage', 'Upper Floor Slab Edge'>",
      "severity": "<One of: 'Low', 'Medium', 'High', 'Critical'>",
      "standard_ref": "<Specific OSHA or IS code clause>",
      "impact": "<Risk description to worker safety>",
      "corrective_remedies": "<Concrete actionable engineering corrective remedy>"
    }
  ],
  "summary": "<2-3 sentence executive safety summary with prioritized action items>"
}
Ensure all keys are provided and JSON is perfectly formatted.
"""

        try:
            image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[image_part, prompt]
            )
            parsed = clean_json_response(response.text)
            return parsed, True, None
        except Exception as e:
            # Fallback gracefully to demo data on API error
            demo_data = get_demo_safety_data()
            err_msg = f"Live Gemini API call failed ({str(e)}). Displaying fallback benchmark audit."
            return demo_data, False, err_msg

    def analyze_crack_diagnostics(self, image_bytes: bytes, mime_type: str = "image/jpeg") -> Tuple[Dict[str, Any], bool, Optional[str]]:
        """
        Multimodal diagnostics of concrete/wall crack defects and structural integrity.
        Returns: (result_dict, is_live_result, error_or_info_message)
        """
        if not self.is_live:
            return get_demo_crack_data(), False, "Running in Demonstration Mode (No active API key provided)"

        prompt = """
You are a Senior Forensic Structural Engineer and Concrete Technology Specialist specializing in IS 456:2000, IS 13920, ACI 224, and ASTM structural repair standards.

Inspect the provided photo of the concrete structural element / wall for cracking, spalling, and structural distress.

CRITICAL REQUIREMENT: Output your analysis STRICTLY as a single valid JSON object with NO markdown wrapper or preamble, adhering exactly to this schema:
{
  "defect_type": "<Classify as one of: 'Hairline Shrinkage Cracks', 'Settlement / Foundation Shear', 'Structural Shear Cracking', 'Thermal Expansion & Contraction', 'Spalling & Rebar Corrosion', or 'Masonry Flexural Shear'>",
  "severity_level": "<One of: 'Cosmetic / Low', 'Moderate', 'High', 'Critical'>",
  "urgency": "<One of: 'Immediate Evacuation & Shoring', 'High Urgency - Remediate Within 7 Days', 'Moderate Urgency - Remediate Within 30 Days', 'Routine Monitoring'>",
  "estimated_width_mm": <estimated crack width in mm as a float e.g. 2.4>,
  "crack_depth_mm": <estimated depth or penetration profile in mm as a float>,
  "depth_profile": "<Description of crack propagation into cover or structural rebar core>",
  "structural_risk_score": <integer from 0 to 100 where 100 is impending structural failure>,
  "affected_element": "<e.g., 'Reinforced Concrete Beam-Column Joint', 'RC Shear Wall', 'Suspended Floor Slab', 'Load-Bearing Masonry'>",
  "is_code_violation": "<Detailed note referencing IS 456:2000 Clause 35.3.2 crack width thresholds>",
  "root_causes": [
    "<Technical root cause 1 with engineering mechanics>",
    "<Technical root cause 2>",
    "<Technical root cause 3>"
  ],
  "recommended_repairs": [
    {
      "stage": "<e.g. 'Step 1: Emergency Shoring'>",
      "action": "<Action title e.g. 'Hydraulic Load Relief'>",
      "specification": "<Detailed technical specification e.g., epoxy injection viscosity, ASTM C881 type, grout strength, or CFRP wrap spec>",
      "standards": "<Relevant Indian/International standards e.g. 'IS 456:2000 / ASTM C881'>"
    }
  ],
  "monitoring_protocol": "<Recommendations for tell-tale crack gauges or NDT tests (UPV / Rebound Hammer)>",
  "estimated_repair_cost_inr": "<Estimated cost range in INR e.g. '₹1,50,000 - ₹2,20,000'>",
  "estimated_remedy_time_days": "<Estimated duration e.g. '4 - 7 Days'>"
}
"""

        try:
            image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[image_part, prompt]
            )
            parsed = clean_json_response(response.text)
            return parsed, True, None
        except Exception as e:
            demo_data = get_demo_crack_data()
            err_msg = f"Live Gemini API call failed ({str(e)}). Displaying fallback structural diagnostics."
            return demo_data, False, err_msg

    def chat_construction_assistant(
        self,
        prompt: str,
        history: List[Dict[str, str]],
        weather_condition: str = "Normal"
    ) -> Tuple[str, bool]:
        """
        Multi-turn construction engineering assistant with weather and code awareness.
        """
        if not self.is_live:
            return get_demo_chat_response(prompt, weather_condition), False

        system_instruction = f"""
You are the Multimodal Construction Intelligence Platform Resident Chief Engineer.
You have 25+ years of experience in structural civil engineering, site execution, CPM/PERT scheduling, quantity surveying, and site safety.
You are intimately familiar with:
- Bureau of Indian Standards: IS 456:2000 (Plain & Reinforced Concrete), IS 13920 (Ductile Detailing), IS 1893 (Earthquake Resistance), IS 875 (Wind/Imposed Loads), IS 1786 (High Strength Deformed Steel Bars).
- OSHA 29 CFR 1926 Safety Regulations.
- Current active site environmental condition: {weather_condition}.

When providing engineering guidance:
1. Always weave in the active weather condition ({weather_condition}) and its safety implications (e.g. curing protocols in extreme heat, crane shut-off in high wind, formwork wetting, dewatering).
2. Cite specific clauses of IS codes or OSHA standards whenever possible.
3. Keep calculations practical, clear, and actionable for project managers and site engineers.
4. Format with clear Markdown headings, bullet points, and callout tips.
"""

        try:
            # Build conversation contents
            contents = [types.Content(role="user", parts=[types.Part.from_text(text=system_instruction)])]
            
            # Add past turns
            for turn in history[-6:]:  # Keep recent turns for context window efficiency
                role = "user" if turn.get("role") == "user" else "model"
                contents.append(
                    types.Content(role=role, parts=[types.Part.from_text(text=turn.get("content", ""))])
                )
            
            # Current query
            contents.append(
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=f"[Current Weather: {weather_condition}]\n\n{prompt}")]
                )
            )

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=contents
            )
            return response.text, True
        except Exception as e:
            return f"{get_demo_chat_response(prompt, weather_condition)}\n\n*(Notice: Live Gemini API query encountered an error: {str(e)}. Answer synthesized via local engineering knowledge base.)*", False
