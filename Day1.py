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
   # Add a comment
    def add_comment(self, comment):
        self.comment.append(comment)
    def display_comment(self):
        print("Comments on the reel are:")
        for c in self.comment:
            print(c)
    def delete_comment(self, comment):
        if comment in self.comment:
            self.comment.remove(comment)
            print("Comment deleted successfully.")

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

# objects
reel1 = Instagram("Dancing", "Chandana", "Bangalore")
reel2 = Instagram("Finance Conference", "Ananya", "mysuru")

# Operations on reel1
reel1.liked() #1
reel1.liked()#2
reel1.disliked()#1


# Operations on reel2
reel2.liked() #1

# reel1 calling methods
reel1.display_title()
reel1.display_creator()
reel1.display_location()
reel1.display_likes()
#
reel1.display_comment()

#reel2
reel2.display_title()
reel2.display_creator()
reel2.display_location()
reel2.display_likes()
reel1.liked()#2
reel1.display_likes()
reel2.add_comment("nice session")

# Display memory addresses using id() function
print(id(reel1))
print(id(reel2))


