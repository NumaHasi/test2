set terminal png
plot "water1" w l
plot [:9] exp(x)
set output "data.png"
replot