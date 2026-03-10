from retriever import retrieve
from groq import Groq

client = Groq(api_key="insert-your-api-here")

KNOWN_DISEASES = [
    "copd", "asthma", "covid-19", "tuberculosis", "malaria", "dengue",
    "typhoid fever", "type2dia", "obesity", "hyperlipidemia", "hypothyroidism",
    "hypertension", "heart failure", "cad", "depression", "general anxiety disorder",
    "gastritis", "gerd", "irretable bm", "pco"
]

def detect_disease(text):
    """Detect disease name from text."""
    text_lower = text.lower()
    for disease in KNOWN_DISEASES:
        if disease in text_lower:
            return disease
    return None

def is_followup(query):
    """Check if query is a follow-up referencing previous context."""
    followup_words = ["it", "this", "that", "those", "these", "the condition",
                      "the disease", "the symptoms", "the treatment", "the medication",
                      "more about", "tell me more", "what else", "how about"]
    query_lower = query.lower()
    return any(word in query_lower for word in followup_words)

def ask(query, chat_history=[], top_k=5):
    # Step 1: Detect disease context
    filter_disease = None

    # Check current query first
    filter_disease = detect_disease(query)

    # If follow-up, look for disease in chat history
    if not filter_disease and is_followup(query) and chat_history:
        for turn in reversed(chat_history):
            found = detect_disease(turn["content"])
            if found:
                filter_disease = found
                print(f"🎯 Follow-up detected — filtering by: {filter_disease}")
                break

    # Step 2: Retrieve with optional disease filter
    results = retrieve(query, top_k=top_k)

    # Fallback to unfiltered if not enough results
    if len(results) < 3:
        print("⚠️ Not enough filtered results, falling back to global search")
        results = retrieve(query, top_k=top_k)

    # Step 3: Build context with source tracking
    context = ""
    sources = []
    for i, r in enumerate(results):
        context += f"[Source {i+1} | Disease: {r['disease']} | File: {r['filename']}]\n{r['text']}\n\n"
        sources.append({
            'source_num': i + 1,
            'disease': r['disease'],
            'filename': r['filename']
        })

    # Step 4: Build messages with full history
    messages = [
        {
            "role": "system",
            "content": """You are a friendly and knowledgeable medical assistant helping patients and caregivers understand medical conditions.
Your response style:
- Use simple, clear language that any person can understand
- Avoid excessive medical jargon; when you must use a medical term, briefly explain it
- Structure your answer with clear sections when needed
- Be empathetic and reassuring in tone
- Cite sources using [Source N] notation when referencing specific information
- Always remind users to consult a doctor for personal medical advice
- Stay focused on the disease being discussed in the conversation"""
        }
    ]

    for turn in chat_history:
        messages.append({"role": turn["role"], "content": turn["content"]})

    messages.append({
        "role": "user",
        "content": f"""Using the following research paper excerpts, answer the question clearly.

Research Context:
{context}

Question: {query}"""
    })

    # Step 5: Call Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.3
    )

    answer = response.choices[0].message.content
    return answer, sources


# Test
if __name__ == "__main__":
    chat_history = []

    print("=== Turn 1 ===")
    q1 = "What are the symptoms of heart failure?"
    answer1, sources1 = ask(q1, chat_history)
    print(f"Q: {q1}\nA: {answer1}\n")
    print("Sources:", [s['disease'] for s in sources1])

    chat_history.append({"role": "user", "content": q1})
    chat_history.append({"role": "assistant", "content": answer1})

    print("\n=== Turn 2 (Follow-up) ===")
    q2 = "What are the treatments for it?"
    answer2, sources2 = ask(q2, chat_history)
    print(f"Q: {q2}\nA: {answer2}\n")
    print("Sources:", [s['disease'] for s in sources2])

    chat_history.append({"role": "user", "content": q2})
    chat_history.append({"role": "assistant", "content": answer2})

    print("\n=== Turn 3 (Follow-up) ===")
    q3 = "What about the side effects of those medications?"
    answer3, sources3 = ask(q3, chat_history)
    print(f"Q: {q3}\nA: {answer3}\n")
    print("Sources:", [s['disease'] for s in sources3])