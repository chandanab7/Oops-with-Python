# Class for Instagram Reel
class Instagram:
    
    # Constructor method
    def __init__(self,title,creator_name,location):
        self.title = title 
        self.comment = [] 
        self.creator_name = creator_name
        self.location = location
        self.likes = 0

    # Dis reel title
    def display_title(self):
        print("The title of the reel is:", self.title)


# the task is......to add comment, creator name,location....
 

    # Display creator name
    def display_creator(self):
        print("Creator of the reel is:", self.creator_name)

    # Display location
    def display_location(self):
        print("Location of the reel is:", self.location)

    # Display likes count
    def display_likes(self):
        print("The likes of the reel is:", self.likes)

    # Add like
    def liked(self):
        self.likes += 1

    # no negative likes
    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

  # Add a comment
    def display_comment(self):
        if len(self.comment)==0:
            print("No comments on the reel.")
        else:    
            print("Comments on the reel are:")
            for c in self.comment:
                print("-",c)

    def add_comment(self, comment): 
        # to take the comment as input  like parameter 
        #---reel1.add_comment("Loved it")
        self.comment.append(comment)  

# deleting the last comment using pop() method 

    def delete_last_comment(self):
        if self.comment:
            removed_comment = self.comment.pop()
            print(f"Deleted the last comment: '{removed_comment}'")

# objects
reel1 = Instagram("Dancing", "Chandana", "Bangalore")

reel1.display_comment()
reel1.add_comment("good dance moves")
reel1.add_comment("Loved it")
reel1.add_comment("Awesome performance")
reel1.add_comment("Great video")

reel1.delete_last_comment()
reel1.display_comment()