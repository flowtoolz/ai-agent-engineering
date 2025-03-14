# Agent Engineering Tools

## Infrastructure Layers

1. Base Layer: LLM Access
2. Middle Layer: Agent/Chain Primitives
3. Top Layer: Pre-built Solutions

## General Notes

- Using agents to build agents (low code tools, Cursor ...)
- Frameworks overview: TensorFlow and PyTorch basics
- TensorFlow: structure and use cases
- PyTorch: flexibility and dynamic computation
- Hugging Face (models), ONNX (interoperability), Replicate (hosting models)

## LlamaIndex

LlamaIndex is an SDK for connecting LLMs to external data sources. It streamlines indexing, chunking, querying, and retrieving external data (e.g., documents, databases) to augment LLM responses with relevant context, making it a go-to tool for RAG workflows.

While being focussed on data-related tasks ("data agent"), LlamaIndex also supports building full agents with task planning, tool use, and memory in addition to RAG.

## LangChain

LangChain is a framework for building AI applications that can use tools, retain context, retrieve knowledge and orchestrate workflows.

### Core Components

- Tools (atomic operations)
- Chains (composed operations)
- Agents (autonomous orchestrators)
- Memory systems

### Composition Patterns

- Hierarchical tool composition
- Chain nesting and reuse
- Agent-tool interaction
- Flow definition and control

### Implied Architecture

LangChain is designed to run heavily on the backend.

- Backend Focus: LangChain excels at orchestrating AI logic (e.g., chains, agents), integrating with data sources (e.g., vector stores), and accessing external tools securely. These tasks require significant compute resources and centralized control, making the backend the natural home.
- Frontend Role: The frontend is limited to sending requests (e.g., user queries) to the backend and displaying responses, with little involvement in AI logic or tool access.

This implies a backend-heavy setup where the backend handles the “heavy lifting” (AI reasoning, data management, tool integrations), and the frontend focuses on user interaction.

## Other AI Engineering Eco Systems

- AutoGen: A framework for building multi-agent systems where LLMs collaborate to solve tasks, offering flexibility for complex workflows and agent interactions.
- CrewAI: Focuses on orchestrating collaborative AI agents with defined roles, enabling task delegation and execution, similar to a team-based approach.
- Haystack: An open-source framework specializing in RAG and search-driven applications, with strong support for pipelines and data retrieval, competing in data-centric agent use cases.