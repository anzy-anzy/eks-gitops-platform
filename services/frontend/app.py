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
          --bg: #050816;
          --bg2: #0b1026;
          --card: rgba(14, 22, 48, 0.72);
          --line: rgba(78, 255, 236, 0.22);
          --text: #ecf7ff;
          --muted: #a7bdd7;
          --cyan: #4effec;
          --violet: #8b5cf6;
          --pink: #ff4fd8;
          --lime: #b6ff5c;
          --shadow: 0 0 30px rgba(78, 255, 236, 0.14);
        }

        * {
          box-sizing: border-box;
          margin: 0;
          padding: 0;
        }

        body {
          font-family: Arial, Helvetica, sans-serif;
          background:
            radial-gradient(circle at top left, rgba(139, 92, 246, 0.22), transparent 28%),
            radial-gradient(circle at top right, rgba(78, 255, 236, 0.16), transparent 25%),
            radial-gradient(circle at bottom center, rgba(255, 79, 216, 0.14), transparent 22%),
            linear-gradient(180deg, var(--bg), var(--bg2));
          color: var(--text);
          min-height: 100vh;
          line-height: 1.6;
        }

        .container {
          width: min(1180px, 92%);
          margin: 0 auto;
        }

        .nav {
          position: sticky;
          top: 0;
          z-index: 10;
          backdrop-filter: blur(14px);
          background: rgba(5, 8, 22, 0.68);
          border-bottom: 1px solid rgba(78, 255, 236, 0.12);
        }

        .nav-inner {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 18px 0;
        }

        .brand {
          font-size: 1.4rem;
          font-weight: 800;
          letter-spacing: 0.5px;
          color: var(--text);
        }

        .brand span {
          color: var(--cyan);
          text-shadow: 0 0 16px rgba(78, 255, 236, 0.6);
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
        }

        .nav-links a:hover {
          color: var(--cyan);
        }

        .hero {
          padding: 88px 0 48px;
        }

        .hero-wrap {
          display: grid;
          grid-template-columns: 1.2fr 0.8fr;
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
          font-size: clamp(2.6rem, 6vw, 5rem);
          line-height: 1.02;
          margin-bottom: 18px;
        }

        h1 .glow {
          color: var(--cyan);
          text-shadow:
            0 0 10px rgba(78, 255, 236, 0.45),
            0 0 22px rgba(78, 255, 236, 0.22);
        }

        .hero p {
          color: var(--muted);
          font-size: 1.08rem;
          max-width: 640px;
          margin-bottom: 26px;
        }

        .cta-row {
          display: flex;
          gap: 14px;
          flex-wrap: wrap;
        }

        .btn {
          display: inline-block;
          padding: 13px 20px;
          border-radius: 14px;
          text-decoration: none;
          font-weight: 700;
          transition: 0.25s ease;
        }

        .btn-primary {
          background: linear-gradient(90deg, var(--cyan), var(--violet));
          color: #04111a;
          box-shadow: var(--shadow);
        }

        .btn-primary:hover {
          transform: translateY(-2px);
          opacity: 0.95;
        }

        .btn-secondary {
          border: 1px solid var(--line);
          color: var(--text);
          background: rgba(255, 255, 255, 0.03);
        }

        .btn-secondary:hover {
          border-color: var(--cyan);
          color: var(--cyan);
        }

        .hero-panel {
          border: 1px solid var(--line);
          background: linear-gradient(180deg, rgba(12, 19, 40, 0.82), rgba(8, 13, 28, 0.9));
          border-radius: 24px;
          padding: 24px;
          box-shadow: var(--shadow);
        }

        .hero-car {
          width: 100%;
          aspect-ratio: 16 / 10;
          border-radius: 18px;
          background:
            radial-gradient(circle at 25% 30%, rgba(78, 255, 236, 0.38), transparent 20%),
            radial-gradient(circle at 70% 35%, rgba(139, 92, 246, 0.35), transparent 22%),
            radial-gradient(circle at 60% 80%, rgba(255, 79, 216, 0.22), transparent 18%),
            linear-gradient(145deg, #0b1631, #091122 55%, #050b18);
          border: 1px solid rgba(78, 255, 236, 0.16);
          position: relative;
          overflow: hidden;
        }

        .hero-car::before {
          content: "";
          position: absolute;
          inset: auto 12% 18% 12%;
          height: 18%;
          border-radius: 999px;
          background: linear-gradient(90deg, rgba(78,255,236,.0), rgba(78,255,236,.85), rgba(139,92,246,.85), rgba(78,255,236,.0));
          filter: blur(16px);
        }

        .hero-car::after {
          content: "TESLA XR-INFINITY";
          position: absolute;
          left: 18px;
          bottom: 16px;
          color: var(--text);
          font-size: 0.9rem;
          letter-spacing: 2px;
        }

        section {
          padding: 30px 0 20px;
        }

        .section-title {
          font-size: 2rem;
          margin-bottom: 10px;
        }

        .section-sub {
          color: var(--muted);
          margin-bottom: 24px;
        }

        .cars-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 20px;
        }

        .car-card {
          background: var(--card);
          border: 1px solid var(--line);
          border-radius: 22px;
          overflow: hidden;
          box-shadow: var(--shadow);
          transition: 0.25s ease;
        }

        .car-card:hover {
          transform: translateY(-4px);
          border-color: rgba(78, 255, 236, 0.38);
        }

        .car-visual {
          height: 190px;
          background:
            radial-gradient(circle at 18% 20%, rgba(78,255,236,.33), transparent 18%),
            radial-gradient(circle at 80% 25%, rgba(139,92,246,.35), transparent 18%),
            linear-gradient(135deg, #0b1736, #091324 60%, #060b17);
          position: relative;
        }

        .car-visual::after {
          content: "";
          position: absolute;
          left: 10%;
          right: 10%;
          bottom: 18%;
          height: 14%;
          border-radius: 999px;
          background: linear-gradient(90deg, rgba(78,255,236,0), rgba(78,255,236,.8), rgba(255,79,216,.7), rgba(78,255,236,0));
          filter: blur(14px);
        }

        .car-body {
          padding: 18px;
        }

        .car-title {
          font-size: 1.18rem;
          margin-bottom: 8px;
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

        .about-grid,
        .contact-grid {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 20px;
        }

        .info-card {
          background: var(--card);
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

        .footer {
          padding: 34px 0 50px;
          text-align: center;
          color: var(--muted);
          font-size: 0.94rem;
        }

        @media (max-width: 980px) {
          .hero-wrap,
          .cars-grid,
          .about-grid,
          .contact-grid {
            grid-template-columns: 1fr;
          }
        }

        @media (max-width: 640px) {
          h1 {
            font-size: 2.4rem;
          }

          .nav-inner {
            gap: 12px;
            align-items: flex-start;
            flex-direction: column;
          }

          .cars-grid {
            grid-template-columns: 1fr;
          }
        }
      </style>
    </head>
    <body>
      <nav class="nav">
        <div class="container nav-inner">
          <div class="brand">Future<span>Cars</span> 2055</div>
          <div class="nav-links">
            <a href="#cars">Cars</a>
            <a href="#about">About</a>
            <a href="#reserve">Reserve</a>
            <a href="#contact">Contact</a>
          </div>
        </div>
      </nav>

      <header class="hero">
        <div class="container hero-wrap">
          <div>
            <div class="eyebrow">Luxury vehicles from tomorrow</div>
            <h1>
              Reserve the <span class="glow">Alien Machines</span><br />
              of 2055.
            </h1>
            <p>
              FutureCars is a digital showroom for ultra-rare concept vehicles
              engineered for the year 2055 — hover systems, chrono-AI navigation,
              plasma nitro, flight mode, and cinematic alien design.
            </p>
            <div class="cta-row">
              <a class="btn btn-primary" href="#cars">Explore Vehicles</a>
              <a class="btn btn-secondary" href="#reserve">Reserve for 2055</a>
            </div>
          </div>

          <div class="hero-panel">
            <div class="hero-car"></div>
          </div>
        </div>
      </header>

      <section id="cars">
        <div class="container">
          <h2 class="section-title">FutureCars Collection</h2>
          <p class="section-sub">
            Seven rare machines inspired by today’s icons, reborn for a sci-fi civilization.
          </p>

          <div class="cars-grid">
            <article class="car-card">
              <div class="car-visual"></div>
              <div class="car-body">
                <div class="tag">Hover Hypercar</div>
                <h3 class="car-title">Tesla Xr-Infinity</h3>
                <p>Mutation of the Tesla Model X, redesigned for anti-gravity urban flight.</p>
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
              <div class="car-visual"></div>
              <div class="car-body">
                <div class="tag">Cosmic Coupe</div>
                <h3 class="car-title">BMW Nebula IX</h3>
                <p>An evolved BMW i8 with stellar energy cells and stealth midnight aura.</p>
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
              <div class="car-visual"></div>
              <div class="car-body">
                <div class="tag">Neural Luxury Sedan</div>
                <h3 class="car-title">Mercedes Vision Æon</h3>
                <p>A future descendant of the EQS with a neural-link drive core.</p>
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
              <div class="car-visual"></div>
              <div class="car-body">
                <div class="tag">Warp Performance</div>
                <h3 class="car-title">Porsche Eclipse 9110</h3>
                <p>The classic 911 reborn as a warp-speed machine with sonic launch.</p>
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
              <div class="car-visual"></div>
              <div class="car-body">
                <div class="tag">Solar Grand Tourer</div>
                <h3 class="car-title">Lucid Astral GT</h3>
                <p>Inspired by Lucid Air, upgraded with solar plasma flow and adaptive luxury.</p>
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
              <div class="car-visual"></div>
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
              <div class="car-visual"></div>
              <div class="car-body">
                <div class="tag">Flight Limited Edition</div>
                <h3 class="car-title">DeLorean Thunderflight</h3>
                <p>A tribute to cinematic time machines, rebuilt for real airborne travel.</p>
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

      <section id="about">
        <div class="container">
          <h2 class="section-title">About FutureCars</h2>
          <p class="section-sub">
            A future-focused concept showroom powered by a cloud-native GitOps platform.
          </p>
          <div class="about-grid">
            <div class="info-card">
              <h3>Why 2055?</h3>
              <p>
                We imagine a world where mobility blends with aerospace, AI,
                alien aesthetics, and extreme luxury. Customers reserve today
                and receive a certified future-delivery allocation in 2055.
              </p>
            </div>
            <div class="info-card">
              <h3>Built on Modern Infrastructure</h3>
              <p>
                This platform is deployed using GitHub Actions, Amazon ECR,
                ArgoCD, Kubernetes on EKS, ALB ingress, Route53, ACM, and Terraform.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section id="reserve">
        <div class="container">
          <h2 class="section-title">Reserve a Vehicle</h2>
          <p class="section-sub">
            Place your reservation today and secure your position in the 2055 delivery wave.
          </p>
          <div class="info-card">
            <h3>Reservation Process</h3>
            <p>
              Customers submit a future reservation request, select a vehicle,
              and receive a digital Future Delivery Certificate confirming their
              2055 allocation slot.
            </p>
          </div>
        </div>
      </section>

      <section id="contact">
        <div class="container">
          <h2 class="section-title">Contact</h2>
          <p class="section-sub">Talk to our future mobility concierge team.</p>
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
          FutureCars 2055 — Purchase today. Drive in 2055.
        </div>
      </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)