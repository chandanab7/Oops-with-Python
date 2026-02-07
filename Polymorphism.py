#Polymorphism is the ability of an object to take on many forms.
#1.method overriding: same method name with same parameters in different classes 

#syntax

# class ClassName:
#     def method1():
#         # implementation code
# class classn(ClassName):
#     def method1():
#         # implementation code
# object=class()
# object.method1() #this will call the method1 of classn, not ClassName, because of method overriding.
   


""""class media_player:
    def play(self):
        print("Playing file")
class audio_player(media_player):
    def play(self):
        print("Playing audio file")
class video_player(media_player):
    def play(self):
        print("Playing video file")

ap=audio_player() #this will call the play method of audio_player, not media_player, because of method overriding.
ap.play()
vp=video_player() #it is depends on the object that is calling the method, not the reference type. This is called dynamic method dispatch.
vp.play()
"""



#2.method overloading: same method name with different parameters in the same class
# python does not support method overloading by default, 
#but we can achieve it using default arguments or variable-length arguments.

class A:
    def func(self,a,b):
        print(a+b)
    
    def func(self,c,d): #this will override the previous fun1 method, because of method overloading.
        print(c*d)

object=A()
object.func(2,3) #this will call the second func method, not the first


#the last defined method will be called, because of method overloading.
