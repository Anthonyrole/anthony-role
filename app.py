from flask import Flask,render_template

app=Flask(__name__)
JOBS=[
  {'id':1,
   'title':'Data Analyst',
   'location': 'Hyderabad',
    'salary':'Rs. 45000','link':'https://usijobs.deloitte.com/careersUSI/JobDetail/USI-Audit-Services-EH-Sr-Data-Scientist/128585'
  },{'id':2,
   'title':'Data Engineer',
   'location': 'Hyderabad',
    'salary':'Rs. 45000','link':'https://www.google.com/'
  },{'id':3,
   'title':'Analyst',
   'location': 'syderabad',
    'salary':'Rs. 65000'
  },{'id':4,
   'title':'Business Analyst',
   'location': 'Hyderabad',
    'salary':'Rs. 85000'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)