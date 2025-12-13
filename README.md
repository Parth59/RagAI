# RAG AI - Vegetable Growing Knowledge Base

A Retrieval-Augmented Generation (RAG) system that enables Q&A over PDF documents about growing vegetables using ChromaDB for vector storage and OpenAI GPT-4o for answer generation.

## Overview

This project consists of two main components:
1. **`fill_db.py`**: Populates a ChromaDB vector database with PDF documents
2. **`ask.py`**: Queries the knowledge base and generates answers using RAG

## Overview

This RAG system:
- Loads PDF documents from a directory
- Splits documents into manageable chunks
- Stores chunks in a persistent ChromaDB vector database
- Retrieves relevant context based on user queries
- Generates accurate answers using GPT-4o with retrieved context

## Features

- 📄 **PDF Document Processing**: Automatically loads all PDFs from a directory
- 🔍 **Semantic Search**: Uses ChromaDB for fast similarity search
- 🤖 **RAG Pipeline**: Combines retrieval with GPT-4o for accurate answers
- 💾 **Persistent Storage**: ChromaDB persists data between sessions
- 📝 **Intelligent Chunking**: Splits documents with overlap for context preservation

## Prerequisites

- Python 3.9 or higher
- OpenAI API key
- PDF documents in the `./data` directory

## Installation

1. Navigate to the project directory:
```bash
cd Luke
```

2. Install required dependencies:
```bash
pip install chromadb langchain-community langchain-text-splitters openai python-dotenv
```

Or use the existing `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project directory with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Getting API Keys

- **OpenAI API Key**: Sign up at [platform.openai.com](https://platform.openai.com) and create an API key

## Usage

### Step 1: Populate the Database

First, ensure you have PDF files in the `./data` directory. Then run:

```bash
python fill_db.py
```

This script will:
- Load all PDFs from the `./data` directory
- Split them into chunks (300 characters with 100 character overlap)
- Store them in a ChromaDB collection named `growing_vegetables`
- Create a persistent database at `./chroma_db`

**Note**: You only need to run this once, or when you add new PDFs to the `./data` directory.

### Step 2: Query the Knowledge Base

Run the Q&A script:

```bash
python ask.py
```

The script will:
- Prompt you for a question about growing vegetables
- Search the ChromaDB for the 4 most relevant document chunks
- Use GPT-4o to generate an answer based on the retrieved context
- Display the answer

## Project Structure

```
Luke/
├── fill_db.py          # Script to populate ChromaDB with PDFs
├── ask.py              # Script to query the knowledge base
├── data/               # Directory containing PDF documents
│   ├── parthkanakya_newsbreak.pdf
│   ├── pdffile.pdf
│   └── r37_parthKanakiya.pdf
├── chroma_db/          # Persistent ChromaDB storage (created automatically)
├── .env                # Environment variables (create this)
└── requirements.txt    # Python dependencies
```

## How It Works

### fill_db.py - Database Population

1. **PDF Loading**: Uses `PyPDFDirectoryLoader` to load all PDFs from `./data`
2. **Text Splitting**: 
   - Chunk size: 300 characters
   - Overlap: 100 characters (for context preservation)
3. **Storage**: Stores chunks in ChromaDB with:
   - Document content
   - Metadata (source file, page numbers, etc.)
   - Unique IDs

### ask.py - Query & Answer

1. **User Input**: Prompts for a question
2. **Retrieval**: Queries ChromaDB for 4 most relevant chunks
3. **Context Building**: Formats retrieved documents as context
4. **Answer Generation**: Uses GPT-4o with:
   - System prompt instructing to answer only from context
   - Retrieved documents as context
   - User's question

## Dependencies

- `chromadb`: Vector database for storing and querying embeddings
- `langchain-community`: PDF document loader
- `langchain-text-splitters`: Text chunking utilities
- `openai`: OpenAI API client for GPT-4o
- `python-dotenv`: Environment variable management

## Customization

### Changing Chunk Size

Modify line 10 in `fill_db.py`:
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Larger chunks
    chunk_overlap=150,   # More overlap
    length_function=len,
    is_separator_regex=False
)
```

### Changing Retrieval Count

Modify line 17 in `ask.py` to retrieve more/fewer chunks:
```python
results = collection.query(
    query_texts=[userquery],
    n_results=6  # Get 6 chunks instead of 4
)
```

### Changing the Model

Modify line 34 in `ask.py`:
```python
model="gpt-4o-mini"  # Cheaper, faster option
```

### Changing Collection Name

Modify the collection name in both files:
- `fill_db.py` line 6: `name="your_collection_name"`
- `ask.py` line 11: `name="your_collection_name"`

### Changing Data Directory

Modify line 8 in `fill_db.py`:
```python
loader = PyPDFDirectoryLoader("./your_data_directory")
```

## Example Queries

- "How do I grow tomatoes?"
- "What is the best soil for vegetables?"
- "When should I plant seeds?"
- "How often should I water my plants?"

## Troubleshooting

- **"No module named 'chromadb'"**: Install dependencies with `pip install -r requirements.txt`
- **"API key not found"**: Ensure your `.env` file exists and contains `OPENAI_API_KEY`
- **"No PDFs found"**: Check that PDF files exist in the `./data` directory
- **"Collection not found"**: Run `fill_db.py` first to create the database
- **Empty results**: The query might not match any documents. Try rephrasing or checking if documents were loaded correctly

## Re-populating the Database

If you add new PDFs or want to refresh the database:

1. Delete the `chroma_db` directory (optional, to start fresh)
2. Add new PDFs to `./data`
3. Run `fill_db.py` again

The `upsert` operation will update existing documents and add new ones.

## Limitations

- Currently only supports PDF documents
- Limited to English text
- Requires documents to have extractable text (not scanned images)
- ChromaDB uses default embeddings (can be customized)
- Limited by OpenAI API rate limits and costs

## Future Enhancements

- Support for other document formats (Word, TXT, etc.)
- Web interface for easier interaction
- Conversation history/memory
- Custom embedding models
- Multi-language support
- Batch query processing

## License

This project is for educational purposes.

## Acknowledgments

- Built with [ChromaDB](https://www.trychroma.com/) for vector storage
- Uses [LangChain](https://www.langchain.com/) for document processing
- Powered by [OpenAI GPT-4o](https://openai.com/) for answer generation
