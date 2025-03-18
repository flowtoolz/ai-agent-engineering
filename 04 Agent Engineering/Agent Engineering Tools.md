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

### LangSmith

LangSmith and LangChain are complementary tools from the same ecosystem, developed by the LangChain team. While LangChain focuses on building LLM applications, LangSmith enhances development and maintenance by providing observability and testing capabilities. LangSmith integrates seamlessly with LangChain, automatically logging traces and formatting data when used together, but it’s also standalone—developers can use it with any LLM application, regardless of whether LangChain is involved. LangChain is the construction toolkit and LangSmith is the diagnostic and quality control system.

### LangGraph

LangGraph builds upon LangChain. It’s not a standalone tool but an extension or evolution of LangChain, designed to address specific needs that LangChain alone doesn’t fully optimize for. LangGraph leverages LangChain’s core components—like LLMs, memory, and tools—but adds a graph-based architecture to handle stateful, multi-step workflows with greater control and structure. Essentially, it’s a specialized layer on top of LangChain, enhancing its capabilities for complex, iterative, or multi-agent applications while relying on LangChain’s foundational infrastructure.

## Other AI Engineering Eco Systems

- AutoGen: A framework for building multi-agent systems where LLMs collaborate to solve tasks, offering flexibility for complex workflows and agent interactions.
- CrewAI: Focuses on orchestrating collaborative AI agents with defined roles, enabling task delegation and execution, similar to a team-based approach.
- Haystack: An open-source framework specializing in RAG and search-driven applications, with strong support for pipelines and data retrieval, competing in data-centric agent use cases.
- AutoGPT ?

## Low-Code Agent Building Tools

- Vertex AI by Google: https://cloud.google.com/vertex-ai
- Dify.ai (open source, https://dify.ai)
- Glide (?) https://www.glideapps.com/agents
- https://www.bizway.io/
- https://relevanceai.com   
- https://www.lyzr.ai
- https://www.flutterflow.io (for apps in general)