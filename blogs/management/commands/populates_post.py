from blogs.models import post,Category
from django.core.management.base import BaseCommand
import random





class Command(BaseCommand):
    help = 'Populates the database with sample blog posts'

    def handle(self, *args, **kwargs):

        # Clear existing data
        post.objects.all().delete()  
        
        titles = [

    "Inkspire",
    "EchoWrite",
    "WordNest",
    "Blogify",
    "MindCanvas",
    "ScriptSphere",
    "ThoughtFlow",
    "PulsePress",
    "LogVerse",
    "WriteWave",
    "NoteForge",
    "IdeaBloom",
    "ChronicleHub",
    "BlogVault",
    "StoryStack",
    "WordCraft",
    "InsightInk",
    "MetaMuse",
    "JournalJet",
    "ThoughtTrail"
]
        blog_contents = [
            "Inkspire is a creative hub where writers share inspiring stories, poetry, and reflections.",
            "EchoWrite amplifies voices by publishing thought-provoking articles and personal experiences.",
            "WordNest is a cozy space for bloggers to nurture and grow their ideas into words.",
            "Blogify offers simple, sleek posts on lifestyle, tech, and everyday hacks.",
            "MindCanvas paints vivid ideas through essays, opinion pieces, and creative writing.",
            "ScriptSphere explores storytelling, scripts, and narrative techniques across genres.",
            "ThoughtFlow captures seamless streams of ideas on productivity, growth, and innovation.",
            "PulsePress delivers trending topics, cultural insights, and the heartbeat of modern life.",
            "LogVerse is a universe of blogs covering tech, travel, and personal journeys.",
            "WriteWave rides the wave of creativity with fresh perspectives and engaging posts.",
            "NoteForge forges powerful notes, guides, and tutorials for learners and creators.",
            "IdeaBloom lets thoughts blossom into articles on self-growth and creative living.",
            "ChronicleHub collects personal chronicles, memoirs, and historical reflections.",
            "BlogVault secures your stories with timeless posts on wisdom and experiences.",
            "StoryStack stacks narratives from fiction, non-fiction, and everyday storytelling.",
            "WordCraft crafts words into elegant essays, poetry, and literary explorations.",
            "InsightInk inks deep insights on technology, psychology, and modern challenges.",
            "MetaMuse muses on philosophy, meta-thinking, and creative exploration.",
            "JournalJet publishes fast, dynamic blogs on travel, lifestyle, and productivity.",
            "ThoughtTrail leaves a trail of ideas on innovation, culture, and personal growth."
        ]
        image_urls = [
            "https://picsum.photos/seed/1/800/400",
            "https://picsum.photos/seed/2/800/400",
            "https://picsum.photos/seed/3/800/400",
            "https://picsum.photos/seed/4/800/400",
            "https://picsum.photos/seed/5/800/400",
            "https://picsum.photos/seed/6/800/400",
            "https://picsum.photos/seed/7/800/400",
            "https://picsum.photos/seed/8/800/400",
            "https://picsum.photos/seed/9/800/400",
            "https://picsum.photos/seed/10/800/400",
            "https://picsum.photos/seed/11/800/400",
            "https://picsum.photos/seed/12/800/400",
            "https://picsum.photos/seed/13/800/400",
            "https://picsum.photos/seed/14/800/400",
            "https://picsum.photos/seed/15/800/400",
            "https://picsum.photos/seed/16/800/400",
            "https://picsum.photos/seed/17/800/400",
            "https://picsum.photos/seed/18/800/400",
            "https://picsum.photos/seed/19/800/400",
            "https://picsum.photos/seed/20/800/400"
        ]

        categories=Category.objects.all()

        for title,content,img_url in zip(titles, blog_contents, image_urls):
            # getteing random category
            category=random.choice(categories)
            
            # Assigning all posts to the first category for simplicity
            post.objects.create(title=title,content=content,img_url=img_url,category=category)  

        return self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample blog posts'))