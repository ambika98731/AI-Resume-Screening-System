function SummaryCard({ summary }) {
    if (!summary) return null;

    return (
        <div className="card">
            <h2>Candidate Summary</h2>
            <p>{summary.summary}</p>
        </div>
    );
}

export default SummaryCard;