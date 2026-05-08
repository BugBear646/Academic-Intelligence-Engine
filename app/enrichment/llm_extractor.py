import os
import json

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


DEFAULT_RESPONSE = {

    "name": "",

    "email": "",

    "department": "",

    "expertise": "",

    "research_interests": "",

    "university": ""
}


def clean_json_response(content):

    content = content.strip()

    if content.startswith("```json"):

        content = content.replace(
            "```json",
            ""
        )

    if content.startswith("```"):

        content = content.replace(
            "```",
            ""
        )

    content = content.strip()

    return content


def extract_professor_metadata(

    text,

    extracted_email=None
):

    prompt = f"""
You are an academic research extraction engine.

Extract structured JSON from this professor profile.

IMPORTANT:
- Email is mandatory
- Use the provided extracted email if available
- Return ONLY valid JSON
- No markdown
- No explanation
- No commentary

Required JSON fields:
- name
- email
- department
- expertise
- research_interests
- university

Rules:
- If extracted email is available, use it
- At least one among:
  department,
  expertise,
  research_interests
  should contain value

Extracted Email:
{extracted_email}

Example:

{{
  "name": "John Doe",
  "email": "john@stanford.edu",
  "department": "Strategy",
  "expertise": "Platform Strategy, Innovation",
  "research_interests": "Consumer behavior and enterprise systems",
  "university": "Stanford"
}}

PROFILE TEXT:
{text}
"""

    try:

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0,

            max_tokens=500
        )

        content = response.choices[
            0
        ].message.content

        if not content:

            print(
                "EMPTY LLM RESPONSE"
            )

            return DEFAULT_RESPONSE

        content = clean_json_response(
            content
        )

        if not content.strip():

            print(
                "BLANK CONTENT"
            )

            return DEFAULT_RESPONSE

        print("\nLLM OUTPUT:")

        print(content)

        parsed = json.loads(
            content
        )

        # ----------------------------------------
        # FORCE EMAIL INJECTION
        # ----------------------------------------

        if (
            not parsed.get("email")
            and extracted_email
        ):

            parsed["email"] = (
                extracted_email
            )

        return parsed

    except Exception as e:

        print(
            f"LLM EXTRACTION FAILED: {e}"
        )

        return DEFAULT_RESPONSE