import os
import asyncio
from dotenv import load_dotenv
from groq import Groq
from hindsight_client import Hindsight

load_dotenv()

groq = Groq(api_key=os.environ["GROQ_API_KEY"])

BANK_ID = os.environ["HINDSIGHT_BANK_ID"]
BASE_URL = os.environ["HINDSIGHT_BASE_URL"]
API_KEY = os.environ["HINDSIGHT_API_KEY"]


async def memory_operation(user_message, answer=None):
    client = Hindsight(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    try:
        if answer is None:
            # Recall previous memories
            return await client.arecall(
                bank_id=BANK_ID,
                query=user_message
            )

        # Store the new experience
        await client.aretain(
            bank_id=BANK_ID,
            content=f"""
Problem:
{user_message}

Solution provided:
{answer}
"""
        )
    finally:
        await client.aclose()


def ask_agent(user_message):

    # Hindsight recall
    memories = asyncio.run(
        memory_operation(user_message)
    )

    memory_text = "\n".join(
        f"- {memory.text}"
        for memory in memories.results
    )

    prompt = f"""
You are DevMemory, an AI DevOps assistant.

Relevant previous memories:
{memory_text}

Current problem:
{user_message}

Give a concise practical answer in 3-6 bullet points.

Use previous memories when they are relevant.
If a previous solution is relevant, explain how it applies.
If there is no useful memory, solve the problem normally.
Do not invent previous experiences.
"""

    response = groq.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    # Store new experience
    asyncio.run(
        memory_operation(user_message, answer)
    )

    return {
        "memories": memories.results,
        "answer": answer
    }


if __name__ == "__main__":
    print("DevMemory AI Agent")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = ask_agent(user_input)

        print("\n🧠 Relevant Memory:")
        for memory in result["memories"]:
            print("-", memory.text)

        print("\n🤖 DevMemory:")
        print(result["answer"])
