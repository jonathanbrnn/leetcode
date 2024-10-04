class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) < 2:
            return -1

        skill.sort()
        res = skill[0] * skill[-1]
        skill_goal = skill[0] + skill[-1]

        l, r = 1, len(skill) - 2

        while l < r:
            if skill_goal != skill[l] + skill[r]:
                return -1
            else:
                res += skill[l] * skill[r]
            l += 1
            r -= 1

        return res
