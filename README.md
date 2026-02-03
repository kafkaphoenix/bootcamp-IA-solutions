# Movie recommendation System using RAG
This repository contains a Movie Recommendation System that leverages Retrieval-Augmented Generation (RAG) techniques to provide personalized movie recommendations based on user preferences and historical data.

## Dependencies
- Python 3.13
- UV as package and project manager
- LangChain for building the RAG pipeline
- FAISS as Vector database for efficient similarity search (CPU mode but it could be changed to GPU mode if available, modifying the pyproject dependency).
- UMAP for dimensionality reduction (a fork was created to upgrade the library to be compatible with Python 3.13).
- Matplotlib and Seaborn for data visualization.
- Other dependencies are listed in the `pyproject.toml` file.

> Conda environment was provided in the bootcamp, but it wasn't used. The instructions are provided in the INSTRUCTIONS.md file if needed.

## Models
Two options are available for generating embeddings:
- all-mpnet-base-v2 from Sentence Transformers for generating embeddings (selected by default for better accuracy).
- all-MiniLM-L6-v2 from Sentence Transformers for generating embeddings (5x times faster but less accurate).

## Testing
Inside the folder `retrieval/analysis` there are some notebooks to analyze the performance of the system with different configurations:
- Sandbox is used to download the embedding models and to create the FAISS vector database.
- Embeddings loads the FAISS vector database and tests the embedding models performance, first reducing the dimensionality with UMAP and then plotting the results.

> Using vscode the two notebooks can be run as Python files directly.