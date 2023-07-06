#this line adds functionality to our project :)
from flask import Flask,render_template, redirect,request

app=Flask(__name__)

items=[]

@app.route('/add',methods=['POST']) #CREATE 
def add_items():
    item=request.form['item']
    items.append(item)#this will append the item to the array items
    return redirect('/')

'''by default route uses GET method 
   which only lets user to receive'''

@app.route('/') #READ 
def checklist():
    return render_template('checklist.html',items=items)

#UPDATE FUNCTIONALITY 

#Edit
@app.route('/edit/<int:item_id>',methods=['GET','POST']) 
def edit_item(item_id):
    item=items[item_id-1]#Retrieves items based on the indexing if 1 it would go to 0 and if 2 it would retrieve the 1st one 
    if request.method=='POST':
        new_item = request.form['item'] #adds the index to new item as the last one 
        items [item_id-1]=new_item
        return redirect('/')
    else:
        return render_template('edit.html', item=item, item_id=item_id)  #if the request method is not POST then it will display the previous item and item id not the one which is updated in the if statement

#Delete
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    del items[item_id-1]
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True,port=8000)