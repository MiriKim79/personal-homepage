from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "slug": "diet",
        "title": "맞춤형 식단 추천 시스템",
        "category": "AI & Data",
        "summary": "개인 정보를 바탕으로 식단을 추천하는 서비스",
        "role": "AI 개발",
        "skills": ["Python", "Flask", "MongoDB"]
    },
    {
        "slug": "dance",
        "title": "AI 기반 댄스 학습 서비스",
        "category": "Web Development",
        "summary": "자세 분석으로 춤 학습을 돕는 웹 서비스",
        "role": "Backend",
        "skills": ["Flask", "MongoDB", "JavaScript"]
    },
    {
        "slug": "taxi",
        "title": "경기대 택시 동승 서비스",
        "category": "Web Development",
        "summary": "같은 방향 학생을 연결하는 택시 동승 플랫폼",
        "role": "Full Stack",
        "skills": ["HTML", "CSS", "JavaScript"]
    },
    {
        "slug": "export-ai",
        "title": "의류 수출 서류 자동 작성 AI",
        "category": "AI & Data",
        "summary": "수출 서류 작성을 자동화하는 AI 서비스",
        "role": "AI 개발",
        "skills": ["Python", "LLM", "OCR"]
    },
    {
        "slug": "carbon",
        "title": "탄소 저감 발주 추천 시스템",
        "category": "Research",
        "summary": "탄소 배출을 줄이는 발주량을 추천하는 시스템",
        "role": "Frontend",
        "skills": ["Python", "데이터 분석"]
    },
    {
        "slug": "krafton",
        "title": "크래프톤 웹 개발 프로젝트",
        "category": "Team Projects",
        "summary": "부트캠프에서 진행한 팀 웹 개발 프로젝트",
        "role": "Full Stack",
        "skills": ["Flask", "MongoDB", "JavaScript"]
    }
]

university = [
    {
        "category": "Leadership",
        "main": "학생회 활동",
        "description": "구성원의 의견을 모으고 행사를 기획하며 조율하는 역할을 맡았습니다.",
        "tags": ["행사 기획", "팀 운영"]
    },
    {
        "category": "Learning",
        "main": "거북이 스터디",
        "description": "동료들과 꾸준히 학습하며 서로의 이해를 점검했습니다.",
        "tags": ["튜터링", "CTL 프로그램"]
    },
    {
        "category": "Community",
        "main": "SWAT 봉사단",
        "description": "지역 사회와 연결되는 활동에 참여했습니다.",
        "tags": ["봉사", "지역 연계"]
    },
    {
        "category": "Activities",
        "main": "산악회",
        "description": "몸을 움직이는 활동으로 새로운 사람들과 관계를 넓혔습니다.",
        "tags": ["사진", "배드민턴", "등산"]
    },
    {
        "category": "Career",
        "main": "인턴십과 연구 경험",
        "description": "현장에서 개발과 연구를 경험하며 진로 방향을 구체화했습니다.",
        "tags": ["인턴십", "자격증", "연구"]
    }
]

interests = [
    {
        "group": "사람과 생각",
        "list": ["심리", "추리", "인간관계"]
    },
    {
        "group": "경험과 취향",
        "list": ["여행", "요리", "운전", "콘서트", "자연"]
    },
    {
        "group": "기술과 진로",
        "list": ["AI", "IoT", "자율주행", "AI 할루시네이션"]
    }
]

future = [
    {
        "label": "지금 배우는 것",
        "text": "웹 개발과 AI를 함께 다루며 두 분야를 잇는 방법을 익히고 있습니다."
    },
    {
        "label": "가까운 목표",
        "text": "직접 기획한 서비스를 끝까지 완성해 사용자에게 닿게 하고 싶습니다."
    },
    {
        "label": "도전하고 싶은 것",
        "text": "해외 연구 및 개발 프로젝트에 참여하며 더 넓은 환경에서 경험을 쌓고 싶습니다."
    },
    {
        "label": "찾아가는 방향",
        "text": "기술이 사람의 일상에 어떻게 스며들 수 있는지 계속 고민하려 합니다."
    }
]

contacts = [
    {
        "label": "Email",
        "value": "miri067979@kyonggi.ac.kr",
        "link": "mailto:miri067979@kyonggi.ac.kr"
    },
    {
        "label": "Instagram",
        "value": "@mm_daily_wy",
        "link": "https://instagram.com/mm_daily_wy"
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        projects=projects,
        university=university,
        interests=interests,
        future=future,
        contacts=contacts
    )

if __name__ == "__main__":
    app.run(debug=True)