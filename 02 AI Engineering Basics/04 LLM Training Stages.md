# LLM Training Stages

1. **Pre-training** (Self-supervised learning)
   - **What**: Self-supervised learning on vast text data.  
   - **Goal**: Build general language understanding by predicting words or tokens.  
   - **Key Aspect**: Creates a broad linguistic foundation for further training.

2. **Supervised Learning (SL)**  
   - **What**: Fine-tuning on labeled datasets (e.g., question-answer pairs).  
   - **Goal**: Align the model with specific tasks, turning a language generator into a chatbot.  
   - **Key Aspect**: Establishes the question-answer format and conversational ability.

3. **Reinforcement Learning (RL)**  
   - **What**: Optimization using an objective reward signal (no human feedback).  
   - **Goal**: Enhance performance on verifiable tasks like reasoning or math.  
   - **Key Aspect**: Crucial for developing chain-of-thought and structured reasoning skills.

4. **Reinforcement Learning from Human Feedback (RLHF)**  
   - **What**: Refinement via a reward model trained on human preferences (involves PPO).
   - **Goal**: Improve subjective qualities like helpfulness, safety, or coherence.  
   - **Key Aspect**: Aligns the model with human values, using a two-step process (reward model + RL).

Each stage builds on the last, transforming a raw language model into a task-oriented, reasoning-capable, and human-aligned chatbot.

This reflects the most common and well-established sequence for training LLMs. Even the last 2 stages are generally doen in this order. RL often focuses on sharpening core capabilities (like reasoning), while RLHF polishes the model for deployment.

Note: RLHF is just one way to optimize for human preference. Another is DPO (direct preference optimization).