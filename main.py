from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

# Define a model for request data
class OpenAIRequest(BaseModel):
    prompt: str

# Set up OpenAI API key (replace with your actual key)
openai.api_key = "your-api-key"

@app.post("/generate/")
async def generate_text(request: OpenAIRequest):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=request.prompt,
            max_tokens=100
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/ok")
async def ok_endpoint():
    return {"message":"ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)