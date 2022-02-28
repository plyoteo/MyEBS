from flask import Flask,render_template,request
import pandas as pd


df=pd.DataFrame(dict(first_name=[],last_name=[],email=[]))
dfn=pd.DataFrame(dict(first_name=[],last_name=[],email=[]))
df.to_csv('out.csv',index=False)

application=Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')
    
@application.route('/enter')
def enter():
    return render_template('addrec.html')
    
@application.route('/addrec',methods=['POST'])
def addrec():
    fn=request.form['fn']
    ln=request.form['ln']
    em=request.form['em']
    df=pd.read_csv('out.csv')
    dfn=pd.DataFrame({'first_name':[fn],'last_name':[ln],'email':[em]})
    df=pd.concat([df,dfn],ignore_index=True)
    df.to_csv('out.csv',index=False)
    return render_template('home.html')
    
@application.route('/delete')
def delete():
    return render_template('delrec.html')
    
@application.route('/delrec',methods=['POST'])
def delrec():
    fn=request.form['fn']
    ln=request.form['ln']
    df=pd.read_csv('out.csv')
    df.drop(df.loc[(df.first_name.eq(fn)) & (df.last_name.eq(ln))].index,inplace=True)
    df.to_csv('out.csv',index=False)
    return render_template('home.html')
    
@application.route('/view')
def view():
    df=pd.read_csv('out.csv')
    return render_template('view.html',title='MyInfo',data=df.to_html(index=False))
        

if __name__=='__main__':
    application.run(debug=True)
