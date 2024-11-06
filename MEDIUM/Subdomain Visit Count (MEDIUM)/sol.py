class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        output = []

        for domain in cpdomains:
            visits, curr_domain = map(str, domain.split())
            visits = int(visits)
            subdomains = curr_domain.split(".")
            constructed = subdomains[-1]
            dic[constructed] += visits

            for sub in subdomains[::-1][1:]:
                constructed = sub + "." + constructed
                dic[constructed] += visits

        for item, val in dic.items():
            output.append(str(val) + " " + item)

        return output
