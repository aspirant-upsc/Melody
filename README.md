
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">
        <!-- Replace assets/logo.png with your actual logo file inside repo/assets/ -->
        <img src="assets/logo.png" alt="MelodyX Logo" onerror="this.style.opacity=0.3; this.src='https://via.placeholder.com/96?text=Mx'"/>
        
      </div>
      <div>
        <h1>MelodyX — Advanced Telegram Music & AI Bot</h1>
        <div class="subtitle">HD VC streaming • Gemini AI voice assistant • Admin dashboard • Music & moderation tools</div>
      </div>

      <div class="badges">
        <!-- Example shields (these links are for visual only) -->
        <img src="https://img.shields.io/badge/python-3.11-blue?logo=python" alt="python" height="20"/>
        <img src="https://img.shields.io/badge/license-MIT-green" alt="license" height="20"/>
        <img src="https://img.shields.io/badge/build-pending-lightgrey" alt="ci" height="20"/>
      </div>
    </header>

    <section class="card owner">
      <div style="display:flex;gap:12px;align-items:center">
        <img src="https://t.me/aspirant_u" alt="Owner" style="width:72px;height:72px;border-radius:12px;object-fit:cover;border:1px solid rgba(255,255,255,0.03)" onerror="this.style.opacity=0.5; this.src='https://via.placeholder.com/72?text=@'"/>
        <div class="meta">
          <strong>Owner:</strong> <a class="link" href="https://t.me/aspirant_u" target="_blank">https://t.me/aspirant_u</a><br/>
          <span style="color:var(--muted)">Maintainer • Telegram community admin</span>
        </div>
      </div>

      <div style="margin-left:auto;text-align:right">
        <a class="btn" href="#quick-start">Quick Start</a>
      </div>
    </section>

    <section class="card">
      <h2>What is MelodyX?</h2>
      <p class="subtitle">MelodyX is a pro-level Telegram music & AI assistant scaffold that includes: voice chat (VC) playback stubs, AI voice assistant hooks (STT & TTS), moderation & file scanning, fancy-name utilities, admin dashboard (FastAPI) and a React admin UI scaffold.</p>

      <div class="grid" style="margin-top:12px">
        <div>
          <h3>Core Features</h3>
          <ul>
            <li>HD audio streaming in Telegram Voice Chats (PyTgCalls stub)</li>
            <li>Gemini/OpenAI-style AI assistant (STT → LLM → TTS) hooks</li>
            <li>Fancy name generator & profile cleaner</li>
            <li>Moderation: bad-words, link scanning, NSFW hooks</li>
            <li>Admin Dashboard (FastAPI) + minimal React scaffold</li>
          </ul>
        </div>
        <div>
          <h3>Use-cases</h3>
          <ul>
            <li>Community music streaming in Telegram groups</li>
            <li>Voice-based AI assistant for Q/A in voice chats</li>
            <li>Moderation & logging for large supergroups</li>
            <li>Learning module for Python (Hindi + English)</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="quick-start" class="card">
      <h2>Quick start</h2>

      <h3>Requirements</h3>
      <ul>
        <li>Python 3.11+</li>
        <li>ffmpeg (for audio processing & streaming)</li>
        <li>Docker (optional, for container deployment)</li>
      </ul>

      <h3>1) Clone repository</h3>
      <pre><code>git clone https://github.com/aspirant-upsc/Melody.git
cd Melody</code></pre>

      <h3>2) Create virtual env & install</h3>
      <pre><code>python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt</code></pre>

      <h3>3) Configure environment</h3>
      <p>Copy the example file and fill values:</p>
      <pre><code>cp .env.example .env
# Open .env and set:
# TELEGRAM_BOT_TOKEN, OWNER_ID, DATABASE_URL, AI_API_KEY, ELEVEN_API_KEY, ADMIN_DASH_TOKEN
</code></pre>

      <h3>4) Run bot (development)</h3>
      <pre><code>python bot.py</code></pre>

      <h3>5) Run admin dashboard (dev)</h3>
      <pre><code>cd dashboard
uvicorn main:app --reload --host 0.0.0.0 --port 8000</code></pre>

      <h3>6) Docker (optional)</h3>
      <pre><code>docker-compose up --build -d</code></pre>
    </section>

    <section class="card">
      <h2>Environment variables</h2>
      <pre><code># .env.example (summary)
TELEGRAM_BOT_TOKEN=your_token_here
OWNER_ID=123456789
OWNER_NAME=https://t.me/aspirant_u
FANCY_DEFAULT_PREFIX=★
FANCY_DEFAULT_SUFFIX=★
DATABASE_URL=sqlite:///./melodyx_complete.db
AI_API_KEY=your_ai_key
STT_PROVIDER=whisper
TTS_PROVIDER=eleven
ADMIN_DASH_TOKEN=your_admin_token
SUPPORT_GROUP_ID=-100xxxxxxxxx
UPDATES_CHANNEL=@your_channel
LOG_GROUP_ID=-100xxxxxxxxx
</code></pre>
      <p class="subtitle">⚠️ <strong>Never</strong> commit your real `.env` to GitHub. Use `.env.example` with placeholder values only.</p>
    </section>

    <section class="card">
      <h2>Folder structure</h2>
      <pre><code>Melody/
├── bot.py
├── config.py
├── .env.example
├── README.html
├── Dockerfile
├── music/
│   ├── vc_player.py
│   └── queue_db.py
├── handlers/
│   ├── start.py
│   ├── play.py
│   └── moderation.py
├── system/
│   ├── ai_manager.py
│   ├── content_filter.py
│   └── file_scanner.py
├── dashboard/
│   └── main.py
└── assets/
    ├── logo.png
    └── start.jpg</code></pre>
    </section>

    <section class="card">
      <h2>Screenshots / Preview</h2>
      <p class="subtitle">(Place images inside <code>assets/</code> and reference them here)</p>
      <img class="preview" src="assets/start.jpg" alt="Start card preview" onerror="this.src='https://via.placeholder.com/900x300?text=Start+Preview'"/>
    </section>

    <section class="card">
      <h2>Contributing</h2>
      <ul>
        <li>Fork the repo → create a feature branch → open a Pull Request</li>
        <li>Keep secrets out of commits (use `.env` and CI secrets)</li>
        <li>Add tests for new features (we use pytest)</li>
      </ul>

      <h2>Security & Responsible Use</h2>
      <ul>
        <li>Only request user data with explicit consent (contacts, location)</li>
        <li>Do not implement or distribute harmful software (phishing, spyware)</li>
        <li>Rotate tokens & API keys regularly</li>
      </ul>
    </section>

    <section class="card">
      <h2>License</h2>
      <p>MIT License — see <code>LICENSE</code> file.</p>
      <p>If you use third-party APIs (ElevenLabs, OpenAI, Google) follow their usage rules and credit as required.</p>
    </section>

    <footer>
      <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap">
        <div>Made with ❤️ by <a class="link" href="https://t.me/aspirant_u" target="_blank">@aspirant_u</a></div>
        <div style="color:var(--muted)">Questions? Open an issue in this repo or contact the owner.</div>
      </div>
    </footer>
  </div>
</body>
</html>
