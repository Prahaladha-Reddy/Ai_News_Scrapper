#!/usr/bin/env python
import os
import warnings
from datetime import datetime
from crew import AiNews

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the AiNews crew for multiple topics.
    """

    # List of topics to process
    topics = [
        
        "Generative AI trends"
    ]

    # Prepare inputs array with multiple topics
    inputs_array = [
        {
            'topic': topic,
            'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        }
        for topic in topics
    ]

    print("Inputs for tasks:", inputs_array)  # Debugging inputs

    # Ensure output directory exists
    output_directory = "news"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Run the crew for each topic
    AiNews().crew().kickoff_for_each(inputs=inputs_array)

if __name__ == "__main__":
    run()
