from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from .models import Upload, db
from .utils import parse_csv

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return redirect(url_for('main.dashboard'))

@main.route('/dashboard')
@login_required
def dashboard():
    uploads = Upload.query.filter_by(user_id=current_user.id).all()
    
    # If a file is selected to view
    selected_file_id = request.args.get('file_id')
    csv_data = None
    
    if selected_file_id:
        upload = Upload.query.get_or_404(selected_file_id)
        if upload.owner != current_user:
            flash('Unauthorized access to file')
            return redirect(url_for('main.dashboard'))
            
        csv_data = parse_csv(upload.filepath)
        csv_data['filename'] = upload.filename
        
    return render_template('dashboard.html', uploads=uploads, csv_data=csv_data)

@main.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
        
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
        
    if file and file.filename.endswith('.csv'):
        filename = secure_filename(file.filename)
        # Ensure unique filename to prevent overwrites or handle it in DB logic
        # For simplicity, we just save it. In prod, use UUID or similar.
        
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], f"{current_user.id}_{filename}")
        file.save(save_path)
        
        new_upload = Upload(filename=filename, filepath=save_path, user_id=current_user.id)
        db.session.add(new_upload)
        db.session.commit()
        
        flash('File uploaded successfully')
        return redirect(url_for('main.dashboard', file_id=new_upload.id))
    else:
        flash('Allowed file types are CSV')
        return redirect(url_for('main.dashboard'))

@main.route('/delete/<int:file_id>', methods=['POST'])
@login_required
def delete_file(file_id):
    upload = Upload.query.get_or_404(file_id)
    if upload.owner != current_user:
        flash('Unauthorized')
        return redirect(url_for('main.dashboard'))
    
    # Remove file from disk
    try:
        if os.path.exists(upload.filepath):
            os.remove(upload.filepath)
    except Exception as e:
        print(f"Error removing file: {e}")
        
    db.session.delete(upload)
    db.session.commit()
    flash('File deleted successfully')
    return redirect(url_for('main.dashboard'))
