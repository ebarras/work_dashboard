import threading
import time
from flask import Flask, render_template

app = Flask(__name__)

def interval_query():
	while True:
		#Code here. Scrape the site, update the database.
		print("Cycle")
		time.sleep(5)

thread = threading.Thread(name='interval_query', target=interval_query)
thread.setDaemon(True)
thread.start()

@app.route('/')
def hello_world():
	return "Hello World!"

if __name__ == "__main__":
	app.run()