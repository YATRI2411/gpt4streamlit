import streamlit as st
from openai import OpenAI


client = OpenAI(api_key="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")


st.title("Text Helper with GPT")

# Dropdown
task = st.selectbox(
    "Select Task",
    ["Text to Text", "Text to Image"]
)

user_input = st.text_area("Type your message:")

if st.button("Ask"):

    # ---------- TEXT TO TEXT ----------
    if task == "Text to Text":
        if user_input:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            st.subheader("Response:")
            st.write(response.choices[0].message.content)

    # ---------- TEXT TO IMAGE ----------
    elif task == "Text to Image":
        if user_input:
            image_response = client.images.generate(
                model="black-forest-labs/FLUX.1-dev",
                prompt=user_input,
                
            )

            image_url = image_response.data[0].url
            st.subheader("Generated Image:")
            st.image(image_url)






            

# from openai import OpenAI
# import streamlit as st
# import os
# from huggingface_hub import InferenceClient

# client = OpenAI(api_key="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")

# st.title("Simple GPT Demo")
# #user se input
# user_input = st.text_input("Enter Your message: ")

# if st.button("Ask"):
#     if user_input:
#         response = client.chat.completions.create(
#             model='gpt-4o-mini',
#             messages=[
#                 {'role': 'user', 'content': user_input}
#             ]
#         )
#         st.write("AI Response:")
#         st.write(response.choices[0].message.content)

# response = client.chat.completions.create(
#     model = 'gpt-4o-mini',
#     messages=[
#         {'role':'user', 'content': user_text}
#     ]
# )

# print('\nAI Response:\n')
# print(response.choices[0].message.content)