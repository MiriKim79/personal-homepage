from flask import Flask, render_template

app = Flask(__name__)

# =========================================================
# 모든 내용과 사진 경로는 이 파일에서만 수정하면 됩니다.
# 사진 경로는 static/images/ 아래 기준으로 적습니다.
#   예) "images/university/council-1.jpg"
# 사진이 아직 없으면 빈 문자열 "" 로 두세요. (자동으로 placeholder 표시)
# =========================================================

# ---------------------------------------------------------
# 1. Intro
# ---------------------------------------------------------
intro = {
    "name": "미리의 성장기",
    "lines": [
        "안녕하세요! 저는 미리예요.",
        "지금의 제가 되기까지",
        "몇 mm의 이야기가 쌓였을까요?"
    ],
    # [사진 추가 필요: 대표 프로필 사진] static/images/intro/ 에 넣고 경로 입력
    "photo": "",
    "photo_alt": "미리의 프로필 사진"
}

# ---------------------------------------------------------
# 2. About Me
# ---------------------------------------------------------
about = {
    "paragraphs": [
        "길을 걷다가 어제와 달라진 간판, 사람들이 줄 서는 방향 같은 걸 자주 봐요. "
        "그냥 지나치기보다 왜 저럴까 한 번 더 생각하는 편입니다.",
        "사람들의 행동이나 말투에서 지금 무엇이 불편한지 짐작해 보는 걸 좋아해요. "
        "택시 동승 서비스도 여러 채팅방을 오가며 동승자를 찾는 게 번거롭다는 걸 보고 시작했습니다.",
        "관찰한 것을 머리로만 두지 않고 일단 만들어 보려고 합니다. "
        "낯선 기술이어도 필요하면 찾아보면서 시작하는 편이에요."
    ],
    "motto": "후회하지 않도록, 할 수 있을 때 해보기",
    # [사진 추가 필요: 본인 사진 또는 활동 사진 2장]
    "photos": [
        {"src": "", "alt": "일상 사진", "caption": ""},
        {"src": "", "alt": "활동 사진", "caption": ""}
    ]
}

# ---------------------------------------------------------
# 3. Life Timeline  (age = 자의 눈금 위치)
# ---------------------------------------------------------
life_events = [
    {
        "age": 1,
        "year": "2006",
        "title": "세상 밖으로",
        "description": "나의 이야기가 시작된 순간.",
        "photos": []  # [사진 추가 필요] {"src": "images/timeline/xxx.jpg", "alt": "", "caption": ""}
    },
    {
        "age": 6,
        "year": "2011",
        "title": "새로운 나이",
        "description": "빠른 년생으로 한 학년 위 친구들과 함께 유치원 생활을 시작했습니다.",
        "photos": []
    },
    {
        "age": 13,
        "year": "2018",
        "title": "졸업 여행",
        "description": "친구들과 함께한 코타키나발루 여행. 오래 기억에 남는 시간이었습니다.",
        "photos": []
    },
    {
        "age": 18,
        "year": "2023",
        "title": "사람과 성장",
        "description": "전교 부회장을 맡고, 열심히 하는 친구들 사이에서 공부했습니다. "
                       "갈등과 화해를 겪으며 상황을 조금 더 객관적으로 보는 법을 배웠습니다.",
        "photos": []
    },
    {
        "age": 20,
        "year": "2025",
        "title": "시작과 끝",
        "description": "첫 대학 입학과 자퇴, 그리고 반수. 다시 선택한 길에서 경기대학교에 들어왔습니다.",
        "photos": []
    },
    {
        "age": 21,
        "year": "2026",
        "title": "현재",
        "description": "전공 공부와 함께 프로젝트, 해커톤, 대외활동에 도전하고 있습니다.",
        "photos": []
    }
]

current_age = 21

