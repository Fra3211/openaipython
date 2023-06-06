import openai

openai.api_key = ""

"""
You can find model documentation at https://platform.openai.com/docs/models
You can find documentation about completion at https://platform.openai.com/docs/api-reference/chat
"""
if __name__ == "__main__":
    prompt = ""
    try:
        # Make your OpenAI API request here
        openai_response = chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                                         messages=[{"role": "user",
                                                                                    "content": prompt}])
        ai_response = openai_response["choices"][0]["message"]["content"]

    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        ai_response = f"OpenAI API returned an API Error \n {e}"
    except openai.error.APIConnectionError as e:
        # Handle connection error here
        ai_response = f"Failed to connect to OpenAI API \n {e}"
    except openai.error.RateLimitError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        ai_response = f"OpenAI API request exceeded rate limit \n {e}"
    except openai.error.InvalidRequestError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        ai_response = f"OpenAI API invalid request error \n {e}"

    print(ai_response)
