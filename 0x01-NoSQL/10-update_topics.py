#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
