public int[] runningSum(int[] nums) {
    int[] runSum = new int[nums.length];
    for(int i = 0; i <nums.length; i++){
        if(i==0){
            runSum[i] = nums[i];
        }else{
            runSum[i] = nums[i]+runSum[i-1];
        }
    }
    return runSum;
}