#!/usr/bin/env python3
"""
REN Commentary Content Generator
Creates respectful, insightful analyses of REN Gill's music with ethical monetization
"""

import os
import random
import re
from datetime import datetime
from urllib.parse import quote

# Content categories
CATEGORIES = {
    "song-stories": {
        "name": "Song Stories",
        "description": "Narrative breakdowns of REN's tracks"
    },
    "themes-meaning": {
        "name": "Themes & Meaning",
        "description": "Exploring meaning, growth, and resilience in REN's work"
    },
    "production-performance": {
        "name": "Production & Performance",
        "description": "Instrumentation, vocal choices, and technical aspects"
    },
    "listening-guides": {
        "name": "Listening Guides",
        "description": "Best order, mood-based lists for REN's catalog"
    },
    "community-creativity": {
        "name": "Community & Creativity",
        "description": "Positive fan community and creativity inspired by REN"
    },
    "gear-tools": {
        "name": "Gear & Tools",
        "description": "Ethical monetization through relevant products"
    }
}

# Affiliate product categories
AFFILIATE_PRODUCTS = {
    "audio-equipment": [
        {"name": "High-Quality Headphones", "description": "Best for appreciating REN's nuanced production", "url": "#"},
        {"name": "Studio Monitors", "description": "Accurate sound reproduction for music analysis", "url": "#"}
    ],
    "music-tools": [
        {"name": "Audio Interface", "description": "Essential for music creation", "url": "#"},
        {"name": "Dynamic Microphone", "description": "Great for recording vocals", "url": "#"}
    ],
    "learning-resources": [
        {"name": "Music Theory Book", "description": "Understanding the fundamentals", "url": "#"},
        {"name": "Songwriter's Journal", "description": "Capture your musical ideas", "url": "#"}
    ],
    "vocal-training": [
        {"name": "Vocal Training Course", "description": "Improve your singing abilities", "url": "#"},
        {"name": "Breathing Exercise Guide", "description": "Techniques for better vocal control", "url": "#"}
    ]
}