# ---------------------------------------------------------
# 4. University Life  (사진 타일 + 팝업)
# ---------------------------------------------------------
university = [
    {
        "id": "council",
        "title": "학생회",
        "category": "Leadership",
        "period": "[내용 추가 필요: 활동 기간]",
        "cover": "",  # [사진 추가 필요: 학생회 대표 사진]
        "cover_alt": "학생회 활동 사진",
        "what": "[내용 추가 필요: 어떤 행사와 업무를 했는지]",
        "role": "[내용 추가 필요: 맡은 역할]",
        "memory": "[내용 추가 필요: 기억에 남는 점]",
        "photos": []  # 3~5장 권장
    },
    {
        "id": "swat",
        "title": "SWAT 봉사단",
        "category": "Community",
        "period": "[내용 추가 필요: 활동 기간]",
        "cover": "",
        "cover_alt": "봉사단 활동 사진",
        "what": "[내용 추가 필요: 어떤 봉사를 했는지]",
        "role": "[내용 추가 필요: 맡은 역할]",
        "memory": "[내용 추가 필요: 기억에 남는 점]",
        "photos": []
    },
    {
        "id": "study",
        "title": "스터디 · 학업",
        "category": "Learning",
        "period": "[내용 추가 필요: 활동 기간]",
        "cover": "",
        "cover_alt": "스터디 사진",
        "what": "거북이 스터디, 튜터링, CTL 프로그램에 참여했습니다. "
                "[내용 추가 필요: 구체적으로 무엇을 공부했는지]",
        "role": "[내용 추가 필요: 맡은 역할]",
        "memory": "[내용 추가 필요: 기억에 남는 점]",
        "photos": []
    },
    {
        "id": "hackathon",
        "title": "해커톤 · 캠프",
        "category": "Challenge",
        "period": "[내용 추가 필요: 참가 시기]",
        "cover": "",
        "cover_alt": "해커톤 참가 사진",
        "what": "인하 넷제로 해커톤, 1박 2일 AI 창업 캠프 등에 참가했습니다.",
        "role": "프론트엔드 화면 제작을 맡았습니다.",
        "memory": "[내용 추가 필요: 기억에 남는 점]",
        "photos": []
    },
    {
        "id": "research",
        "title": "연구 활동",
        "category": "Research",
        "period": "[내용 추가 필요: 활동 기간]",
        "cover": "",
        "cover_alt": "연구 활동 사진",
        "what": "[내용 추가 필요: 어떤 연구에 참여했는지]",
        "role": "[내용 추가 필요: 맡은 역할]",
        "memory": "[내용 추가 필요: 기억에 남는 점]",
        "photos": []
    },
    {
        "id": "club",
        "title": "동아리 · 일상",
        "category": "Daily",
        "period": "[내용 추가 필요: 활동 기간]",
        "cover": "",
        "cover_alt": "동아리 활동 사진",
        "what": "산악회, 사진, 배드민턴 등 몸을 움직이는 활동에 참여했습니다.",
        "role": "[내용 추가 필요: 맡은 역할]",
        "memory": "[내용 추가 필요: 기억에 남는 점]",
        "photos": []
    }
]

