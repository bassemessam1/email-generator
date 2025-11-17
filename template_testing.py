from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  prompt={
    "id": "pmpt_69187ebdd0a88190b8fbb5c57a2a26bf091cbc031e057111",
    "version": "2",
    "variables": {
      "recipient_name": "Ahmed",
      "topic": "discuss the progress of the project",
      "tone": "neutral",
      "cta": "set up a meeting with customers",
      "your_name": "Bassem"
    }
  }
)
print(response.output_text)