# Article templates
ARTICLE_TEMPLATES = [
    {
        "title": "The Storytelling Mastery in REN's '{song}': A Narrative Breakdown",
        "category": "song-stories",
        "hook": "REN has a unique ability to weave complex narratives into his music, creating vivid scenes that resonate with listeners. In this track, he demonstrates his exceptional storytelling skills through carefully crafted imagery and emotional depth.",
        "analysis": "This track showcases REN's evolution as a storyteller. The narrative structure moves seamlessly between different perspectives, creating a cinematic experience that draws the listener into the story. His word choices are deliberate and impactful, painting vivid imagery while maintaining the emotional core of the piece.",
        "themes": "The central themes of this track include resilience, personal growth, and the complexity of human relationships. REN explores these concepts with nuance, avoiding simple interpretations in favor of more complex emotional landscapes.",
        "production_notes": "From a production standpoint, this track features intricate layering that supports the narrative without overwhelming it. The instrumental choices enhance the emotional journey, with subtle shifts that mirror the story's progression.",
        "takeaway": "Listeners can appreciate this track on multiple levels - as a compelling story, as an example of technical skill, and as an emotional journey. It represents REN's growth as an artist and his ability to connect with audiences through authentic expression.",
        "actions": [
            "Listen to this track with attention to the narrative arc",
            "Compare the production choices to REN's earlier work",
            "Explore similar storytelling techniques in other artists",
            "Try writing your own story using similar structural elements",
            "Share your interpretation with the REN community",
            "Practice active listening to appreciate the nuances"
        ],
        "sources": [
            {"title": "REN Discography Analysis", "url": "https://example.com", "date": "2024-01-15"},
            {"title": "Hip-Hop Storytelling Techniques", "url": "https://example.com", "date": "2024-02-01"}
        ]
    },
    {
        "title": "Exploring Resilience in REN's Musical Journey: Growth Through Adversity",
        "category": "themes-meaning",
        "hook": "Throughout his discography, REN consistently returns to themes of resilience and personal growth. His music reflects a deep understanding of adversity and the strength required to overcome it, offering listeners both validation and inspiration.",
        "analysis": "REN's exploration of resilience goes beyond simple motivational messaging. He presents struggle as an integral part of the human experience, neither glorifying pain nor minimizing its impact. Instead, he offers a balanced perspective that acknowledges difficulty while emphasizing the potential for growth.",
        "themes": "Key themes include the transformative power of struggle, the importance of self-awareness, and the role of community in healing. REN approaches these topics with sensitivity and authenticity, drawing from personal experience while remaining accessible to diverse audiences.",
        "production_notes": "The musical arrangements in these thematic pieces often feature subtle complexity that mirrors the emotional content. REN uses production elements to reinforce the themes, with instrumental choices that evoke both struggle and hope.",
        "takeaway": "REN's treatment of resilience offers a mature perspective on personal growth that avoids oversimplification. His work demonstrates that acknowledging struggle is not defeatist but rather an essential step toward meaningful progress.",
        "actions": [
            "Reflect on your own experiences with resilience",
            "Identify the growth that emerged from your challenges",
            "Explore how music can be a tool for emotional processing",
            "Connect with others who share similar experiences",
            "Practice self-compassion during difficult times",
            "Seek out music that validates your emotional journey"
        ],
        "sources": [
            {"title": "Psychology of Resilience", "url": "https://example.com", "date": "2024-01-20"},
            {"title": "Music Therapy Research", "url": "https://example.com", "date": "2024-02-05"}
        ]
    },
    {
        "title": "The Technical Craft of REN: Vocal Techniques and Production Choices",
        "category": "production-performance",
        "hook": "REN's technical abilities often take a backseat to his emotional resonance, but his mastery of vocal techniques and understanding of production are fundamental to his success. Examining these elements reveals the craft behind the artistry.",
        "analysis": "REN's vocal delivery combines technical precision with emotional authenticity. His rhythm and flow adapt to the needs of each song, sometimes prioritizing melodic sensibility and other times emphasizing rhythmic complexity. This flexibility demonstrates a sophisticated understanding of how vocal technique serves the overall artistic vision.",
        "themes": "While focusing on technical elements, the underlying themes of REN's work remain consistent. His technical choices always serve the emotional and narrative content, never existing purely for show. This integration of technique and artistry sets him apart in contemporary music.",
        "production_notes": "The production in REN's tracks consistently supports his vocal performance without overshadowing it. Instrumental choices are made with attention to how they complement his voice, creating a cohesive sonic landscape. The mixing and mastering preserve the intimate feel of his performances while giving them appropriate presence.",
        "takeaway": "REN's technical proficiency enhances rather than overshadows his artistic message. His approach demonstrates how craft and creativity can work together to create more powerful artistic statements.",
        "actions": [
            "Analyze REN's flow patterns in different tracks",
            "Study how production elements support vocal delivery",
            "Practice vocal techniques inspired by REN's approach",
            "Experiment with production styles that complement your voice",
            "Focus on how technical skills serve artistic vision",
            "Develop your own signature vocal style"
        ],
        "sources": [
            {"title": "Hip-Hop Vocal Techniques", "url": "https://example.com", "date": "2024-01-25"},
            {"title": "Music Production Analysis", "url": "https://example.com", "date": "2024-02-10"}
        ]
    }
]

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def generate_article(topic=None):
    """Generate a complete article based on templates"""
    if topic:
        # Use provided topic if available
        template = topic
    else:
        # Select random template
        template = random.choice(ARTICLE_TEMPLATES)
    
    # Fill in template variables if needed
    if '{song}' in template['title']:
        songs = ['Losing It', 'Stand Up', 'Just Right', 'Change', 'Ghost']
        song = random.choice(songs)
        title = template['title'].format(song=song)
    else:
        title = template['title']
    
    category_key = template['category']
    category_info = CATEGORIES[category_key]
    
    # Generate slug
    slug = slugify(title)
    
    # Generate meta description
    meta_description = f"{template['hook'][:100]}... Respectful analysis of {category_info['description'].lower()}"
    
    # Select random affiliate products for this post
    affiliate_category = random.choice(list(AFFILIATE_PRODUCTS.keys()))
    selected_affiliates = random.sample(AFFILIATE_PRODUCTS[affiliate_category], min(2, len(AFFILIATE_PRODUCTS[affiliate_category])))
    
    article = {
        "title": title,
        "slug": slug,
        "meta_description": meta_description,
        "date": datetime.now().strftime("%B %d, %Y"),
        "category": category_key,
        "category_name": category_info["name"],
        "hook": template["hook"],
        "analysis": template["analysis"],
        "themes": template["themes"],
        "production_notes": template["production_notes"],
        "takeaway": template["takeaway"],
        "actions": template["actions"],
        "sources": template["sources"],
        "affiliate_products": selected_affiliates,
        "related_posts": []  # Will be populated later
    }
    
    return article

