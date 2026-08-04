// =========================================================
// 0. 데이터 읽기
// =========================================================
const siteData = JSON.parse(document.querySelector("#site-data").textContent);
const lifeEvents = siteData.lifeEvents;
const currentAge = siteData.currentAge;
const staticBase = siteData.staticBase;

function imgUrl(path) {
    return staticBase + path;
}

// 사진이 있으면 <img>, 없으면 placeholder
function photoHtml(src, alt, cls) {
    if (src) {
        return '<img class="' + cls + '" src="' + imgUrl(src) +
            '" alt="' + (alt || "") + '" loading="lazy">';
    }
    return '<div class="photo-empty ' + cls + '" role="img" aria-label="사진 준비 중"><span>사진 준비 중</span></div>';
}

function galleryHtml(photos) {
    if (!photos || photos.length === 0) {
        return '<div class="modal-note">사진을 추가하면 이곳에 갤러리가 표시됩니다.</div>';
    }
    let html = '<div class="modal-gallery">';
    for (let i = 0; i < photos.length; i++) {
        html += photoHtml(photos[i].src, photos[i].alt, "");
    }
    return html + "</div>";
}

// =========================================================
// 1. Intro → 본문 전환
// =========================================================
const introSection = document.querySelector("#intro");
const mainContent = document.querySelector("#main-content");
const siteNav = document.querySelector("#site-nav");
const startButton = document.querySelector("#start-button");
const aboutSection = document.querySelector("#about");

function showMain() {
    mainContent.classList.add("main-on");
    siteNav.classList.add("nav-on");
}

startButton.addEventListener("click", function () {
    showMain();
    introSection.classList.add("intro-away");
    window.setTimeout(function () {
        aboutSection.scrollIntoView({ behavior: "smooth" });
        introSection.classList.remove("intro-away");
    }, 380);
});

// 스크롤로 내려가도 본문이 보이도록
window.addEventListener("scroll", function () {
    if (window.scrollY > 80) {
        showMain();
    }
});

// =========================================================
// 2. 상단 메뉴 이동 + 현재 위치 표시
// =========================================================
const navButtons = document.querySelectorAll(".nav-link, .nav-home");

for (let i = 0; i < navButtons.length; i++) {
    navButtons[i].addEventListener("click", function (e) {
        const targetId = e.currentTarget.dataset.target;
        const target = document.querySelector("#" + targetId);
        if (target) {
            showMain();
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
}

const progressBar = document.querySelector("#progress-bar");
const allSections = document.querySelectorAll("main section");
const navLinks = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", function () {
    // 진행 막대
    const scrollable = document.body.scrollHeight - window.innerHeight;
    const ratio = scrollable > 0 ? window.scrollY / scrollable : 0;
    progressBar.style.width = ratio * 100 + "%";

    // 현재 섹션 표시
    let currentId = "";
    for (let i = 0; i < allSections.length; i++) {
        if (allSections[i].getBoundingClientRect().top <= 120) {
            currentId = allSections[i].id;
        }
    }
    for (let i = 0; i < navLinks.length; i++) {
        if (navLinks[i].dataset.target === currentId) {
            navLinks[i].classList.add("nav-active");
        } else {
            navLinks[i].classList.remove("nav-active");
        }
    }
});

// =========================================================
// 3. 팝업 (공용)
// =========================================================
const overlay = document.querySelector("#modal-overlay");
const modalBody = document.querySelector("#modal-body");
const modalClose = document.querySelector("#modal-close");
let lastFocused = null;

function openModal(html) {
    lastFocused = document.activeElement;
    modalBody.innerHTML = html;
    overlay.hidden = false;
    document.body.classList.add("no-scroll");
    modalClose.focus();
}

function closeModal() {
    overlay.hidden = true;
    modalBody.innerHTML = "";
    document.body.classList.remove("no-scroll");
    if (lastFocused) {
        lastFocused.focus();
    }
}

modalClose.addEventListener("click", closeModal);

// 바깥 클릭으로 닫기
overlay.addEventListener("click", function (e) {
    if (e.target === overlay) {
        closeModal();
    }
});

// ESC로 닫기
document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !overlay.hidden) {
        closeModal();
    }
});

