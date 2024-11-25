#include <string>

class HistoryNode {
public:
    std::string val;
    HistoryNode* next;
    HistoryNode* prev;

    HistoryNode(const std::string& value, HistoryNode* nextNode = nullptr, HistoryNode* prevNode = nullptr)
        : val(value), next(nextNode), prev(prevNode) {}
};


class BrowserHistory {
    HistoryNode* currentPage;
public:
    BrowserHistory(string homepage) {
        currentPage = new HistoryNode(homepage, nullptr, nullptr);
    }
    
    void visit(string url) {
        currentPage->next = new HistoryNode(url, nullptr, currentPage);
        currentPage = currentPage->next; 
    }
    
    string back(int steps) {
        while (steps-- > 0 && currentPage->prev != nullptr)
        {
            currentPage = currentPage->prev;
        } 

        return currentPage->val;
    }
    
    string forward(int steps) {
        while (steps-- > 0 && currentPage->next != nullptr)
        {
            currentPage = currentPage->next; 
        }

        return currentPage->val;
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */
