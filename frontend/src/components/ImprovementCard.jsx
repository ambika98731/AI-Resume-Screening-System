function ImprovementCard({ improvements }) {
    if (!improvements) return null;

    return (
        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "20px",
                backgroundColor: "#ffffff",
            }}
        >
            <h2>Resume Improvements</h2>

            <ul>
                {improvements.suggestions &&
                improvements.suggestions.length > 0 ? (
                    improvements.suggestions.map((item, index) => (
                        <li key={index}>{item}</li>
                    ))
                ) : (
                    <li>No improvement suggestions available.</li>
                )}
            </ul>
        </div>
    );
}

export default ImprovementCard;