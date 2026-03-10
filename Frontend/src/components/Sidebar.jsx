export default function Sidebar({ topK, setTopK, clearChat }) {
  const diseases = [
    { icon: "🫁", category: "Respiratory", items: "COPD, Asthma, COVID-19, Tuberculosis" },
    { icon: "🦟", category: "Infectious", items: "Malaria, Dengue, Typhoid" },
    { icon: "🩸", category: "Metabolic", items: "Type 2 Diabetes, Obesity, Hyperlipidemia, Hypothyroidism" },
    { icon: "❤️", category: "Cardiovascular", items: "Hypertension, CAD, Heart Failure" },
    { icon: "🧠", category: "Mental Health", items: "Depression, Anxiety Disorder" },
    { icon: "🫃", category: "Digestive", items: "Gastritis/GERD, IBS" },
    { icon: "🔬", category: "Endocrine", items: "PCO" },
  ];

  return (
    <aside className="sidebar">
      <h2>📚 Knowledge Base</h2>
      <div className="disease-list">
        {diseases.map((d) => (
          <div key={d.category} className="disease-category">
            <span className="category-icon">{d.icon}</span>
            <div>
              <strong>{d.category}</strong>
              <p>{d.items}</p>
            </div>
          </div>
        ))}
      </div>

      <div className="slider-section">
        <label>Sources to retrieve: <strong>{topK}</strong></label>
        <input
          type="range"
          min={3}
          max={10}
          value={topK}
          onChange={(e) => setTopK(Number(e.target.value))}
        />
      </div>

      <button className="clear-btn" onClick={clearChat}>
        🗑️ Clear Chat
      </button>
    </aside>
  );
}