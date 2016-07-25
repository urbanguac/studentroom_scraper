import sys, os
from lxml import html
import requests
import unicodedata

#url = "http://www.thestudentroom.co.uk/showthread.php?t=2426280"
url = "http://www.thestudentroom.co.uk/showthread.php?t=1760892"
related = []
for page_number in range(1,343):
    print("[+] Requesting page "+str(page_number)+"...",end="")
    page = requests.get(url+"&page="+str(page_number))
    tree = html.fromstring(page.content)
    posts = tree.xpath('//blockquote[@class="postcontent restore"]')
    print(" iterating "+str(len(posts))+" posts...",end="")
#    print(posts[0].text_content())
    post_count = 0
    for post in posts:
        if "SAT" in post.text_content() or " AP" in post.text_content() or " ACT" in post.text_content() or " US" in post.text_content() or "america" in post.text_content() or "USA" in post or "America" in post.text_content() or "United States" in post.text_content() or "united states" in post.text_content():
            related.append(post.text_content())
            post_count = post_count + 1
    print(" found "+str(post_count)+" relevant posts.")
print("\n\n[+] Found "+str(len(related))+" total relevant posts.")
f = open("search_results.html",'w')
body = "<html><body>"
for post in related:
    body = body + post + "<br /><br /><div style='width:100%;height:15px;background-color:blue;color:blue;'></div>"
body = body + "</body></html>"
f.write(body.encode('ascii','ignore').decode(sys.stdout.encoding))
f.close()