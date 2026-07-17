from app.db.vector_store import add_documents, persist


def seed_sample_data():
    texts = [
        "The university exam timetable is published on the first Monday of the semester.",
        "Tuition fees are due by the 10th of each month for all students.",
        "Faculty office hours are from 10am to 4pm, Monday through Friday.",
        "The library closes at 9pm on weekdays and 5pm on weekends."
    ]
    metadatas = [
        {"source": "sample_docs.txt", "chunk_index": i}
        for i in range(len(texts))
    ]
    ids = [f"sample-{i}" for i in range(len(texts))]
    add_documents(texts, metadatas, ids)
    persist()
    print(f"Seeded {len(texts)} documents into ChromaDB.")


if __name__ == "__main__":
    seed_sample_data()
