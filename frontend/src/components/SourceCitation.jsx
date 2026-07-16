import React from "react";

export default function SourceCitation({ sources }) {
  if (!sources || sources.length === 0) return null;

  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: 8, marginTop: 8 }}>
      {sources.map((source, index) => (
        <div
          key={index}
          style={{
            background: "#eef2ff",
            color: "#1d4ed8",
            padding: "6px 10px",
            borderRadius: 999,
            fontSize: "0.85rem",
          }}
        >
          {source}
        </div>
      ))}
    </div>
  );
}
