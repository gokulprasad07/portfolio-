/* Main behaviour: nav, rendering, filters, modal, scroll effects */
const $ = (s, el = document) => el.querySelector(s);
const el = (tag, cls, html) => { const n = document.createElement(tag); if (cls) n.className = cls; if (html) n.innerHTML = html; return n; };
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

// Mobile menu
const menu = $("#menu"), burger = $("#burger");
burger.onclick = () => { const o = menu.classList.toggle("open"); burger.setAttribute("aria-expanded", o); };
menu.onclick = e => { if (e.target.tagName === "A") { menu.classList.remove("open"); burger.setAttribute("aria-expanded", false); } };

// Active nav highlighting
const links = [...menu.querySelectorAll("a")];
const spy = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) links.forEach(a => a.classList.toggle("active", a.hash === "#" + e.target.id));
}), { rootMargin: "-45% 0px -50% 0px" });
document.querySelectorAll("main section").forEach(s => spy.observe(s));

// Scroll reveal
const reveal = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); reveal.unobserve(e.target); } }), { threshold: .12 });
const watch = (n, i = 0) => { n.classList.add("rv"); n.style.transitionDelay = Math.min(i, 8) * 70 + "ms"; reveal.observe(n); };

// Hero typed code
const codeLines = "# gokul.py\nfrom sklearn.cluster import KMeans\n\nclass Gokul:\n    studying = 'B.Sc. AI & ML'\n    design_years = 2\n    now_building = ['ML', 'Full Stack']\n\n    def approach(self):\n        return 'design clarity + data'";
const typed = $("#typed");
if (matchMedia("(prefers-reduced-motion: reduce)").matches) typed.textContent = codeLines;
else { let i = 0; setTimeout(function t() { typed.textContent = codeLines.slice(0, ++i); if (i < codeLines.length) setTimeout(t, 28); }, 1500); }

// Skills
const skillGrid = $("#skillGrid");
Object.entries(SKILLS).forEach(([group, items], i) => {
  const c = el("div", "card skill", `<h3>${esc(group)}</h3>` + items.map(s => `<span class="${s.includes("(learning)") ? "learn" : ""}">${esc(s)}</span>`).join(""));
  skillGrid.append(c); watch(c, i);
});

// Link buttons: real href => anchor, otherwise a disabled, clearly labelled button
function linkButton(label, href) {
  if (!href) { const b = el("span", "btn off", esc(label) + " (not added yet)"); b.setAttribute("aria-disabled", "true"); return b; }
  const a = el("a", "btn", esc(label)); a.href = href; a.target = "_blank"; a.rel = "noopener"; return a;
}

// Projects
let activeCat = "All";
const filters = $("#filters"), grid = $("#projectGrid"), search = $("#search");
["All", ...new Set(PROJECTS.map(p => p.category))].forEach(cat => {
  const b = el("button", cat === "All" ? "on" : "", esc(cat));
  b.onclick = () => { activeCat = cat; filters.querySelectorAll("button").forEach(x => x.classList.toggle("on", x === b)); renderProjects(); };
  filters.append(b);
});
function renderProjects() {
  const q = search.value.trim().toLowerCase();
  grid.innerHTML = "";
  const shown = PROJECTS.filter(p => (activeCat === "All" || p.category === activeCat) &&
    (p.title + p.summary + p.stack.join(" ")).toLowerCase().includes(q));
  if (!shown.length) grid.append(el("p", "muted", "No projects match."));
  shown.forEach((p, i) => {
    const c = el("button", "card proj", `<div class="thumb">${esc(p.title.split(" ").map(w => w[0]).join("").slice(0, 3))}</div>
      <span class="status-tag">${esc(p.status)}</span><h3>${esc(p.title)}</h3><p class="muted">${esc(p.summary)}</p>
      <div class="stack">${p.stack.map(s => `<span>${esc(s)}</span>`).join("")}</div>`);
    c.onclick = () => openProject(p); grid.append(c); watch(c, i);
  });
}
search.oninput = renderProjects; renderProjects();

