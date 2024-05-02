import sqlite3
import numpy as np

dbName="bd_empresa"
def createTables(table_name):
    mydb=sqlite3.connect(dbName)
    mycursor=mydb.cursor()
    if table_name == 'departments':
        mycursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
        id INTEGER,
        department TEXT,
        upload_timestamp DATETIME);
        ''')
    elif table_name == 'jobs':
        mycursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER,
        job TEXT,
        upload_timestamp DATETIME);
        ''')
    elif table_name == 'hired_employees':
        mycursor.execute('''
            CREATE TABLE IF NOT EXISTS hired_employees
            (id INTEGER,
            name TEXT,
            datetime TEXT,
            department_id INTEGER,
            job_id INTEGER,
            upload_timestamp DATETIME);
        ''')
    
    mydb.commit()
    mydb.close()

def  updateTable(table_name,df):
    mydb=sqlite3.connect(dbName)
    
    # Split the DataFrame into 1000-row fragments
    #Be able to insert batch transactions (1 up to 1000 rows) with one request
    for chunk in np.array_split(df, len(df) // 1000 + 1):
            chunk.to_sql(table_name, mydb, if_exists='append', index=False)
    mydb.commit()
    mydb.close()

def  metric(metric_number):
    mydb=sqlite3.connect(dbName)
    mycursor=mydb.cursor()
    if metric_number == '1':
        mycursor.execute('''
            SELECT  departments.department, 
                    jobs.job,
                    SUM(CASE WHEN strftime('%m', datetime) BETWEEN '01' AND '03' THEN 1 ELSE 0 END) as Q1,
                    SUM(CASE WHEN strftime('%m', datetime) BETWEEN '04' AND '06' THEN 1 ELSE 0 END) as Q2,
                    SUM(CASE WHEN strftime('%m', datetime) BETWEEN '07' AND '09' THEN 1 ELSE 0 END) as Q3,
                    SUM(CASE WHEN strftime('%m', datetime) BETWEEN '10' AND '12' THEN 1 ELSE 0 END) as Q4
            FROM hired_employees
            LEFT JOIN departments ON hired_employees.department_id = departments.id
            LEFT JOIN jobs ON hired_employees.job_id = jobs.id
            WHERE strftime('%Y', datetime) = '2021'
            GROUP BY departments.department, jobs.job
            ORDER BY departments.department, jobs.job
        ''')
        
    elif metric_number == '2':
        mycursor.execute('''
                    SELECT  departments.id as department_id,departments.department as department_name, 
                    COUNT(he.id) as hired
                    FROM departments
                    JOIN hired_employees he 
                    ON (departments.id = he.department_id)
                    WHERE strftime('%Y', he.datetime) = '2021'
                    GROUP BY departments.id, departments.department
                    HAVING COUNT(he.id) > (
                                            SELECT AVG(department_hired)
                                            FROM (
                                                SELECT COUNT(he2.id) as department_hired
                                                FROM hired_employees he2
                                                WHERE strftime('%Y', he2.datetime) = '2021'
                                                GROUP BY he2.department_id
                                            ) AS subquery
                    )
                    ORDER BY hired DESC;''')
    else:
        return 400

    result = mycursor.fetchall()
    
    #convert to dictionary
    insertObject=[]
    columnNames=[column[0] for column in mycursor.description]
    for record in result:
        insertObject.append(dict(zip(columnNames,record)))
    mydb.close()
    return insertObject
    
    
    