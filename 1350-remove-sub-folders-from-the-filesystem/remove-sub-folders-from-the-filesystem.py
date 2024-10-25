class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        sorted_folders=(sorted(folder))
        ans=[sorted_folders[0]]
        for i in range(1, len(sorted_folders)):
            last_added=ans[-1] + "/"
            if not sorted_folders[i].startswith(last_added):
                ans.append(sorted_folders[i])
        return ans