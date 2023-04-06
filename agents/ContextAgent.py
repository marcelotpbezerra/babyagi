from helpers import OpenAIHelper

class ContextAgent:
    def __init__(self, pinecone_index, objective: str):
        self.pinecone_index = pinecone_index
        self.objective = objective

    def get_context(self, query: str, n: int):
        query_embedding = OpenAIHelper.get_ada_embedding(query)
        results = self.pinecone_index.query(query_embedding, top_k=n, include_metadata=True)
        sorted_results = sorted(results.matches, key=lambda x: x.score, reverse=True)    
        return [(str(item.metadata['task'])) for item in sorted_results]
    
    def get_objective(self):
        return self.objective