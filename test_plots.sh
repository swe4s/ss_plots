test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

function tear_down
{
    rm -f rand_1_col.txt \
        rand_2_col.txt \
        rand_3_col.txt \
        rand_10_x_10.txt \
        rand_1_col_1000.txt
}

#run test_for_success python -c "print 'zzz: example success'"
#assert_in_stdout "zzz"

(for i in `seq 0 9`; do echo $RANDOM; done) > rand_1_col.txt
rm -f s_just_y.png
run test_just__y python scatter.py --in_file rand_1_col.txt --out_file s_just_y.png --x_label 'Non rand' --y_label 'Rand'
assert_no_stdout
assert_no_stderr
assert_exit_code 0
assert_equal s_just_y.png $( ls s_just_y.png )

rm -f s_x_and_y.png
(for i in `seq 0 9`; do echo $RANDOM $RANDOM; done) > rand_2_col.txt
run test_x_and_y python scatter.py --in_file rand_2_col.txt --out_file s_x_and_y.png --x_label 'Rand' --y_label 'Rand'
assert_no_stdout
assert_no_stderr
assert_exit_code 0
assert_equal s_x_and_y.png $( ls s_x_and_y.png )

rm -f s_x_y_and_name.png
letters=({A..Z})
(for i in `seq 0 9`; do 
    echo ${letters[$i]} $RANDOM $RANDOM;
done) > rand_3_col.txt
run test_x_y_and_named python scatter.py --in_file rand_3_col.txt --out_file s_x_y_and_name.png --x_label 'Rand' --y_label 'Rand'
assert_no_stdout
assert_no_stderr
assert_exit_code 0
assert_equal s_x_y_and_name.png $( ls s_x_y_and_name.png )

rm -f b_rand.png
letters=({A..Z})
(for i in `seq 0 9`; do 
    echo -n ${letters[$i]} 
    for j in `seq 0 9`; do 
        echo -n " $RANDOM"
    done
    echo
done) > rand_10_x_10.txt
run test_boxplot python box.py --in_file rand_10_x_10.txt --out_file b_rand.png --x_label 'Rand' --y_label 'Rand'
assert_no_stdout
assert_no_stderr
assert_exit_code 0
assert_equal b_rand.png $( ls b_rand.png )


rm -f h_rand.png
(for i in `seq 0 999`; do echo $RANDOM; done) > rand_1_col_1000.txt
run test_histogram python histogram.py --in_file rand_1_col_1000.txt --out_file h_rand.png --x_label 'Rand' --y_label 'Freq'
assert_no_stdout
assert_no_stderr
assert_exit_code 0
assert_equal h_rand.png $( ls h_rand.png )


