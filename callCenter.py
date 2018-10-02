import ccUtil

count = None
queue = []
ringQueue = []
ongoingCall = []
   
ccUtil.callCenter.__init__();

A = ccUtil.operator("A");
B = ccUtil.operator("B");

# infinity looping
while True:
    ccUtil.cls()

    # Temporary area for debugging
    print("\n------ Debug Area ------")
    print("QUEUE:  ",queue)
    print("RINGING:",ringQueue)
    print("ONGOING:",ongoingCall)
    print("------------------------")

    # main menu
    print("\nCALL CENTER VULCANET")
    print("\n   [1] - CALL")
    print("   [2] - SHOW QUEUE")
    print("   [3] - ANSWER A")
    print("   [4] - ANSWER B")
    print("   [5] - REJECT A")
    print("   [6] - REJECT B")
    print("   [7] - HANGUP A")
    print("   [8] - HANGUP B")
    answer = input("\nChoose an option: ")

    if answer == "1":
        ccUtil.callCenter.call(A, B, ringQueue, queue)
            
    elif answer == "2":
        ccUtil.callCenter.showQueue(queue)            
        
    elif answer == "3":
        ccUtil.callCenter.answerA(A, ringQueue, queue, ongoingCall)

    elif answer == "4":
         ccUtil.callCenter.answerB(B, ringQueue, queue, ongoingCall)

    elif answer == "5":
        ccUtil.callCenter.rejectA(A, B, ringQueue)
        
    elif answer == "6":
        ccUtil.callCenter.rejectB(A, B, ringQueue)

    elif answer == "7":
        ccUtil.callCenter.hangupA(A, B,ongoingCall, ringQueue)

    elif answer == "8":
        ccUtil.callCenter.hangupB(A, B,ongoingCall, ringQueue)


