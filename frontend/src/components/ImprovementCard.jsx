function ImprovementCard({ improvements }) {
    if (!improvements) return null;

    return (
        <div className="card">

            <h2>Resume Improvements</h2>

            <ul>
                {improvements.suggestions.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>

        </div>
    );
}

export default ImprovementCard;