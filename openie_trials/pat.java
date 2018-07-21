import java.util.regex.*;  
import java.util.*;

///////////////////////////////////REMOVE PREPOSITIONS FROM tokens
public class pat{
	public static void main(String[] args) {
		String t1="(?!on\b)([a-zA-Z0-9',[\\.][\\-][\\(\\)]]{1,15})";
		String tokens="[\\s]*"+t1+"([\\s]{1,2}"+t1+"){0,8}[\\s]*";
		Scanner sc=new Scanner(System.in);
		String p0="into("+tokens+"along)?"+tokens+"in"+tokens;	
		String p1="into"+tokens+"in"+tokens;
		String p2="into("+tokens+"near)?"+tokens+"(on|at)"+tokens;
		String p3="into"+tokens+"near"+tokens+"(in"+tokens+")?";
		String p4="reported from"+tokens+"in"+tokens;
		String p5="in"+tokens+"(on|at)"+tokens;
		String p6="in"+tokens+"at"+tokens;
		String p7="in front of"+tokens;
		String p8="in"+tokens+"(area )?(of"+tokens+"(district)?)?";//(on TIME)?   in ___________(area)?(of_________(district)?(on TIME)?)?
		String p9="in"+tokens+"in"+tokens+"(on"+tokens+")?";
		String p10="near"+tokens+"(on"+tokens+")? under"+tokens+"police station (area|jurisdiction)?";//( in"+tokens+")?";

		while(true)
		{
			String s=sc.nextLine();
			System.out.println(Pattern.matches(t1,s));
		}
		
	}
}