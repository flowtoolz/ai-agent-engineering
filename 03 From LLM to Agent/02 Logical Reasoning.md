# Logical Reasoning

## Chain of Thought (CoT)

Chain-of-thought (CoT) reasoning is an advanced technique where models generate step-by-step reasoning to solve complex problems. The paradigms used to achieve CoT are:

- Prompt Engineering: Just using the right prompt can nudge the model to lay out a detailed chain of reasoning and thereby actually perform better on reasoning benchmarks
- Supervised Learning (SL): Initially, models are trained on datasets with labeled examples of reasoning steps. For instance, a math problem might include both the question and a detailed solution with each intermediate step.
- Reinforcement Learning from Human Feedback (RLHF): After SL establishes the base, RLHF is often used to refine the reasoning quality. Human feedback acts as rewards to improve the coherence and accuracy of the generated reasoning.
- Pure RL (without human feedback): The model is trained to reason step-by-step on tasks with clear right/wrong answers (e.g., math, coding), receiving rewards based on correctness. Allows to trade inference time for accuracy, allowing them to "think" more deeply and refine their reasoning during inference. This has led to features like "Think" and "DeepThink" modes.

## Advanced Techniques

- Tree of Thoughts (ToT): A reasoning framework where the model explores multiple possible thought paths, like branches of a tree, to solve complex problems, evaluating and pruning less promising options to focus on the best solutions.
- Group Relative Policy Optimization (GRPO): A reinforcement learning method that optimizes reasoning by comparing and ranking multiple model outputs, refining performance based on relative quality rather than absolute correctness.