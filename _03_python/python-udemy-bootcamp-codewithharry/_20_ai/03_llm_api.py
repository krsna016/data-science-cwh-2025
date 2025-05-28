# key = key
#
# from openai import OpenAI
# client = OpenAI(api_key=key)
#
# response = client.chat.completions.create(
#   model="gpt-4o",
#   messages=[
#         {
#             "role": "user",
#             "content": "complete this chat: Jack: Hey; Jill: How are you?; Jack: now what?; Jill:  ",
#         }
#   ],
#   response_format={
#     "type": "text"
#   },
#   temperature=1,
#   max_completion_tokens=2048,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
#
#
# for choice in response.choices:
#     print(choice.message.content)
