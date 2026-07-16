from rag.retriever import retrieve_policy

query = "When should a loan be approved?"

result = retrieve_policy(query)

print("Retrieved Policy:\n")
print(result)