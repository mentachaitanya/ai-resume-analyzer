import requests
import json
import time
import sys

# Ensure UTF-8 for output
sys.stdout.reconfigure(encoding='utf-8')

# --- MOCK DATA FOR 5 COMPANIES ---
SAMPLES = [
    {
        "company": "Google (Software Engineer III)",
        "jd": "Minimum qualifications: Bachelor's degree in Computer Science. 5+ years experience with Python or C++. Experience with large-scale distributed systems and microservices. Preferred: Experience with Go and Kubernetes.",
        "resume": "Software Developer with 4 years experience in Python. Built REST APIs using Flask. Familiar with Docker."
    },
    {
        "company": "Meta (Data Engineer)",
        "jd": "Responsibilities: Build and maintain scalable data pipelines. Expertise in SQL, Python, and Spark required. Experience with Presto and Hive is a plus. Must demonstrate ability to handle petabyte-scale data.",
        "resume": "Backend dev with SQL knowledge. Used Python for script automation. No big data experience."
    },
    {
        "company": "Stripe (Fullstack Engineer)",
        "jd": "We need a product-minded engineer. Fluent in Ruby or Java. Frontend experience with React/TypeScript. Passion for financial infrastructure and API design.",
        "resume": "Frontend developer focused on React and Tailwind. Interested in fintech. Minimal Ruby or Java knowledge."
    },
    {
        "company": "OpenAI (AI Platform Engineer)",
        "jd": "Focus on high-performance infrastructure. Expertise in PyTorch, CUDA, and distributed training. Strong background in system architecture and C++ optimization.",
        "resume": "Machine Learning Engineer. Worked with TensorFlow and Python. Deployed models on AWS."
    },
    {
        "company": "Airbnb (Lead Backend Developer)",
        "jd": "Leadership role. Expertise in Java/Ruby. Proven track record of leading teams and architecting complex systems. Scalability and performance optimization are key.",
        "resume": "Senior Developer. 10 years in backend dev. Lead a team of 3 developers for a year. Deep Java expertise."
    }
]

API_URL = "http://127.0.0.1:8000/tailor"

def run_tests():
    print("[START] ELITE STRATEGIST ACCURACY TEST (5 COMPANIES)\n")
    print("="*60)
    
    for sample in SAMPLES:
        print(f"[TESTING] FOR: {sample['company']}")
        try:
            start_time = time.time()
            response = requests.post(API_URL, json={
                "resume_text": sample["resume"],
                "job_description": sample["jd"]
            }, timeout=30)
            
            end_time = time.time()
            
            if response.status_code == 200:
                data = response.json()
                print(f"[SUCCESS] (Elapsed: {round(end_time - start_time, 2)}s)")
                print(f"-> Strategic Match: {data['scores']['strategic_match']}%")
                print(f"-> Hiring Prob: {data['hiring_probability']}")
                print(f"-> Red Flags: {len(data['red_flags'])}")
                print(f"-> Matrix Size: {len(data['gap_matrix'])} items")
            else:
                print(f"[FAIL] Status {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[ERROR] Error connecting to server: {str(e)}")
        
        print("-" * 30)

if __name__ == "__main__":
    run_tests()
