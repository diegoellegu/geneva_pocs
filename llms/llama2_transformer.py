# este código utiliza la biblioteca Transformers de Hugging Face para cargar el modelo "Llama-2-7b-chat-hf"
# y generar secuencias de texto a partir de un prompt específico.
# https://huggingface.co/docs/transformers/quicktour
import time

# Importa las clases necesarias de la biblioteca Transformers
from transformers import AutoTokenizer, LlamaForCausalLM
from huggingface_hub import login
import transformers  # Importa el módulo transformers
import torch  # Importa la biblioteca PyTorch para trabajar con tensores

# Define el identificador del modelo
model_id = "meta-llama/Llama-2-7b-chat-hf"
print("Modelo: ", model_id)
#login()

# Carga el tokenizador preentrenado asociado al modelo
tokenizer = AutoTokenizer.from_pretrained(model_id)
print("Tokenizador iniciado")

# Crea un pipeline para generación de texto utilizando el modelo especificado
pipeline = transformers.pipeline(
    "text-generation",  # Tipo de tarea: generación de texto
    model=model_id,  # Especifica el modelo a utilizar
    #torch_dtype=torch.bfloat16,  # Especifica el tipo de datos para tensores PyTorch: BFloat16
    device_map="cpu",  # Especifica el mapeo automático del dispositivo a utilizar
)

print("Pipeline iniciada")  # I

start_time = time.time()  # Registra el tiempo de inicio
# Genera secuencias de texto utilizando el modelo y el pipeline configurado
sequences = pipeline(
    'Que es la inteligenia artifical generativa?',  # Prompt de entrada
    do_sample=True,  # Permite la generación de muestras (no siempre la secuencia más probable)
    top_k=5,  # Limita la elección de las top-k opciones de siguiente palabra durante la generación
    num_return_sequences=1,  # Número de secuencias a devolver
    eos_token_id=tokenizer.eos_token_id,  # Especifica el token de final de secuencia
    max_length=50,  # Especifica la longitud máxima de la secuencia generada
)

print("Sequences iniciada")

end_time = time.time()  # Registra el tiempo de finalización
elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")

# Itera sobre las secuencias generadas e imprime el texto generado para cada una
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

