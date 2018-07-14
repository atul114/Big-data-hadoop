<?php



print '<head>';
  print '<title>List of services provided : </title>';
  print '<meta charset="utf-8">';
  print '<meta name="viewport" content="width=device-width, initial-scale=1">';
  print '<link rel="stylesheet" href="/static/c1.css">';
  print '<script src="/static/j2.js"></script>';
  print '<script src="/static/j3.js"></script>';
print '</head>';
print '<style type="text/css">';
print 'body{
background-color: #b0e0e6;
padding 20px;
}';
print '</style>';
print '<body>';
print '<div class="container">';
print '<h2>YOUR OPTIONS ARE:-</h2>';
print '<p>Choose the desired</p>';
$a1=$_GET['usrname'];
#echo $a1;
$a2=$_GET['comment'];
#echo $a2;
#echo $a2.$a;
$myfile = fopen("/var/www/cgi-bin/nameip", "r");
$a3=fgets($myfile);
fclose($myfile);
#echo $a3;
$myfile1 = fopen("/var/www/cgi-bin/command", "w");
fwrite($myfile1,$a2);
fclose($myfile1);
#$q=exec(" sudo hive -e  '".$a2."'");
#echo $q;
#$c=" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@".$a3." echo  |  hive -e '".$a2."'";
$c="sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@".$a3." hive -f /var/www/cgi-bin/command";
#echo $c;
echo "<pre>";
$output = shell_exec($c);
echo $output;
#$output = shell_exec("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +$a3+' hive -e '+$a2);
#echo "<pre>";
#echo "$output";
echo "</pre>";

print '<form method="post" action="/cgi-bin/hivequerystart.py">';
print '<label><input type="submit" value="Click to go back"></label>';
print '</form>';
print '</body>';

?>
