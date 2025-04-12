# very simplified fixed length chunking strategy
def simple_fixed_length_chunker(text, chunkSize):
    start_index = 0

    chunks = []
    while start_index < len(text):
        end_index = start_index + chunkSize
        
        if end_index > len(text):
            end_index = len(text)        
        
        chunk = text[start_index:end_index]

        chunks.append(chunk)
        start_index = end_index

    return chunks

chunks = simple_fixed_length_chunker("This is a test string to demonstrate the fixed length chunking strategy.", 10)
print(chunks)
    


