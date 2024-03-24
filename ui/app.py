import asyncio
import os

import streamlit as st
from dotenv import load_dotenv
from langserve import RemoteRunnable

load_dotenv()
remote_chain = RemoteRunnable(os.getenv("REMOTE_ENDPOINT"))
st.title("Colombian Law Agent")
st.image("assets/flow.png", use_column_width=True)

example_queries = [
    "¿Qué necesito para que mi emprendimiento sea legal?",
    "¿Qué significan la territorialidad y la antijuridicidad en el ámbito penal?",
    "¿Cuáles son mis derechos como trabajador?",
    "¿Qué dice la sentencia T-237 de 2023?",
]


async def send_message(input_text, steps_placeholder):
    inputs = {"input": input_text, "chat_history": []}
    steps_placeholder.markdown("Below, you can see the steps I am taking to answer your query.")
    async for chunk in remote_chain.astream(input=inputs):
        for key, value in chunk.items():
            if key == "__end__":
                steps_placeholder.empty()
                return value["agent_outcome"].return_values["output"]
            else:
                st.markdown(f"#### Output from node '{key}':")
                st.write(value)


async def display_thinking_message(thinking_message):
    base_message = "#### Thinking :brain: "
    dots = "."
    while True:
        thinking_message.markdown(base_message + dots)
        dots += "."
        if len(dots) > 3:
            dots = "."
        await asyncio.sleep(0.5)


async def main():
    user_input = st.selectbox(
        "Enter your query or select an example:",
        [""] + example_queries,
        index=1,
        key="user_input",
        format_func=lambda x: x,
    )

    if st.button("Send"):
        final_answer_container = st.empty()
        steps_placeholder = st.empty()

        with final_answer_container:
            thinking_message = st.empty()
            thinking_task = asyncio.create_task(display_thinking_message(thinking_message))

        response = await send_message(user_input, steps_placeholder)

        thinking_task.cancel()
        thinking_message.empty()

        with final_answer_container:
            st.markdown(f"#### Agent says:\n{response}")


if __name__ == "__main__":
    asyncio.run(main())
