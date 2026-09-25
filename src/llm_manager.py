from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1:8b"
)


def generer_reponse(question, contexte):

    prompt = f"""
Tu es un assistant intelligent spécialisé dans l'analyse et l'explication
de documents.

Tu dois répondre à la question de l'utilisateur en utilisant en priorité
les informations présentes dans le CONTEXTE fourni.

RÈGLES :

- Analyse attentivement le contexte avant de répondre.
- Si le contexte contient suffisamment d'informations pour répondre,
  réponds directement et explique clairement la réponse.
- Reformule les informations du document lorsque cela améliore
  la compréhension.
- Si le contexte contient un exemple, une définition, une formule
  ou une explication importante, utilise-le dans ta réponse.
- Ne demande jamais à l'utilisateur de fournir à nouveau le document :
  le contexte fourni correspond déjà au document sélectionné.
- Si les informations nécessaires ne sont réellement pas présentes
  dans le contexte, indique-le clairement.
- Dans ce cas, tu peux ajouter une courte explication générale si elle
  peut être utile, mais indique clairement qu'elle ne provient pas
  du document.
- Ne présente jamais une information générale comme provenant du document.

CONTEXTE DU DOCUMENT :
{contexte}

QUESTION :
{question}

Réponds directement à la question de l'utilisateur.
"""

    reponse = llm.invoke(prompt)

    return reponse.content