import re, torch, torch.nn as nn

torch.manual_seed(42)

# raw training data: documents and their class labels

docs = [
    "Movies are fun for everyone.",
    "Watching movies is great fun.",
    "Enjoy a great movie today.",
    "Research is interesting and important.",
    "Learning math is very important.",
    "Science discovery is interesting.",
    "Rock is great to listen to.",
    "Listen to music for fun.",
    "Music is fun for everyone.",
    "Listen to folk music!"
]

class_names = ["cinema", "music", "science"]
num_classes = len(class_names)
correct_class_indices = [1, 1, 1, 3, 3, 3, 2, 2, 2, 2]

# vectorize the training data

def tokenize(text):
    return re.findall(r"\w+", text.lower())

def get_vocabulary(texts):
    tokens = {token for text in texts for token in tokenize(text)}
    return {word: idx for idx, word in enumerate(sorted(tokens))}

vocabulary = get_vocabulary(docs)

def doc_to_bow(doc, vocabulary):
    tokens = set(tokenize(doc))
    bow = [0] * len(vocabulary)
    for token in tokens:
        if token in vocabulary:
            bow[vocabulary[token]] = 1
    return bow

doc_vectors = torch.tensor(
    [doc_to_bow(doc, vocabulary) for doc in docs],
    dtype=torch.float32
)

correct_class_indices = torch.tensor(correct_class_indices, dtype=torch.long) - 1

# build the model

input_dim = len(vocabulary)
hidden_dim = 50

class SimpleClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, num_classes)
       
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
    
model = SimpleClassifier(input_dim, hidden_dim, num_classes)

# train the model

loss_function = nn.CrossEntropyLoss()   
gradient_descent = torch.optim.SGD(model.parameters(), lr=0.001)

print("Beginning training ...")

for step in range(1, 10000 + 1):
    gradient_descent.zero_grad()
    predicted_class_indices = model(doc_vectors)
    loss = loss_function(predicted_class_indices, correct_class_indices)
    loss.backward()
    gradient_descent.step()
    
    if step == 1 or step % 1000 == 0:
        print(f"Step {step}, Loss: {loss.item():.4f}")

# do some inference

print("Beginning inference ...")

new_docs = [
    "I love to watch movies.",
    "I hate math.",
    "I love to listen to music.",
    "I hate science."
]

new_doc_vectors = torch.tensor(
    [doc_to_bow(doc, vocabulary) for doc in new_docs],
    dtype=torch.float32
)

with torch.no_grad():
    outputs = model(new_doc_vectors)
    predicted_class_indices = torch.argmax(outputs, dim=1) + 1

for i, new_doc in enumerate(new_docs):
    print(f"{new_doc}: {class_names[predicted_class_indices[i].item() - 1]}")

print("Done ✅")