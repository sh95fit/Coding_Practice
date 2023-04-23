from flask import Flask, render_template, request, redirect
from .flask_test import topics

def getContents() :
    liTags = ''
    for topic in topics :
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

def getUpdate(id=None) :
    contextUI = ''
    if id != None :
        contextUI = f'''
            <li style="list-style-type:none"><a href="/update/{id}">Update</a></li>
            <li style="list-style-type:none"><form action="/delete/{id}" method="POST"><input type="submit" value="Delete"></from><li>
        '''
        return contextUI

def create_app(config=None) :
    app = Flask(__name__)

    @app.route('/')
    def index() :
        return render_template('test.html', liTags = getContents(), title = "Welcome", body = "Hello, WEB")

    @app.route('/create/', methods =['GET', 'POST'])
    def create() :
        content = '''
            <form action="/create/" method='POST'>
                <p><input type='text' placeholder='title' name='title' /></p>
                <p><textarea placeholder='body' name='body'></textarea></p>
                <p><input type='submit' value='Create' /></p>
            </form>
        '''
        if request.method == 'POST' :
            topics.append({'id':len(topics)+1, 'title':request.form['title'], 'body':request.form['body']})
            return redirect('/')

        return render_template('test_create.html', LiTags = getContents(), title = 'Create', body = content)
        

    @app.route('/read/<int:id>/')
    def read(id) : 
        title = ''
        body = ''
        for topic in topics :
            if id == topic['id'] :
                title = topic['title']
                body = topic['body']
                break
        return render_template('test.html', liTags = getContents(), title = title, body = body, getUpdate = getUpdate(id))
        
    @app.route('/update/<int:id>/', methods=['GET', 'POST'])
    def update(id) :
        title = ''
        body = ''
        for topic in topics :
            if id == topic['id'] :
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}" method='POST'>
                <p><input type='text' placeholder='title' name='title' value="{title}"/></p>
                <p><textarea placeholder='body' name='body'>{body}</textarea></p>
                <p><input type='submit' value='Update' /></p>
            </form>
        '''
        if request.method == "POST" :
            for topic in topics :
                if id == topic['id']:
                    topic['title'] = request.form['title']
                    topic['body'] = request.form['body']
                    break
            return redirect('/')
        return render_template('test_update.html', LiTags = getContents(), title = 'Update', body = content)

    @app.route('/delete/<int:id>/', methods=['POST'])
    def delete(id) :
        for topic in topics :
            if id == topic['id'] :
                topics.remove(topic)
                break
        return redirect('/')

    @app.route('/random')
    def random() :
        import random
        return 'random number : ' + str(random.random())

    return app