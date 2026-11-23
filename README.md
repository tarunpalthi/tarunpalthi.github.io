# Tarun Palthi | Analytics Portfolio

Personal portfolio website for **Tarun Palthi**, a Senior Analytics Leader with 8+ years of experience in digital analytics, experimentation, business intelligence, and AI-enabled reporting across telecom, finance, healthcare, and retail.

**Live site:** [tarunpalthi.github.io](https://tarunpalthi.github.io)
**LinkedIn:** [linkedin.com/in/tarunpalthi](https://linkedin.com/in/tarunpalthi)

---

## About This Project

This repository hosts my portfolio, built as a single, self-contained HTML file with no build step and no framework. The goal was to present an analytics career the way an analytics person would: with real data visualizations, clear structure, and fast load times, rather than a static resume.

If you are a recruiter, hiring manager, or fellow analyst, the site is designed to answer three questions quickly:

1. What kind of problems do I solve?
2. What impact has my work had?
3. What tools and methods do I use?

## What's on the Site

| Section | What it covers |
| --- | --- |
| **Hero** | Quick summary of who I am, key focus areas, and current availability |
| **About** | Career story, color-coded by the companies I worked with |
| **Experience** | Full timeline of roles, from internships to enterprise analytics leadership, with client-first presentation for contract roles |
| **Impact** | Headline results: $500M+ business impact, 150+ experiments, 150+ executive dashboards |
| **Skills** | Core expertise pills, tools grid, and skill depth chart |
| **Certifications** | Browsable slider of certifications across analytics, BI, cloud, and AI |
| **Projects** | Selected work and independent projects |
| **Education** | MBA and MS in Computer & Information Science (both 3.9 GPA), plus B.Tech |
| **Recommendations** | LinkedIn recommendations from managers, directors, and peers |
| **Honors and Languages** | Recognition and spoken languages |
| **Contact** | Email and meeting scheduling modals, plus social links |

## Interactive Data Visualizations

The site includes three custom charts built with [Chart.js](https://www.chartjs.org/):

- **Career Composition:** a horizontal stacked bar showing time spent in each role, including real gaps between roles. Hover for tenure details and click any segment to jump to the matching experience card.
- **Tools by Category:** a donut chart of my tool stack grouped by category, with hover effects and tooltips.
- **Skill Radar:** a spider chart of skill depth with a heat-style gradient fill.

All charts animate when they scroll into view, using the browser's `IntersectionObserver`.

## Other Features

- Light and dark mode toggle
- Fully responsive layout for desktop, tablet, and mobile
- Custom glowing cursor and subtle UI sound effects
- Built-in assistant that answers common questions about my background
- Email and calendar request modals for getting in touch
- Inline SVG flags and base64-embedded images, so there are no broken asset links

## Tech Stack

- **HTML5, CSS3, and vanilla JavaScript** (no framework, no bundler)
- **Chart.js 4.4** (loaded from cdnjs) for data visualizations
- **Google Fonts** (Syne and DM Sans) for typography
- **GitHub Pages** for hosting

## Repository Structure

```
.
├── index.html     # The entire portfolio: markup, styles, and scripts
└── README.md      # You are here
```

## Run It Locally

No installation needed.

```bash
# Clone the repository
git clone https://github.com/tarunpalthi/tarunpalthi.github.io.git
cd tarunpalthi.github.io

# Open in your browser
open index.html          # macOS
start index.html         # Windows
xdg-open index.html      # Linux
```

An internet connection is needed on first load for Chart.js and Google Fonts.

## Deployment

The site is deployed with **GitHub Pages**:

1. Push changes to the branch configured under **Settings → Pages**.
2. Wait for the **pages build and deployment** workflow in the **Actions** tab to finish. This usually takes a minute or two.
3. Hard refresh the site to bypass the browser cache.

## Design Notes

- **One file, on purpose.** Keeping everything in a single HTML file makes the site easy to host, easy to version, and fast to load.
- **Color-coded companies.** Each employer or client has its own color, used consistently across the About section, experience timeline, and cards.
- **Client-first contract roles.** For consulting engagements, the client (for example Verizon or PricewaterhouseCoopers) is highlighted, with the employing firm shown as a secondary "via" note.

## Contact

I'm open to analytics leadership opportunities in data and product analytics, business intelligence, experimentation, AI, and modern data platforms.

- Website: [tarunpalthi.github.io](https://tarunpalthi.github.io)
- LinkedIn: [linkedin.com/in/tarunpalthi](https://linkedin.com/in/tarunpalthi)

## License and Usage

The content of this site (text, images, and personal information) belongs to Tarun Palthi and is not licensed for reuse. You are welcome to look at the code for inspiration, but please do not copy the content or present it as your own.
