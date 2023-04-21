class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        sum=0
        sum+=ord(coordinates[0])-96
        sum+=int(coordinates[1])
        if sum%2==1:
            return True
        return False