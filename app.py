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
    "photo": "/images/intro/profile2.jpg",
    "photo_alt": "미리의 프로필 사진"
}

# ---------------------------------------------------------
# 2. About Me
# ---------------------------------------------------------
about = {
    "paragraphs": [
        " 길을 걷다가 어제와 달라진 간판, 식물의 모양. 주변을 둘러보는 것을 좋아해요. "
        "그냥 지나치기보다 왜 저럴까 한 번 더 생각하는 편이에요.",
        " 사람들의 행동이나 말투에서 각자의 특징을 파악해 보는 걸 좋아해요. "
        "사람들과 장난치며 이야기하는 것에서 즐거움을 얻어요.",
        " 새로운 경험을 하는 것에 거부감이 없는 편이에요. "
        "언젠가 어떻게든 도움이 된다고 생각해요. "
        "그리고 이왕 시작한 일은 끝까지 최선을 다 하려고 노력해요."
    ],
    "motto": "후회하지 않도록, 할 수 있을 때 해보기",
    # [사진 추가 필요: 본인 사진 또는 활동 사진 2장]
    "photos": [
        {"src": "/images/intro/cat.jpg", "alt": "일상 사진", "caption": "경기대 마스코트 야옹이들"},
        {"src": "/images/intro/intro.jpg", "alt": "활동 사진", "caption": "부산에서"}
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
        "photos": [{"src" : "images/timeline/age1_1.jpg", "alt": "", "caption": ""},
                   {"src" : "images/timeline/age1_2.jpg", "alt": "", "caption": ""}
                   ]  # [사진 추가 필요] {"src": "images/timeline/xxx.jpg", "alt": "", "caption": ""}
    },
    {
        "age": 6,
        "year": "2011",
        "title": "새로운 나이",
        "description": "빠른 년생으로 한 학년 위 친구들과 함께 유치원 생활을 시작했어요!",
        "photos": [{"src" : "images/timeline/age6_1.jpg", "alt": "", "caption": ""},
                   {"src" : "images/timeline/age6_2.jpg", "alt": "", "caption": ""}
                   ]
    },
    {
        "age": 13,
        "year": "2018",
        "title": "졸업 여행",
        "description": "친구들과 함께한 코타키나발루 졸업 여행. 잊지 못 할 추억이에요:)",
        "photos": [{"src" : "images/timeline/age13_1.jpg", "alt": "", "caption": ""},
                   {"src" : "images/timeline/age13_2.jpg", "alt": "", "caption": ""}
                   ]
    },
    {
        "age": 17,
        "year": "2023",
        "title": "사람과 성장",
        "description": "방송부와 전교 부회장 활동을 병행하는 동시에, 친구들을 따라다니며 공부도 열심히 했어요. 처음으로 친구와 갈등과 화해도 겪으며 성격이 T로 변하는 계기가 되기도 했지만..",
        "photos": [{"src" : "images/timeline/age17_1.jpg", "alt": "", "caption": ""},
                   {"src" : "images/timeline/age17_2.jpg", "alt": "", "caption": ""}
                   ]
    },
    {
            "age": 19,
            "year": "2024",
            "title": "시작과 끝",
            "description": "첫 대학의 입학과 자퇴, 그리고 반수. 그 결과 빠른 년생의 삶을 끝낼 수 있었어요.",
            "photos": [{"src" : "images/timeline/age19_1.jpg", "alt": "", "caption": ""},
                   {"src" : "images/timeline/age19_2.jpg", "alt": "", "caption": ""}]
        },
    {
        "age": 20,
        "year": "2025",
        "title": "원점",
        "description": "경기대학교에 입학하여 '진짜' 친구들을 만날 수 있었어요 ㅋ",
        "photos": [{"src" : "images/timeline/age20_1.jpg", "alt": "", "caption": ""},
                   {"src" : "images/timeline/age20_2.jpg", "alt": "", "caption": ""}]
    },
    {
        "age": 21,
        "year": "2026",
        "title": "현재",
        "description": "전공 공부와 함께 다양한 프로젝트, 해커톤, 대외활동 등에 도전하고 있어요.",
        "photos": [{"src" : "images/timeline/age21_1.webp", "alt": "", "caption": ""},
                   {"src" : "images/timeline/age21_2.jpg", "alt": "", "caption": ""}]
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
        "period": "2026.02 ~ ",
        "cover": "images/university/u1.jpg",  # [사진 추가 필요: 학생회 대표 사진]
        "cover_alt": "학생회 활동 사진",
        "memory": "기획차장으로서 여러 행사를 주최하고, 다양한 사람을 만나볼 수 있어요",
        "photos": [{"src" : "images/university/u1_1.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u1_2.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u1_3.jpg", "alt" : "", "caption" : ""}]  # 3~5장 권장
    },
    {
        "id": "swat",
        "title": "SWAT 봉사단",
        "category": "Community",
        "period": "2025.09 ~ ",
        "cover": "images/university/u2.jpg",
        "cover_alt": "봉사단 활동 사진",
        "memory": "창의적인 아이들과 교감하며 힐링이 돼요",
        "photos": [{"src" : "images/university/u2_1.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u2_2.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u2_3.jpg", "alt" : "", "caption" : ""}]
    },
    {
        "id": "study",
        "title": "스터디 · 학업",
        "category": "Learning",
        "period": "~ always ~",
        "cover": "images/university/u3.jpg",
        "cover_alt": "스터디 사진",
        "memory": "4점대 성적을 유지하며 CSTS, SQLD, 토익 등 자격증 공부도 해요",
        "photos": [{"src" : "images/university/u3_1.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u3_2.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u3_3.jpg", "alt" : "", "caption" : ""}]
    },
    {
        "id": "hackathon",
        "title": "해커톤 · 캠프",
        "category": "Challenge",
        "period": "2026.06 ~ ",
        "cover": "images/university/u4.webp",
        "cover_alt": "해커톤 참가 사진",
        "memory": "인하 넷제로 해커톤, AI 창업 캠프, 크래프톤 등에 참가하며 AI를 활용한 개발 실력을 기르고 있어요.",
        "photos": [{"src" : "images/university/u4_1.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u4_2.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u4_3.jpg", "alt" : "", "caption" : ""}]
    },
    {
        "id": "experience",
        "title": "대외 활동",
        "category": "Experience",
        "period": "~ always ~",
        "cover": "images/university/u5.jpg",
        "cover_alt": "활동 사진",
        "memory": "거북이 스터디, 튜터링, CTL 공모전 그리고 SW 대학의 여러 프로그램 등에 참여했어요.",
        "photos": [{"src" : "images/university/u5_1.png", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u5_2.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u5_3.jpg", "alt" : "", "caption" : ""}]
    },
    {
        "id": "club",
        "title": "동아리 · 일상",
        "category": "Daily",
        "period": "2025.03 ~ ",
        "cover": "images/university/u6.jpg",
        "cover_alt": "동아리 활동 사진",
        "memory": "산악회, 사진, 배드민턴 등 평소 관심 있던 동아리 뿐만 아니라 과 동아리에도 참여했어요.",
        "photos": [{"src" : "images/university/u6_1.webp", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u6_2.webp", "alt" : "", "caption" : ""},
                   {"src" : "images/university/u6_3.jpg", "alt" : "", "caption" : ""}]
    }
]

# ---------------------------------------------------------
# 5. Projects  (카드 + 팝업)
#    status: "done" | "ongoing"
# ---------------------------------------------------------
projects = [
    {
            "id": "diet",
            "title": "NUMATE",
            "subtitle": "SW 상상기업",
            "category": "AI & Data",
            "status": "done",
            "period": "2025.04 ~ 06",
            "summary": "개인의 조건에 맞춰 식단을 추천해주는 맞춤형 식단 추천 어플리케이션",
            "cover": "images/projects/p1.png",
            "cover_alt": "식단 추천 서비스 화면",
            "role": "기획 · AI",
            "detail": [
                "이용자의 BMI, 기초대사량과 같은 기본 정보와 선호/기피 식품, 식단 목적 등의 정보에 기반하여 개인 맞춤형 식사를 제공해주는 시스템이에요.",
                "식약처, USDA 등의 CSV를 활용하여 시중에 판매하는 식품을 추천해주기도 해요.",
                "해당 어플리케이션에 사용자의 로그가 쌓이면 그에 기반한 식단 로그를 생성할 수도 있어요."
            ],
            "skills": ["Python", "Pandas", "React"],
            "award": "우수 사업계획서상",
            "todo": "",
            "link": "",
            "photos": [{"src" : "images/projects/p1_1.jpg", "alt" : "", "caption" : ""}]
        },
    {
            "id": "taxi",
            "title": "TAXI-POT",
            "subtitle": "웹 프로그래밍",
            "category": "Web Development",
            "status": "done",
            "period": "2026.05",
            "summary": "출발지와 목적지가 유사한 경기대 학생들을 위한 택시 동승 어플리케이션",
            "cover": "images/projects/p2.png",
            "cover_alt": "택시 동승 서비스 화면",
            "role": "기획 · 디자인 · Full Stack",
            "detail": [
                "등하교 시간대에 매일같이 올라오는 커뮤니티의 택시팟 모집 글을 읽으며, 출발지와 도착지가 유사함에도 불구하고 택시 동승자를 찾는 과정이 번거롭다는 생각에서 시작했어요",
                "경기대 학생들을 대상으로 출발지가 유사한 학생들끼리 경기대 혹은 유사한 목적지로 이동할 수 있도록 구현했어요.",
                "자유로운 모집과 택시 관련 소통이 가능하도록 페이지를 구현했어요."
            ],
            "skills": ["HTML", "CSS", "JavaScript"],
            "award": "우수 발표 논문상",
            "todo": "",
            "link": "",
            "photos": [{"src" : "images/projects/p1_1.jpg", "alt" : "", "caption" : ""}]
        },
    {
        "id": "groovo",
        "title": "Groovo",
        "subtitle": "SW 상상기업",
        "category": "Web Development",
        "status": "ongoing",
        "period": "2026.03 ~ ",
        "summary": "해외 1020 대상 K-POP 댄스 학습 어플리케이션",
        "cover": "images/projects/p3.png",  # [사진 추가 필요: images/projects/groovo/]
        "cover_alt": "Groovo 서비스 화면",
        "role": "Backend",
        "detail": [
            "사용자 인증·인가 기능을 구현했어요.",
            "프론트엔드에서 만든 댄스 학습 화면과 연결할 API를 만들었어요.",
            "프론트엔드와 백엔드, AI 사이의 요청·응답 데이터 구조를 바탕으로 댄스 학습 화면을 구성하는 작업을 진행하고 있어요."
        ],
        "skills": ["Spring Boot", "Java", "REST API"],
        "award": "우수 사업계획서상",
        "todo": "현재 프로젝트가 진행 중이에요.",
        "link": "",  # [링크 확인 필요: GitHub 저장소]
        "photos": [{"src" : "images/projects/p3_1.jpg", "alt" : "", "caption" : ""}]
    },
    {
        "id": "export-ai",
        "title": "무역이지",
        "subtitle": "AI 창업 시뮬레이션 캠프",
        "category": "Hackathon",
        "status": "done",
        "period": "2026.06",
        "summary": "해외 배송 시 의류별 통관 번호 및 수출 관련 서류 자동 작성 및 제안 서비스",
        "cover": "images/projects/p4.png",
        "cover_alt": "해외배송 서류 자동화 화면",
        "role": "기획 · 디자인",
        "detail": [
            "소재마다 통관 번호가 다른 의류의 특징에 기반하여 해외 배송 시 통관번호 확인과 복잡한 서류 작성을 자동으로 할 수 있도록 구현했어요.",
            "기존에 존재하던 화장품 수출 서류 자동 작성 서비스를 벤치마킹 했어요."
        ],
        "skills": ["ChatGPT", "Gemini", "Prompt Engineering"],
        "award": "우수상",
        "todo": "",
        "link": "",
        "photos": [{"src" : "images/projects/p4_1.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/projects/p4_2.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/projects/p4_3.jpg", "alt" : "", "caption" : ""}]
    },
    {
        "id": "net-zero",
        "title": "ZeroWave",
        "subtitle": "INHA NET-ZERO 공동 해커톤",
        "category": "Hackathon",
        "status": "done",
        "period": "2026.06",
        "summary": "F&B 매장의 과잉 발주와 식품 폐기 문제를 줄이기 위한 AI 기반 발주 추천 서비스",
        "cover": "images/projects/p5.png",
        "cover_alt": "넷제로 프로젝트 화면",
        "role": "Frontend",
        "detail": [
            "중소형 F&B 매장에서 발생하는 유통 및 폐기 단계의 탄소 배출을 줄이기 위해 발주량을 제안하는 서비스를 기획하고 구현했어요.",
            "판매 데이터, 날씨, 요일, 행사 정보 등을 활용한 수요예측 결과와 추천 발주량을 직관적으로 확인할 수 있는 대시보드를 구현했어요.",
            "백엔드 API와 AI 챗봇을 연동하여 재고 현황, 발주 추천, 리포트, 자연어 질의 기능을 하나의 서비스에서 사용할 수 있도록 구현했어요."
        ],
        "skills": ["Vite", "React Router", "Javascript", "CSS3"],
        "award": "장려상",
        "todo": "",
        "link": "",
        "photos": [{"src" : "images/projects/p5_1.webp", "alt" : "", "caption" : ""},
                   {"src" : "images/projects/p5_2.jpg", "alt" : "", "caption" : ""},
                   {"src" : "images/projects/p5_3.jpg", "alt" : "", "caption" : ""}]
    },
    {
        "id": "krafton",
        "title": "미리의 성장기",
        "subtitle": "크래프톤 정글 캠프 진행 중",
        "category": "Web Development",
        "status": "ongoing",
        "period": "2026.08",
        "summary": "지금 보고 계신 이 홈페이지가 바로 크래프톤 캠프에서 진행 중인 개인 프로젝트 작업이에요.",
        "cover": "images/projects/p6.png",
        "cover_alt": "개인 홈페이지 화면",
        "role": "기획 · 디자인 · Full Stack",
        "detail": [
            "별명이 밀리리터(mm)였던 점을 이용하여 일생 타임라인을 자 모양으로 정리해봤어요.",
            "Flask 라우팅과 템플릿 연결, 모바일 대응, AWS EC2 배포 등의 기능을 바탕으로 진행했어요.",
            "개인 프로젝트와 팀 프로젝트를 다양하게 경험할 수 있어요."
        ],
        "skills": ["Flask", "HTML", "CSS", "JavaScript", "AWS EC2"],
        "award": "",
        "todo": "현재 프로젝트가 진행 중이에요.",
        "link": "",
        "photos": [{"src" : "images/projects/p6_1.png", "alt" : "", "caption" : ""}]
    }
]

# ---------------------------------------------------------
# 6. Skills  (숙련도 % 대신 실제 경험으로 표시)
# ---------------------------------------------------------
skills = [
    {
        "group": "Languages",
        "list": [
            {"name": "Java"},
            {"name": "Python"},
            {"name": "JavaScript"},
            {"name": "C"}
        ]
    },
    {
        "group": "Backend",
        "list": [
            {"name": "Spring Boot"},
            {"name": "Flask"},
            {"name": "REST API"}
        ]
    },
    {
        "group": "Frontend",
        "list": [
            {"name": "HTML"},
            {"name": "CSS"},
            {"name": "React"}
        ]
    },
    {
        "group": "Tools",
        "list": [
            {"name": "Git"},
            {"name": "GitHub"},
            {"name": "Figma"},
            {"name": "AWS EC2"},
            {"name": "Docker"}
        ]
    }
]

# ---------------------------------------------------------
# 7. Interests  (사진 콜라주 + 라이트박스)
#    size: "wide" | "tall" | "" (기본)
# ---------------------------------------------------------
interests = [
    {"src": "images/interests/i1.jpg", "alt": "여행 사진", "caption": "대학 동기들과 제주도 여행", "size": "wide"},
    {"src": "images/interests/i2.jpg", "alt": "요리 사진", "caption": "미리표 오삼불고기", "size": ""},
    {"src": "images/interests/i3.jpg", "alt": "콘서트 사진", "caption": "데이식스 콘서트", "size": "tall"},
    {"src": "images/interests/i4.jpg", "alt": "자연 사진", "caption": "제주 바다", "size": ""},
    {"src": "images/interests/i5.webp", "alt": "일상 사진", "caption": "흔한 시험 기간", "size": ""},
    {"src": "images/interests/i6.jpg", "alt": "일상 사진", "caption": "눈사람 로망", "size": ""},
    {"src": "images/interests/i7.jpg", "alt": "일상 사진", "caption": "맛집 탐방", "size": "wide"}
]

# ---------------------------------------------------------
# 8. Future
# ---------------------------------------------------------
future = [
    {
        "label": "관심 분야 탐색",
        "text": "여러 분야를 접해보면서 어디에 마음이 끌리는지 찾아보려고 해요."
    },
    {
        "label": "기록하는 습관",
        "text": "프로젝트를 하면서 겪은 과정과 배운 점을 그때그때 남기는 습관을 만들려고 노력 중이에요."
    },
    {
        "label": "해외 진출",
        "text": "국내에서의 대외활동 뿐만 아니라 학교에서 지원해주는 해외 연수 활동을 해보고 싶어요."
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
