#!/usr/bin/env python3
"""
The script returns the list of school
having specific topic
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of school
    """
    return mongo_collection.find({"topic": topic})