import json

# basic template for generate:

# a_element = """
#             <div class="card" style="width: 10rem;">
#                 <img src="{img}" class="img-thumbnail" alt="{title}">
#                 <div class="card-body">
#                     <h5 class="card-title">{title}</h5>
#                     <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
#                     <a href="{url}" class="btn btn-primary">Click Here</a>
#                 </div>
#             </div>
#             """
# a_element = """
#             <div class="card">
#                 <img src="{img}" class="card-img-top" alt="{title}">
#                 <div class="card-body">
#                 <h5 class="card-title">{title}</h5>
#                 <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
#                 </div>
#                 <div class="card-footer">
#                 <small class="text-muted">Last updated 3 mins ago</small>
#                 </div>
#             </div>
#             """

a_element = """
<div class="mycard" style="width: 10rem;"> 
    <img src="{img}" class="thumbnail" alt="{title}"> 
    <div class="cardbody"> 
        <h5 class="cardtitle">{title}</h5> 
        <p class="cardtext">Some quick example text to build on the card title and make up the bulk of the card's content.</p> 
        <a href="{url}" class="btn btn-primary">Click Here</a>
    </div>
</div>
"""

def gen_list():
    # load data from json:
    with open('09/data.json', encoding='utf-8') as file:
        data = json.load(file)
        
        result = ''
        
        # loop for each item in loaded data.
        # we push this values from json acording to key or item names. 
        for item in data:
            link = a_element.format(
                url   = item['url'],
                title = item['title'],
                img   = item['img'],
            )
            # add each row to result value
            result += link

        return result
    
def save_list():

    list_html = gen_list()
    print(list_html)
    
    with open('09/template.html', mode = 'r', encoding='utf-8') as file:
        html = file.read()
        html = html.replace('<!-- HTML -->', list_html)
        
    
    with open('09/export.html', mode = 'w', encoding='utf-8') as file:
        file.write(html)

save_list()