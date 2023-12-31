import os
import openai

class GPT():
    def __init__(self,
                 model='gpt-4'):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model

    def text_completion_basic(self, prompt):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        result = response['choices'][0]['message']['content']
        return result


def main():
    gpt = GPT()
    result = gpt.text_completion_basic('what is 1+1')
    print(result)

if __name__ == '__main__':
    main()

