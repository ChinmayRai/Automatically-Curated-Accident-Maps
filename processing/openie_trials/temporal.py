import jpype 
jvmPath = jpype.getDefaultJVMPath() 
classpath='/home/chinmay/Documents/SURA/processing/openie_trials'
jpype.startJVM(jvmPath,'-Djava.class.path=%s' % classpath)

#startJVM("C:/Program Files/Java/jre6/bin/client/jvm.dll", "-ea")
"""
public class temporal
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);  
		String s=sc.nextLine();
		time_detect t = new time_detect();
		System.out.println(t.extract(s));
	}
}

Time_detect=autoclass('time_detect')
td=Time_detect()
s=td.extract("on 22th july at 2.00 p.m.")
print (s)
"""
td=time.time_detect
s=jpype.td.extract('on 22th july at 2.00 p.m.') 
print s
jpype.shutdownJVM() 	