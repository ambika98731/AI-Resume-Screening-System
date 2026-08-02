function ScoreCard({ matching, semanticMatching }) {
    if (!matching) return null;

    return (
        <div className="card">

            <h2>Resume Score</h2>

            <div className="score-section">

                <div className="score-header">
                    <span>Overall Match</span>
                    <span>{matching.overall_score}%</span>
                </div>

                <div className="progress-bar">
                    <div
                        className="progress-fill"
                        style={{
                            width: `${matching.overall_score}%`,
                        }}
                    ></div>
                </div>

            </div>

            <div className="score-section">

                <div className="score-header">
                    <span>Semantic Similarity</span>
                    <span>{semanticMatching.similarity_score}%</span>
                </div>

                <div className="progress-bar">
                    <div
                        className="progress-fill secondary"
                        style={{
                            width: `${semanticMatching.similarity_score}%`,
                        }}
                    ></div>
                </div>

            </div>

            <div className="score-section">

                <div className="score-header">
                    <span>Experience Requirement</span>

                    <span>
                        {matching.experience_match
                            ? "✅ Matched"
                            : "❌ Not Matched"}
                    </span>
                </div>

            </div>

        </div>
    );
}

export default ScoreCard;