// =========================================================
// 4. 팝업 내용 만들기
// =========================================================
function findById(list, id) {
    for (let i = 0; i < list.length; i++) {
        if (list[i].id === id) {
            return list[i];
        }
    }
    return null;
}

function openUniModal(id) {
    const item = findById(siteData.university, id);
    if (!item) return;

    let html = '<h3 id="modal-title">' + item.title + "</h3>";
    html += '<p class="modal-meta">' + item.category + " · " + item.period + "</p>";
    html += photoHtml(item.cover, item.cover_alt, "modal-cover");
    html += '<div class="modal-section"><h4>무엇을 했나</h4><p>' + item.what + "</p></div>";
    html += '<div class="modal-section"><h4>맡은 역할</h4><p>' + item.role + "</p></div>";
    html += '<div class="modal-section"><h4>기억에 남는 점</h4><p>' + item.memory + "</p></div>";
    html += galleryHtml(item.photos);
    openModal(html);
}

function openProjectModal(id) {
    const p = findById(siteData.projects, id);
    if (!p) return;

    let html = '<h3 id="modal-title">' + p.title + "</h3>";
    html += '<p class="modal-meta">' + p.subtitle + " · " + p.period + "</p>";
    html += photoHtml(p.cover, p.cover_alt, "modal-cover");

    if (p.status === "ongoing" && p.todo) {
        html += '<div class="modal-note">' + p.todo + "</div>";
    }
    if (p.award) {
        html += '<div class="modal-note">수상 · ' + p.award + "</div>";
    }

    html += '<div class="modal-section"><h4>어떤 프로젝트인가</h4><p>' + p.summary + "</p></div>";

    html += '<div class="modal-section"><h4>한 일</h4><ul>';
    for (let i = 0; i < p.detail.length; i++) {
        html += "<li>" + p.detail[i] + "</li>";
    }
    html += "</ul></div>";

    html += '<div class="modal-section"><h4>역할</h4><p>' + p.role + "</p></div>";

    html += '<div class="modal-section"><h4>사용 기술</h4><div class="tag-row">';
    for (let i = 0; i < p.skills.length; i++) {
        html += '<span class="tag">' + p.skills[i] + "</span>";
    }
    html += "</div></div>";

    if (p.link) {
        html += '<a class="modal-link" href="' + p.link + '" target="_blank" rel="noopener">관련 링크 열기</a>';
    }
    html += galleryHtml(p.photos);
    openModal(html);
}

function openEventModal(age) {
    let ev = null;
    for (let i = 0; i < lifeEvents.length; i++) {
        if (lifeEvents[i].age === age) {
            ev = lifeEvents[i];
        }
    }
    if (!ev) return;

    let html = '<h3 id="modal-title">' + ev.title + "</h3>";
    html += '<p class="modal-meta">' + ev.year + " · " + ev.age + "세</p>";
    html += '<div class="modal-section"><p>' + ev.description + "</p></div>";
    html += galleryHtml(ev.photos);
    openModal(html);
}

function openPhotoModal(index) {
    const photo = siteData.interests[index];
    if (!photo || !photo.src) return;

    let html = '<h3 id="modal-title" class="sr-title">' + (photo.alt || "사진") + "</h3>";
    html += '<img class="modal-photo" src="' + imgUrl(photo.src) + '" alt="' + photo.alt + '">';
    html += '<p class="modal-meta" style="margin-top:12px">' + photo.caption + "</p>";
    openModal(html);
}

// 클릭 연결
const uniTiles = document.querySelectorAll('[data-kind="uni"]');
for (let i = 0; i < uniTiles.length; i++) {
    uniTiles[i].addEventListener("click", function (e) {
        openUniModal(e.currentTarget.dataset.id);
    });
}

