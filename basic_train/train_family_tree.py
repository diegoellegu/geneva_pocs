import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Cargar el modelo preentrenado GPT-2 y el tokenizador
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Datos de ejemplo del árbol familiar
tree_data = """
El padre de Juan es Carlos.
La madre de Juan es María.
Juan tiene un hermano llamado Pedro.
Carlos es hijo único.
"""

# Tokenizar y codificar los datos
input_ids = tokenizer.encode(tree_data, return_tensors="pt")

# Entrenar el modelo con los datos de ejemplo
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
model.train()
for epoch in range(3):  # Ajusta el número de épocas según sea necesario
    outputs = model(input_ids, labels=input_ids)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

# Guardar el modelo entrenado
model.save_pretrained("family_tree_model")

# Cargar el modelo entrenado
loaded_model = GPT2LMHeadModel.from_pretrained("/home/dparrilla/development/ude_proyecto_grado/geneva_pocs/basic_train/family_tree_model/")
loaded_tokenizer = GPT2Tokenizer.from_pretrained("/home/dparrilla/development/ude_proyecto_grado/geneva_pocs/basic_train/family_tree_model/")

# Preguntar al modelo sobre el árbol familiar
question = "¿Quién es el hermano de Juan?"
input_ids = loaded_tokenizer.encode(question, return_tensors="pt")
output = loaded_model.generate(question, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

response = loaded_tokenizer.decode(output[0], skip_special_tokens=True)
print(response)