// Modal (projects + creative lightbox)
const modal = $("#modal"), body = $("#mBody"); let lastFocus;
function openModal(node) {
  lastFocus = document.activeElement; body.replaceChildren(node); modal.hidden = false;
  requestAnimationFrame(() => modal.classList.add("open")); $("#mClose").focus(); document.body.style.overflow = "hidden";
}
function closeModal() {
  modal.classList.remove("open"); document.body.style.overflow = "";
  setTimeout(() => { modal.hidden = true; body.replaceChildren(); lastFocus && lastFocus.focus(); }, 300);
}
$("#mClose").onclick = closeModal;
modal.onclick = e => { if (e.target === modal) closeModal(); };
addEventListener("keydown", e => { if (e.key === "Escape" && !modal.hidden) closeModal(); });

function openProject(p) {
  const n = el("div");
  n.innerHTML = `<span class="status-tag">${esc(p.category)} &middot; ${esc(p.status)}</span><h2 id="mTitle">${esc(p.title)}</h2>
    <h3>Problem</h3><p>${esc(p.problem)}</p>` + p.details.map(([h, t]) => `<h3>${esc(h)}</h3><p>${esc(t)}</p>`).join("") +
    `<h3>Technologies</h3><div class="stack">${p.stack.map(s => `<span>${esc(s)}</span>`).join("")}</div><h3>Files and links</h3>`;
  if (p.images) {
    n.append(el("h3", "", "Charts from the notebook (click to enlarge)"));
    const strip = el("div", "grid"); strip.style.gridTemplateColumns = "repeat(auto-fill,minmax(150px,1fr))";
    p.images.forEach(([src, alt]) => { const b = el("button", "creative-item", `<img src="${esc(src)}" alt="${esc(alt)}" loading="lazy" style="height:100px"><div class="muted" style="font-size:.78rem">${esc(alt)}</div>`);
      b.onclick = () => { const big = el("div"); big.append(Object.assign(el("img"), { src, alt }), el("p", "muted", esc(alt))); const back = el("button", "btn", "Back to project"); back.onclick = () => openProject(p); big.append(back); body.replaceChildren(big); };
      strip.append(b); });
    n.append(strip);
  }
  const row = el("div", "btns");
  LINK_TYPES.forEach(t => row.append(linkButton(t, p.links[t])));
  n.append(row); openModal(n);
}

// Creative gallery
const cg = $("#creativeGrid");
if (!CREATIVE.length) {
  cg.append(el("div", "creative-empty", "No creative work added yet.<br>Planned categories: " + CREATIVE_CATEGORIES.map(esc).join(", ") + "."));
} else CREATIVE.forEach((c, i) => {
  const b = el("button", "creative-item", `<img src="${esc(c.thumb || c.src)}" alt="${esc(c.title)}" loading="lazy"><div><strong>${esc(c.title)}</strong><br><span class="muted">${esc(c.category)}</span></div>`);
  b.querySelector("img").onerror = e => { e.target.alt = "Image file missing: " + c.src; };
  b.onclick = () => {
    const n = el("div"); n.append(c.type === "video" ? Object.assign(el("video"), { src: c.src, controls: true }) : Object.assign(el("img"), { src: c.src, alt: c.title }));
    n.append(el("h3", "", esc(c.title)), el("p", "", esc(c.description || ""))); openModal(n);
  };
  cg.append(b); watch(b, i);
});

// Resume and contact (graceful when not provided)
const rb = $("#resumeBtn"), hr = $("#heroResume");
if (PROFILE.resume) { rb.href = PROFILE.resume; rb.setAttribute("download", ""); hr.href = PROFILE.resume; hr.setAttribute("download", ""); $("#resumeMsg").textContent = "My latest resume as a PDF."; }
else { $("#resumeMsg").textContent = "My latest resume as a PDF."; }
const cl = $("#contactLinks");
[["Email", PROFILE.email && "mailto:" + PROFILE.email], ["GitHub", PROFILE.github], ["LinkedIn", PROFILE.linkedin]].forEach(([l, h]) => cl.append(linkButton(l, h)));
$("#yr").textContent = new Date().getFullYear();
document.querySelectorAll(".sec,.card.feature,.edu,.prose").forEach(n => watch(n));
