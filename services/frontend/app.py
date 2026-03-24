from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>FutureCars 2055</title>
      <style>
        :root {
          --bg: #040714;
          --bg2: #091127;
          --bg3: #0f1836;
          --card: rgba(10, 18, 40, 0.78);
          --card-2: rgba(14, 24, 52, 0.82);
          --line: rgba(78, 255, 236, 0.18);
          --text: #edf8ff;
          --muted: #9eb8d2;
          --cyan: #4effec;
          --violet: #8b5cf6;
          --pink: #ff4fd8;
          --lime: #b6ff5c;
          --gold: #ffca63;
          --shadow: 0 0 30px rgba(78, 255, 236, 0.12);
          --shadow-strong: 0 0 40px rgba(139, 92, 246, 0.15);
          --radius: 24px;
        }

        * {
          box-sizing: border-box;
          margin: 0;
          padding: 0;
        }

        html {
          scroll-behavior: smooth;
        }

        body {
          font-family: Arial, Helvetica, sans-serif;
          background:
            radial-gradient(circle at top left, rgba(139, 92, 246, 0.18), transparent 25%),
            radial-gradient(circle at top right, rgba(78, 255, 236, 0.14), transparent 20%),
            radial-gradient(circle at bottom center, rgba(255, 79, 216, 0.12), transparent 20%),
            linear-gradient(180deg, var(--bg), var(--bg2) 55%, var(--bg3));
          color: var(--text);
          min-height: 100vh;
          line-height: 1.6;
        }

        img {
          max-width: 100%;
          display: block;
        }

        .container {
          width: min(1240px, 92%);
          margin: 0 auto;
        }

        .nav {
          position: sticky;
          top: 0;
          z-index: 50;
          backdrop-filter: blur(14px);
          background: rgba(4, 7, 20, 0.72);
          border-bottom: 1px solid rgba(78, 255, 236, 0.1);
        }

        .nav-inner {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 16px 0;
          gap: 16px;
        }

        .brand {
          display: flex;
          align-items: center;
          gap: 12px;
          text-decoration: none;
          color: var(--text);
        }

        .brand img {
          width: 190px;
          max-width: 100%;
          filter: drop-shadow(0 0 12px rgba(78, 255, 236, 0.22));
        }

        .brand-fallback {
          display: none;
          font-size: 1.35rem;
          font-weight: 800;
          letter-spacing: 0.5px;
        }

        .brand-fallback span {
          color: var(--cyan);
          text-shadow: 0 0 16px rgba(78, 255, 236, 0.5);
        }

        .nav-links {
          display: flex;
          gap: 18px;
          flex-wrap: wrap;
        }

        .nav-links a {
          color: var(--muted);
          text-decoration: none;
          font-size: 0.95rem;
          transition: 0.2s ease;
        }

        .nav-links a:hover {
          color: var(--cyan);
        }

        .hero {
          padding: 88px 0 40px;
        }

        .hero-wrap {
          display: grid;
          grid-template-columns: 1.08fr 0.92fr;
          gap: 28px;
          align-items: center;
        }

        .eyebrow {
          display: inline-block;
          margin-bottom: 14px;
          padding: 8px 14px;
          border: 1px solid var(--line);
          border-radius: 999px;
          color: var(--cyan);
          background: rgba(78, 255, 236, 0.06);
          font-size: 0.84rem;
        }

        h1 {
          font-size: clamp(2.7rem, 6vw, 5.2rem);
          line-height: 1.02;
          margin-bottom: 18px;
          letter-spacing: -1px;
        }

        h1 .glow {
          color: var(--cyan);
          text-shadow:
            0 0 12px rgba(78, 255, 236, 0.42),
            0 0 24px rgba(78, 255, 236, 0.2);
        }

        .hero p {
          color: var(--muted);
          font-size: 1.06rem;
          max-width: 640px;
          margin-bottom: 26px;
        }

        .cta-row {
          display: flex;
          gap: 14px;
          flex-wrap: wrap;
          margin-bottom: 22px;
        }

        .hero-meta {
          display: flex;
          gap: 12px;
          flex-wrap: wrap;
        }

        .meta-pill {
          padding: 8px 12px;
          border-radius: 999px;
          border: 1px solid rgba(255,255,255,0.08);
          background: rgba(255,255,255,0.03);
          color: var(--muted);
          font-size: 0.88rem;
        }

        .btn {
          display: inline-block;
          padding: 13px 20px;
          border-radius: 14px;
          text-decoration: none;
          font-weight: 700;
          transition: 0.25s ease;
          cursor: pointer;
        }

        .btn-primary {
          background: linear-gradient(90deg, var(--cyan), var(--violet));
          color: #04111a;
          box-shadow: var(--shadow);
        }

        .btn-primary:hover {
          transform: translateY(-2px);
          opacity: 0.96;
        }

        .btn-secondary {
          border: 1px solid var(--line);
          color: var(--text);
          background: rgba(255, 255, 255, 0.03);
        }

        .btn-secondary:hover {
          border-color: var(--cyan);
          color: var(--cyan);
          transform: translateY(-2px);
        }

        .hero-panel {
          border: 1px solid var(--line);
          background: linear-gradient(180deg, rgba(12, 19, 40, 0.82), rgba(8, 13, 28, 0.94));
          border-radius: var(--radius);
          padding: 18px;
          box-shadow: var(--shadow);
          overflow: hidden;
        }

        .hero-car {
          position: relative;
          overflow: hidden;
          border-radius: 18px;
          border: 1px solid rgba(78, 255, 236, 0.12);
          background: linear-gradient(145deg, #0b1631, #091122 55%, #050b18);
        }

        .hero-car img {
          width: 100%;
          aspect-ratio: 16 / 10;
          object-fit: cover;
          opacity: 0.96;
        }

        .hero-car-badge {
          position: absolute;
          left: 16px;
          top: 16px;
          background: rgba(4, 10, 25, 0.72);
          border: 1px solid rgba(78,255,236,0.18);
          color: var(--cyan);
          padding: 8px 12px;
          border-radius: 999px;
          font-size: 0.8rem;
          backdrop-filter: blur(10px);
        }

        .hero-car-name {
          position: absolute;
          left: 16px;
          bottom: 14px;
          color: white;
          font-size: 0.96rem;
          letter-spacing: 1.5px;
          background: rgba(4, 10, 25, 0.6);
          padding: 8px 12px;
          border-radius: 12px;
          border: 1px solid rgba(255,255,255,0.06);
        }

        section {
          padding: 34px 0 24px;
        }

        .section-header {
          display: flex;
          justify-content: space-between;
          align-items: end;
          gap: 16px;
          margin-bottom: 24px;
          flex-wrap: wrap;
        }

        .section-title {
          font-size: 2rem;
          margin-bottom: 8px;
        }

        .section-sub {
          color: var(--muted);
          max-width: 760px;
        }

        .currency-note {
          color: var(--gold);
          font-size: 0.95rem;
          background: rgba(255, 202, 99, 0.06);
          border: 1px solid rgba(255, 202, 99, 0.16);
          padding: 10px 14px;
          border-radius: 14px;
        }

        .cars-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 20px;
        }

        .car-card {
          background: linear-gradient(180deg, var(--card), var(--card-2));
          border: 1px solid var(--line);
          border-radius: 22px;
          overflow: hidden;
          box-shadow: var(--shadow);
          transition: 0.25s ease;
          position: relative;
        }

        .car-card:hover {
          transform: translateY(-6px);
          border-color: rgba(78, 255, 236, 0.36);
          box-shadow: var(--shadow-strong);
        }

        .car-card::before {
          content: "";
          position: absolute;
          inset: 0;
          background: linear-gradient(180deg, rgba(78,255,236,0.03), transparent 45%);
          pointer-events: none;
        }

        .car-visual {
          position: relative;
          height: 230px;
          overflow: hidden;
          background: linear-gradient(135deg, #0b1736, #091324 60%, #060b17);
        }

        .car-visual img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transition: transform 0.35s ease, filter 0.35s ease;
        }

        .car-card:hover .car-visual img {
          transform: scale(1.05);
          filter: saturate(1.08);
        }

        .car-price {
          position: absolute;
          top: 14px;
          right: 14px;
          padding: 8px 12px;
          border-radius: 999px;
          background: rgba(4, 10, 25, 0.76);
          border: 1px solid rgba(78,255,236,0.18);
          color: var(--gold);
          font-weight: 700;
          font-size: 0.88rem;
          backdrop-filter: blur(8px);
        }

        .car-body {
          padding: 18px;
        }

        .tag {
          display: inline-block;
          padding: 6px 10px;
          border-radius: 999px;
          font-size: 0.78rem;
          margin-bottom: 12px;
          color: var(--cyan);
          border: 1px solid rgba(78, 255, 236, 0.2);
          background: rgba(78, 255, 236, 0.06);
        }

        .car-title {
          font-size: 1.18rem;
          margin-bottom: 8px;
        }

        .car-body p {
          color: var(--muted);
          font-size: 0.95rem;
          margin-bottom: 12px;
        }

        .car-body ul {
          padding-left: 18px;
          color: var(--text);
          margin-bottom: 14px;
        }

        .car-body li {
          margin-bottom: 6px;
          color: var(--muted);
        }

        .delivery {
          color: var(--lime);
          font-weight: 700;
          margin-bottom: 14px;
        }

        .story-grid,
        .about-grid,
        .contact-grid {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 20px;
        }

        .info-card {
          background: linear-gradient(180deg, var(--card), var(--card-2));
          border: 1px solid var(--line);
          border-radius: 22px;
          padding: 22px;
          box-shadow: var(--shadow);
        }

        .info-card h3 {
          margin-bottom: 10px;
          color: var(--cyan);
        }

        .info-card p {
          color: var(--muted);
        }

        .reserve-panel {
          display: grid;
          grid-template-columns: 1.2fr 0.8fr;
          gap: 20px;
        }

        .reserve-box {
          background: linear-gradient(180deg, rgba(14, 22, 48, 0.9), rgba(8, 14, 30, 0.94));
          border: 1px solid var(--line);
          border-radius: 22px;
          padding: 24px;
          box-shadow: var(--shadow);
        }

        .reserve-box h3 {
          color: var(--cyan);
          margin-bottom: 10px;
        }

        .reserve-box p,
        .reserve-box li {
          color: var(--muted);
        }

        .reserve-box ul {
          padding-left: 18px;
          margin: 12px 0 16px;
        }

        .reserve-highlight {
          color: var(--gold);
          font-weight: 700;
        }

        .timeline {
          display: grid;
          gap: 12px;
          margin-top: 12px;
        }

        .timeline-step {
          padding: 12px 14px;
          border-radius: 16px;
          background: rgba(255,255,255,0.03);
          border: 1px solid rgba(255,255,255,0.05);
          color: var(--muted);
        }

        .footer {
          padding: 38px 0 54px;
          text-align: center;
          color: var(--muted);
          font-size: 0.94rem;
        }

        .footer strong {
          color: var(--cyan);
        }

        @media (max-width: 1100px) {
          .cars-grid {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        @media (max-width: 980px) {
          .hero-wrap,
          .about-grid,
          .story-grid,
          .contact-grid,
          .reserve-panel {
            grid-template-columns: 1fr;
          }
        }

        @media (max-width: 640px) {
          h1 {
            font-size: 2.35rem;
          }

          .nav-inner {
            gap: 12px;
            align-items: flex-start;
            flex-direction: column;
          }

          .cars-grid {
            grid-template-columns: 1fr;
          }

          .brand img {
            width: 160px;
          }
        }
      </style>
    </head>
    <body>
      <nav class="nav">
        <div class="container nav-inner">
          <a class="brand" href="#top">
            <img src="/static/cars/futurecars-logo-2055.png" alt="FutureCars 2055 Logo" onerror="this.style.display='none'; document.querySelector('.brand-fallback').style.display='block';">
            <div class="brand-fallback">Future<span>Cars</span> 2055</div>
          </a>

          <div class="nav-links">
            <a href="#cars">Cars</a>
            <a href="#story">Story</a>
            <a href="#about">About</a>
            <a href="#reserve">Reserve</a>
            <a href="#contact">Contact</a>
          </div>
        </div>
      </nav>

      <header class="hero" id="top">
        <div class="container hero-wrap">
          <div>
            <div class="eyebrow">Luxury vehicles from tomorrow</div>
            <h1>
              Reserve the <span class="glow">Alien Machines</span><br />
              of 2055.
            </h1>
            <p>
              FutureCars is a digital showroom for ultra-rare concept vehicles engineered
              for the year 2055 — hover systems, chrono-AI navigation, plasma nitro,
              cinematic alien design, and luxury beyond Earth.
            </p>

            <div class="cta-row">
              <a class="btn btn-primary" href="#cars">Explore Vehicles</a>
              <a class="btn btn-secondary" href="#reserve">Reserve for 2055</a>
            </div>

            <div class="hero-meta">
              <div class="meta-pill">7 mutated luxury machines</div>
              <div class="meta-pill">Delivery wave: 2055</div>
              <div class="meta-pill">Currency: Cosmic Credits ⟠C</div>
            </div>
          </div>

          <div class="hero-panel">
            <div class="hero-car">
              <img src="/static/cars/tesla-xr-infinity.jpg" alt="Tesla Xr-Infinity">
              <div class="hero-car-badge">Flagship Hypercar</div>
              <div class="hero-car-name">TESLA XR-INFINITY</div>
            </div>
          </div>
        </div>
      </header>

      <section id="cars">
        <div class="container">
          <div class="section-header">
            <div>
              <h2 class="section-title">FutureCars Collection</h2>
              <p class="section-sub">
                Seven rare machines inspired by today’s icons, reborn for a sci-fi civilization.
              </p>
            </div>
            <div class="currency-note">
              All prices are listed in <strong>Cosmic Credits (⟠C)</strong>, the luxury reserve currency of 2055.
            </div>
          </div>

          <div class="cars-grid">
            <article class="car-card">
              <div class="car-visual">
                <img src="/static/cars/tesla-xr-infinity.jpg" alt="Tesla Xr-Infinity">
                <div class="car-price">⟠C 2.2M</div>
              </div>
              <div class="car-body">
                <div class="tag">Hover Hypercar</div>
                <h3 class="car-title">Tesla Xr-Infinity</h3>
                <p>Mutation of the Tesla Model X, redesigned for anti-gravity urban flight and plasma speed bursts.</p>
                <ul>
                  <li>Anti-gravity hover mode</li>
                  <li>Quantum autopilot</li>
                  <li>Plasma-nitro burst</li>
                </ul>
                <div class="delivery">Delivery: January 2055</div>
                <a class="btn btn-secondary" href="#reserve">Reserve Now</a>
              </div>
            </article>

            <article class="car-card">
              <div class="car-visual">
                <img src="/static/cars/bmw-nebula-ix.jpg" alt="BMW Nebula IX">
                <div class="car-price">⟠C 2.9M</div>
              </div>
              <div class="car-body">
                <div class="tag">Cosmic Coupe</div>
                <h3 class="car-title">BMW Nebula IX</h3>
                <p>An evolved BMW i8 with stellar energy cells, neural handling, and a stealth midnight aura.</p>
                <ul>
                  <li>Star-drive propulsion</li>
                  <li>Holographic cockpit</li>
                  <li>Night stealth mode</li>
                </ul>
                <div class="delivery">Delivery: March 2055</div>
                <a class="btn btn-secondary" href="#reserve">Reserve Now</a>
              </div>
            </article>

            <article class="car-card">
              <div class="car-visual">
                <img src="/static/cars/mercedes-vision-aeon.jpg" alt="Mercedes Vision Aeon">
                <div class="car-price">⟠C 3.6M</div>
              </div>
              <div class="car-body">
                <div class="tag">Neural Luxury Sedan</div>
                <h3 class="car-title">Mercedes Vision Æon</h3>
                <p>A future descendant of the EQS with a neural-link drive core and liquid metal elegance.</p>
                <ul>
                  <li>Floating suspension</li>
                  <li>Transparent alloy body</li>
                  <li>Autonomous flight mode</li>
                </ul>
                <div class="delivery">Delivery: May 2055</div>
                <a class="btn btn-secondary" href="#reserve">Reserve Now</a>
              </div>
            </article>

            <article class="car-card">
              <div class="car-visual">
                <img src="/static/cars/porsche-eclipse-9110.jpg" alt="Porsche Eclipse 9110">
                <div class="car-price">⟠C 4.1M</div>
              </div>
              <div class="car-body">
                <div class="tag">Warp Performance</div>
                <h3 class="car-title">Porsche Eclipse 9110</h3>
                <p>The classic 911 reborn as a warp-speed machine with sonic launch and an alien shell.</p>
                <ul>
                  <li>Warp-boost nitro engine</li>
                  <li>Quantum chassis</li>
                  <li>Self-regenerating tires</li>
                </ul>
                <div class="delivery">Delivery: August 2055</div>
                <a class="btn btn-secondary" href="#reserve">Reserve Now</a>
              </div>
            </article>

            <article class="car-card">
              <div class="car-visual">
                <img src="/static/cars/lucid-astral-gt.jpg" alt="Lucid Astral GT">
                <div class="car-price">⟠C 3.3M</div>
              </div>
              <div class="car-body">
                <div class="tag">Solar Grand Tourer</div>
                <h3 class="car-title">Lucid Astral GT</h3>
                <p>Inspired by Lucid Air, upgraded with solar plasma flow, cosmic lighting, and adaptive luxury.</p>
                <ul>
                  <li>Solar plasma engine</li>
                  <li>AI predictive routing</li>
                  <li>Bio-adaptive seating</li>
                </ul>
                <div class="delivery">Delivery: October 2055</div>
                <a class="btn btn-secondary" href="#reserve">Reserve Now</a>
              </div>
            </article>

            <article class="car-card">
              <div class="car-visual">
                <img src="/static/cars/cadillac-quantum-limo.jpg" alt="Cadillac Quantum Limo">
                <div class="car-price">⟠C 6.0M</div>
              </div>
              <div class="car-body">
                <div class="tag">Ultra-Luxury Limo</div>
                <h3 class="car-title">Cadillac Quantum Limo</h3>
                <p>A futuristic limousine for elites, diplomats, and off-world executives.</p>
                <ul>
                  <li>10-seat lounge cabin</li>
                  <li>Holographic wall displays</li>
                  <li>Gravity-stabilized comfort</li>
                </ul>
                <div class="delivery">Delivery: December 2055</div>
                <a class="btn btn-secondary" href="#reserve">Reserve Now</a>
              </div>
            </article>

            <article class="car-card">
              <div class="car-visual">
                <img src="/static/cars/delorean-thunderflight.jpg" alt="DeLorean Thunderflight">
                <div class="car-price">⟠C 5.4M</div>
              </div>
              <div class="car-body">
                <div class="tag">Flight Limited Edition</div>
                <h3 class="car-title">DeLorean Thunderflight</h3>
                <p>A tribute to cinematic time machines, rebuilt for real airborne travel with lightning propulsion.</p>
                <ul>
                  <li>Vertical takeoff wings</li>
                  <li>Flux-drive acceleration</li>
                  <li>Chrono-navigation AI</li>
                </ul>
                <div class="delivery">Special Limited Edition 2055</div>
                <a class="btn btn-secondary" href="#reserve">Reserve Now</a>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section id="story">
        <div class="container">
          <div class="section-header">
            <div>
              <h2 class="section-title">The Founder Story</h2>
              <p class="section-sub">
                Behind FutureCars is a vision to make tomorrow’s mobility reservable today.
              </p>
            </div>
          </div>

          <div class="story-grid">
            <div class="info-card">
              <h3>Anslem Ebsiy</h3>
              <p>
                FutureCars was founded by <strong>Anslem Ebsiy</strong>, a visionary technologist,
                cloud infrastructure architect, and future mobility investor.
              </p>
              <p style="margin-top: 10px;">
                After building high-value digital infrastructure and accumulating a fortune of
                <strong>5,900,000,000 Cosmic Credits</strong>, he launched FutureCars as a luxury concept
                marketplace for the machines of 2055.
              </p>
            </div>

            <div class="info-card">
              <h3>The Mission</h3>
              <p>
                FutureCars exists to preview the next era of transportation — where AI, alien-inspired design,
                aerospace engineering, and extreme luxury merge into a single machine.
              </p>
              <p style="margin-top: 10px;">
                Every reservation secures a place in the official 2055 production wave.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section id="about">
        <div class="container">
          <div class="section-header">
            <div>
              <h2 class="section-title">About FutureCars</h2>
              <p class="section-sub">
                A future-focused concept showroom powered by a cloud-native GitOps platform.
              </p>
            </div>
          </div>

          <div class="about-grid">
            <div class="info-card">
              <h3>Why 2055?</h3>
              <p>
                We imagine a world where mobility blends with aerospace, AI, alien aesthetics,
                and ultra-premium engineering. Customers reserve today and receive a certified
                future-delivery allocation for the year 2055.
              </p>
            </div>

            <div class="info-card">
              <h3>Built on Modern Infrastructure</h3>
              <p>
                This platform is deployed using GitHub Actions, Amazon ECR, ArgoCD,
                Kubernetes on EKS, ALB ingress, Route53, ACM, Terraform, health probes,
                autoscaling, and production-ready GitOps workflows.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section id="reserve">
        <div class="container">
          <div class="section-header">
            <div>
              <h2 class="section-title">Reserve a Vehicle</h2>
              <p class="section-sub">
                Place your reservation today and secure your position in the 2055 delivery wave.
              </p>
            </div>
          </div>

          <div class="reserve-panel">
            <div class="reserve-box">
              <h3>Reservation Protocol</h3>
              <p>
                Customers submit a future reservation request, select a vehicle,
                and receive a digital <span class="reserve-highlight">Future Delivery Certificate</span>
                confirming their 2055 allocation slot.
              </p>

              <ul>
                <li>Select your FutureCars model</li>
                <li>Choose your preferred delivery wave</li>
                <li>Receive a Priority Quantum Allocation Certificate</li>
                <li>Await production activation in 2055</li>
              </ul>

              <a class="btn btn-primary" href="#contact">Start Reservation</a>
            </div>

            <div class="reserve-box">
              <h3>Delivery Timeline</h3>
              <div class="timeline">
                <div class="timeline-step">2026 — Reservation window opens</div>
                <div class="timeline-step">2035 — Prototype validation wave</div>
                <div class="timeline-step">2045 — Quantum assembly launch</div>
                <div class="timeline-step">2055 — Official delivery begins</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="contact">
        <div class="container">
          <div class="section-header">
            <div>
              <h2 class="section-title">Contact</h2>
              <p class="section-sub">Talk to our future mobility concierge team.</p>
            </div>
          </div>

          <div class="contact-grid">
            <div class="info-card">
              <h3>Email</h3>
              <p>reserve@futurecars.anzyworld.com</p>
            </div>

            <div class="info-card">
              <h3>Headquarters</h3>
              <p>Neo Mobility District, Orbit City, Earth Sector 2055</p>
            </div>
          </div>
        </div>
      </section>

      <footer class="footer">
        <div class="container">
          <strong>FutureCars 2055</strong> — Purchase today. Drive in 2055.
        </div>
      </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)