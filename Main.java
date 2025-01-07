public class Main 
{
    public static void main(String[] args) 
    {
        int [][] matt = {{5,4,3},{2,3,4},{9,2,6}};
        int c = matt.length;
        int r = matt.length;
        for(int i=0;i<r;i++)
        {

            for(int j=0;j<c;j++)
            {
                System.out.println(matt[j][0]);
            }
        }
    }
}
