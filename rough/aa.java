import java.util.*;

enum Day{	unspecified,monday,tuesday,wednesday,thursday,friday,saturday,sunday;	}
public class aa{
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		int dd=s.nextInt();
		int mm=s.nextInt();
		int yyyy=2017;
		Calendar cal = Calendar.getInstance();cal.set(Calendar.DAY_OF_MONTH,dd);
		cal.set(Calendar.MONTH,mm-1);cal.set(Calendar.YEAR,yyyy);
		
		System.out.println(getDay(cal.get(Calendar.DAY_OF_WEEK)));
		//cal.add(Calendar.DAY_OF_MONTH,-5);
		//System.out.println(getDay(cal.get(Calendar.DAY_OF_WEEK)));
		//System.out.println(cal.get(Calendar.DAY_OF_MONTH)+"-"+(cal.get(Calendar.MONTH)+1)+"-"+cal.get(Calendar.YEAR));

	}

	public static Day getDay(int n)
	{
		switch(n)
		{
			case 1: return Day.sunday;case 2: return Day.monday;case 3: return Day.tuesday;case 4: return Day.wednesday;
			case 5: return Day.thursday;case 6: return Day.friday;case 7: return Day.saturday;default: return Day.unspecified;
		}
	}
	
}
