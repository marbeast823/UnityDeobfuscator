# noinspection PyUnresolvedReferences
import copy
# noinspection PyUnresolvedReferences
from typing import *
import string

def removeattributes(thisobject, toremovenewlines=False):
    """
    Function has been removed
    """
    raise NotImplementedError("removeattributes function has been removed.\
     Attributes are removed from the whole dumpcs, so the call to removeattributes can be deleted.")


def removewhitespace(fullstr, beginning=True, end=True, allwhitespace=False):
    """
    Function has been removed
    """
    raise NotImplementedError("removewhitespace function has been removed.\
         To trim whitespace, use the trim function. To remove all whitespace, use the removeallwhitespace funnction.")

def getobjects(**kwargs):
    """
    Function has been removed
    """
    raise NotImplementedError("getobjects function has been removed.\
         To get objects, use dumpcs_getobjects directly on dumpcs."

def getfullobjects(**kwargs):
        """
        Function has been removed
        """
        raise NotImplementedError("getfullobjects function has been removed.\
             To get objects, use dumpcs_getobjects directly on dumpcs."

def removesubstring(s: str, sub: str) -> str:
    #Done
    """
    Possible Improvements:

    Remove one substring from a string

    Example:
        String: "Removing Substrings"
        Sub:    "ing"
        Return: "Remov Substrs"

    Arguments:
        s: string to remove substring from
        sub: substring to remove from string

    Return:
        string with substring removed
    """
    return s.replace(sub, "")


def removesubstrings(s: str, subs: list[str]) -> str:
    #Done
    """
    Possible Improvements:

    Remove multiple substring from a string, in order of list

    Example:
        String: "Removing Substrings"
        Subs:    ["e","in","ing"]
        Return: "Rmovg Substrgs"

    Arguments:
        s: string to remove substrings from
        subs: list of substrings to remove from string

    Return:
        string with substrings removed
    """
    for sub in subs:
        s = removesubstring(s, sub)
    return s


def replacesubstring(s: str, sub: str, replace: str) -> str:
    #Done
    """
    Doc Not Done
    """
    return s.replace(sub, replace)


def replacesubstrings(s: str, subs: list[str], replace: str) -> str:
    #Done
    """
    Doc Not Done
    """
    for sub in subs:
        s = replacesubstring(s, sub, replace)
    return s


def removeallwhitespace(s: str) -> str:
    #Done, but maybe could be optimized
    #NOTE: Function is named removeallwhitespace because old function removewhitespace
    #was for trimming. Once all functions use trim instead, this function can be renamed
    #back to removewhitespace.
    """
    Possible Improvements:
        Make whitespace a constant instead of unpacking each time function is called

    Removes all whitespace from a string
    Does not just trim leading and trailing. For that, use the trim function.

    Example:
        String: "   Whitespace  will be      removed from
        this string"
        Return: "Whitespacewillberemovedfromthisstring"

    Arguments:
        s: string to remove whitespace from

    Return:
        string with whitespace removed
    """
    # Should have a constant instead of unpacking
    # string.whitespace each time
    _whitespace = [*string.whitespace]
    return removesubstrings(s, _whitespace)


def removeblanklines(s: str, toremovewhitespacelines=True) -> str:
    #Not Done
    """
    Possible Improvements:

    Removes all blank lines from a string

    Example:
        String: "
        blank
            lines will be

            removed from

            thisst
         ing"
        toremovewhitespacelines: true
        Return: "blank
            lines will be
            removed from
            thisst
         ing"

    Arguments:
        s: string to remove blank lines from
        toremovewhitespacelines: whether to remove lines with only whitespace (eg: "    ")

    Return:
        string with blank lines removed
    """
    if toremovewhitespacelines:
        raise NotImplementedError("removeblanklines with toremovewhitespacelines is not done")
    else:
        return replacesubstring(s, "\n\n", "\n")


def iswhitespace(s: str) -> bool:
    #Done
    """
    Possible Improvements:

    Detects if a string is all whitespace
    Works on strings with any length, including 0

    Example:
        String: "
             "
        Return: true

        String: "   hello world!
            hi"
        Return: false

    Arguments:
        s: string to check for whitespace

    Return:
        bool whether string is all whitespace
    """
    for letter in s:
        #Check whether each letter in the string is not whitespace
        if not(letter.isspace()):
            #Letter is not whitespace
            return False
    #All letters are whitespace
    return True


def trim(s: str, leading=True, trailing=True) -> str:
    """
    Possible Improvements:

    Trims whitespace from a string

    Example:
        String: "   hello world!
        "
        Leading: true
        Trailing: true
        Return: "hello world!"

    Arguments:
        s: string to trim whitespace from
        leading: whether to trim leading whitespace
        trailing: whether to trim trailing whitespace

    Return:
        string with trimmed whitespace
    """
    if leading and trailing:
        return s.strip()
    elif leading:
        return s.lstrip()
    elif trailing:
        return s.rstrip()
    else:
        return s


def getlines(s: str, toremoveblanklines: object = False, totrimlines: object = False) -> list[str]:
    # Done, but maybe could be optimized
    """
    Possible Improvements:
        1. Creating a new list is inefficient, modifying existing list would be ideal
        2. Directly using s.splitlines() instead of using lines variable may be faster, but sacrifices readability

    Splits a string into a list of lines

    Example:
        String: "a
                    b

                 c  "
        toremoveblanklines: true
        totrimlines: true
        Return: ["a","b","c"]

    Arguments:
        s: string to split into lines
        toremoveblanklines: whether to ignore blank lines
        totrimlines: whether to trim leading and trailing whitespace
        (only leadhing / only trailing whitespace is not supported)

    Return:
        list of the string's lines
    """
    lines = s.splitlines()
    newlines = []
    for line in lines:
        if totrimlines:
            line = trim(line, True, True)
        if not (iswhitespace(line) and toremoveblanklines):
            newlines.append(line)
    return newlines


def linestostring(lines: list[str]) -> str:
    #Done
    """
    Possible Improvements:

    joins a list of lines into a string

    Example:
        lines: ["a","","b","    ","cd",""]
        Return: "a

                 b

                 cd
                 "

    Arguments:
        lines: list of lines to join into a string

    Return:
        string containing all the lines concatenated with new line
    """
    return "\n".join(lines)


def dumpcs_isvalid(dumpcs: str) -> bool:
    #Not done
    """
    Bad detection, needs proper algorithm

    Determines whether a dumpcs file is valid
    All dumpcs files entered should be valid, but of course they must be checked.
    Note: This function only performs a short check on the file as a whole.
    On the other hand, the dumpcs_checkformat function analyzes the whole thing and is very picky .

    Arguments:
        dumpcs: the string of the dumpcs file

    Return:
        bool whether the dumpcs is valid
    """
    # return "// Image" in dumpcs and "// RVA: 0x" in dumpcs and "// Namespace:" in dumpcs\
    # and " TypeDefIndex: " in dumpcs
    raise NotImplementedError("Dumpcs_isvalid function needs improvement")
    if len(dumpcs) == 0:
        return False
    return True


def dumpcs_checkformat(dumpcs: str) -> list[str]:
    #Not done
    """
    Scan dump.cs for unexpected formatting
    Returns list of unexpected formatting errors

    Arguments:
        dumpcs: the string of the dumpcs file

    Return:
        List of errors with the line number and error
    """
    raise NotImplementedError("Dumpcs_checkformat function not completed")


def dumpcs_hasattributes(dumpcs: str) -> bool:
    #Not done
    """
    Bad detection, needs proper algorithm

    Determines whether a dumpcs file has attributes

    Arguments:
        dumpcs: the string of the dumpcs file

    Return:
        bool whether the dumpcs has attributes
    """
    raise NotImplementedError("Dumpcs_hasattributes function not completed")
    #return "[CompilerGeneratedAttribute]" in dumpcs


def dumpcs_constructor(path: str, attributeswarning=False) -> str:
    #Done, but needs improvement
    """
    Possible Improvements:
        1. No need to warn about attributes as they should be removed automatically.
        However, I want to keep this code commented out and not delete it in case I
        change my mind later.
        2. Setting dumpcs variable after removing attributes makes code more readable and concise,
        but is less inefficient than directing passing result of dumpcs_removeattributes.
        In addition, attributes must be removed *before* dumpcs is checked for format errors
        3. Does try except clause make a difference? IDK whether to keep it.

    Loads and initializes a dumpcs file

    Arguments:
        path: the file path of the dumpcs file

    Returns:
        string containing the contents of the dump.cs file
    """
    #Does this try except clause make a difference? IDK whether to keep it
    #try:
        #dumpcs = filehandler.read_file(path)
        #raise NotImplementedError("filehandler.read_file function does not exist")
    #except Exception as exception:
        #raise exception
    # dumpcs = filehandler.read_file(path)
    raise NotImplementedError("filehandler.read_file function does not exist")
    if not(dumpcs_isvalid(dumpcs)):
        #raise exceptions.errors.invaliddumpcs(path)
        raise NotImplementedError("exceptions.errors.invaliddumpcs exception does not exist")
    #No need to warn about attributes as they should be removed automatically
    #if attributeswarning and dumpcs_hasattributes(dumpcs):
        #exceptions.warnings.dumpcsattributeswarning(path)
    if dumpcs_hasattributes(dumpcs):
        dumpcs = dumpcs_removeattributes(dumpcs)
    formaterrors = dumpcs_checkformat(dumpcs)
    if formaterrors != []:
        #exceptions.warnings.unexpecteddumpcsformat(path,formaterrors)
        raise NotImplementedError("exceptions.warnings.unexpecteddumpcsformat function does not exist")
    return dumpcs


def dumpcs_removeattributes(dumpcs: str) -> str:
    #Not done
    """
    Possible Improvements:
        1. Creating a new list of lines is inefficient, modifying existing list would be ideal
        2. Directly using getlines() instead of using lines variable may be faster, but sacrifices readability

    Removes attributes from a dumpcs file
    Does not process attributes, only removes them
    Does not remove blank lines yet

    Arguments:
        dumpcs: the string of the dumpcs file

    Returns:
        string containing dumpcs contents with attributes removed
   """
    lines = getlines(dumpcs, False, False)
    newlines = []
    for line in lines:
        #Trim leading whitespace from line
        trimmedline = trim(line, True, False)
        # If the first non-whitespace character on the line is a square bracket,
        # this means the line is an attribute
        if trimmedline[0] != "[":
            #The line is not an attribute, so keep it
            newlines.append(line)
    return linestostring(newlines)


def dumpcs_getobjects(dumpcs: str, objecttypes=None) -> dict:
    #Not Done
    """
    Instead of getfullobjects, go straight to this function!
    Does not remove blank lines yet

    objecttypes: if not object type in object types, ignore object
    """
    if objecttypes is None:
        #Set default here to avoid mutable default argument
        objecttypes = ["class", "struct", "enum", "interface"]
