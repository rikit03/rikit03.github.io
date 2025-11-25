<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Rikit Thapa — Portfolio</title>
  <meta name="description" content="Rikit Thapa — Computer Systems Technician. Networking, Azure, Cloud Security, IT Support. Portfolio, projects and resume." />

  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg: linear-gradient(180deg, #f7fbff 0%, #f1f7ff 100%);
      --card: #ffffff;
      --muted: #6b7280;
      --accent1: #7c3aed;
      --accent2: #06b6d4;
      --accent3: #f97316;
      --text: #071024;
      --radius: 14px;
      --shadow: 0 8px 30px rgba(10, 15, 30, 0.08);
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      font-family: Inter, sans-serif;
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 60px;
    }

    .wrap {
      max-width: 1100px;
      margin: 36px auto;
      padding: 0 20px;
    }

    /* Hero */
    header.hero {
      border-radius: 18px;
      padding: 36px;
      display: flex;
      align-items: center;
      gap: 20px;
      background: linear-gradient(135deg,
        rgba(124, 58, 237, 0.12),
        rgba(6, 182, 212, 0.08) 45%,
        rgba(249, 115, 22, 0.06) 100%
      );
      position: relative;
      box-shadow: var(--shadow);
      overflow: hidden;
    }

    .shape {
      position: absolute;
      filter: blur(40px);
      opacity: .12;
      border-radius: 50%;
    }
    .s1 { width: 300px; height: 300px; right: -60px; top: -60px; background: var(--accent1); }
    .s2 { width: 220px; height: 220px; left: -40px; bottom: -40px; background: var(--accent3); opacity: .08; }

    .avatar {
      width: 120px;
      height: 120px;
      border-radius: 18px;
      background: linear-gradient(135deg, var(--accent1), var(--accent2));
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 42px;
      font-weight: 700;
      flex-shrink: 0;
    }

    .hero h1 { margin: 0; font-size: 28px; }
    .lead { color: var(--muted); margin-top: 6px; }

    .actions {
      margin-top: 12px;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    .btn {
      padding: 10px 14px;
      border-radius: 10px;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
    }
    .btn.primary { background: linear-gradient(90deg, var(--accent1), var(--accent2)); color: #fff; }
    .btn.secondary { background: #fff; border: 1px solid rgba(0,0,0,0.08); color: var(--text); }

    /* Grid */
    .grid {
      display: grid;
      gap: 22px;
      margin-top: 28px;
      grid-template-columns: 2fr 1fr;
    }
    @media (max-width: 900px) {
      .grid { grid-template-columns: 1fr; }
    }

    .card {
      background: var(--card);
      padding: 18px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      transition: .25s;
    }
    .card:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 50px rgba(10,15,30,0.12);
    }

    h2 { margin: 0 0 10px; font-size: 18px; }

    /* Projects */
    ul.projects { padding: 0; list-style: none; }
    .proj {
      display: flex;
      gap: 12px;
      padding: 12px;
      margin-bottom: 10px;
      border-radius: 12px;
      border: 1px solid rgba(0,0,0,0.05);
      background: rgba(0,0,0,0.02);
    }

    .tag {
      background: linear-gradient(90deg, var(--accent2), var(--accent1));
      padding: 6px 10px;
      border-radius: 999px;
      color: white;
      font-size: 12px;
      font-weight: 700;
      white-space: nowrap;
    }

    .proj a.title {
      font-weight: 700;
      color: var(--text);
      text-decoration: none;
    }

    /* Skills */
    .skills { display: flex; flex-wrap: wrap; gap: 8px; }
    .skill-pill {
      background: linear-gradient(90deg, #eef2ff, #fff8ed);
      padding: 8px 12px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
    }

    /* Resume preview */
    .resume-preview {
      width: 100%;
      height: 160px;
      border-radius: 10px;
      object-fit: cover;
      border: 1px solid rgba(0,0,0,0.05);
    }

    footer {
      text-align: center;
      margin-top: 36px;
      font-size: 13px;
      color: var(--muted);
    }

  </style>
</head>

<body>
  <div class="wrap">

    <!-- HERO -->
    <header class="hero">
      <div class="shape s1"></div>
      <div class="shape s2"></div>

      <div class="avatar">RT</div>

      <div style="flex: 1;">
        <h1>Hi, I'm <strong>Rikit Thapa</strong> 👋</h1>
        <p class="lead">Computer Systems Technician • Networking • Azure Security • IT Support</p>

        <div class="actions">
          <a class="btn primary" href="https://github.com/rikit03" target="_blank">GitHub</a>
          <a class="btn secondary" href="https://www.linkedin.com/in/rikit-thapa-294ab028a/" target="_blank">LinkedIn</a>
          <a class="btn secondary" href="resume.png" download>Resume</a>
        </div>
      </div>
    </header>

    <!-- MAIN -->
    <main class="grid">

      <!-- LEFT COLUMN -->
      <section>

        <!-- About -->
        <article class="card">
          <h2>About Me</h2>
          <p class="muted">
            I'm a Computer Systems Technician specializing in networking, cloud security, and IT operations.
            I design secure Azure environments, build reliable networks, automate tasks with PowerShell/Python,
            and troubleshoot complex hardware/software issues.
          </p>
        </article>

        <!-- Projects -->
        <article class="card" style="margin-top: 16px;">
          <h2>Highlighted Projects</h2>

          <ul class="projects">

            <li class="proj">
              <div class="tag">Cloud</div>
              <div class="meta">
                <a class="title" href="https://github.com/rikit03" target="_blank">Azure Security Lab (AZ-500)</a>
                <p class="muted">
                  Hardened Azure environment using RBAC, NSGs, Azure Firewall, log analytics,
                  resource segmentation, and security policy automation.
                </p>
              </div>
            </li>

            <li class="proj">
              <div class="tag">DB</div>
              <div class="meta">
                <a class="title" href="https://github.com/rikit03" target="_blank">SQL Security & Backup Strategy</a>
                <p class="muted">
                  Role-based access, automated backup/restore workflows, retention management,
                  and database recovery planning.
                </p>
              </div>
            </li>

            <li class="proj">
              <div class="tag">Code</div>
              <div class="meta">
                <a class="title" href="https://github.com/rikit03" target="_blank">Python + SQL Integration Tool</a>
                <p class="muted">
                  Automates SQL queries, generates reports, and triggers stored procedures to simplify DBA tasks.
                </p>
              </div>
            </li>

            <li class="proj">
              <div class="tag">Network</div>
              <div class="meta">
                <a class="title" href="https://github.com/rikit03" target="_blank">Network Design Simulation</a>
                <p class="muted">
                  Multi-site GNS3/Packet Tracer network using VLANs, OSPF, DHCP, ACLs, and NAT,
                  with full documentation.
                </p>
              </div>
            </li>

          </ul>
        </article>

        <!-- Experience -->
        <article class="card" style="margin-top: 16px;">
          <h2>Experience</h2>
          <ul class="muted">
            <li><strong>Technical Sales Advisor</strong> — Best Buy, Belleville, ON (2023–2025)</li>
            <li><strong>Customer Support Representative</strong> — Techlink Solutions, Kathmandu (2022–2023)</li>
            <li><strong>Lab Assistant</strong> — Southwestern State College (2022)</li>
          </ul>
        </article>

      </section>

      <!-- RIGHT SIDEBAR -->
      <aside>

        <!-- Skills -->
        <div class="card">
          <h2>Skills & Tools</h2>
          <div class="skills">
            <div class="skill-pill">Routing & Switching</div>
            <div class="skill-pill">VLANs</div>
            <div class="skill-pill">OSPF</div>
            <div class="skill-pill">Azure RBAC</div>
            <div class="skill-pill">Azure Firewall</div>
            <div class="skill-pill">Windows Server</div>
            <div class="skill-pill">Linux</div>
            <div class="skill-pill">PowerShell</div>
            <div class="skill-pill">Python</div>
            <div class="skill-pill">SQL Server</div>
          </div>
        </div>

        <!-- Resume -->
        <div class="card" style="margin-top: 16px;">
          <h2>Resume</h2>
          <a href="resume.png" target="_blank">
            <img class="resume-preview" src="resume.png" alt="Resume preview">
          </a>
        </div>

        <!-- Contact -->
        <div class="card" style="margin-top: 16px;">
          <h2>Contact</h2>
          <div class="contact-line">
            <a class="btn secondary" href="mailto:youremail@example.com">Email Me</a>
            <a class="btn secondary" href="https://www.linkedin.com/in/rikit-thapa-294ab028a/" target="_blank">LinkedIn</a>
          </div>
          <p class="muted" style="margin-top: 12px;">
            GitHub: <a href="https://github.com/rikit03" target="_blank">github.com/rikit03</a>
          </p>
        </div>

      </aside>

    </main>

    <footer>
      © 2025 Rikit Thapa • Portfolio for recruiters & hiring managers
    </footer>

  </div>
</body>
</html>
