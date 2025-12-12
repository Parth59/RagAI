import chromadb
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = "./data"
CHROMA_DB_PATH = "./chroma_db"

chromadb_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chromadb_client.get_or_create_collection(name="growing_vegetables")

userquery = input("What do you want to know about growing vegetables?")

results = collection.query(
    query_texts=[userquery],
    n_results=4
)

client = OpenAI()

system_prompt = """
You are a helpful assistant. 
You answer questions only based on the context provided from knowledge I'm providing you.
You don't use your internal kowledge and you don't make up answers.
If you don't know the answer, just say: I don't know. 
-------------------
The data:
"""+str(results['documents'])

print(results['documents'])

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": userquery}
    ]
)
print(response.choices[0].message.content)