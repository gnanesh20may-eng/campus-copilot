import React, { useState } from "react";
import { chatQuery } from "../api";
import ChatWindow from "../components/ChatWindow";

export default function ChatPage({ department, subgroup }) {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleSend(e) {
    e?.preventDefault();
    if (!query.trim()) {
      setError("Please enter a question before sending.");
      return;
    }

    setError(null);
    const userMessage = { role: "user", text: query };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const res = await chatQuery(query, department, subgroup);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: res.answer, sources: res.sources },
      ]);
      setQuery("");
    } catch (err) {
      setError(err.message || "Unable to contact the backend.");
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "There was an error processing your request.",
          sources: [],
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <h2>Chat</h2>
      <p className="small">Ask questions about the uploaded documents.</p>
      <div style={{ marginTop: 12, marginBottom: 16 }}>
        <strong>Department:</strong> {department} · <strong>Subgroup:</strong> {subgroup}
      </div>

      <form onSubmit={handleSend}>
        <textarea
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Type your question..."
        />
        <div className="input-row">
          <button className="button primary" disabled={loading}>
            {loading ? "Thinking..." : "Send"}
          </button>
          <button
            type="button"
            className="button"
            onClick={() => {
              setQuery("");
              setError(null);
            }}
          >
            Clear
          </button>
        </div>
      </form>

      {error && <div style={{ marginTop: 12, color: "crimson" }}>{error}</div>}

      <ChatWindow messages={messages} />
    </div>
  );
}
