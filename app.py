from flask import Flask, render_template, request, url_for,redirect, jsonify
import os
import pandas as pd
from controller_db import createTables,updateTable,metric
from datetime import datetime



app=Flask(__name__)

app.config["DEBUG"]=True
UPLOAD_FOLDER='files_csv'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/part1')
def part1():
    return render_template('part1.html')

@app.route("/part1", methods=['POST'])
def uploadFiles():
    uploaded_file=request.files['file']
    if uploaded_file:
        column_names = {
            'departments': ['id', 'department'],
            'jobs': ['id', 'job'],
            'hired_employees': ['id', 'name', 'datetime', 'department_id', 'job_id']
        }
        table_name=uploaded_file.filename.split(".")[0]
        if table_name not in column_names:
            return jsonify({'error': 'Invalid table name provided'})
        
        #save the csv file in directory: files_csv
        file_path=os.path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename)
        uploaded_file.save(file_path)
        #convert de csv file to dataframe
        df=pd.read_csv(file_path,names=column_names[table_name],header=None)
        #drop the NaN values
        df.dropna(inplace=True)
        df['upload_timestamp'] = datetime.now()
        createTables(table_name)
        updateTable(table_name,df)
        
        return jsonify({'message': f'Data uploaded to {table_name} successfully'})
    else:
        return jsonify({'error': 'No file provided in the request'}), 400 

@app.route('/part2')
def part2():
    return render_template('part2.html')

@app.route('/metric/<string:id>')
def metrics(id):
    result=metric(id)
    if result == 400:
        return jsonify({'error': 'Invalid metric'}), result
    else: 
        return render_template('part2.html',id=id,data=result)

    

if(__name__=="__main__"):
    app.run(debug=True,host= '0.0.0.0',port=5000)

