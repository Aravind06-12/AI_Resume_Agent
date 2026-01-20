import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please upload a resume PDF");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("https://ai-resume-agent-backend.onrender.com/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("❌ Failed to connect to backend. Is backend running?");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "40px", maxWidth: "900px", margin: "auto" }}>
      <h1>AI Resume Screening & Career Advisor Agent</h1>

      {/* Upload Section */}
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <br /><br />

      <button onClick={handleUpload}>
        Analyze Resume
      </button>

      {loading && <p>🔄 Analyzing resume… Please wait</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Results Section */}
      {result && result.parsed_info && (
        <div style={{ marginTop: "40px", background: "#fff", padding: "20px", borderRadius: "8px" }}>
          <h2>Results</h2>

          <h3>Candidate Info</h3>
          <p><b>Name:</b> {result.parsed_info.name || "Not found"}</p>
          <p><b>Education:</b> {result.parsed_info.education}</p>
          <p><b>Experience:</b> {result.parsed_info.experience}</p>
          <p><b>Skills:</b> {(result.parsed_info.skills || []).join(", ")}</p>

          <h3>Predicted Category</h3>
          <p>{result.category}</p>

          <h3>Resume Review</h3>
          <p><b>Score:</b> {result.review?.score}/10</p>

          <p><b>Strengths:</b></p>
          <ul>
            {(result.review?.strengths || []).map((s, i) => <li key={i}>{s}</li>)}
          </ul>

          <p><b>Weaknesses:</b></p>
          <ul>
            {(result.review?.weaknesses || []).map((w, i) => <li key={i}>{w}</li>)}
          </ul>

          <p><b>Suggestions:</b></p>
          <ul>
            {(result.review?.suggestions || []).map((s, i) => <li key={i}>{s}</li>)}
          </ul>

          <h3>Career Advice</h3>
          <ul>
            {(result.career_advice?.best_roles || []).map((r, i) => <li key={i}>{r}</li>)}
          </ul>

          <h3>Interview Questions</h3>
          <ul>
            {(result.interview_prep?.questions || []).map((q, i) => <li key={i}>{q}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
