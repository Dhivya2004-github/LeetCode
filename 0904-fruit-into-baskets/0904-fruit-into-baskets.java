class Solution {
    public int totalFruit(int[] fruits) {
        int maxsum=0;
        int left,right=0;
        int n=fruits.length;
        
        HashMap<Integer,Integer>basket=new HashMap<>();
        for(left=right=0;right<n;right++){
            int key=fruits[right];
            basket.put(
                key,
                basket.getOrDefault(key,0)+1
            );
            
            while(basket.size()>2){
                int lkey =fruits[left];
                basket.put(
                    lkey,
                    basket.get(lkey)-1);
            
                if (basket.get(lkey)==0){
                  basket.remove(lkey);
              }
                left++;
            }



        
            maxsum=Math.max(maxsum,right-left+1);}
        return maxsum;
        
    }
}