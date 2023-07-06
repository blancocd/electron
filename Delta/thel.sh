window=25
dump_dir=dumps
for kel in Thetae_Howes Thetae_Kawazura_18 Thetae_Kawazura_22 Thetae_Werner Thetae_Sharma Thetae_Rowan
do
    vmin=5e-01
    vmax=1400
    echo  "pyharm-movie -o frames_w$window --fig_x 6 --fig_y 6 --size $window --vmin $vmin --vmax $vmax log_"$kel"_poloidal ./$dump_dir"
    pyharm-movie -o frames_w$window --fig_x 6 --fig_y 6 --size $window --vmin $vmin --vmax $vmax log_"$kel"_poloidal ./$dump_dir
done