def save_article_to_file(article, base_dir="posts"):
    """Save the generated article as an HTML file"""
    os.makedirs(os.path.join(base_dir, article['category']), exist_ok=True)
    
    # Read the post template
    with open('templates/post.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Format the content
    content_html = f"""
    <article class="content-section">
        <h1>{article['title']}</h1>
        <div class="date">{article['date']}</div>
        <span class="category-tag">{article['category_name']}</span>
        
        <div class="hook">
            {article['hook']}
        </div>
        
        <h2 class="section-title">Thematic Analysis</h2>
        <div class="thematic-analysis">
            <p>{article['analysis']}</p>
        </div>
        
        <h2 class="section-title">Thematic Exploration</h2>
        <div class="storytelling-insights">
            <p>{article['themes']}</p>
        </div>
        
        <h2 class="section-title">Production & Performance Notes</h2>
        <div class="production-breakdown">
            <p>{article['production_notes']}</p>
        </div>
        
        <h2 class="section-title">Listener Takeaway</h2>
        <div class="listener-takeaway">
            <p>{article['takeaway']}</p>
            <h3>What You Can Explore Further:</h3>
            <ul class="actions-list">
                {''.join([f'<li>{action}</li>' for action in article['actions']])}
            </ul>
        </div>
        
        <div class="affiliate-disclaimer">
            <strong>Affiliate Notice:</strong> This post contains links to products that can enhance your music appreciation or creation experience. Purchases through these links may earn a small commission that supports our continued analysis.
            <div style="margin-top: 1rem;">
                <h3>Products That Can Enhance Your Experience:</h3>
                {''.join([f'<p><a href="{prod["url"]}" target="_blank">{prod["name"]}</a>: {prod["description"]}</p>' for prod in article['affiliate_products']])}
            </div>
        </div>
        
        <h2 class="section-title">Sources & Further Reading</h2>
        <div class="sources">
            <ul>
                {''.join([f'<li><a href="{source["url"]}">{source["title"]}</a> ({source["date"]})</li>' for source in article['sources']])}
            </ul>
        </div>
        
        <div class="related-posts">
            <h3>Related Analyses</h3>
            <p>Explore more articles in the <a href="/category/{article['category']}/">{article['category_name']}</a> category.</p>
        </div>
    </article>
    """
    
    # Replace template variables
    html_content = template.replace('{{TITLE}}', article['title'])
    html_content = html_content.replace('{{META_DESCRIPTION}}', article['meta_description'])
    html_content = html_content.replace('{{CONTENT}}', content_html)
    
    # Save the article
    filename = os.path.join(base_dir, article['category'], f"{article['slug']}.html")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filename

def update_index_page(new_post=None):
    """Update the index page with the latest posts"""
    # Read index template
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Get list of recent posts
    post_links = []
    
    for category in CATEGORIES:
        category_dir = os.path.join('posts', category)
        if os.path.exists(category_dir):
            posts = sorted(os.listdir(category_dir), reverse=True)[:5]  # Get 5 most recent from each category
            for post in posts[:2]:  # Take 2 from each category
                if post.endswith('.html'):
                    slug = post[:-5]  # Remove .html
                    # Need to extract title from the file
                    post_path = os.path.join(category_dir, post)
                    with open(post_path, 'r', encoding='utf-8') as pf:
                        content = pf.read()
                        # Extract title from the content
                        import re
                        title_match = re.search(r'<h1>(.*?)</h1>', content)
                        title = title_match.group(1) if title_match else slug.replace('-', ' ').title()
                    
                    post_links.append({
                        'title': title,
                        'url': f"/{category}/{slug}/",
                        'date': '2024-02-01',  # Placeholder - would need to extract from file
                        'category': CATEGORIES[category]['name']
                    })
    
    # Limit to 6 most recent posts
    post_links = post_links[:6]
    
    # Create HTML for post grid
    posts_html = ""
    for post in post_links:
        posts_html += f"""
        <div class="post-card">
            <span class="category-tag">{post['category']}</span>
            <h3><a href="{post['url']}">{post['title']}</a></h3>
            <div class="date">{post['date']}</div>
            <p>Respectful analysis and insights into REN's artistry...</p>
        </div>
        """
    
    # Replace in template
    html_content = template.replace('{{POSTS}}', posts_html)
    
    # Save index page
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_sitemap():
    """Generate sitemap.xml for SEO"""
    urls = [
        {"loc": "https://example.com/", "lastmod": datetime.now().strftime("%Y-%m-%d"), "changefreq": "daily", "priority": "1.0"},
        {"loc": "https://example.com/affiliate-disclosure/", "lastmod": datetime.now().strftime("%Y-%m-%d"), "changefreq": "monthly", "priority": "0.8"},
    ]
    
    # Add category pages
    for cat_key, cat_info in CATEGORIES.items():
        urls.append({
            "loc": f"https://example.com/category/{cat_key}/",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "weekly",
            "priority": "0.9"
        })
    
    # Add posts
    for category in CATEGORIES:
        category_dir = os.path.join('posts', category)
        if os.path.exists(category_dir):
            posts = os.listdir(category_dir)
            for post in posts:
                if post.endswith('.html'):
                    slug = post[:-5]
                    urls.append({
                        "loc": f"https://example.com/{category}/{slug}/",
                        "lastmod": datetime.now().strftime("%Y-%m-%d"),
                        "changefreq": "monthly",
                        "priority": "0.7"
                    })
    
    # Create sitemap XML
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url in urls:
        sitemap_xml += f'  <url>\n'
        sitemap_xml += f'    <loc>{url["loc"]}</loc>\n'
        sitemap_xml += f'    <lastmod>{url["lastmod"]}</lastmod>\n'
        sitemap_xml += f'    <changefreq>{url["changefreq"]}</changefreq>\n'
        sitemap_xml += f'    <priority>{url["priority"]}</priority>\n'
        sitemap_xml += f'  </url>\n'
    
    sitemap_xml += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)

