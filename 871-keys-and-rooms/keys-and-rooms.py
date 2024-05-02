class Solution(object):
    def canVisitAllRooms(self, rooms):
        room_list = [False]*len(rooms)
        key_stack = [0]
        while len(key_stack)>0:
            current = key_stack.pop()
            if not room_list[current]:
                room_list[current] = True
                for key in rooms[current]:
                    if not room_list[key]:
                        key_stack.append(key)
                        
        if False in room_list:
            return False
        else:
            return True
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """