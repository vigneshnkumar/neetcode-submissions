class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = set()

        for pointer in nums:
            if pointer in holder:
                return True
            else:
                holder.add(pointer)
            
        return False