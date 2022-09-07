from flask import Blueprint, request, g, redirect, url_for, render_template, jsonify

from apps.article.models import Article, Article_type
from exts import db

article_bp1 = Blueprint('article', __name__, url_prefix='/article')


# 自定义过滤器

@article_bp1.app_template_filter('cdecode')
def content_decode(content):
    content = content.decode('utf-8')
    return content


@article_bp1.route('/publish', methods=['POST', 'GET'])
def publish_article():
    if request.method == 'POST':
        title = request.form.get('title')
        type_id = request.form.get('type')
        content = request.form.get('content')
        # 添加文章
        article = Article()
        article.title = title
        article.type_id = type_id
        article.content = content
        article.user_id = g.user.id
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('user.index'))


@article_bp1.route('/detail')
def article_detail():
    # 获取文章对象通过id
    article_id = request.args.get('aid')
    article = Article.query.get(article_id)
    # 获取文章分类
    types = Article_type.query.all()

    return render_template('article/detail.html', article=article, types=types)


@article_bp1.route('/love')
def article_love():
    article_id = request.args.get('aid')
    tag = request.args.get('tag')

    article = Article.query.get(article_id)
    if tag == '1':
        article.love_num -= 1
    else:
        article.love_num += 1
    db.session.commit()
    return jsonify(num=article.love_num)
