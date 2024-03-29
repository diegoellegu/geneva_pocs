#https://github.com/run-llama/llama-hub/tree/main
#https://llamahub.ai/l/file-pdf
import time
from pathlib import Path

from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from llama_index import download_loader
start_time = time.time()  # Registra el tiempo de inicio

PDFReader = download_loader("PDFReader")

loader = PDFReader()
documents = loader.load_data(file=Path('./Acta IV - 03012023.pdf'))

langchain_documents = [d.to_langchain_format() for d in documents]

model_name = "/home/dparrilla/development/modelos/llama-2-7b-chat.Q4_K_M.gguf"

print("Modelo:", model_name)
print("Archivo:", Path('./Acta IV - 03012023.pdf'))

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    model_path=model_name,            # Ruta al modelo LlamaCpp
    temperature=0.75,                 # Controla la aleatoriedad de las predicciones (0.75 es un valor común)
    max_tokens=500,                  # Límite máximo de tokens para la generación de texto
    top_p=1,                           # Umbral acumulativo para el top-p sampling (1 significa que se consideran todas las predicciones)
    #callback_manager=callback_manager, # Objeto CallbackManager para gestionar callbacks durante la generación de texto
    verbose=False, # Modo detallado activado (necesario para pasar al callback manager)
    n_ctx=1200

)

qa_chain = load_qa_chain(llm)
#question="Cual fue el asunto?"
question="What was the date of the meeting?"
answer = qa_chain.run(input_documents=langchain_documents, question=question)
print(question)
print(answer)

end_time = time.time()  # Registra el tiempo de finalización
elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")

