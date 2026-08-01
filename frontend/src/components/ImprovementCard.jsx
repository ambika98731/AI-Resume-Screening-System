function ImprovementCard({ improvements }) {
    if (!improvements) return null;

    return (
        <div className="card">
            <h2>Resume Improvements</h2>

            <div className="improvement-list">
                {improvements.suggestions.map((item, index) => (
                    <div key={index} className="improvement-item">
                        <span className="improvement-icon">💡</span>
                        <span>{item}</span>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ImprovementCard;