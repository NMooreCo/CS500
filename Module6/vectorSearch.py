# simplified vector search showing how in memeory cache is used
def perform_vector_search(query):
    # simulate returning document ids
    return [1, 2, 3, 4, 5]

class Document:
    def __init__(self, content, metadata):
        self.content = content
        self.metadata = metadata    

def get_document_content_and_metatdata(id):
    # simulate getting document content and metadata using documentCache and Document tuple
    if id in documentCache:
        print(f"Cache hit for document ID: {id}")
        return documentCache[id]
    else:
        # Simulate fetching from a database or external source
        content = f"Content of document {id}"
        metadata = {"title": f"Document {id}", "author": "Author Name"}        
        documentCache[id] = Document(content, metadata)
        return documentCache[id]
    
documentCache = {}
documentCache[3] = Document("Content of document 3", {"title": "Document 3", "author": "Author Name"})
query = "example query"
document_ids = perform_vector_search(query)

for doc_id in document_ids:
    doc = get_document_content_and_metatdata(doc_id)
    print(f"Document ID: {doc_id}, Content: {doc.content}, Metadata: {doc.metadata}")
    