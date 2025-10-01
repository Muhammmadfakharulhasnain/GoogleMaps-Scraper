from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
import datetime
from main import scrape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search = request.form.get('search')
        try:
            total = int(request.form.get('total'))
            if total < 1:
                raise ValueError
        except ValueError:
            return render_template('index.html', error='Total must be a positive integer.')
        
        scrape(search, total)
        filename = search.replace(' ', '_')
        return redirect(url_for('results', filename=filename))
    
    return render_template('index.html')

@app.route('/results')
def results():
    filename = request.args.get('filename')
    if not filename:
        return redirect(url_for('index'))
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    csv_path = os.path.join('GMaps Data', today, f"{filename}.csv")
    
    if not os.path.exists(csv_path):
        return render_template('results.html', error='No data found for this search.')
    
    df = pd.read_csv(csv_path)
    
    # Compute unique values for filterable columns
    unique_values = {}
    for col in df.columns:
        uniques = df[col].dropna().unique()
        if 1 < len(uniques) < 50:  # Reasonable number for dropdown
            if df[col].dtype in ['float64', 'int64']:
                uniques = sorted(uniques)
            else:
                uniques = sorted(uniques.astype(str))
            unique_values[col] = [str(u) for u in uniques]
    
    sort_by = request.args.get('sort_by', 'name')
    if sort_by not in df.columns:
        sort_by = 'name'
    
    sort_order = request.args.get('sort_order', 'asc')
    ascending = sort_order == 'asc'
    
    df = df.sort_values(by=sort_by, ascending=ascending, na_position='last')
    
    filter_by = request.args.get('filter_by')
    filter_value = request.args.get('filter_value')
    
    if filter_by and filter_value and filter_by in df.columns:
        try:
            if df[filter_by].dtype == 'float64':
                value = float(filter_value)
            elif df[filter_by].dtype == 'int64':
                value = int(filter_value)
            else:
                value = filter_value
            df = df[df[filter_by] == value]
        except ValueError:
            pass
    
    # Pagination logic
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_rows = len(df)
    total_pages = (total_rows + per_page - 1) // per_page
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = df.iloc[start:end].to_dict('records')
    
    data = paginated_data
    columns = df.columns.tolist()
    search = filename.replace('_', ' ')
    
    return render_template('results.html', 
                           data=data, 
                           columns=columns, 
                           sort_by=sort_by, 
                           sort_order=sort_order, 
                           filename=filename, 
                           search=search,
                           page=page,
                           total_pages=total_pages,
                           today=today,
                           unique_values=unique_values,
                           filter_by=filter_by or '',
                           filter_value=filter_value or '')

if __name__ == '__main__':
    app.run(debug=True)