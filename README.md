# REN Commentary Website

An automated content website focused on REN Gill music analysis, storytelling, and thematic exploration with ethical monetization.

## Theme/Voice
- Respectful, uplifting, insightful analysis of REN Gill's music
- Focus on storytelling, production techniques, and listener takeaways
- Original writing only with careful attention to copyright

## Site Structure
1. **Song Stories** - Narrative breakdowns of REN's tracks
2. **Themes & Psychology** - Meaning, growth, resilience in REN's work
3. **Production & Performance** - Instrumentation, vocal choices, technical aspects
4. **Listening Guides** - Best order, mood-based lists for REN's catalog
5. **Community & Culture** - Positive fan community, creativity inspired by REN
6. **Gear & Tools** - Ethical monetization through relevant products

## Automation Features
- Content generator script that creates 1 new post per run
- Automatic site index updates
- Sitemap.xml and RSS feed generation
- Topic queue system for planned content
- Daily scheduled content generation

## Monetization Strategy
Ethical affiliate marketing focused on music-related products:
- Headphones and audio equipment
- Budget audio interfaces
- Microphones
- Notebooks/journals for songwriting
- Music theory books
- Vocal training resources
- REN-related merchandise (officially licensed when possible)

## Directory Structure
```
ren-commentary/
├── css/                 # Stylesheets
├── js/                  # JavaScript files
├── posts/               # Generated content organized by category
├── pages/               # Static pages
├── templates/           # HTML templates for generation
├── content_generator.py # Main content generation script
├── topic_queue.txt      # Queue of topics to cover
├── deploy.sh           # Deployment script
├── README.md           # This file
└── _build/             # Generated site ready for deployment
```

## Content Rules Implemented
- No full lyrics or large lyric excerpts (0-10 words max when necessary)
- Paraphrasing and analysis preferred over direct quotes
- Each post includes: title, slug, meta description, hook intro, 3-7 subheads, bullet summary, listener takeaway, and related posts
- Sources section with links and dates when referencing facts