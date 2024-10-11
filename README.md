# QA PDF RAG
It is a RAG system built on top of Llama3, and its local.

# Pre-requisite:
```
1. Ollama should be installed and running
2. respective model i.e. llama3.1 should be pulled and is in serve and run stage.

```

# Run in Local
```
create env: python -m venv venv
activate venv (command may varry system to system) : venv/Source/activate 
intsall required pkgs: pip install -r requirements.txt
run app: python app.py

```

# POST end points:
```
1. /ai:  to test model by asking general query
2. /pdf: To upload pdf 
3. /ask_pdf: to ask questions from pdf

```

# payload: /ai and /ask_pdf
** test via postman **
{
    "query":<question>
}

# payload: /pdf
** test via postman **
-> in postman in body section select form-data:->
key should be 'file' and value should be a pdf file.

# Evaluation:
*** Data Preparation: Prepare a test dataset that includes queries along with expected results. This dataset should be diverse and representative of the types of queries the model will encounter. ***
```
Human Evaluation: Consider conducting qualitative assessments through human reviewers who can judge the relevance and quality of the responses.

A/B Testing: If applicable, compare the RAG model’s performance against baseline models or previous versions to assess improvements.

BLEU or ROUGE: Useful for evaluating generated text against reference text.
```