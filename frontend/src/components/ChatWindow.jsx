import React from "react";
import MessageBubble from "./MessageBubble";
import SourceCitation from "./SourceCitation";

export default function ChatWindow({ messages }) {
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 12, marginTop: 16, maxHeight: 420, overflowY: "auto" }}>
      {messages.map((message, index) => (
        <div key={index} style={{ display: "flex", flexDirection: "column" }}>
          <MessageBubble text={message.text} role={message.role} />
          {message.sources && message.sources.length > 0 && (
            <SourceCitation sources={message.sources} />
          )}
        </div>
      ))}
    </div>
  );
}