# ---------------------------------------------------------
# 5. Projects  (카드 + 팝업)
#    status: "done" | "ongoing"
# ---------------------------------------------------------
projects = [
    {
        "id": "groovo",
        "title": "Groovo",
        "subtitle": "댄스 학습 서비스",
        "category": "Web Development",
        "status": "ongoing",
        "period": "[내용 추가 필요: 진행 기간]",
        "summary": "춤을 배우고 싶은 사람을 위한 댄스 학습 서비스입니다.",
        "cover": "",  # [사진 추가 필요: images/projects/groovo/]
        "cover_alt": "Groovo 서비스 화면",
        "role": "백엔드 담당",
        "detail": [
            "사용자 인증·인가 기능을 구현했습니다.",
            "프론트엔드에서 만든 댄스 학습 화면과 연결할 API를 만들었습니다.",
            "프론트엔드와 백엔드 사이의 요청·응답 데이터 구조를 이해하고 맞추는 작업을 했습니다."
        ],
        "skills": ["Spring Boot", "Java", "REST API"],
        "award": "",
        "todo": "현재 진행 중인 프로젝트입니다. 남은 기능은 계속 구현하고 있습니다.",
        "link": "",  # [링크 확인 필요: GitHub 저장소]
        "photos": []
    },
    {
        "id": "export-ai",
        "title": "해외배송 서류 자동화",
        "subtitle": "1박 2일 AI 창업 캠프",
        "category": "Hackathon",
        "status": "done",
        "period": "1박 2일 AI 창업 캠프",
        "summary": "해외로 물건을 보낼 때 통관번호를 찾고 서류를 작성하는 과정이 번거롭다는 점에서 시작한 프로젝트입니다.",
        "cover": "",
        "cover_alt": "해외배송 서류 자동화 화면",
        "role": "[내용 추가 필요: 캠프에서 담당한 역할]",
        "detail": [
            "해외배송 과정에서 필요한 통관번호 확인과 서류 작성의 불편을 줄이는 것이 목표였습니다.",
            "[내용 추가 필요: 실제로 만든 기능이나 화면]"
        ],
        "skills": ["[내용 추가 필요: 실제 사용 기술]"],
        "award": "우수상",
        "todo": "",
        "link": "",
        "photos": []
    },
    {
        "id": "taxi",
        "title": "택시 동승 서비스",
        "subtitle": "경기대 학생을 위한 동승자 매칭",
        "category": "Web Development",
        "status": "done",
        "period": "[내용 추가 필요: 진행 기간]",
        "summary": "여러 채팅방을 돌아다니며 택시 동승자를 찾는 게 번거롭다는 관찰에서 시작한 프로젝트입니다.",
        "cover": "",
        "cover_alt": "택시 동승 서비스 화면",
        "role": "[내용 추가 필요: 팀/개인 여부와 담당 기능]",
        "detail": [
            "같은 방향으로 가는 학생끼리 흩어진 채팅방을 찾아다니는 상황을 자주 봤습니다.",
            "한곳에서 목적지와 시간을 맞춰볼 수 있으면 좋겠다는 생각으로 시작했습니다.",
            "[내용 추가 필요: 본인이 담당한 기능]",
            "[내용 추가 필요: 어려웠던 점과 해결 방법]",
            "[내용 추가 필요: 배운 점]"
        ],
        "skills": ["HTML", "CSS", "JavaScript"],
        "award": "",
        "todo": "",
        "link": "",
        "photos": []
    },
    {
        "id": "net-zero",
        "title": "탄소 저감 발주 추천",
        "subtitle": "인하 넷제로 해커톤",
        "category": "Hackathon",
        "status": "done",
        "period": "인하 넷제로 해커톤",
        "summary": "탄소 배출을 줄이는 방향으로 발주량을 제안하는 아이디어로 참가했습니다.",
        "cover": "",
        "cover_alt": "넷제로 프로젝트 화면",
        "role": "프론트엔드",
        "detail": [
            "서비스 화면을 직접 만들었습니다.",
            "[내용 추가 필요: 직접 제작한 화면이나 기능]",
            "[내용 추가 필요: 발표 또는 결과]"
        ],
        "skills": ["HTML", "CSS", "JavaScript"],
        "award": "",
        "todo": "",
        "link": "",
        "photos": []
    },
    {
        "id": "diet",
        "title": "맞춤형 식단 추천",
        "subtitle": "개인 상황에 맞는 식단 제안",
        "category": "AI & Data",
        "status": "done",
        "period": "[내용 추가 필요: 진행 기간]",
        "summary": "개인의 조건에 맞춰 식단을 추천하는 서비스입니다.",
        "cover": "",
        "cover_alt": "식단 추천 서비스 화면",
        "role": "[내용 추가 필요: 담당한 역할]",
        "detail": [
            "[내용 추가 필요: 어떤 문제에서 시작했는지]",
            "[내용 추가 필요: 본인이 담당한 기능]"
        ],
        "skills": ["[내용 추가 필요: 실제 사용 기술]"],
        "award": "",
        "todo": "",
        "link": "",
        "photos": []
    },
    {
        "id": "krafton",
        "title": "개인 홈페이지",
        "subtitle": "크래프톤 정글 캠프 진행 중",
        "category": "Web Development",
        "status": "ongoing",
        "period": "[내용 추가 필요: 진행 기간]",
        "summary": "지금 보고 계신 이 홈페이지입니다. 크래프톤 캠프에서 진행 중인 작업물입니다.",
        "cover": "",
        "cover_alt": "개인 홈페이지 화면",
        "role": "기획 · 디자인 · 개발 전부",
        "detail": [
            "지금까지 구현한 것: Flask 라우팅과 템플릿 연결, 자 모양 인생 타임라인, "
            "프로젝트·활동 팝업, 사진 영역, 모바일 대응, AWS EC2 배포.",
            "앞으로 할 것: 사진과 실제 내용 채우기, 세부 디자인 다듬기."
        ],
        "skills": ["Flask", "HTML", "CSS", "JavaScript", "AWS EC2"],
        "award": "",
        "todo": "현재 진행 중입니다.",
        "link": "",
        "photos": []
    }
]

