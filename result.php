<?php
header('Content-Type: application/x-www-form-urlencoded');
{
  $lat = $_POST['lat'];
  $lon = $_POST['lon'];
  $data['info'] = array();
  $data['info'][] = array(
    'lat' => $lat,
    'lon' => $lon);


  $jdata = json_encode($data);
  echo $jdata;
  $f = fopen('result.json', 'w+');
  fwrite($f, $jdata);
  fclose($f);
}
?>