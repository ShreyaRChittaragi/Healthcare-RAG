import { useState, useRef, useEffect } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

export default function ChatWindow({ topK, chatHistory, setChatHistory }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatHistory]);

  const sendMessage = async () => {
    if (!query.trim() || loading) return;

    const userMessage = { role: "user", content: query };
    const updatedHistory = [...chatHistory, userMessage];
    setChatHistory(updatedHistory);
    setQuery("");
    setLoading(true);

    try {
      const apiHistory = updatedHistory.map((m) => ({
        role: m.role,
        content: m.content,
      }));

      const res = await axios.post(`http://127.0.0.1:8000/chat`, {
        query,
        chat_history: apiHistory,
        top_k: topK,
      });

      const assistantMessage = {
        role: "assistant",
        content: res.data.answer,
        sources: res.data.sources,
      };

      setChatHistory([...updatedHistory, assistantMessage]);
    } catch (err) {
      setChatHistory([
        ...updatedHistory,
        {
          role: "assistant",
          content: "⚠️ Something went wrong. Please try again.",
          sources: [],
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {chatHistory.length === 0 && (
          <div className="empty-state">
            <p>👋 Ask me anything about the 19 diseases in my knowledge base!</p>
            <p>Example: <em>"What are the symptoms of Hypertension?"</em></p>
          </div>
        )}

        {chatHistory.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <div className="bubble">
              <ReactMarkdown>{msg.content}</ReactMarkdown>
            </div>
            {msg.sources && msg.sources.length > 0 && (
              <details className="sources">
                <summary>📄 View Sources ({msg.sources.length})</summary>
                <ul>
                  {msg.sources.map((s) => (
                    <li key={s.source_num}>
                      <strong>[Source {s.source_num}]</strong> {s.disease} — {s.filename}
                    </li>
                  ))}
                </ul>
              </details>
            )}
          </div>
        ))}

        {loading && (
          <div className="message assistant">
            <div className="bubble loading">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <div className="input-area">
        <textarea
          rows={2}
          placeholder="Ask a medical question... (Enter to send)"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button onClick={sendMessage} disabled={loading}>
          {loading ? "..." : "Send"}
        </button>
      </div>
    </div>
  );
}