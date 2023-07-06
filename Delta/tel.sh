window=25
dump_dir=dumps
for kel in T Te_Howes Te_Kawazura_18 Te_Kawazura_22 Te_Werner Te_Sharma Te_Rowan
do
    vmin=5e-05
    vmax=0.8
    echo  "pyharm-movie -o frames_w$window --fig_x 6 --fig_y 6 --size $window --vmin $vmin --vmax $vmax log_"$kel"_poloidal ./$dump_dir"
    pyharm-movie -o frames_w$window --fig_x 6 --fig_y 6 --size $window --vmin $vmin --vmax $vmax log_"$kel"_poloidal ./$dump_dir
done
