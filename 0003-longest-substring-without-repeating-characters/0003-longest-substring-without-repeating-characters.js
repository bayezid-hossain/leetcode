var lengthOfLongestSubstring = function (s) {
    let set=new Set(); //initialize a set as i'm about to solve it with sliding window algorithm
    let left=0,right=0,max=0; //initialize all values with 0

    while(right<s.length){ //as per sliding window algorithm the loop will run till sliding through all the way to last element, as there is no constraints like 2 or 3 elements at a time i am going one element at a time to slide
        if(set.has(s[right])){  //if the set hast the current element then we delete the last duplicate element from the set and increase the index of last element
            set.delete(s[left])
            left++
        }
        else{   //else we add the current element to the set and slide to the next element
            set.add(s[right])
            right++
        }
        max=max>set.size?max:set.size //just determining the max value between current max value and set size
    }
    return max;
};