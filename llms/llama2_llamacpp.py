#https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
#https://python.langchain.com/docs/integrations/llms/llamacpp
import time

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp

# Ruta al modelo LlamaCpp
model_name = "/home/dparrilla/development/modelos/llama-2-7b-chat.Q4_K_M.gguf"

# Plantilla de prompt con una estructura específica
template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

# Configuración de la plantilla del prompt
prompt = PromptTemplate(template=template, input_variables=["question"])

# Gestión de callbacks que admiten transmisión de tokens
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Creación de una instancia del modelo de lenguaje LlamaCpp
# Creación de una instancia del modelo de lenguaje LlamaCpp
llm = LlamaCpp(
    model_path=model_name,            # Ruta al modelo LlamaCpp
    temperature=0.75,                 # Controla la aleatoriedad de las predicciones (0.75 es un valor común)
    max_tokens=2000,                  # Límite máximo de tokens para la generación de texto
    top_p=1,                           # Umbral acumulativo para el top-p sampling (1 significa que se consideran todas las predicciones)
    callback_manager=callback_manager, # Objeto CallbackManager para gestionar callbacks durante la generación de texto
    verbose=True,                      # Modo detallado activado (necesario para pasar al callback manager)
)

# Definición de un prompt específico
prompt_text = """
Question: Que es la inteligenia artifical generativa?
"""
start_time = time.time()  # Registra el tiempo de inicio
# Uso del modelo LlamaCpp para generar una respuesta al prompt
llm(prompt_text)
end_time = time.time()  # Registra el tiempo de finalización
elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")

