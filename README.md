<!DOCTYPE html>
<html lang="en" class="dark">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>BNTiyan – Open Source Analytics</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&family=Syne:wght@700;800&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #09090b;
    --bg2: #111113;
    --border: #27272a;
    --border-hover: #7c3aed55;
    --text: #fafafa;
    --muted: #71717a;
    --purple: #a855f7;
    --purple-dark: #7c3aed;
    --blue: #3b82f6;
    --emerald: #10b981;
    --amber: #f59e0b;
    --pink: #ec4899;
    --orange: #ea580c;
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    min-height: 100vh;
    padding: 40px 24px;
  }

  /* ── HEADER ── */
  .header {
    text-align: center;
    margin-bottom: 40px;
  }
  .header h2 {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    color: var(--text);
  }
  .header h2 svg { color: var(--purple); }
  .header p {
    color: var(--muted);
    margin-top: 8px;
    font-size: 0.78rem;
    max-width: 520px;
    margin-inline: auto;
    line-height: 1.6;
  }

  /* ── GRID ── */
  .grid-3 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 20px;
  }
  .grid-bottom {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 20px;
  }
  @media (max-width: 900px) {
    .grid-bottom { grid-template-columns: 1fr; }
  }

  /* ── CARD BASE ── */
  .card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    transition: border-color .3s, transform .2s;
  }
  .card:hover { border-color: var(--border-hover); transform: translateY(-2px); }

  .card-header {
    padding: 14px 18px;
    border-bottom: 1px solid var(--border);
    background: var(--bg);
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .06em;
    color: #d4d4d8;
  }
  .card-body { padding: 20px; }

  /* ── STAT GRID (repo metrics) ── */
  .stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .stat-item {
    background: #18181b;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px;
  }
  .stat-label-row { display: flex; align-items: center; gap: 6px; margin-bottom: 4px; }
  .stat-label { font-size: 0.6rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; }
  .stat-value { font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 800; }
  .badge-top5 {
    margin-top: 14px;
    background: #a855f720;
    border: 1px solid #a855f740;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    font-size: 0.65rem;
    font-weight: 700;
    color: var(--purple);
    letter-spacing: .04em;
  }

  /* ── LANGUAGE BARS ── */
  .lang-list { display: flex; flex-direction: column; gap: 14px; }
  .lang-row { display: flex; flex-direction: column; gap: 4px; }
  .lang-label-row { display: flex; justify-content: space-between; font-size: 0.63rem; font-weight: 700; color: #a1a1aa; text-transform: uppercase; letter-spacing: .06em; }
  .bar-track { height: 6px; width: 100%; background: #27272a; border-radius: 999px; overflow: hidden; }
  .bar-fill { height: 100%; border-radius: 999px; transition: width 1.2s cubic-bezier(.22,1,.36,1); }

  /* ── FEATURED CARD ── */
  .featured {
    background: linear-gradient(135deg, #7c3aed, #4338ca);
    border: none;
    border-radius: 16px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }
  .featured-bg-icon {
    position: absolute; top: 0; right: 0;
    padding: 20px; opacity: .08;
    transition: transform .5s;
  }
  .featured:hover .featured-bg-icon { transform: scale(1.15); }
  .feat-meta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
  .feat-chip {
    display: flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,.15);
    border-radius: 8px;
    padding: 5px 10px;
    font-size: 0.6rem; font-weight: 700; text-transform: uppercase; letter-spacing: .08em;
    color: #ddd6fe;
    backdrop-filter: blur(8px);
  }
  .feat-badge {
    background: #10b98130; border: 1px solid #10b98150;
    color: #6ee7b7; font-size: 0.55rem; font-weight: 700;
    padding: 2px 8px; border-radius: 6px;
  }
  .feat-title { font-family: 'Syne', sans-serif; font-size: 1.6rem; font-weight: 800; color: #fff; margin-bottom: 2px; }
  .feat-sub { font-size: 0.58rem; color: rgba(221,214,254,.5); text-transform: uppercase; letter-spacing: .1em; margin-bottom: 10px; }
  .feat-desc { font-size: 0.72rem; color: rgba(237,233,254,.85); line-height: 1.6; margin-bottom: 16px; }
  .feat-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px; }
  .feat-stat {
    background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.12);
    border-radius: 10px; padding: 8px; text-align: center;
  }
  .feat-stat-val { font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 800; color: #fff; }
  .feat-stat-lbl { font-size: 0.55rem; color: rgba(221,214,254,.55); text-transform: uppercase; font-weight: 700; letter-spacing: .08em; }
  .feat-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 18px; }
  .feat-tag {
    background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.2);
    color: #fff; font-size: 0.58rem; font-weight: 700;
    padding: 3px 8px; border-radius: 6px; backdrop-filter: blur(4px);
  }
  .feat-btn {
    display: flex; align-items: center; justify-content: center; gap: 8px;
    width: 100%; background: #fff; color: #6d28d9;
    border: none; border-radius: 12px; padding: 12px;
    font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; font-weight: 700;
    cursor: pointer; transition: background .2s, transform .15s;
    text-decoration: none;
  }
  .feat-btn:hover { background: #ede9fe; transform: scale(1.02); }

  /* ── MASTERY MATRIX ── */
  .mastery-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 28px; }
  .mastery-title { font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 800; display: flex; align-items: center; gap: 8px; }
  .mastery-sub { font-size: 0.58rem; color: var(--muted); margin-top: 4px; text-transform: uppercase; letter-spacing: .12em; }
  .mastery-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
  @media (max-width: 700px) { .mastery-grid { grid-template-columns: 1fr; } }
  .skill-section-title {
    font-size: 0.6rem; font-weight: 700; text-transform: uppercase; letter-spacing: .12em;
    padding-bottom: 8px; border-bottom: 1px solid;
    margin-bottom: 14px;
  }
  .skill-list { display: flex; flex-direction: column; gap: 12px; }
  .skill-row { display: flex; flex-direction: column; gap: 4px; }
  .skill-label-row { display: flex; justify-content: space-between; font-size: 0.63rem; font-weight: 700; color: #d4d4d8; }
  .skill-track { height: 5px; background: #27272a; border-radius: 999px; overflow: hidden; }
  .skill-fill { height: 100%; border-radius: 999px; }

  /* ── RIGHT COLUMN ── */
  .right-col { display: flex; flex-direction: column; gap: 16px; }
  .contrib-card { flex: 1; }
  .contrib-inner { display: flex; flex-direction: column; justify-content: space-between; height: 100%; }
  .contrib-label { font-size: 0.6rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: .12em; margin-bottom: 14px; }
  .contrib-list { display: flex; flex-direction: column; gap: 12px; }
  .contrib-item { display: flex; align-items: center; gap: 12px; }
  .contrib-badge {
    width: 32px; height: 32px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.6rem; font-weight: 700; flex-shrink: 0;
  }
  .contrib-text { font-size: 0.68rem; color: var(--muted); line-height: 1.4; }
  .contrib-footer { margin-top: 16px; padding-top: 14px; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
  .avail-label { font-size: 0.55rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: .1em; }
  .avail-status { display: flex; align-items: center; gap: 6px; font-size: 0.65rem; font-weight: 700; color: var(--emerald); }
  .ping { position: relative; width: 8px; height: 8px; }
  .ping-inner, .ping-outer { position: absolute; inset: 0; border-radius: 50%; background: var(--emerald); }
  .ping-outer { animation: ping 1.2s ease-out infinite; opacity: .7; }
  @keyframes ping { 0%{transform:scale(1);opacity:.7} 100%{transform:scale(2.2);opacity:0} }

  .analytics-card {
    background: linear-gradient(135deg, #18181b, #09090b);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    text-align: center;
  }
  .analytics-label { font-size: 0.6rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: .12em; margin-bottom: 8px; }
  .analytics-val { font-family: 'Syne', sans-serif; font-size: 2.2rem; font-weight: 800; color: #fff; }
  .analytics-sub { font-size: 0.65rem; font-weight: 700; color: var(--purple); margin-top: 4px; }
  .pulse-bars { display: flex; justify-content: center; gap: 4px; margin-top: 16px; }
  .pulse-bar {
    width: 4px; border-radius: 999px; background: #a855f740;
    animation: pulsebar 1s ease-in-out infinite alternate;
  }
  @keyframes pulsebar { from{height:8px;opacity:.4} to{height:20px;opacity:1} }

  /* svg icons inline */
  svg { display: inline-block; vertical-align: middle; }
</style>
</head>
<body>

<section id="github-stats" style="max-width:1200px;margin:0 auto;">

  <!-- Header -->
  <div class="header">
    <h2>
      <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
      Open Source Analytics
    </h2>
    <p>Real-time visibility into development activity, tech stack distribution, and repository impact.</p>
  </div>

  <!-- Top 3-col grid -->
  <div class="grid-3">

    <!-- Repo Metrics -->
    <div class="card">
      <div class="card-header">
        <svg width="14" height="14" fill="#f59e0b" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.851 1.416 8.255L12 19.771l-7.416 4.083L6 15.599 0 9.748l8.332-1.73z"/></svg>
        Repository Metrics
      </div>
      <div class="card-body">
        <div class="stat-grid">
          <div class="stat-item">
            <div class="stat-label-row">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="#a855f7"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
              <span class="stat-label">Public Repos</span>
            </div>
            <div class="stat-value" style="color:#a855f7">42</div>
          </div>
          <div class="stat-item">
            <div class="stat-label-row">
              <svg width="12" height="12" fill="#f59e0b" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.851 1.416 8.255L12 19.771l-7.416 4.083L6 15.599 0 9.748l8.332-1.73z"/></svg>
              <span class="stat-label">Total Stars</span>
            </div>
            <div class="stat-value" style="color:#f59e0b">128</div>
          </div>
          <div class="stat-item">
            <div class="stat-label-row">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="#10b981"><rect x="3" y="3" width="4" height="18" rx="1"/><rect x="10" y="8" width="4" height="13" rx="1"/><rect x="17" y="5" width="4" height="16" rx="1"/></svg>
              <span class="stat-label">Commits (2024)</span>
            </div>
            <div class="stat-value" style="color:#10b981">1.2k+</div>
          </div>
          <div class="stat-item">
            <div class="stat-label-row">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="#3b82f6"><path d="M6 3a3 3 0 1 1 0 6 3 3 0 0 1 0-6zm12 12a3 3 0 1 1 0 6 3 3 0 0 1 0-6zM6 7a1 1 0 0 0 0 2c1.65 0 3 1.35 3 3v1c0 2.76 2.24 5 5 5h.17A3 3 0 0 0 21 19a3 3 0 0 0-3-3c-.55 0-1.07.16-1.51.44C16.15 14.85 14.72 14 13 14v-2c0-2.76-2.24-5-5-5z"/></svg>
              <span class="stat-label">Pull Requests</span>
            </div>
            <div class="stat-value" style="color:#3b82f6">340</div>
          </div>
        </div>
        <div class="badge-top5">⚡ Top 5% Contributor in AI/ML Repos</div>
      </div>
    </div>

    <!-- Language Distribution -->
    <div class="card">
      <div class="card-header">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="#3b82f6"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
        Language Distribution
      </div>
      <div class="card-body">
        <div class="lang-list">
          <div class="lang-row">
            <div class="lang-label-row"><span>Python</span><span>65%</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:65%;background:#3b82f6"></div></div>
          </div>
          <div class="lang-row">
            <div class="lang-label-row"><span>JavaScript / TS</span><span>15%</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:15%;background:#f59e0b"></div></div>
          </div>
          <div class="lang-row">
            <div class="lang-label-row"><span>Java</span><span>10%</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:10%;background:#ea580c"></div></div>
          </div>
          <div class="lang-row">
            <div class="lang-label-row"><span>C++</span><span>5%</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:5%;background:#ec4899"></div></div>
          </div>
          <div class="lang-row">
            <div class="lang-label-row"><span>Shell / Bash</span><span>3%</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:3%;background:#71717a"></div></div>
          </div>
          <div class="lang-row">
            <div class="lang-label-row"><span>Other</span><span>2%</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:2%;background:#3f3f46"></div></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Featured Project -->
    <div class="featured">
      <div class="featured-bg-icon">
        <svg width="120" height="120" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/><path d="M9 1v3m6-3v3M9 20v3m6-3v3M1 9h3m-3 6h3M20 9h3m-3 6h3"/></svg>
      </div>
      <div>
        <div class="feat-meta">
          <div class="feat-chip">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="2" y="2" width="20" height="20" rx="3"/><path d="M8 12h8M12 8v8" stroke="white" stroke-width="2" fill="none"/></svg>
            Featured Open Source
          </div>
          <span class="feat-badge">ACTIVE</span>
        </div>
        <div class="feat-title">resume_py</div>
        <div class="feat-sub">Agentic Architecture · 5,000+ LOC</div>
        <div class="feat-desc">Intelligent job application agent that scrapes 25+ company pages, targeting Hybrid/Remote roles in the USA and auto-filling portals using LLM reasoning.</div>
        <div class="feat-stats">
          <div class="feat-stat">
            <div class="feat-stat-val">25+</div>
            <div class="feat-stat-lbl">Selenium Portals</div>
          </div>
          <div class="feat-stat">
            <div class="feat-stat-val">76</div>
            <div class="feat-stat-lbl">Jobs Matched</div>
          </div>
        </div>
      </div>
      <div>
        <div class="feat-tags">
          <span class="feat-tag">Selenium</span>
          <span class="feat-tag">Playwright</span>
          <span class="feat-tag">RAG</span>
          <span class="feat-tag">Agentic Workflow</span>
        </div>
        <a href="https://github.com/BNTiyan/resume_py" target="_blank" class="feat-btn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
          View Documentation
        </a>
      </div>
    </div>
  </div>

  <!-- Bottom Row -->
  <div class="grid-bottom">

    <!-- Mastery Matrix -->
    <div class="card">
      <div class="card-body" style="padding:28px">
        <div class="mastery-header">
          <div>
            <div class="mastery-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="#a855f7"><rect x="3" y="3" width="4" height="18" rx="1"/><rect x="10" y="8" width="4" height="13" rx="1"/><rect x="17" y="5" width="4" height="16" rx="1"/></svg>
              Mastery Matrix
            </div>
            <div class="mastery-sub">Architectural & Framework Expertise</div>
          </div>
        </div>
        <div class="mastery-grid">

          <!-- Architecture -->
          <div>
            <div class="skill-section-title" style="color:#a855f7;border-color:#a855f720">Architecture Patterns</div>
            <div class="skill-list">
              <div class="skill-row"><div class="skill-label-row"><span>RAG Systems</span><span>95%</span></div><div class="skill-track"><div class="skill-fill" style="width:95%;background:#a855f7"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>Agentic Workflows</span><span>92%</span></div><div class="skill-track"><div class="skill-fill" style="width:92%;background:#a855f7"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>Microservices (AWS)</span><span>90%</span></div><div class="skill-track"><div class="skill-fill" style="width:90%;background:#a855f7"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>Event-Driven Arch</span><span>88%</span></div><div class="skill-track"><div class="skill-fill" style="width:88%;background:#a855f7"></div></div></div>
            </div>
          </div>

          <!-- Frameworks -->
          <div>
            <div class="skill-section-title" style="color:#3b82f6;border-color:#3b82f620">Top Frameworks</div>
            <div class="skill-list">
              <div class="skill-row"><div class="skill-label-row"><span>FastAPI / Django</span><span>94%</span></div><div class="skill-track"><div class="skill-fill" style="width:94%;background:#3b82f6"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>React / Next.js</span><span>85%</span></div><div class="skill-track"><div class="skill-fill" style="width:85%;background:#3b82f6"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>PyTorch / YOLO</span><span>90%</span></div><div class="skill-track"><div class="skill-fill" style="width:90%;background:#3b82f6"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>Selenium / Playwright</span><span>96%</span></div><div class="skill-track"><div class="skill-fill" style="width:96%;background:#3b82f6"></div></div></div>
            </div>
          </div>

          <!-- Infrastructure -->
          <div>
            <div class="skill-section-title" style="color:#10b981;border-color:#10b98120">Infrastructure</div>
            <div class="skill-list">
              <div class="skill-row"><div class="skill-label-row"><span>AWS Cloud (Expert)</span><span>85%</span></div><div class="skill-track"><div class="skill-fill" style="width:85%;background:#10b981"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>Google Vertex AI</span><span>90%</span></div><div class="skill-track"><div class="skill-fill" style="width:90%;background:#10b981"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>Docker / K8s</span><span>78%</span></div><div class="skill-track"><div class="skill-fill" style="width:78%;background:#10b981"></div></div></div>
              <div class="skill-row"><div class="skill-label-row"><span>GitLab/GitHub CI</span><span>92%</span></div><div class="skill-track"><div class="skill-fill" style="width:92%;background:#10b981"></div></div></div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- Right Column -->
    <div class="right-col">

      <!-- Contribution Activity -->
      <div class="card contrib-card" style="flex:1">
        <div class="card-body" style="height:100%">
          <div class="contrib-inner">
            <div>
              <div class="contrib-label">Contribution Activity</div>
              <div class="contrib-list">
                <div class="contrib-item">
                  <div class="contrib-badge" style="background:#10b98120;color:#10b981">+14</div>
                  <div class="contrib-text">Repositories contributed to in 2024</div>
                </div>
                <div class="contrib-item">
                  <div class="contrib-badge" style="background:#a855f720;color:#a855f7;font-size:14px">🚀</div>
                  <div class="contrib-text">12 Major open-source releases merged</div>
                </div>
                <div class="contrib-item">
                  <div class="contrib-badge" style="background:#3b82f620;color:#3b82f6">99%</div>
                  <div class="contrib-text">Code review response rate (Top Tier)</div>
                </div>
              </div>
            </div>
            <div class="contrib-footer">
              <span class="avail-label">Availability</span>
              <div class="avail-status">
                <div class="ping"><div class="ping-outer"></div><div class="ping-inner"></div></div>
                OPEN FOR COLLAB
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Analytics -->
      <div class="analytics-card">
        <div class="analytics-label">Portfolio Analytics</div>
        <div class="analytics-val">5,000+</div>
        <div class="analytics-sub">Lines of Code Deployed</div>
        <div class="pulse-bars">
          <div class="pulse-bar" style="animation-delay:0ms"></div>
          <div class="pulse-bar" style="animation-delay:100ms"></div>
          <div class="pulse-bar" style="animation-delay:200ms"></div>
          <div class="pulse-bar" style="animation-delay:300ms"></div>
          <div class="pulse-bar" style="animation-delay:400ms"></div>
        </div>
      </div>

    </div>
  </div>

</section>
</body>
</html>
