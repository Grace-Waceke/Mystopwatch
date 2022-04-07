import time
Start:input("Press Enter To Start The Timer")
print("The Timer Has Started . . .")
begin=time.time()
endtimer=input("Press Enter To Stop The Timer")
end=time.time()
elapsed=end-begin
elapsed=int(elapsed)
print("The Time Elapsed Is . . .",elapsed,"seconds")


