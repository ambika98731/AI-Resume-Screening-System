function RecommendationCard({ recommendation }) {
    if (!recommendation) return null;

    return (
        <div className="card">

            <h2>Recommendations</h2>

            <div className="two-column">

                <div className="column">

                    <h3>💪 Strengths</h3>

                    <div className="recommendation-container">

                        {recommendation.strengths.length > 0 ? (
                            recommendation.strengths.map((item, i) => (
                                <span
                                    key={i}
                                    className="recommendation-chip strength-chip"
                                >
                                    {item}
                                </span>
                            ))
                        ) : (
                            <p>No strengths detected.</p>
                        )}

                    </div>

                </div>

                <div className="column">

                    <h3>⚠️ Weaknesses</h3>

                    <div className="recommendation-container">

                        {recommendation.weaknesses.length > 0 ? (
                            recommendation.weaknesses.map((item, i) => (
                                <span
                                    key={i}
                                    className="recommendation-chip weakness-chip"
                                >
                                    {item}
                                </span>
                            ))
                        ) : (
                            <p className="success-text">
                                🎉 No major weaknesses detected!
                            </p>
                        )}

                    </div>

                </div>

            </div>

            <h3 style={{ marginTop: "35px" }}>
                📌 Suggested Actions
            </h3>

            <div className="recommendation-container">

                {recommendation.recommendations.map((item, i) => (
                    <span
                        key={i}
                        className="recommendation-chip action-chip"
                    >
                        {item}
                    </span>
                ))}

            </div>

        </div>
    );
}

export default RecommendationCard;