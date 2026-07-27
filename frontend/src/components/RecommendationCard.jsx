function RecommendationCard({ recommendation }) {
    if (!recommendation) return null;

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
            <h2>Recommendations</h2>

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    gap: "40px",
                }}
            >
                {/* Strengths */}
                <div style={{ flex: 1 }}>
                    <h3>💪 Strengths</h3>

                    <ul>
                        {recommendation.strengths.length > 0 ? (
                            recommendation.strengths.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))
                        ) : (
                            <li>No strengths found.</li>
                        )}
                    </ul>
                </div>

                {/* Weaknesses */}
                <div style={{ flex: 1 }}>
                    <h3>⚠ Weaknesses</h3>

                    <ul>
                        {recommendation.weaknesses.length > 0 ? (
                            recommendation.weaknesses.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))
                        ) : (
                            <li>No weaknesses found.</li>
                        )}
                    </ul>
                </div>

                {/* Recommendations */}
                <div style={{ flex: 1 }}>
                    <h3>📌 Suggested Actions</h3>

                    <ul>
                        {recommendation.recommendations.length > 0 ? (
                            recommendation.recommendations.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))
                        ) : (
                            <li>No recommendations.</li>
                        )}
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default RecommendationCard;