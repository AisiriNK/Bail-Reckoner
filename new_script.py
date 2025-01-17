from transformers import pipeline

# Load a pre-trained GPT-2 model from Hugging Face
generator = pipeline('text-generation', model='gpt2')

# Generate text
response = generator("Summarize this text: The coupling of computer science and theoretical bases such as nonlinear dynamics and chaos theory allows the creation of 'intelligent' agents, such as artificial neural networks (ANNs), able to adapt themselves dynamically to problems of high complexity. ANNs are able to reproduce the dynamic interaction of multiple factors simultaneously, allowing the study of complexity; they can also draw conclusions on individual basis and not as average trends. These tools can offer specific advantages with respect to classical statistical techniques. This article is designed to acquaint gastroenterologists with concepts and paradigms related to ANNs. The family of ANNs, when appropriately selected and used, permits the maximization of what can be derived from available data and from complex, dynamic, and multidimensional phenomena, which are often poorly predictable in the traditional 'cause and effect' philosophy.", max_length=1000)

# Print the generated text
print(response[0]['generated_text'])
