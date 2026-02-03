from __future__ import annotations

from langchain_core.documents import Document

from data_utils import Movie
from retrieval import config


def create_docs_to_embedd(movies: list[Movie], config: config.RetrievalExpsConfig) -> list[Document]:
    """
    Convierte una lista de objetos `Movie` a una lista the objetos `Document`(usada por Langchain).
    En esta función se decide que parte de los datos será usado como embeddings y que parte como metadata.
    """
    movies_as_docs = []
    for movie in movies:
        content = config.text_to_embed_fn(movie)
        metadata = movie.model_dump()
        doc = Document(page_content=content, metadata=metadata)
        movies_as_docs.append(doc)

    return movies_as_docs


## Posibles funciones para usar como `text_to_embed_fn` en `RetrievalExpsConfig` ##

# Right now text_to_embed_fn is set to get_synopsys_txt in config.py
def get_synopsys_txt(movie: Movie) -> str:
    return movie.synopsis

def process_movie_info(movie: Movie) -> str:
    info =  f"{movie.title_es}. Dirigida por {movie.director_top_5}. Protagonizada por {', '.join(movie.cast_top_5)}. Género: {movie.genre_tags}. Sinopsis: {movie.synopsis}. Año: {movie.year}. País: {movie.country}. Duración: {movie.duration_mins} minutos. Es serie de TV: {'Sí' if movie.tv_show_flag else 'No'}."
    return info