from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-4-mini-instruct",
    device_map="mps",
    torch_dtype="auto",
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-4-mini-instruct")

# Set pad token explicitly to avoid warning
tokenizer.pad_token = tokenizer.eos_token

prompt = "Write an email apologizing to Sarah for the tragic gardening mishap. Explain how it happened.<|assistant|>"

# Tokenize with proper inputs
inputs = tokenizer(prompt, return_tensors="pt").to("mps")

# Generate text
outputs = model.generate(
    **inputs,
    max_new_tokens=100,
)

# Decode the generated text
print(tokenizer.decode(outputs[0]))

