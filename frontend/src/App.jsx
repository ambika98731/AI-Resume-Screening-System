import { useState } from "react";

import UploadForm from "./components/UploadForm";

import ScoreCard from "./components/ScoreCard";
import SkillsCard from "./components/SkillsCard";
import RecommendationCard from "./components/RecommendationCard";
import InterviewCard from "./components/InterviewCard";
import SummaryCard from "./components/SummaryCard";
import ImprovementCard from "./components/ImprovementCard";

import DownloadReportButton from "./components/DownloadReportButton";
import PersonalInfoCard from "./components/PersonalInfoCard";

import ProjectsCard from "./components/ProjectsCard";

function App() {

    const [result, setResult] = useState(null);

    const handleAnalyze = async (resumeFile, jdFile) => {
      try {
        const formData = new FormData();

        formData.append("resume_file", resumeFile);
        formData.append("jd_file", jdFile);

        const response = await fetch("http://127.0.0.1:8000/match", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();

        setResult(data);

      } catch (error) {
          console.error(error);
      }
    };

    return (
       <div className="app">

            <div className="header">
                <h1>AI Resume Screening System</h1>
                <p>
                    Intelligent Resume Analysis using FastAPI, React and NLP
                </p>
            </div>

        <UploadForm onAnalyze={handleAnalyze} />

            {result && (
              <>
                <PersonalInfoCard
                  personalInfo={result.resume.personal_info}
                />

                <ProjectsCard
                  projects={result.resume.projects}
                />

                <ScoreCard
                  matching={result.matching}
                  semanticMatching={result.semantic_matching}
                />

                <SkillsCard matching={result.matching} />

                <RecommendationCard
                  recommendation={result.recommendation}
                />

                <InterviewCard
                  interview={result.interview_questions}
                />

                <SummaryCard
                  summary={result.summary}
                />

                <ImprovementCard
                  improvements={result.improvements}
                />
                <DownloadReportButton
                  result={result}
                />
              </>
          )}

        </div>
    );
}

export default App;