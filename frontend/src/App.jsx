import { useState } from "react";

import UploadForm from "./components/UploadForm";

import ScoreCard from "./components/ScoreCard";
import SkillsCard from "./components/SkillsCard";
import RecommendationCard from "./components/RecommendationCard";
import InterviewCard from "./components/InterviewCard";
import SummaryCard from "./components/SummaryCard";
import ImprovementCard from "./components/ImprovementCard";

function App() {

    const [result, setResult] = useState(null);

    return (
       <div className="app">

            <div className="header">
                <h1>AI Resume Screening System</h1>
                <p>
                    Intelligent Resume Analysis using FastAPI, React and NLP
                </p>
            </div>

        <UploadForm setResult={setResult} />

            {result && (
              <>
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
              </>
          )}

        </div>
    );
}

export default App;