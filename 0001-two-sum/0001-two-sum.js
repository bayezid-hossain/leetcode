var twoSum = function(nums, target) {
    let hashmap=new Map()
    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i]
       if (hashmap.has(diff)) {
            return [i, hashmap.get(diff)]
        }
        hashmap.set(nums[i],i)
    }
};