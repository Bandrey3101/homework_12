from flask import Blueprint, request, render_template
from functions import load_posts, uploads_posts
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)
loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static', template_folder='templates')

@loader_blueprint.route('/form/')
def form():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=["GET", "POST"])
def upload():
    picture = request.files.get('picture')
    filename = picture.filename
    content = request.values['content']
    posts = load_posts()
    posts.append({
        'pic': f'/uploads/images/{filename}',
        'content': content
    })


    uploads_posts(posts)
    picture.save(f'uploads/images/{filename}')
    if filename.split('.')[-1] not in ['png', 'jpeg', 'jpg']:
        logging.info('Это не изображение')
    return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)