const projectCards = document.querySelectorAll('[data-kind="project"]');
for (let i = 0; i < projectCards.length; i++) {
    projectCards[i].addEventListener("click", function (e) {
        openProjectModal(e.currentTarget.dataset.id);
    });
}

const photoButtons = document.querySelectorAll('[data-kind="photo"]');
for (let i = 0; i < photoButtons.length; i++) {
    photoButtons[i].addEventListener("click", function (e) {
        openPhotoModal(Number(e.currentTarget.dataset.index));
    });
}

// =========================================================
// 5. 자 눈금 만들기
// =========================================================
const eventAges = [];
for (let i = 0; i < lifeEvents.length; i++) {
    eventAges.push(lifeEvents[i].age);
}

const ruler = document.querySelector(".ruler");

for (let age = 0; age <= 100; age++) {
    const isEvent = eventAges.includes(age);
    const tick = document.createElement(isEvent ? "button" : "div");
    tick.className = "tick";
    tick.style.left = age * 26 + 24 + "px";

    if (age % 10 === 0) {
        tick.classList.add("tick-big");
        tick.innerHTML = "<span class='tick-label'>" + age + "</span>";
    }

    if (age > currentAge) {
        tick.classList.add("tick-future");
    }

    if (isEvent) {
        tick.classList.add("tick-event");
        tick.dataset.age = age;
        tick.setAttribute("aria-label", age + "세 이야기 보기");
        tick.addEventListener("click", function (e) {
            const clickedAge = Number(e.currentTarget.dataset.age);
            const all = document.querySelectorAll(".tick-event");
            for (let j = 0; j < all.length; j++) {
                all[j].classList.remove("tick-active");
            }
            e.currentTarget.classList.add("tick-active");
            openEventModal(clickedAge);
        });
    }

    ruler.appendChild(tick);
}

// 지나온 구간 채우기
const filled = document.createElement("div");
filled.className = "ruler-filled";
filled.style.width = currentAge * 26 + 24 + 3 + "px";
ruler.appendChild(filled);

// 오른쪽 끝 안내 문구
const futureNote = document.createElement("div");
futureNote.className = "future-note";
futureNote.textContent = "아직 쓰지 않은 이야기가 남아 있어요";
futureNote.style.left = 60 * 26 + 24 + "px";
ruler.appendChild(futureNote);

// =========================================================
// 6. 모바일용 세로 타임라인
// =========================================================
const timelineVertical = document.querySelector(".timeline-vertical");

for (let i = 0; i < lifeEvents.length; i++) {
    const ev = lifeEvents[i];
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.className = "tv-btn";
    btn.innerHTML =
        '<span class="tv-age">' + ev.year + " · " + ev.age + "세</span>" +
        '<span class="tv-title">' + ev.title + "</span>";
    btn.addEventListener("click", function () {
        openEventModal(ev.age);
    });
    li.appendChild(btn);
    timelineVertical.appendChild(li);
}

// =========================================================
// 7. 스크롤 등장 효과
// =========================================================
const revealTargets = document.querySelectorAll(
    "main section h2, .about-layout, .about-motto, .ruler-area, .timeline-vertical, " +
    ".tile, .project-card, .skill-group, .collage-item, .future-item, .contact-item"
);

for (let i = 0; i < revealTargets.length; i++) {
    revealTargets[i].classList.add("reveal");
}

const revealWatcher = new IntersectionObserver(function (entries) {
    for (let i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
            entries[i].target.classList.add("reveal-on");
        }
    }
}, { threshold: 0.12 });

for (let i = 0; i < revealTargets.length; i++) {
    revealWatcher.observe(revealTargets[i]);
}

// =========================================================
// 8. 처음으로 돌아가기
// =========================================================
const topButton = document.querySelector("#top-button");

topButton.addEventListener("click", function () {
    introSection.scrollIntoView({ behavior: "smooth" });
});
