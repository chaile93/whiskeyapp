#THESE ARE THE ROUTES.PY FOR ALL WEB/APP PAGES. THESE ROUTES WILL NEED TO BE IMPORTED IN __INIT__
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, abort
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)
    

@views.route('/')
def home():
    return render_template('home.html')



@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('profile.html', user=current_user)

#DELETE
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})








    
