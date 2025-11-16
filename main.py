from flask import Flask, render_template, request, redirect, url_for, session, make_response
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'hts2k25-blackxmask-secret-key')

users_db = {
    1: {"username": "john_doe", "role": "user", "email": "john@rivertown.com", "flag": "FLAG{1D0R_BR34CH_C0MPL3T3}"},
    2: {"username": "admin", "role": "admin", "email": "admin@rivertown.com", "flag": "FLAG{ADM1N_PR0F1L3_H4CK3D}"},
    3: {"username": "guest", "role": "user", "email": "guest@rivertown.com", "flag": "FLAG{GU3ST_ACC3SS_GR4NT3D}"}
}

sql_users = [
    {"username": "admin", "password": "SecurePass123!", "flag": "FLAG{SQL1_F1R3W4LL_BYP4SS3D}"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/challenge/idor')
def idor_challenge():
    user_id = request.args.get('id', '1')
    try:
        user_id = int(user_id)
        if user_id in users_db:
            user = users_db[user_id]
            return render_template('idor.html', user=user, user_id=user_id)
        else:
            return render_template('idor.html', user=None, user_id=user_id, error="Access denied. Resource not available.")
    except:
        return render_template('idor.html', user=None, user_id=1, error="Invalid request format.")

@app.route('/challenge/xss', methods=['GET', 'POST'])
def xss_challenge():
    result = None
    if request.method == 'POST':
        search_query = request.form.get('search', '')
        if '<script>' in search_query.lower() and 'alert' in search_query.lower():
            result = f"Search results for: {search_query}<br><br><div class='flag-reveal'>XSS Payload Executed! FLAG{{XSS_3XPL01T4T10N_SUCC3SS}}</div>"
        else:
            result = f"Search results for: {search_query}<br><br>No results found matching your query."
    return render_template('xss.html', result=result)

@app.route('/challenge/sqli', methods=['GET', 'POST'])
def sqli_challenge():
    error = None
    success = None
    
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        if "' or '1'='1" in username.lower() or "' or 1=1" in username.lower() or "admin'--" in username.lower() or "' or" in username.lower():
            success = f"Login successful! Welcome admin!<br><br><div class='flag-reveal'>FLAG{{SQL1_F1R3W4LL_BYP4SS3D}}</div>"
        else:
            for user in sql_users:
                if user['username'] == username and user['password'] == password:
                    success = f"Login successful! FLAG: {user['flag']}"
                    break
            if not success:
                error = "Authentication failed. Access denied."
        
        return render_template('sqli.html', error=error, success=success)
    
    return render_template('sqli.html', error=error, success=success)

@app.route('/challenge/admin')
def admin_challenge():
    return render_template('admin.html')

@app.route('/secret_admin_panel_x9z2k')
def secret_admin():
    flag = "FLAG{S3CR3T_ADM1N_P4N3L_F0UND}"
    return f"""
    <html>
    <head>
        <title>Secret Admin Panel</title>
        <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
    </head>
    <body>
        <div class="container">
            <h1 class="glitch" data-text="ACCESS GRANTED">ACCESS GRANTED</h1>
            <div class="terminal-box">
                <h2>BlackHaze Admin Console</h2>
                <p>Congratulations, Agent! You've discovered the hidden admin backdoor.</p>
                <div class="flag-reveal">
                    {flag}
                </div>
                <br>
                <p>System Status: COMPROMISED</p>
                <p>Firewall: DISABLED</p>
                <p>Mission Progress: 4/4 Modules Breached</p>
                <br>
                <a href="/" class="btn">Return to Command Center</a>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
