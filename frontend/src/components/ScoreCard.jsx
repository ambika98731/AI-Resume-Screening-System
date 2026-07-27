function ScoreCard({ matching, semanticMatching }) {
    if (!matching) return null;

    return (
        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "20px",
                backgroundColor: "#f8f9fa",
            }}
        >
            <h2>Resume Score</h2>

            <h3>
                Overall Match: {matching.overall_score}%
            </h3>

            <progress
                value={matching.overall_score}
                max="100"
                style={{
                    width: "100%",
                    height: "20px",
                }}
            />

            <br />
            <br />

            {semanticMatching && (
                <>
                    <h3>
                        Semantic Similarity: {semanticMatching.similarity_score}%
                    </h3>

                    <progress
                        value={semanticMatching.similarity_score}
                        max="100"
                        style={{
                            width: "100%",
                            height: "20px",
                        }}
                    />
                </>
            )}
        </div>
    );
}

export default ScoreCard;