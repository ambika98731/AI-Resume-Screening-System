function DownloadReportButton({ result }) {
    const downloadReport = async () => {
        try {
            const response = await fetch(
                "http://127.0.0.1:8000/report",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(result),
                }
            );

            const blob = await response.blob();

            const url = window.URL.createObjectURL(blob);

            const link = document.createElement("a");

            link.href = url;
            link.download = "Resume_Report.pdf";

            document.body.appendChild(link);

            link.click();

            link.remove();

            window.URL.revokeObjectURL(url);

        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="card">
            <button
                onClick={downloadReport}
                className="analyze-btn"
            >
                📄 Download PDF Report
            </button>
        </div>
    );
}

export default DownloadReportButton;