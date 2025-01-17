import openai

# Set up OpenAI API key
openai.api_key = "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"

# Summarization example
response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt="Summarize the following: 'Artificial intelligence is a rapidly growing field...'",
    max_tokens=50
)

print(response.choices[0].text.strip())