import openai

openai.api_key = ""

"""
You can find model documentation at https://platform.openai.com/docs/models
You can find documentation about completion at https://platform.openai.com/docs/api-reference/completions
"""
if __name__ == "__main__":
    prompt = ""
    try:
        # Make your OpenAI API request here
        openai_response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7
        )
        ai_response = openai_response["choices"][0]["text"]

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
