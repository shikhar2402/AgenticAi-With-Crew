from crewai import Crew,Process
from tasks import research_task,write_task
from agent import news_researcher,news_writer
from dotenv import load_dotenv
import os
load_dotenv()

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)