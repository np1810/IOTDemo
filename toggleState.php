<?php
$res = "fail";
if(sha1($_POST["code"])=="44d16cbe12265f91d76bad742da61ab7194c0e5a")
{
	$fr = fopen("state.txt", "r");
	$state = fread($fr,filesize("state.txt"));
	fclose($fr);
	if($state=="on")
	{
		$state = "off";
		$res = "off";
	} else {
		$state = "on";
		$res = "on";
	}
	$fw = fopen("state.txt", "w");
	fwrite($fw, $state);
	fclose($fw);
}
echo $res;
?>

