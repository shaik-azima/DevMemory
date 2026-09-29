import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.environ["HINDSIGHT_BASE_URL"],
    api_key=os.environ["HINDSIGHT_API_KEY"]
)

bank_id = os.environ["HINDSIGHT_BANK_ID"]

client.retain(
    bank_id=bank_id,
    content="A Docker deployment failed because port 5000 was already in use. Stopping the process using port 5000 fixed the issue."
)

print("Memory stored successfully!")

results = client.recall(
    bank_id=bank_id,
    query="What happened with the previous Docker port 5000 problem?"
)

print("\nRelevant memories:")

for memory in results.results:
    print("-", memory.text)

client.close()