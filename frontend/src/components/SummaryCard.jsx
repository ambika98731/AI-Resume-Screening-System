function SummaryCard({ summary }) {
    if (!summary) return null;

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
            <h2>Candidate Summary</h2>

            <p
                style={{
                    lineHeight: "1.7",
                    fontSize: "16px",
                }}
            >
                {summary.summary}
            </p>
        </div>
    );
}

export default SummaryCard;