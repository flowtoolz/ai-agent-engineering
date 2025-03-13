# Context Management

Why? token management for cost and performance, improving performance, augmenting additional knowledge

## General Strategies

### 1. Simple Window Sliding
- Keep only last N messages in context
- Oldest messages gradually fall out
- Allows infinite conversation length
- Maintains recent context while limiting tokens
- Cost-effective but loses historical context

### 2. Embedding-Based Selection
- Convert documents/content to vectors
- Find relevant pieces via similarity
- Can use local embedding models (no API cost)
- Enables smart context selection
- Particularly useful for large documentation/codebases

### 3. Pure Reference Retrieval
- Embed only current user query
- Return references/locations instead of generating text
- More like semantic search than chat
- Extremely token-efficient
- Points users to relevant documentation/code

### 4. Model-Driven Information Extraction
- compression through summarization
- Let model extract essential project-specific facts
- Omit what can be inferred from common knowledge
- Build actual information hierarchy
- Creates denser, more relevant context
- Different from pure embedding hierarchies

### 5. Multi-Step Context Navigation
- Model explores context in steps
- Requests specific context as needed
- Like a dialogue with the knowledge base
- Reduces total context needed
- More intelligent than pure retrieval

### 6. Code-Focused Context Management
- Prioritize code in context window
- Compress chat history into concise manual
- Update manual progressively
- Provide manual + relevant code
- Optimize token usage for actual content

## Retrieval-Augmented Generation (RAG)

*Enhancing agents with external knowledge*

- What is RAG? Combining retrieval and generation for grounded responses  
- Core components: embeddings, vector stores, and retrieval pipelines
- Integrating RAG into agent workflows for real-time information access  
- Advanced RAG: dynamic retrieval and relevance filtering  
- RAG as a complement to persistent memory
- naive vs. advanced RAG
- prompt rewriting
- Dense Passage Retrieval (DPR): uses dense vector representations of text passages (or chunks) to improve retrieval accuracy

### Embeddings
- Model-agnostic nature
- Local generation possibility
- Semantic space representation
- Simple geometric comparison (cosine similarity)