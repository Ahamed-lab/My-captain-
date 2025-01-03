
import openai

# Replace 'your-api-key' with your OpenAI API key
openai.api_key = "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"


def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=150):
    """
    Generates text based on the given prompt using OpenAI's ChatGPT models.

    Parameters:
        prompt (str): The input prompt for the model.
        model (str): The ChatGPT model to use. Default is "gpt-3.5-turbo".
        max_tokens (int): The maximum number of tokens to generate.

    Returns:
        str: The generated text.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter a prompt: ")
    generated_text = generate_text(user_prompt)
    print("\nGenerated Text:\n", generated_text)

    
