from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Communities
views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/test')
def test():
    return render_template('test.html')

@views.route('/guides',methods=['GET','POST'])
def guides():
    entries = User.query.filter_by(role='guide').all()
    if request.method == 'POST':
        query = request.form['query']
        entries = User.query.filter(User.city.contains(query)).all()
    return render_template("guides.html",entries=entries)

@views.route('/community',methods=['GET','POST'])
def communities():
    entries = Communities.query.all()
    if request.method == 'POST':
        query = request.form['query']
        entries = Communities.query.filter(Communities.name.contains(query)).all()
    return render_template("community.html",entries=entries)



@views.route('/videocall')
def videocall():
    username="Evan"
    return render_template('videocall.html',username=username)

@views.route('/radio')
def radio():
    return render_template('radio.html')

@views.route('/travel')
def travel():
    return render_template('mainpage.html')

@views.route('/travel/ahemdabad')
def ahemdabad():
    return render_template('ahemdabad_page.html')

@views.route('/travel/delhi')
def delhi():
    return render_template('delhi_page.html')
 
@views.route('/travel/kashmir')
def kashmir():
    return render_template('kashmir_page.html')
 
@views.route('/travel/lakshadweep')
def lakshadweep():
    return render_template('lakshadweep_page.html')
 
@views.route('/travel/lucknow')
def lucknow():
    return render_template('lucknow_page.html')
 
@views.route('/travel/mumbai')
def mumbai():
    return render_template('mumbai_page.html')
 
@views.route('/travel/puducherry')
def puducherry():
    return render_template('puducherry_page.html')
 
@views.route('/travel/sikkim')
def sikkim():
    return render_template('sikkim_page.html')
 
