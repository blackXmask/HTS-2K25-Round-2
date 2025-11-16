# HTS-2K25 - Operation: Broken Web

## Overview
This is a web security challenge platform built for the HTS-2K25 hackathon Round 2, hosted by BlackXmask Cyber Division. The platform features 4 CTF-style security challenges in a single Flask application with a dark hacker-themed GUI. **All hints have been removed to make challenges more challenging and realistic.**

## Project Structure
```
main.py                 # Flask backend with all challenge routes
templates/              # HTML templates
  ├── index.html        # Landing page with GUI dashboard
  ├── idor.html         # IDOR challenge (no hints)
  ├── xss.html          # XSS challenge (no hints)
  ├── sqli.html         # SQL Injection challenge (no hints)
  └── admin.html        # Admin panel challenge (no hints)
static/
  └── style.css         # Dark hacker-themed styling
```

## Challenges

### 1. IDOR Breach (🟦)
- **Vulnerability:** Insecure Direct Object Reference
- **Objective:** Access other users' profiles by manipulating URL parameters
- **Difficulty:** ★★★☆ (Increased - no hints provided)
- **Flag Location:** Admin user profile (ID: 2)
- **Flag:** `FLAG{ADM1N_PR0F1L3_H4CK3D}`
- **Notes:** Quick access buttons removed, participants must discover ID manipulation on their own

### 2. XSS Exploitation (🟩)
- **Vulnerability:** Cross-Site Scripting
- **Objective:** Inject JavaScript payload in the search module to execute code
- **Difficulty:** ★★★☆ (Increased - no example payloads)
- **Solution:** Submit `<script>alert('XSS')</script>` in search field
- **Flag:** `FLAG{XSS_3XPL01T4T10N_SUCC3SS}`
- **Notes:** All hints and examples removed, generic error messages only

### 3. SQL Injection Firewall Bypass (🟥)
- **Vulnerability:** SQL Injection
- **Objective:** Bypass login authentication using SQL injection techniques
- **Difficulty:** ★★★★ (Increased - no query structure shown)
- **Solution:** Use payloads like `admin' OR '1'='1` or `admin'--` or `' OR 1=1--`
- **Flag:** `FLAG{SQL1_F1R3W4LL_BYP4SS3D}`
- **Notes:** Query display removed, no example payloads, generic error messages

### 4. Admin Panel Takeover (🟪)
- **Vulnerability:** Hidden endpoint discovery
- **Objective:** Find the secret admin panel URL through reconnaissance
- **Difficulty:** ★★★★★ (Significantly increased - all clues removed)
- **Solution:** Navigate to `/secret_admin_panel_x9z2k`
- **Flag:** `FLAG{S3CR3T_ADM1N_P4N3L_F0UND}`
- **Notes:** Developer comments removed, quick test buttons removed, requires proper recon skills

## Technology Stack
- **Backend:** Flask (Python 3.11) + Gunicorn
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Styling:** Custom dark hacker theme with neon effects
- **Server:** Runs on 0.0.0.0:5000
- **Deployment:** Autoscale deployment configured

## Features
- Dark hacker-themed GUI with glitch effects
- Responsive design
- Real-time flag reveal on successful exploits
- **NO hints or tutorials** - realistic CTF difficulty
- Generic error messages to increase challenge difficulty
- Cinematic storyline: Rivertown vs BlackHaze
- Production-ready deployment configuration

## Running the Application

### Development
The application runs automatically via the configured workflow:
```bash
python main.py
```

### Production
Configured for Replit autoscale deployment:
```bash
gunicorn --bind=0.0.0.0:5000 --reuse-port main:app
```

Access the platform at the webview URL on port 5000.

## Hackathon Info
- **Event:** HTS-2K25 Round 2
- **Host:** BlackXmask Cyber Community
- **Theme:** Cyber Attack Simulation
- **Total Flags:** 4
- **Difficulty Range:** ★★★☆ to ★★★★★ (All increased)
- **Challenge Level:** Hard (No hints provided)

## Recent Changes
- **2025-11-16:** Initial project creation with all 4 security challenges
- **2025-11-16:** Implemented dark hacker-themed GUI with glitch animations
- **2025-11-16:** Added Flask backend with vulnerable endpoints for CTF challenges
- **2025-11-16:** Removed all hints, examples, and helper buttons to significantly increase difficulty
- **2025-11-16:** Hardened challenges with generic error messages and removed debug information
- **2025-11-16:** Configured production deployment with Gunicorn
