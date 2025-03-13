## Perceptive AI

* AI that helps perceiving and interpreting existing data

  - Image classification/recognition, object detection with CNNs (e.g., YOLO)
  - Audio perception: speech recognition with RNNs
  - Classification tasks
    - FNNs for basic categorization (e.g., MNIST)
    - Text classification (Spam or not Spam)
    - Discriminative Transformers: BERT-style tasks (e.g., sentiment analysis)
  - maybe mention Torque Clustering here?

- **4 basic paradigms:**
	- Classification: Recognizes which category a data point belongs to (e.g., labeling an email as "spam" or "not spam").
	- Clustering: Identifies natural groupings in data without predefined labels (e.g., grouping customers by behavior).
	- Dimensionality Reduction: Simplifies data by extracting its most important features (e.g., reducing a dataset to key variables).
	- Anomaly Detection: Spots outliers or irregularities (e.g., detecting fraud in transactions).

## Predictive AI

- AI that helps predicting existing or future data
- **3 basic paradigms:**
  - Regression: Predicts continuous numeric values (e.g., forecasting a house price).
  - Sequence Prediction: Forecasts the next items in a sequence (e.g., predicting the next word in a sentence).
  - Reinforcement Learning: Learns to make decisions to maximize rewards (e.g., training a robot to navigate).

## Generative AI

- Generative Adversarial Networks (GANs): image/video synthesis
- Diffusion Models: high-quality image creation
- Large Language Models (LLMs): text generation
  - Self-supervised learning, historical: Autoregressive models

## Agentic AI

- From LLMs to Agents (building autonomous systems)
- Prompt engineering: crafting effective LLM inputs
- Context management: token efficiency, Memory, RAG
- Flow orchestration: managing multi-step tasks
- Tool use: integrating external tools/APIs with LLMs

## Embodied AI

- Navigation and planning: pathfinding, SLAM (Simultaneous Localization and Mapping)
- Real-time control: policy networks for robotic actions
- RLHF: refining embodied systems with human feedback
- Simulation: Training on simulators (e.g., Gazebo, MuJoCo)