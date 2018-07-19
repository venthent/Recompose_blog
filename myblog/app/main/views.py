from flask import render_template, url_for, redirect
from . import main
from ..models import Post, User
from .form import EditForm
from myblog.app import db


@main.route('/')
def post_list():
    posts = Post.query.order_by(Post.created_date).all()
    return render_template('post_list.html', posts=posts)


@main.route('/detail/<int:id>')
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template('post_detail.html', post=post)


@main.route('/edit/<int:id>', methods=['POST', 'GET'])
def post_edit(id):
    form = EditForm()
    post = Post.query.get_or_404(id)
    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.publish()
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.post_detail', id=id))
    form.text.data = post.text
    form.title.data = post.title
    return render_template('post_edit.html', form=form)


@main.route('/new', methods=['POST', 'GET'])
def post_new():
    form = EditForm()
    if form.validate_on_submit():
        u = User.query.get_or_404(1)
        post = Post(title=form.title.data, text=form.text.data, author=u)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.post_list'))
    return render_template('post_edit.html',form=form)
