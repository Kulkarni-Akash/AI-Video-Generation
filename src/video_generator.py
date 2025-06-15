import requests
import base64 
import os
import time
from dotenv import load_dotenv

load_dotenv()

class VideoGeneration():
    def __init__(self):
        self.endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
        self.api_key=os.getenv('AZURE_OPENAI_API_KEY')
        self.headers = { "api-key": self.api_key, "Content-Type": "application/json" }
        self.api_version='Preview'

    def video_generation_job(self,prompt):
        create_url = f"{self.endpoint}/openai/v1/video/generations/jobs?api-version={self.api_version}"
        body = {
            "prompt": prompt,
            "width": 480,
            "height": 480,
            "n_seconds": 5,
            "model": "sora"
        }
        response = requests.post(create_url, headers=self.headers, json=body)
        response.raise_for_status()
        print("Full response JSON:", response.json())
        job_id = response.json()["id"]
        print(f"Job created: {job_id}")
        return job_id

    def job_status(self, job_id):
        status_url = f"{self.endpoint}/openai/v1/video/generations/jobs/{job_id}?api-version={self.api_version}"
        status=None
        while status not in ("succeeded", "failed", "cancelled"):
            time.sleep(5)  # Wait before polling again
            status_response = requests.get(status_url, headers=self.headers).json()
            status = status_response.get("status")
            print(f"Job status: {status}")
        return status, status_response

    def get_video(self, status, status_response):
        if status == "succeeded":
            generations = status_response.get("generations", [])
        if generations:
            print(f"✅ Video generation succeeded.")
            generation_id = generations[0].get("id")
            video_url = f"{self.endpoint}/openai/v1/video/generations/{generation_id}/content/video?api-version={self.api_version}"
            video_response = requests.get(video_url, headers=self.headers)
            if video_response.ok:
                output_filename = "output/output.mp4"
                with open(output_filename, "wb") as file:
                    file.write(video_response.content)
                    print(f'Generated video saved as "{output_filename}"')
            else:
                raise Exception("No generations found in job result.")
        else:
            raise Exception(f"Job didn't succeed. Status: {status}")