class ListNode:
    def __init__(self, val: str, next: None, prev: None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentPage = ListNode(homepage, None, None)

    def visit(self, url: str) -> None:
        self.currentPage.next = ListNode(url, None, self.currentPage)
        self.currentPage = self.currentPage.next


    def back(self, steps: int) -> str:
        while steps > 0 and self.currentPage.prev:
            self.currentPage = self.currentPage.prev
            steps -= 1

        return self.currentPage.val


    def forward(self, steps: int) -> str:
        while steps > 0 and self.currentPage.next:
            self.currentPage = self.currentPage.next
            steps -= 1

        return self.currentPage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
