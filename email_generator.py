from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse

load_dotenv()  # Load variables from .env file
api_key = os.getenv("OPENAI_API_KEY")

client= OpenAI(api_key=api_key)
prompt_template = '''
system:
You are an expert professional communicator.
user:
Write a short professional email. Replace the placeholders with the provided values.

- Recipient: {{recipient_name}}
- Topic: {{topic}}
- Tone: {{tone}}    # e.g., "friendly", "formal", "concise"
- Call to action: {{cta}}

The email should:
1. Start with a short greeting addressing the recipient by name.
2. Explain the topic in 2–3 sentences.
3. Have a single clear call-to-action sentence based on {{cta}}.
4. Close politely with a one-line sign-off. {{your_name}}

Output only the email body (no extra commentary).


Example 1:
Inputs:
- recipient_name: "Dr. Ahmed"
- topic: "project timeline update for X"
- tone: "formal"
- cta: "please confirm availability for a 30-minute meeting next week"

Expected email:
Dear Dr. Ahmed,

I wanted to update you on the project timeline for X. We completed the initial design phase and are on track to start implementation next Monday. I’ll send weekly progress notes to keep you informed.

Could you please confirm your availability for a 30-minute meeting next week so we can discuss next steps?

Kind regards,
{{your_name}}

---

Example 2:
Inputs:
- recipient_name: "Sara"
- topic: "demo of the new dashboard"
- tone: "friendly"
- cta: "let me know which day this week works for you"

Expected email:
Hi Sara,

I hope you're well! I wanted to invite you to a quick demo of the new dashboard—I'll show the new filters and reports and how they can help your team. The demo takes about 20 minutes.

Please let me know which day this week works for you.

Thanks,
{{your_name}}
'''
def fill_template(template: str, values: dict) -> str:
    filled = template
    for key, val in values.items():
        filled = filled.replace(f"{{{{{key}}}}}", val)
    return filled


def main():
    parser = argparse.ArgumentParser(description="Generate professional emails using OpenAI.")
    parser.add_argument("--recipient", required=True)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--tone", required=True)
    parser.add_argument("--cta", required=True)
    parser.add_argument("--your_name", required=True)
    parser.add_argument("--model", default="gpt-4.1-mini")

    args = parser.parse_args()

    values = {
        "recipient_name": args.recipient,
        "topic": args.topic,
        "tone": args.tone,
        "cta": args.cta,
        "your_name": args.your_name,
    }

    final_prompt = fill_template(prompt_template, values)

    response = client.responses.create(
        model=args.model,
        input=final_prompt,
        max_output_tokens=300,
        temperature=0.2
    )

    print("\nGenerated Email:\n")
    print(response.output_text)

if __name__ == "__main__":
    main()
