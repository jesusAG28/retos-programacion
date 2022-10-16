<?php

for ($i = 1; $i <= 100; $i++) {
    $m3 = ($i % 3 == 0) ? true : false;
    $m5 = ($i % 5 == 0) ? true : false;
    if (!$m3 && !$m5)
        print_r($i . PHP_EOL);
    elseif ($m3 && $m5)
        print_r('fizzbuzz' . PHP_EOL);
    elseif ($m3)
        print_r('fizz' . PHP_EOL);
    elseif ($m5)
        print_r('buzz' . PHP_EOL);
}
