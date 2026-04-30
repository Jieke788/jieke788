import openai

class CodeRestructureSuggester:
    def __init__(self, openai_key):
        openai.api_key = openai_key

    def generate_suggestions(self, code_snippet):
        prompt = f"Suggest improvements for the following Python code:\n\n{code_snippet}\n\nImprovements:"
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-4 可替换为 GPT-4 的相关引擎
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
