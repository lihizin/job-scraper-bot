from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def fetch_jobs():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT jp.found_on, jp.title, jp.link, w.name
        FROM job_posts jp
        JOIN websites w ON jp.website_id = w.id
        ORDER BY jp.found_on DESC
    """)
    jobs = cursor.fetchall()
    conn.close()
    return jobs

@app.route('/jobs')
def show_jobs():
    jobs = fetch_jobs()
    return render_template('jobs.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)
