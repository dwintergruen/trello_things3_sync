import re

## todo: enum for list locations, map names to the enum in extending classes

# See: https://developer.apple.com/library/Mac/DOCUMENTATION/Cocoa/Conceptual/ScriptingBridgeConcepts/AboutScriptingBridge/AboutScriptingBridge.html
status = {'Open': 1952737647, 'Completed': 1952736109, 'Cancelled': 1952736108}

def getStatusString(id):
    """Return the equivalent string"""
    for key, value in status.iteritems():
        if value == id:
            return key

    return ''

class Task(object):
    """Represent a task"""

    def __init__(self):
        self.id = ''
        self.name = ''
        self.description = ''
        self.status = ''
        self.dueDate = None
        self.lastModifiedDate = None
        self.notes = None

        self.main_attributes = ('name', 'description', 'status', 'dueDate', 'lastModifiedDate', 'notes')

    def modified_later_than(self, task):
        if self.lastModifiedDate == None:
            return False
        elif task.lastModifiedDate ==None:
            return True
        else:
            return self.lastModifiedDate > task.lastModifiedDate

    def set_attributes(self, task):
        '''sets most of the attributes of this task from another task (besides id)'''

        for attr_name in self.main_attributes:
            self.__setattr__(attr_name, task.__getattribute__(attr_name))

        if self.dueDate == task.dueDate:
            print "Due date set successfully"

