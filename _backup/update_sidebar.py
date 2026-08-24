import os
import re
from bs4 import BeautifulSoup

def generate_sidebar_html():
    base_dir = r'c:\Users\shota\hookx-dev\amazon-afi'
    index_path = os.path.join(base_dir, 'index.html')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    grid = soup.find('div', class_='article-grid')
    cards = grid.find_all('article', class_='card')
    
    # 1. Count categories
    categories = {}
    
    # 2. Extract recent 3 posts
    recent_posts = []
    
    for i, card in enumerate(cards):
        cat = card.find('span', class_='category-label').text.strip()
        categories[cat] = categories.get(cat, 0) + 1
        
        if i < 3:
            link = card.find('a', class_='card-link')
            href = link.get('href')
            img_src = card.find('img').get('src')
            img_alt = card.find('img').get('alt')
            title = card.find('h2', class_='card-title').text.strip()
            
            recent_posts.append({
                'href': href,
                'img_src': img_src,
                'img_alt': img_alt,
                'title': title
            })
            
    # Sort categories by count descending
    sorted_cats = sorted(categories.items(), key=lambda item: item[1], reverse=True)
    
    # Build HTML
    cat_html = ""
    for cat, count in sorted_cats:
        cat_html += f'                    <li><a href="#">{cat} <span class="category-count">{count}</span></a></li>\n'
        
    recent_html = ""
    for post in recent_posts:
        recent_html += f"""                <div class="recent-post-item">
                    <div class="recent-post-img">
                        <img src="{post['img_src']}" alt="{post['img_alt']}">
                    </div>
                    <div class="recent-post-title">
                        <a href="{post['href']}">{post['title']}</a>
                    </div>
                </div>\n"""

    sidebar_html = f"""        <aside class="sidebar">
            <div class="widget widget-category">
                <h3 class="widget-title">カテゴリー</h3>
                <ul>
{cat_html}                </ul>
            </div>

            <div class="widget widget-recent-posts">
                <h3 class="widget-title">新着記事</h3>
                
{recent_html}            </div>
        </aside>"""
        
    return sidebar_html

def update_files():
    sidebar_html = generate_sidebar_html()
    base_dir = r'c:\Users\shota\hookx-dev\amazon-afi'
    
    for f in os.listdir(base_dir):
        if not f.endswith('.html'):
            continue
        
        filepath = os.path.join(base_dir, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regex to find <aside class="sidebar">...</aside>
        pattern = r'<aside class="sidebar">.*?</aside>'
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, sidebar_html, content, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}")

if __name__ == '__main__':
    update_files()
