import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)
history=[]
print("bot : hello,how can i help you? ")
while True:

    user_input= input("you :")

    chat_session = model.start_chat(
    history=history
    )

    response = chat_session.send_message(user_input)
    model_response = response.text
    print(f"bot :",model_response)
    print()

    history.append({"role":"user",'part':[user_input]})
    history.append({"role":"bot",'part':[model_response]})
 
 
