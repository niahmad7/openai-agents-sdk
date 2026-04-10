import asyncio
from openai import AsyncOpenAI,OpenAI
from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel

from agents.tracing import set_tracing_disabled

set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model="minimax-m2.5:cloud",
    openai_client=AsyncOpenAI(
        api_key="ollama",
        base_url="http://localhost:11434/v1"
    )
)

history_agent = Agent(
    model=model,
    name="History Tutor",
    instructions="you answer for history questions clearly and concisely"
)

async def main():
    query = "Who built the badshahi moque in Lahore?"
    result = await Runner.run(history_agent, query)
    print(result.final_output)

asyncio.run(main())

# query = "Who built the badshahi moque in Lahore?"
# result = Runner.run_sync(
#     history_agent, query)

# print(result.final_output)