from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/hai')
def hai():
    return render_template('hai.html')


@FAI.route('/img_insert')
def img_insert():
    return render_template('img.html')
if __name__=='__main__':
    FAI.run(debug=True)