<?php
include_once('simple_html_dom.php');
function check($title)
{
    exec("/usr/bin/python /home/chinmay/Documents/dump/predict.py \"$title\"",$out);
    return $out[0];
}




for ($x = 1; $x <=30; $x++)
{

$y=$x+86;

ob_start();

$html = file_get_html('https://timesofindia.indiatimes.com/2017/6/'.$x.'/archivelist/year-2017,month-6,starttime-428'.$y.'.cms');
echo "[";
$z=0;
foreach($html->find('td[width=49%]') as $e)
{
	$e->innertext . '<br>';
	foreach($e->find('a') as $f) 
	{
		if($z==1){echo ",";}
		elseif ($z==0){$z=1;}
		echo "\n{\"title\":\"";
		$g=$f->innertext;
		$h=str_replace("\"", "'",$g);
		echo $h."\",\"url\":\"https://timesofindia.indiatimes.com";
		echo $f->href."\"}";
	}
}
echo ']';
$htmlStr = ob_get_contents();
ob_end_clean(); 
file_put_contents('acc.json', $htmlStr);

$z=0;
$u=file_get_contents('acc.json');
$json = json_decode($u, true);
$handle = fopen('final.json', 'a');
$data="[";
for ($i = 0; $i < count($json); $i++)
{
	$title=$json[$i]["title"];
	$r=check($title);
	if($r==1)
	{
		if($z==1){$data = $data.",";}
		elseif ($z==0){$z=1;}
		$data=$data."\"";
		$data=$data.$json[$i]["url"];
		$data=$data."\"\n";
	}
} 
$data = $data."],";;
fwrite($handle, $data);
fclose($handle);
}

?>
