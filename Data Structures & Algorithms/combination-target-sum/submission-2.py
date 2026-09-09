class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def aux(curr_sum,current_list,possible_values,target,start_value):
            if curr_sum > target:
                return

            if curr_sum == target:
                output.append(current_list)
                return

            for i in range(start_value,len(possible_values)):
                aux(curr_sum+possible_values[i],current_list + [possible_values[i]],possible_values,target, i)

        aux(0,[],nums,target,0)
        return output


        