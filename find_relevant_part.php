<?php
include_once('../simple_html_dom.php');

// get DOM from URL or file
$html = file_get_html('https://timesofindia.indiatimes.com/2018/5/25/archivelist/year-2018,month-5,starttime-43245.cms');

ob_start();
	
foreach($html->find('td[width=49%]') as $e)
{
	$e->innertext . '<br>';
	foreach($e->find('a') as $f) 
	{
		echo $f->href . '<br>';		
	}
}
$htmlStr = ob_get_contents();

ob_end_clean(); 

file_put_contents('result.html', $htmlStr);


?>