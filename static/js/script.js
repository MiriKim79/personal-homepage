const startButton = document.querySelector("#start-button");
const aboutSecton = document.querySelector("#about");
const currentAge = 21;

startButton.addEventListener("click", function () {
    aboutSection.scrollIntoView({
        behavior: "smooth"
    });
});

// 인생 사건 데이터
const lifeEvents = [
    { age: 1, title: "세상 밖으로", description: "2006년, 나의 이야기가 시작된 순간" },
    { age: 6, title: "새로운 나이", description: "빠른 년생의 시작 5살 이후 6살이 아닌 7살 반의 유치원으로 가며, " },
    { age: 13, title: "졸업 여행", description: "친구들과 코타키나발루 여행, 잊지 못 할 추억" },
    { age: 18, title: "사람과 성장", description: "전교 부회장, 우등생 친구들, 공부 열정, 친구와의 싸움, 성격 변화" },
    { age: 20, title: "시작과 끝", description: "첫 대학의 입학과 자퇴, 반수, 빠른 년생의 끝, 경기대" },
    { age: 21, title: "현재", description: "경험, 도전, 성장" }
];

const eventAges = [];
for (let i = 0; i < lifeEvents.length; i++) {
    eventAges.push(lifeEvents[i].age);
}

// 자 눈금 만들기
const ruler = document.querySelector(".ruler");
for (let age = 0; age <= 100; age++) {
    const tick = document.createElement("div");
    tick.className = "tick";
    tick.style.left = age * 26 + 24 + "px";

    if (age % 10 === 0) {
        tick.classList.add("tick-big");
        tick.innerHTML = "<span class='tick-label'>" + age + "</span>"
    }

    if (age > currentAge) {
        tick.classList.add("tick-future");
    }

    if (eventAges.includes(age)) {
        tick.classList.add("tick-event");
        tick.dataset.age = age;
        tick.addEventListener("click", showEvent);
    }

    ruler.appendChild(tick);
}

// 눈금 클릭 시 카드 내용 바꾸기
const eventTitle = document.querySelector("#event-title");
const eventDescription = document.querySelector("#event-description");

function showEvent(clickEvent) {
    const clickedTick = clickEvent.currentTarget;
    const clickedAge = Number(clickedTick.dataset.age);

    for (let i = 0; i < lifeEvents.length; i++) {
        if (lifeEvents[i].age === clickedAge) {
            eventTitle.textContent = lifeEvents[i].age + "세 · " + lifeEvents[i].title;
            eventDescription.textContent = lifeEvents[i].description;
        }
    }

    const allTicks = document.querySelectorAll(".tick-event");
    for (let i = 0; i < allTicks.length; i++) {
        allTicks[i].classList.remove("tick-active");
    }
    clickedTick.classList.add("tick-active");
}

// 지나온 구간 채우기
const filled = document.createElement("div");
filled.className = "ruler-filled";
filled.style.width = currentAge * 26 + 24 + 3 + "px";
ruler.appendChild(filled);

// 스크롤 등장 효과
const revealTargets = document.querySelectorAll("section h2, .card, .ruler-area");

for (let i = 0; i < revealTargets.length; i++) {
  revealTargets[i].classList.add("reveal");
}

const revealWatcher = new IntersectionObserver(function (entries) {
  for (let i = 0; i < entries.length; i++) {
    if (entries[i].isIntersecting) {
      entries[i].target.classList.add("reveal-on");
    }
  }
}, { threshold: 0.15 });

for (let i = 0; i < revealTargets.length; i++) {
  revealWatcher.observe(revealTargets[i]);
}

// 오른쪽 끝 안내 문구
const futureNote = document.createElement("div");
futureNote.className = "future-note";
futureNote.textContent = "아직 채워지지 않은 이야기가 많이 남아 있어요";
futureNote.style.left = 60 * 26 + 24 + "px";
ruler.appendChild(futureNote);

// 첫 사건 자동 선택
const firstTick = document.querySelector(".tick-event");
if (firstTick) {
  firstTick.click();
}

// 처음으로 돌아가기
const topButton = document.querySelector("#top-button");
const introSection = document.querySelector("#intro");

topButton.addEventListener("click", function () {
  introSection.scrollIntoView({
    behavior: "smooth"
  });
});