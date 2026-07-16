import React from "react";

export default function MessageBubble({ text, role }) {
  return (
    <div style={{
      marginBottom: 12,
      padding: 14,
      borderRadius: 14,
      background: role === "user" ? "#eef2ff" : "#f3f4f6",
      alignSelf: role === "user" ? "flex-end" : "flex-start",
      maxWidth: "100%",
    }}>
      <div style={{ whiteSpace: "pre-wrap", color: "#111827" }}>{text}</div>
    </div>
  );
}