def generate_rss_feed():
    """Generate RSS feed for the site"""
    # This would typically pull from actual posts, but for now we'll create a template
    rss_content = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>REN Commentary</title>
  <link>https://example.com</link>
  <description>Respectful analysis of REN Gill's music and artistry</description>
  <language>en-us</language>
  <pubDate>{pub_date}</pubDate>
  <lastBuildDate>{build_date}</lastBuildDate>
  <generator>Custom RSS Generator</generator>
</channel>
</rss>'''.format(
        pub_date=datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z"),
        build_date=datetime.now().strftime("%a, %d %b Y %H:%M:%S %z")
    )
    
    with open('feed.rss', 'w', encoding='utf-8') as f:
        f.write(rss_content)

def main():
    """Generate a new article and update the site"""
    print("Generating new REN commentary article...")
    
    # Generate a new article
    article = generate_article()
    filename = save_article_to_file(article)
    
    print(f"Generated article: {filename}")
    
    # Update the index page
    update_index_page(article)
    print("Updated index page with new article")
    
    # Generate sitemap
    generate_sitemap()
    print("Generated sitemap.xml")
    
    # Generate RSS feed
    generate_rss_feed()
    print("Generated RSS feed")
    
    print("\nSite generation complete!")
    print("Files created:")
    print(f"- Article: {filename}")
    print("- Index page: index.html")
    print("- Sitemap: sitemap.xml")
    print("- RSS feed: feed.rss")

if __name__ == "__main__":
    main()