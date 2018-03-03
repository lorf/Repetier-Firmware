#!/usr/bin/perl
#
# for i in 470 1000 2200 4700 10000; do v=$(echo "(4096*$i)/(4700+$i)" | bc); min=$(echo "$v*9/10" | bc); max=$(echo "$v*11/10" | bc); echo "$i: $v, $min - $max"; done
#

$r1 = 4700;
@r2 = qw(470 1000 2200 4700 10000);

sub min {
    $_[0] < $_[1] ? $_[0] : $_[1];
}

for $r2 (@r2) {
    $adc = (4096*$r2)/($r1+$r2);
    $min = $adc * (10 - &min(2,$r1/$r2))/10;
    $max = $adc * (10 + &min(2,$r1/$r2))/10;
    print "$r2: $adc, $min - $max\n";
}
