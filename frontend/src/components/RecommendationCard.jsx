function RecommendationCard({ recommendation }) {
    if (!recommendation) return null;

    return (
        <div className="card">

            <h2>Recommendations</h2>

            <div className="two-column">

                <div className="column">

                    <h3>💪 Strengths</h3>

                    <ul>
                        {recommendation.strengths.map((item, i) => (
                            <li key={i}>{item}</li>
                        ))}
                    </ul>

                </div>

                <div className="column">

                    <h3>⚠ Weaknesses</h3>

                    <ul>
                        {recommendation.weaknesses.map((item, i) => (
                            <li key={i}>{item}</li>
                        ))}
                    </ul>

                </div>

            </div>

            <h3>📌 Suggested Actions</h3>

            <ul>
                {recommendation.recommendations.map((item, i) => (
                    <li key={i}>{item}</li>
                ))}
            </ul>  
        </div>
    );
}

export default RecommendationCard;