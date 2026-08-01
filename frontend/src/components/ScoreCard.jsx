function ScoreCard({ matching, semanticMatching }) {
    if (!matching) return null;

    return (
        <div className="card">

            <h2>Resume Score</h2>

            <h3>
                Overall Match: {matching.overall_score}%
            </h3>

            <progress
                value={matching.overall_score}
                max="100"
            />
            
            <h3 style={{ marginTop: 30 }}>
                Semantic Similarity: {semanticMatching.similarity_score}%
            </h3>

            <progress
                value={semanticMatching.similarity_score}
                max="100"
            />          
        </div>
    );
}

export default ScoreCard;