# ---------------------------------------------------------
# 6. Skills  (숙련도 % 대신 실제 경험으로 표시)
# ---------------------------------------------------------
skills = [
    {
        "group": "Backend",
        "list": [
            {"name": "Spring Boot", "desc": "사용자 인증·인가 및 REST API 구현 경험"},
            {"name": "Flask", "desc": "개인 홈페이지 라우팅과 템플릿 연결"}
        ]
    },
    {
        "group": "Frontend",
        "list": [
            {"name": "HTML / CSS", "desc": "개인 홈페이지와 프로젝트 화면 제작"},
            {"name": "JavaScript", "desc": "화면 상호작용과 API 연결"}
        ]
    },
    {
        "group": "Tools",
        "list": [
            {"name": "Git / GitHub", "desc": "버전 관리와 협업"},
            {"name": "Figma", "desc": "화면 구조 및 사용자 흐름 정리"},
            {"name": "AWS EC2", "desc": "Flask 애플리케이션 실행 및 외부 접속 설정"}
        ]
    }
]

# ---------------------------------------------------------
# 7. Interests  (사진 콜라주 + 라이트박스)
#    size: "wide" | "tall" | "" (기본)
# ---------------------------------------------------------
interests = [
    {"src": "", "alt": "여행 사진", "caption": "[캡션 추가 필요: 여행]", "size": "wide"},
    {"src": "", "alt": "요리 사진", "caption": "[캡션 추가 필요: 요리]", "size": ""},
    {"src": "", "alt": "콘서트 사진", "caption": "[캡션 추가 필요: 콘서트]", "size": "tall"},
    {"src": "", "alt": "등산 사진", "caption": "[캡션 추가 필요: 자연·등산]", "size": ""},
    {"src": "", "alt": "일상 사진", "caption": "[캡션 추가 필요: 일상]", "size": ""},
    {"src": "", "alt": "일상 사진", "caption": "[캡션 추가 필요: 일상]", "size": "wide"}
]

# ---------------------------------------------------------
# 8. Future
# ---------------------------------------------------------
future = [
    {
        "label": "관심 분야 찾기",
        "text": "여러 분야를 직접 해보면서 어디에 오래 머물고 싶은지 찾아보려고 합니다."
    },
    {
        "label": "배포까지 완성하기",
        "text": "직접 기획한 서비스를 만들다 마는 게 아니라 배포해서 실제로 쓰이게 하고 싶습니다."
    },
    {
        "label": "기록하는 습관",
        "text": "프로젝트를 하면서 겪은 과정과 배운 점을 그때그때 남기는 습관을 만들려고 합니다."
    }
]

# ---------------------------------------------------------
# 9. Contact
# ---------------------------------------------------------
contacts = [
    {
        "label": "Email",
        "value": "miri067979@kyonggi.ac.kr",
        "link": "mailto:miri067979@kyonggi.ac.kr"
    },
    {
        "label": "GitHub",
        "value": "github.com/MiriKim79",
        "link": "https://github.com/MiriKim79"
    },
    {
        "label": "Instagram",
        "value": "@mm_daily_wy",
        "link": "https://instagram.com/mm_daily_wy"
    }
]

# ---------------------------------------------------------
# 화면 이동용 메뉴
# ---------------------------------------------------------
nav_items = [
    {"id": "about", "label": "About"},
    {"id": "timeline", "label": "Timeline"},
    {"id": "university", "label": "University"},
    {"id": "projects", "label": "Projects"},
    {"id": "skills", "label": "Skills"},
    {"id": "interests", "label": "Interests"},
    {"id": "future", "label": "Future"},
    {"id": "contact", "label": "Contact"}
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        intro=intro,
        about=about,
        life_events=life_events,
        current_age=current_age,
        university=university,
        projects=projects,
        skills=skills,
        interests=interests,
        future=future,
        contacts=contacts,
        nav_items=nav_items
    )


if __name__ == "__main__":
    app.run(debug=True)
