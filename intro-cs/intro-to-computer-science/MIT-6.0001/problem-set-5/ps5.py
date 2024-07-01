# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: eurodollarclub
# Collaborators: None
# Time: 10+ hours

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import re
import pytz
import sys

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        pubdate = translate_html(entry.published)
        description = translate_html(entry.description)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        print(newsStory.description, "newsStory")
        ret.append(newsStory)
    return ret


class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


class Trigger(object):
    def evaluate(self, story):
        """
        Abstract base class
        Returns: True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, text):
        """
        Match the self.phrase with text;
        ex1: self.phrase = 'microsoft office' text = 'microsoft!%@# office is very good' -> True
        ex2: self.phrase = 'microsoft office' text = 'microsoft's!%@# office is very good' -> False
        return: boolean
        """
        text = text.lower()
        splitted_phrase = self.phrase.split(" ")
        re_pattern = f"[\\s{string.punctuation}]"
        phrase = ""
        for i in range(len(splitted_phrase)):
            if len(splitted_phrase) - 1 == i:
                phrase += splitted_phrase[i].lower() + re_pattern + "*\\b"
            else:
                phrase += splitted_phrase[i].lower() + re_pattern + "+"
        if re.search(phrase, text):
            return True
        else:
            return False


class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())


class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())


class TimeTrigger(Trigger):
    """
    Initialize abstract sub class and parses EST timezone
    """

    def __init__(self, input):
        self.input = datetime.strptime(input, "%d %b %Y %H:%M:%S")


class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        return story.get_pubdate().replace(tzinfo=None) < self.input


class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        return story.get_pubdate().replace(tzinfo=None) > self.input


class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)


class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)


def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances and list of triggers
    Returns: a list of only the stories for which a trigger in triggerlist fires.

    goal: takes a list of triggers and a list of stories
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    strategy:
    stories a list of story instances, triggerList a list of trigger instances
    trigger per stories
    """
    f_stories = list()
    for trigger in triggerlist:
        for story in stories:
            if trigger.evaluate(story):
                f_stories.append(story)
    return f_stories


def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file
    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    triggers_set = {
        "TITLE": lambda x: TitleTrigger(x),
        "DESCRIPTION": lambda x: DescriptionTrigger(x),
        "AFTER": lambda x: AfterTrigger(x),
        "BEFORE": lambda x: BeforeTrigger(x),
        "AND": lambda x, y: AndTrigger(x, y),
        "OR": lambda x, y: OrTrigger(x, y),
        "NOT": lambda x: NotTrigger(x),
    }
    triggers_list = list()
    triggers_dict = dict()
    trigger_types = ["TITLE", "DESCRIPTION", "AFTER", "BEFORE", "NOT"]

    trigger_file = open(filename, "r")
    lines = list()
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith("//")):
            lines.append(line)

    for i in lines:
        line_list = i.split(",")
        for j in range(1, len(line_list)):
            print(j)
            if line_list[j] in trigger_types:
                triggers_dict[f"{line_list[j - 1]}"] = triggers_set[f"{line_list[j]}"](
                    f"{line_list[j + 1]}"
                )
                break
            else:
                triggers_dict[f"{line_list[j]}"] = triggers_set[f"{line_list[j]}"](
                    triggers_dict[f"{line_list[j+1]}"],
                    triggers_dict[f"{line_list[j+2]}"],
                )
                break
    
    for k,v in triggers_dict.items():
        triggers_list.append(v)
    
    return triggers_list


SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        trigger_list = read_trigger_config('triggers.txt')
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify="center")
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(
                    END,
                    "\n---------------------------------------------------------------\n",
                    "title",
                )
                cont.insert(END, newstory.get_description())
                cont.insert(
                    END,
                    "\n*********************************************************************\n",
                    "title",
                )
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=" ")
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")
            # Get stories from Yahoo's Top Stories RSS news feed
            """ stories.extend(process("http://news.yahoo.com/rss/topstories")) """
            stories = filter_stories(stories, trigger_list)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)
                  
    except Exception as e:
        print(e)

if __name__ == "__main__":
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
