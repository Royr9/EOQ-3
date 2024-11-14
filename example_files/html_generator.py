items = ["python", "lua", "php", "basic", "html", "fortran", "actionscript", "brainfck"]


def page_template(list_items):
    return """<!DOCT YPE html>
<html>
<head>
    <title>My favorite programming languages</title>
    <script>
        // This bit of javascript auto-reloads the page every few seconds
        window.addEventListener("beforeunload", function() {
            localStorage.setItem("scrollPosition", window.scrollY);
        });
        window.addEventListener("load", function() {
            const scrollPosition = localStorage.getItem("scrollPosition");
            if (scrollPosition) {
                window.scrollTo(0, parseInt(scrollPosition, 10));
            }
        });
        setTimeout(function() {
            location.reload();
        }, 3000);
    </script>
</head>
<body>
    <h1>Best languages:</h1>
    <ul>""" + list_items + """
    </ul>
</body>
</html>"""


def item_template(item):
    return f"        <li>{item}</li>"


items_html = []
for item in items:
    items_html.append(item_template(item))

page_html = page_template("\n".join(items_html))

with open("index.html", "w") as file:
    file.write(page_html)
