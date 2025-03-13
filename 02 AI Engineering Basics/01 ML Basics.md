# ML Basics

- Core concepts: neurons, layers, weights, biases
- Forward propagation and computation
- Backpropagation and weight updates
- Activation functions: sigmoid, ReLU, etc.
- Loss functions and optimization: gradient descent
- Regularization Techniques: like dropout or L2 regularization
- Embeddings: vector representations (e.g., word2vec, BERT)
- Datasets: pretraining, data splits

## Training

### Language Model Training Data

the dataset is often treated as a large stream of text, ignoring document boundaries. The training process handles document boundaries pragmatically. Some datasets might insert separators (e.g., [SEP]), but typically, the stream is continuous, and learning happens within the context window, not per document. **document-aware pre-training** helps for specific domains (e.g., legal texts) but isn’t universally superior.

### Parameter Initialization

In general ML training, initial parameters are mostly set random, but some areas initialize them:

- Xavier/Glorot Initialization: Common in deep networks, sets initial weights based on layer size to stabilize gradients.
- Pre-trained Models: In transfer learning (e.g., computer vision with ImageNet), initial parameters come from a prior model, not random.
- K-Means Clustering: Initial centroids can be seeded with data statistics (e.g., k-means++) rather than random.
- Gaussian Mixture Models: Parameters might start with estimates from data distributions.

Actual initialization happens where prior knowledge or stability matters, unlike LLMs where random starts leverage vast data and computation to find effective solutions.

### Loss Function

the loss function typically computes a distance—usually cross-entropy loss—between the model's predicted probability vector and the actual correct token/class/answer in the training data. It measures how well the model's output distribution matches the correct answer, penalizing deviations in probability across all possible answers.

### Gradient Descent

...

### Local Optima

Local optima in high dimensional models (like LLMs) are less significant than in lower-dimensional models. The ultra-high dimensionality of the parameter space (often billions) means the optimization landscape is vast and complex, with many saddle points rather than strict local minima. Gradient-based methods like SGD can often escape these due to the high-dimensional geometry and noise in gradients, making local optima less of a practical barrier to finding good solutions.

### Sampling

- Frage: der output vom Modell ist eine Wahrscheinlichkeitsverteilung über alle tokens. Warum ist das gewählte token bei inference dann aber quasi zufällig? Warum und in welchem masse und nach welchem Algorithmus wird das token dann gewählt? Es wäre ja nicht zufällig wenn einfach das wahrscheinlichste gewählt werden würde. Aber würde das wahrscheinlichste nicht auch die beste Antwort ergeben?
- Antwort: Sampling!

## Key Architectures
- Feedforward Neural Networks (FNNs): classification and regression
- Convolutional Neural Networks (CNNs): image processing
- Recurrent Neural Networks (RNNs): sequences and LSTMs
- Transformers: attention mechanisms and scalability