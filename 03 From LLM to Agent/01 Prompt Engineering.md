# Prompt Engineering

*Crafting prompts to steer agent performance*

- The importance of prompts in agent interactions  
- Base model behavior guidance
- Techniques: zero-shot, few-shot, and chain-of-thought prompting
- System messages and role definition
- instruction design
- Output formatting and structure
- Avoiding common pitfalls: ambiguity, over-complexity, and drift

## The Role of Model Temperature

**Temperature *is* a hugely undervalued, low-hanging fruit.**

The reason: the vast majority of people's experience with LLMs comes from the **conversational chat interface**.

### The Conversational Chat Paradigm

In a chatbot context (like ChatGPT, Claude etc.), the primary goal is **engagement and creativity.**

*   **You want variety:** If you ask the same question twice, you don't want the exact same canned response.
*   **You want fluency:** The conversation needs to flow naturally.
*   **You want creativity:** For brainstorming, writing stories, or exploring ideas, a high temperature is a feature, not a bug.

This paradigm has trained millions of users (and even many developers) to think of LLMs as creative partners where a bit of randomness is essential. This is why the default temperature for most models is high (`~0.7` to `1.0`).

### The Shift to the Agentic / Tool-Use Paradigm

Now, we are moving into a new era of using LLMs as the reasoning engine for **agents and tools.** In this paradigm, the goals are the complete opposite of a creative chatbot.

The primary goals are:

*   **Reliability**
*   **Predictability**
*   **Accuracy**
*   **Deterministic Behavior**

Achieving these goals requires a fundamental shift in thinking: **turn the temperature to zero.**

Because the "chatbot" use case was the first to become mainstream, the mental model of "LLMs should be a bit random" has stuck, even when it's counterproductive for the emerging, more powerful use cases in software development and automation.

This is a major shift in understanding. Recognizing the power of `temperature=0` is a key step in moving from using an LLM as a "creative toy" to using it as a "reliable engineering tool." It's the simplest and most effective lever for making agents and automated workflows more accurate and trustworthy.