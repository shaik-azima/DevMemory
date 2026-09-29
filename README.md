# DevMemory 🧠

DevMemory is an AI-powered DevOps incident assistant that remembers previous technical problems and their solutions.

Instead of solving every incident from scratch, DevMemory uses persistent memory to recall relevant past incidents and apply those experiences to new problems.

## How It Works

1. User describes a DevOps problem.
2. DevMemory recalls relevant previous incidents using Hindsight.
3. Groq LLM uses the recalled memories to generate a practical response.
4. The new problem and solution are stored back in Hindsight.
5. Future incidents can benefit from previous experiences.

## Example

A previous Docker deployment failed because port `5000` was already in use.

DevMemory remembers that incident and its solution.

If the same problem happens again, DevMemory can recall the previous solution. If the user has a new constraint, such as not wanting to stop the existing service, the AI can adapt the solution, for example by using another host port.

## Architecture

User  
↓  
Streamlit UI  
↓  
DevMemory AI Agent  
↓  
Hindsight Recall  
↓  
Groq LLM  
↓  
Response  
↓  
Hindsight Retain

## Technology Stack

- Python
- Streamlit
- Groq
- Hindsight
- GitHub

## Hindsight Memory

Hindsight is the core memory layer of DevMemory.

It is used to:

- Recall relevant previous DevOps incidents
- Store problems and their solutions
- Provide context to the AI before generating a response
- Build a persistent history of troubleshooting experiences

This allows DevMemory to improve its responses based on previous incidents instead of treating every request as completely new.

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
