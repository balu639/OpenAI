import openai
from sk import my_sk
openai.api_key = my_sk

def chat_with_gpt():
    prompt = 'write a small paragraph about newyork'
    response= openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages= [
            {"role": "user", "content":'write a small paragraph about newyork'}

        ]
    )
    print(response.choices[0].message.content)
if __name__ == '__main__':
    chat_with_gpt()