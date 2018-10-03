# Python 3.7 - Simulated Call Center
#
# Created by Pedro P Pimentel
#
# VulcaNet Challenge
#
# GOALS
#
# Implement a simulated telephony application using Python
# Different implementations with different complexities are proposed to achieve the goal.
# Whichever implementation type is chosen, the same set of prerequisites apply.
# There are also some bonus points that may be implemented if desired and time allows
#
# ALGORITHM
#
# class callCenter:
#  function init:
#   initialize callCenter
#
#  function call:
#   receives a call and print to stdout
#   verify A status
#   if "available" print message and set status to "ringing"
#   add call on ringing queue
#
#  function show:
#   show queue
#   verify if queue is empty
#   if not empty then print queue
#
#  function answer:
#   answer call and print to stdout
#   verify if A status is "ringing", if true set status to "answering"
#   print message
#   add ringing call to ongoing call
#   remove from ringing call
#
#  function reject:
#   reject call and print to stdout
#   verify if ringing queue is not empty
#   print message
#   set A status to "available"
#   remove ring queue
#   check status, if there is some call ringing will be asign to an available operator
#
#  function hangup:
#   hangup call and print to stdout
#   verify if ongoing call is not empty
#   print message
#   remove from ongoing call
#   set A status to "available"
#   check status, if there is some call ringing will be asign to an available operator
#
# class operator:
#  function init
#   initialize operator
#
# When callCenter receives a call this call is asign to an operator with status "available"
# then status change to "ringing"
# 
# the operator with "ringing" status can "answer" one call each time 

import ccUtil

count = None
queue = []
ringQueue = [0, 0]
ongoingCall = [0, 0]
   
ccUtil.callCenter.__init__()

A = ccUtil.operator("A")
B = ccUtil.operator("B")

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
    print("   [9] - FREE QUEUE")
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
        ccUtil.callCenter.rejectA(A, B, ringQueue, queue)
        
    elif answer == "6":
        ccUtil.callCenter.rejectB(A, B, ringQueue, queue)

    elif answer == "7":
        ccUtil.callCenter.hangupA(A, B,ongoingCall, ringQueue, queue)

    elif answer == "8":
        ccUtil.callCenter.hangupB(A, B,ongoingCall, ringQueue, queue)

    elif answer == "9":
        ccUtil.callCenter.freeQueue(queue)
