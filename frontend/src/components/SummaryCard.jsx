function SummaryCard({ summary }) {

    if (!summary) return null;

    return (

        <div className="card">

            <h2>Candidate Summary</h2>

            <div className="summary-card">

                <div className="summary-icon">
                    📄
                </div>

                <div className="summary-text">
                    {summary.summary}
                </div>

            </div>

        </div>

    );

}

export default SummaryCard;