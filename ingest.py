from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from pdf2image import convert_from_path
from langchain_core.documents import Document
import pytesseract
import os

# Paths
DATA_PATH = "data"
DB_PATH = "vectordb"


def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(DATA_PATH, file)

            print(f"Processing {file} with OCR...")

            images = convert_from_path(
                pdf_path,
                poppler_path=r"C:\Users\INTEL\Downloads\Release-25.12.0-0 (1)\poppler-25.12.0\Library\bin"
            )

            for i, image in enumerate(images):
                text = pytesseract.image_to_string(image)

                if text.strip():
                    documents.append(
                        Document(
                            page_content=text,
                            metadata={"source": file, "page": i}
                        )
                    )

    # 🌐 Web data
    print("Processing Academic Calendar (Web)...")
    web_loader = WebBaseLoader("https://ahduni.edu.in/academics/academic-calendar/")
    documents.extend(web_loader.load())

    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    return text_splitter.split_documents(documents)


def create_vector_db(chunks):
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )

    print("✅ Vector DB created successfully!")


if __name__ == "__main__":
    print("📄 Loading documents...")
    docs = load_documents()

    print("\n📄 Sample Document:\n")
    print(docs[0].page_content[:1000])

    print(f"Loaded {len(docs)} pages")

    print("\n📄 Checking documents...\n")

    for i in range(3):
        print(f"\n--- Document {i} ---")
        print("Length:", len(docs[i].page_content))
        print(docs[i].page_content[:500])

    print("✂️ Splitting documents...")
    chunks = split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    print("🧠 Creating embeddings & storing in DB...")
    create_vector_db(chunks)