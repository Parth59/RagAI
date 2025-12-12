from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

chromadb_client = chromadb.PersistentClient(path="./chroma_db")
collection = chromadb_client.get_or_create_collection(name="growing_vegetables")

loader = PyPDFDirectoryLoader("./data")
raw_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100,length_function=len,is_separator_regex=False)
chunks = text_splitter.split_documents(raw_documents)


documents = []
metadata= []
ids = []

i=0
for chunk in chunks:
    documents.append(chunk.page_content)
    metadata.append(chunk.metadata)
    ids.append(f"ID{i}")
    i+=1

collection.upsert(
    documents=documents,
    metadatas=metadata,
    ids=ids
)