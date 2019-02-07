from celery import Celery
from core.pipelines import AutomatizedTool
from core.integrative_result import IntegrativeResult


app = Celery('tasks', broker='amqp://localhost')

@app.task
def start_pipeline(selected_tools,analysis_path,filepath):
    for tool in selected_tools:
        print(tool)
        #call Analysis
        job = AutomatizedTool(tool,filepath)
        job.start()

    integrateJob = IntegrativeResult(analysis_path+"out_virulence/results_tab.txt", analysis_path+"out_resistance/out_resistance.txt")
    integrateJob.start("E_faecalis_V583", analysis_path)
    return "Pipeline finished!"
