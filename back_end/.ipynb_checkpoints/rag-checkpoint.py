from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load PDF 
pdf_loader = PyPDFLoader("14.DavidWerner-WhereThereIsNoDoctor.pdf")
pdf_docs = pdf_loader.load()

# Load CSV 
csv_loader = CSVLoader(file_path="Medi_Drug.csv", encoding="utf-8")
csv_docs = csv_loader.load()

# Combine PDF and CSV documents
all_docs = pdf_docs + csv_docs

#  Text Splitting 
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(all_docs)

# Embedding Model 
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# FAISS Vector Store
faiss_index = FAISS.from_documents(chunks, embedding_model)

# Save to disk
faiss_index.save_local("faiss_index")
print("✅ FAISS index saved including PDF + CSV!")