from flask import Flask, request
from langchain.prompts import PromptTemplate

from Utility import get_response_from_query, load_llm, load_split_embed_save_vector_store_func, prompt, retreiver_func, vector_store_func

app = Flask(__name__)

folder_path = "db"
#load llm
cached_llm=load_llm()
#create pdf directory


#test the model
@app.route("/ai", methods=["POST"])
def aiPost():
    print("Post /ai called")
    json_content = request.json
    query = json_content.get("query")

    print(f"query: {query}")

    response = cached_llm.invoke(query)

    print(response)

    response_answer = {"answer": response}
    return response_answer

#ask qa rom pdf
@app.route("/ask_pdf", methods=["POST"])
def askPDFPost():
    print("Post /ask_pdf called")
    json_content = request.json
    query = json_content.get("query")

    print(f"query: {query}")

    response_answer = get_response_from_query(query,folder_path)
    return response_answer

#upload pdf
@app.route("/pdf", methods=["POST"])
def pdfPost():
    file = request.files["file"]
    file_name = file.filename
    save_file = "pdf/" + file_name
    file.save(save_file)
    print(f"filename: {file_name}")

    response = load_split_embed_save_vector_store_func(save_file,folder_path,file_name)
    return response


def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    start_app()
