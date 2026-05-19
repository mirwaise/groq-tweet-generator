from groq import Groq

def generate_tweet():
    topic=input('Enter tweet topic: ')
    prompt=f'Write a short engaging tweet about {topic}. Keep it under 280 characters. Make it motivational.'
    client=Groq(api_key='YOUR_GROQ_API_KEY')
    response=client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[{'role':'user','content':prompt}]
    )
    return response.choices[0].message.content

# topic=input('Enter tweet topic: ')
# prompt=f'Write a short engaging tweet about {topic}. Keep it under 280 characters. Make it motivational.'
quote=generate_tweet()
print(quote)


