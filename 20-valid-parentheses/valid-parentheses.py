class Solution(object):
    def isValid(self, s):
        paranthesis_stack = []

        for i in range(0,len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                paranthesis_stack.append(s[i])
            else:
                if not paranthesis_stack:
                    return False
                value_popped = paranthesis_stack.pop()
                if s[i] == ')' and value_popped != '(':
                    return False
                if s[i] == '}' and value_popped != '{':
                    return False 
                if s[i] == ']' and value_popped != '[':
                    return False

        if paranthesis_stack:
            return False
        return True
        """
        :type s: str
        :rtype: bool
        """