import java.util.regex.*;  
import java.util.*;

enum Day{	unspecified,monday,tuesday,wednesday,thursday,friday,saturday,sunday;	}
enum TimePeriod{	none,early_morning,late_night,noon;   }
class date_time
{
	public int hrs,min;	public boolean am; public TimePeriod period; public int date; public int month; public Day day;
	public date_time(){}
}

public class reg
{
	public static void main(String[] args) {

		int yyyy = 2018;	int mm = 7;		int dd = 9; //set date of reporting.
		Calendar cal = Calendar.getInstance();cal.set(Calendar.DAY_OF_MONTH,dd);
		cal.set(Calendar.MONTH,mm-1);cal.set(Calendar.YEAR,yyyy);
		//System.out.println(getDay(cal.get(Calendar.DAY_OF_WEEK))); //prints day of reporting
		//System.out.println(getInt(Day.monday));

		Scanner sc=new Scanner(System.in);  
		String s=sc.nextLine();
		date_time a=new date_time();

		String day_of_week="([Mm]on(day)?|[Tt]ue(sday)?|[Ww]ed(nesday)?|[Tt]hu(rsday)?|[Ff]ri(day)?|[Ss]at(urday)?|[Ss]un(day)?)";
		String num_time="([\\d]{1,2}[[\\.:][\\d]{2}]*[\\s]{0,1}[ap][\\.]{0,1}[m][\\.]{0,1})";
		String late="("+day_of_week+" midnight|late on "+day_of_week+"( night){0,1}|"+day_of_week+" night)";
		String early="((wee|early) hours of "+day_of_week+"|((early|wee) on ){0,1}"+day_of_week+" morning|(early|wee) on "+day_of_week+")";
		String noon="("+day_of_week+" (after)?noon)";

		
		String month="([Jj]an(?:uary)?|[Ff]eb(?:ruary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]un(?:e)?|[Jj]ul(?:y)?|[Aa]ug(?:ust)?|[Ss]ept(?:ember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?)";
		String date="([\\d]{1,2}th|[\\d]{1,2}nd|[\\d]{1,2}st|[\\d]{1,2}rd|[\\d]{1,2})";
		String month_date=month+"[\\s]{0,1}"+date;
		String date_month=date+"[\\s]{0,1}"+month;


		Matcher m = Pattern.compile(num_time).matcher(s);
		while(m.find())
		{
			String numeral_time=s.substring(m.start(),m.end());String am_pm;String num;
			Matcher m1 = Pattern.compile("([\\d]{1,2}[\\.:][\\d]{2})").matcher(numeral_time);
			if(m1.find())//numeral time has minutes
			{
				num=numeral_time.substring(m1.start(),m1.end());
				am_pm=numeral_time.substring(m1.end(),numeral_time.length()-1);
				if(num.contains(".")){String[] data=num.split(".");a.hrs=Integer.valueOf(data[0]);a.min=Integer.valueOf(data[1]);}
				else if(num.contains(":")){String[] data=num.split(":");a.hrs=Integer.valueOf(data[0]);a.min=Integer.valueOf(data[1]);}
			}
			else
			{
				Matcher m2 = Pattern.compile("([\\d]{1,2})").matcher(numeral_time);m2.find();
				am_pm=numeral_time.substring(m2.end(),numeral_time.length()-1);
				a.hrs=Integer.valueOf(numeral_time.substring(m2.start(),m2.end()));a.min=0;
			}
			if(am_pm.contains("a"))a.am=true;else a.am=false;
		} 

		if(Pattern.compile(late).matcher(s).find()){a.period=TimePeriod.late_night;}
		else if(Pattern.compile(noon).matcher(s).find())a.period=TimePeriod.noon;
		else if(Pattern.compile(early).matcher(s).find()){a.period=TimePeriod.early_morning;}
		else a.period=TimePeriod.none;
		
		Matcher m3= Pattern.compile(day_of_week).matcher(s);
		if(m3.find())
		{
			String dAY=s.substring(m3.start(),m3.end());a.day=find(dAY);
		}

		Matcher m4=Pattern.compile(month_date).matcher(s);Matcher m5=Pattern.compile(date_month).matcher(s);
		if(m4.find() || m5.find())
		{
			Matcher m6=Pattern.compile(month).matcher(s);m6.find();a.month=finder(m6.group(0));
			Matcher m7=Pattern.compile("([\\d]{1,2})").matcher(s);m7.find();a.date=Integer.valueOf(m7.group(0));	
		}
		
		print(a);
	}

	public static int finder(String s)
	{

		String g=s.substring(0,3).toLowerCase();
		System.out.println(g);
		if(Pattern.matches("jan",g)) return 1;else if(Pattern.matches("feb",g)) return 2;else if(Pattern.matches("mar",g)) return 3;
		else if(Pattern.matches("apr",g)) return 4;else if(Pattern.matches("may",g)) return 5;else if(Pattern.matches("jun",g)) return 6;
		else if(Pattern.matches("jul",g)) return 7;else if(Pattern.matches("aug",g)) return 8;else if(Pattern.matches("sep",g)) return 9;
		else if(Pattern.matches("oct",g)) return 10;else if(Pattern.matches("nov",g)) return 11;else if(Pattern.matches("dec",g)) return 12;
		else return 0;
	}

	public static Day find(String s)
	{
		if(Pattern.matches("[Mm]on(day)?",s))return Day.monday;else if(Pattern.matches("[Tt]ue(sday)?",s))return Day.tuesday;
		else if(Pattern.matches("[Ww]ed(nesday)?",s))return Day.wednesday;else if(Pattern.matches("[Tt]hu(rsday)?",s))return Day.thursday;
		else if(Pattern.matches("[Ff]ri(day)?",s))return Day.friday;else if(Pattern.matches("[Ss]at(urday)?",s))return Day.saturday;
		else if(Pattern.matches("[Ss]un(day)?",s))return Day.sunday;
		else return Day.unspecified;
	}

	public static Day getDay(int n)
	{
		switch(n)
		{
			case 1: return Day.sunday;case 2: return Day.monday;case 3: return Day.tuesday;case 4: return Day.wednesday;
			case 5: return Day.thursday;case 6: return Day.friday;case 7: return Day.saturday;default: return Day.unspecified;
		}
	}
	public static int getInt(Day d)
	{
		switch(d)
		{
			case sunday: return 1;case monday: return 2;case tuesday: return 3;case wednesday: return 4;
			case thursday: return 5;case friday: return 6;case saturday: return 7;default: return 0;	
		}
	}

	public static void print(date_time a)
	{
		if(a.hrs+a.min!=0)
		{
			System.out.print(a.hrs);if(a.min!=0){System.out.print(":");System.out.print(a.min);}
			if(a.am)System.out.println(" am");else System.out.println(" pm");
		}
		if(a.period!=TimePeriod.none)System.out.println(a.period);
		if(a.day!=null)System.out.println(a.day);
		System.out.print(a.date+"-"+a.month);
	}

	
}


/*

N(:NN)am/pm
N(:NN) am/pm
N(.NN)am/pm
N(.NN) am/pm


DAY midnight
late on DAY 
(late on)DAY night


wee hours of DAY
early hours of DAY
early on DAY
(early on)DAY morning

DAY afternoon*/