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

## Running the Movie Recommendation System
- Run the following command to start mlflow server and the project:
```bash
make start-movie-recommender
```

Results can be seen in the mlflow UI at `http://localhost:8080/#/experiments`

> If the test notebooks have been run before, the `retrieval/.cache` folder has to be deleted.

## Exercise
- The function `clean_query_txt_v2` in the file `retrieval/retrieval_pipeline_utils.py` has been modified to improve the text preprocessing for Spanish queries. The changes include adapting the stop words to Spanish and adding lemmatization using spaCy with a Spanish lemmatizer.
- The function `process_movie_info` has been added to the file `retrieval/indexing_pipeline_utils.py` to create a comprehensive text representation of movie information for indexing purposes.
- The default embedding model has been changed to `all-mpnet-base-v2` in the `retrieval/config.py` file for better accuracy in recommendations.
- UV has been set as the package and project manager, and a `pyproject.toml` file has been created to manage dependencies and project configuration.
- A Makefile has been added to facilitate common tasks such as setting up the environment and running the movie recommendation system.

> Lemmatization rules requires executing `uv run python -m spacy_spanish_lemmatizer download wiki` and `uv run python -m spacy download es_core_news_sm` before running the project for the first time.

## Results
- First try was using the default embedding model `all-MiniLM-L6-v2` and default preprocessing. Relevant movie found at the top 10 is 23.7%  and mmr10 is 0.163.

- Second try was using the embedding model `all-mpnet-base-v2`. Relevant movie found at the top 10 is 24.3% and mmr10 is 0.162.

- Third try was using the embedding model `all-MiniLM-L12-v2`. Relevant movie found at the top 10 is 29.7% and mmr10 is 0.185.

- Fourth try was using the embedding model `all-MiniLM-L12-v2` and enabling normalization of embeddings. It stays the same: Relevant movie found at the top 10 is 29.7% and mmr10 is 0.185.

- Fifth try was using the embedding model `all-MiniLM-L12-v2` and the new preprocessing function `clean_query_txt_v2`. Because the query follows always the same pattern, it doesn't seem to be helpful. Lemmatization, removing stop words made the results slightly worse and removing special characters way worse, lower case didn't have any effect. Relevant movie found at the top 10 is 29.7% and mmr10 is 0.185.

- Sixth try was using the embedding model `intfloat/e5-large-v2`. Relevant movie found at the top 10 is 37% and mmr10 is 0.246.

- Seventh try was using the embedding model `paraphrase-multilingual-MiniLM-L12-v2`. Relevant movie found at the top 10 is 36.3% and mmr10 is 0.223. 4X faster than e5-large-v2.

- Eighth try was using the embedding model `bertin-project/bertin-roberta-base-spanish`. The results were really bad 5.7% relevant at top 10 and mmr10 0.037. The model seems not suitable for the task.

- Ninth try was using the embedding model `jaimevera1107/all-MiniLM-L6-v2-similarity-es`. Relevant movie found at the top 10 is 26% and mmr10 is 0.194. A bit better than the original all-MiniLM-L6-v2 but still far from the best ones.

- Tenth try was using the embedding model `hiiamsid/sentence_similarity_spanish_es`. Relevant movie found at the top 10 is 52.7% and mmr10 is 0.37.

- Eleventh try was using the embedding model `Shaharyar6/finetuned_sentence_similarity_spanish`. Relevant movie found at the top 10 is 57.3% and mmr10 is 0.393. This is the best model so far, times are similar to the previous one.