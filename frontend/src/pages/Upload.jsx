import React, { useState } from "react";
import { uploadPDF } from "../api";

export default function UploadPage() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");
  const [progress, setProgress] = useState(0);
  const [chunks, setChunks] = useState(null);
  const [uploadedDocs, setUploadedDocs] = useState([]);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);
    if (!file) return setError("Pick a PDF to upload.");
    setStatus("Uploading...");
    setProgress(0);
    try {
      const result = await uploadPDF(file, (p) => setProgress(p));
      setStatus("Ingested");
      setChunks(result.chunks_added ?? result.chunksAdded ?? null);
      setUploadedDocs((prev) => [...new Set([...prev, result.filename])]);
      setFile(null);
    } catch (err) {
      setError(err.message || "Upload failed.");
      setStatus("Failed");
    }
  }

  return (
    <div>
      <h2>Upload PDF</h2>
      <p className="small">Upload a PDF to ingest into the vector store.</p>

      <form onSubmit={handleSubmit}>
        <div style={{ marginTop: 12 }}>
          <input
            type="file"
            accept="application/pdf"
            onChange={(e) => {
              setFile(e.target.files?.[0] ?? null);
              setStatus("");
              setChunks(null);
              setError(null);
            }}
          />
        </div>

        <div className="input-row" style={{ marginTop: 12 }}>
          <button className="button primary" type="submit">Upload & Ingest</button>
          <div className="small" style={{ marginLeft: 8 }}>
            {status} {progress ? `(${progress}%)` : ""}
            {chunks !== null ? ` — ${chunks} chunks added` : ""}
          </div>
        </div>

        {error && <div style={{ marginTop: 12, color: "crimson" }}>{error}</div>}
      </form>

      {uploadedDocs.length > 0 && (
        <div style={{ marginTop: 16 }}>
          <h3>Uploaded documents</h3>
          <ul className="file-list">
            {uploadedDocs.map((name) => (
              <li key={name} className="file-item">{name}</li>
            ))}
          </ul>
        </div>
      )}

      <div style={{ marginTop: 16 }}>
        <p className="small">
          Note: The backend must be running at <code>http://127.0.0.1:8000</code> or set VITE_API_URL.
        </p>
      </div>
    </div>
  );
}
