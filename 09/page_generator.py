import json

# basic template for generate:
a_element = """
            <a href="{url}">
                <h2>{title}</h2>
                <img src="{img}" alt="{title}">
            </a>
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