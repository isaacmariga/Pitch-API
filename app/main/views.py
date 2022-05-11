from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Group,Pitch,Comment,Vote
from .forms import PitchForm,CommentForm,GroupForm
from flask_login import current_user, login_required



# Views
@main.route('/')
def index():
    title = 'Home'

    groups = Group.get_groups()

    return render_template('index.html', title = title, groups=groups )

@main.route('/group/new', methods=['GET','POST'])
@login_required
def new_group():
    form = GroupForm()

    if form.validate_on_submit():
        name = form.name.data
        new_group = Group(name=name)
        new_group.save_group()

        return redirect(url_for('.index'))

    title = 'New Group'
    return render_template('new_group.html', group_form = form)


@main.route('/group/<int:id>')
def group(id):
    group = Group.query.get(id)

    if group is None:
        abort(404)

    pitches = Pitch.get_pitches(id)
    title = f'{group.name} page'

    return render_template('group.html', title=title, group=group, pitches=pitches)

@main.route('/group/pitch/new/<int:id>', methods=['GET','POST'])
@login_required
def new_pitch(id):
    group = Group.query.filter_by(id=id).first()

    if group is None:
        abort(404)

    form = PitchForm()

    if form.validate_on_submit():
        pitch_content = form.pitch_content.data
        new_pitch = Pitch( pitch_content=pitch_content, group=group)
        new_pitch.save_pitch()

        return redirect(url_for('.group', id=group.id ))

    title = 'New Pitch'
    return render_template('new_pitch.html', title=title, pitch_form=form)


@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitch = Pitch.query.get(id)
    
    if pitch is None:
        abort(404)

    comments = Comment.get_comments(id)

    # vote = Vote.query.all()

    total_votes = Vote.num_vote(pitch.id)

    title = f'Pitch {pitch.id}'

    return render_template('pitch.html', title=title, pitch=pitch, comments=comments, total_votes=total_votes)

@main.route('/pitch/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    pitch = Pitch.query.filter_by(id=id).first()

    if pitch is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        comment_content = form.comment_content.data
        new_comment = Comment( comment_content=comment_content, pitch=pitch )
        # user=current_user(add later)
        new_comment.save_comment()

        return redirect(url_for('.single_pitch', id=pitch.id ))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)

@main.route('/pitch/upvote/<int:id>')
@login_required
def upvote(id):
    pitch = Pitch.query.get(id)
    new_vote = Vote( pitch=pitch, vote_number=1)
    new_vote.save_vote()
    return redirect(url_for('.single_pitch', id=pitch.id))


@main.route('/pitch/downvote/<int:id>')
@login_required
def downvote(id):
    pitch = Pitch.query.filter_by(id=id).first()
    new_vote = Vote(pitch=pitch, vote_number= -1)
    new_vote.save_vote()

    return redirect(url_for('.single_pitch', id=pitch.id))



