window=25
dump_dir=dumps
for var in sigma_w
do
    vmin=1e-7
    vmax=90
    echo  "pyharm-movie -o frames_w$window --fig_x 6 --fig_y 6 --size $window --vmin $vmin --vmax $vmax log_"$var"_poloidal ./$dump_dir"
    pyharm-movie -o frames_w$window --fig_x 6 --fig_y 6 --size $window --vmin $vmin --vmax $vmax log_"$var"_poloidal ./$dump_dir
done

