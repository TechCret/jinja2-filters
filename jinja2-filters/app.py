from flask import Flask, render_template

from util.template_filters import calculate_date_date

app = Flask(__name__)


@app.route('/dob')
def person_dob():
    dob_list = ['01/05/1992', '21/02/1990', '09/11/1991', '18/07/1994', '28/10/1987', '19/03/1990']
    return render_template('person_dob.html', dob_list=dob_list)


app.add_template_filter(calculate_date_date)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
