class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        1.Find least common multiple of p and q
        2.Determine whether the side is on 2nd receptor side
        3.Determine the ray is on 0th or 1st receptor
        """
        lcm = math.lcm(p,q)
        n = lcm/q
        if(n%2==0):
            return 2
        elif((lcm/p)%2==1):
            return 1
        else:
            return 0
