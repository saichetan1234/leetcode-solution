class Solution:
    def trafficSignal(self, timer: int) -> str:

        if timer ==0:
            return "Green"
      
        if timer  == 30:
            return "Orange"

        if 30 < timer <=90:
            return "Red"

        if 0<timer<=30 or timer >90:
            return "Invalid"
