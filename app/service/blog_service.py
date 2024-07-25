import os
import secrets
from pymongo import MongoClient
from bson import ObjectId, json_util
from flask import current_app as app

class BlogService:

    def __init__(self):
        # initialize the database connection and store it in an instance variable
        client = MongoClient(os.getenv('DATABASE_URI'))

        # Access specific db
        self.db = client.get_database('blog')

        self.users_collection = self.db['users']



    def get_all(self):
        # Fetch all blog posts from blogs collection
        return list(self.db.blogs.find({}))
    


    def get_by_id(self, blog_id):
        # Fetch a single blog post by using its id
        result = self.db.blogs.find_one({"_id": ObjectId(blog_id)})

        if result:
            result['_id'] = str(result['_id'])
            return result
        else:
            return None
        
    

    def get_latest_blog(self):
        # Fetch the latest blog post:
        # 1. `find()`: Retrieve all documents from the 'blogs' collection without any filtering.
        # 2. `sort('created_at', -1)`: Sort these documents by the 'created_at' field in descending order.
        #    This arranges the blog posts from the most recent to the oldest.
        # 3. `limit(1)`: Limit the query result to only the top document from the sorted list, 
        #    which is the most recent blog post due to the sorting order.
        # 4. `next()`: Retrieve this single, most recent blog post from the cursor. 
        #    Using `next()` directly accesses the first (and only) document in our limited result set.
        # Note: This method assumes there is at least one blog post in the collection. 
        # It may raise `StopIteration` if the collection is empty, which should be handled appropriately.
        try:
            return self.db.blogs.find().sort('date', -1).limit(1).next()
        except StopIteration:
            # Return None or handle case where there are no blog posts
            return None



    def save_to_db(self, blog):
        # Add a new blog post into db
        result = self.db.blogs.insert_one(blog.to_dict())
        return str(result.inserted_id)



    def update_blog(self, blog_id, updated_blog):
        # Update a blog post through its blog id
        result = self.db.blogs.update_one({"_id": ObjectId(blog_id)}, {"$set": updated_blog})
        if result.matched_count:
            return True
        return False
    
    

    def delete_blog(self, blog_id):
        # Delete a blog post via blog id
        result = self.db.blogs.delete_one({"_id": ObjectId(blog_id)})
        if result.deleted_count:
            return True
        return False
    

    def save_user(self, user):
        # Add new user into db
        result = self.db.users.insert_one(user.to_dict())
        return str(result.inserted_id)
    

    
    def create_verification_token():
        """ Generate a secure random token for email verification """
        return secrets.token_urlsafe(16)