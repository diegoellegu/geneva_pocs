import time

#https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
#https://python.langchain.com/docs/integrations/providers/ctransformers
#https://python.langchain.com/docs/integrations/llms/ctransformers

#Prueba con LLama2 de thebloke gguf descargado localmente
from ctransformers import AutoModelForCausalLM

# Ruta al directorio que contiene el modelo
model_name = "/home/dparrilla/development/modelos/"

# Cargar el modelo de lenguaje de causalidad LLM
# Se especifica el archivo del modelo ("llama-2-7b-chat.Q4_K_M.gguf") y el tipo de modelo ("llama")
# Además, se configura el parámetro gpu_layers para la aceleración de GPU
llm = AutoModelForCausalLM.from_pretrained(
    model_name,
    model_file="llama-2-7b-chat.Q4_K_M.gguf",
    model_type="llama",
    gpu_layers=0  # Número de capas a offload a GPU. Se establece en 0 si no hay aceleración de GPU disponible.
)
start_time = time.time()  # Registra el tiempo de inicio

# Generar texto a partir de un prompt específico
output_text = llm("Que es la inteligenia artifical generativa?")

end_time = time.time()  # Registra el tiempo de finalización
elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")


# Imprimir el texto generado
print(output_text)

