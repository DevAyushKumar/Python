'''Static meathods:
Static meathod in Python are meathods that belong to a class rather than instance of the class rather than an instance of the class. They are defined using the @staticmeathod decorator and do not have access to the instance of the class (i.e, self). They are called on the class itself, not on an instance of the class. Static meathods are often used to create utility functions that don't need access to instance data.'''
class math:
    @staticmethod
    def add(a,b):
        return a+b
result = math.add(1,2)
print(result)
'''In this example, the add meathod is a static meathod of the Math class. It takes two parameters a and b and returns their sum. The meathod can be called on the class itself, without the need to create an instance of class. '''
