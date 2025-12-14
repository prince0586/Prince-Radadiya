---

### 3. `EXPLANATION.md`

```markdown
# 💡 Project Philosophy & Design Decisions

## Why "Agentic" AI?
Traditional LLMs suffer from two critical flaws:
1.  **Knowledge Cutoff:** They cannot answer questions about today's news.
2.  **Hallucination:** They often present false information confidently.

Veritas solves this by treating the LLM not as a database, but as a **Reasoning Engine** that drives external tools.

## Why Gemini 3 Pro Preview?
We chose `gemini-3-pro-preview` over older models specifically for its **"Deep Think"** capabilities.
* **Planning:** Gemini 3 demonstrates superior ability in decomposing complex, multi-step problems compared to Flash or Pro 1.5.
* **Nuance:** The model captures subtle context during the "Review" phase, making the self-correction loop significantly more reliable.

## The "Reflexion" Pattern
Our architecture implements the **Reflexion** framework (Shinn et al.). Instead of accepting the first output, Veritas:
1.  **Drafts** a research summary.
2.  **Critiques** its own draft (The Reviewer).
3.  **Refines** the final output based on that critique.

This mimicry of the human editorial process (Draft -> Edit -> Publish) results in higher accuracy and trust.

## Limitations & Future Work
* **Latency:** The "Deep Think" process + Live Search adds latency (approx. 15-30s per query). This is a trade-off for accuracy.
* **Persistence:** Currently, memory is session-based. Future versions will implement a Vector Database (ChromaDB) for long-term recall.