def cls(): print ("\n" * 50)

# verify if list ongoingCall is empty
def isEmptyOngoing(ongoingCall):
    if len(ongoingCall) == 0:
        return 1
    else: return 0

# verify if list queue is empty
def isEmptyQueue(queue):
    if len(queue) == 0:
        return 1
    else: return 0

# verify if list ringQueue is empty
def isEmptyRingQueue(ringQueue):
    if len(ringQueue) == 0:
        return 1
    else: return 0    

# check if status is available, if true and there is a call on queue, then status become ringing and a new call is asigned to operator
def checkStatus(A, B, ringQueue):
    if A.status == "available":
        if not (isEmptyRingQueue(ringQueue)) and (ringQueue[0] != 0):
            print("Call", ringQueue[0], "is ringing for operator A")
            A.status = "ringing"
            input("\nPress Enter to continue...")
            return 1

    elif B.status == "available":
        if not (isEmptyRingQueue(ringQueue)) and (ringQueue[1] != 0):
            print("Call", ringQueue[1], "is ringing for operator B")
            B.status = "ringing"
            input("\nPress Enter to continue...")
            return 1              
    else:
        print(ringQueue)
        print("Empty queue")
        return 0

#
# main class
# has all the functionalities of call center
# function available: call, showQueue, answerA, answerB, rejectA, rejectB, hangupA, hangupB
#
# there is a class called operator, responsible for initialize the A and B operators
# this class operator set name and status to available
#
class callCenter():
    def __init__():
       global count
       count = 0
       return count
       
    def call(A, B, ringQueue, queue):
        global count
        count += 1
        print("\nCall", count, "received")

        if A.status == "available":
            print("Call", count,"ringing for operator A")
            A.status = "ringing"
            ringQueue[0] = count
            input("\nPress Enter to continue...")
            cls()
        elif B.status == "available":
            print("Call", count, "ringing for operator B")
            B.status = "ringing"
            ringQueue[1] = count
            input("\nPress Enter to continue...")
            cls()
        else:
            print("Call", count, "waiting in queue")
            input("\nPress Enter to continue...")
            cls()
            queue.append(count)        

    # Show queue 
    def showQueue(queue):
        if not isEmptyQueue(queue):
        
            for i in range(len(queue)):
                print("Call", queue[i], "on queue")
            input("\nPress Enter to continue...")
            cls()
        else:
            print("Empty queue")
            input("\nPress Enter to continue...")   

    # function to answer a call ringing on operator A     
    def answerA(A, ringQueue, queue, ongoingCall):
        if A.status == "ringing":
            A.status = "answering"
            print("Call", ringQueue[0], "answered by operator A")
            ongoingCall[0] = ringQueue[0]
            ringQueue[0] = 0
            
            if not isEmptyQueue(queue):
                ringQueue[0] = queue[0]
                queue.pop(0)
                
            input("\nPress Enter to continue...")
            cls()
        else:
            print("Your phone is not ringing")
            input("\nPress Enter to continue...")

    # function to answer a call ringing on operator B
    def answerB(B, ringQueue, queue, ongoingCall):
        if B.status == "ringing":
            if len(ringQueue) == 2:
                B.status = "answering"
                print("Call", ringQueue[1], "answered by operator B")
                ongoingCall[1] = ringQueue[1]
                ringQueue[1] = 0              
            
            if not isEmptyQueue(queue):
                ringQueue[1] = queue[0]
                queue.pop(0)
                
            input("\nPress Enter to continue...")
            cls()
        else:
            print("Your phone is not ringing")
            input("\nPress Enter to continue...")           

    # function to reject a call on operator A
    def rejectA(A, B, ringQueue):
        if not isEmptyRingQueue(ringQueue):
            print("Call", ringQueue[0], "rejected by operator A")
            input("\nPress Enter to continue...")
            A.status = "available"
            ringQueue[0] = 0
            checkStatus(A, B, ringQueue)
        else:
            print("You don't have any call")
            input("\nPress Enter to continue...")

    # function to reject a call on operator B
    def rejectB(A, B, ringQueue):
        if not isEmptyRingQueue(ringQueue):
            print("Call", ringQueue[0], "rejected by operator B")
            input("\nPress Enter to continue...")
            B.status = "available"
            ringQueue[0] = 0
            checkStatus(A, B, ringQueue)
        else:
            print("You don't have any call")
            input("\nPress Enter to continue...")

    #function to hangup a call on operator A
    def hangupA(A, B,ongoingCall, ringQueue):
        if not (isEmptyOngoing(ongoingCall)) and (ongoingCall[0] != 0):
            print("Call", ongoingCall[0], "finished and operator A available")
            input("\nPress Enter to continue...")
            ongoingCall[0] = 0 
            A.status = "available"
            checkStatus(A, B, ringQueue)
        else:
            print("You don't have any ongoing call")
            input("\nPress Enter to continue...")

    #function to hangup a call on operator B
    def hangupB(A, B,ongoingCall, ringQueue):
        if not (isEmptyOngoing(ongoingCall)) and (ongoingCall[1] != 0):
            print("Call", ongoingCall[1], "finished and operator B available")
            input("\nPress Enter to continue...")
            ongoingCall[1] = 0
            B.status = "available"
            checkStatus(A, B, ringQueue)           
        else:
            print("You don't have any ongoing call")
            input("\nPress Enter to continue...")   

class operator():
    def __init__(self, name, status = "available"):
        self.name = name
        self.status = status
