set terminal png
plot "water1" w l
plot [:9] exp(x) [Enter]
set output "data.png"
replot