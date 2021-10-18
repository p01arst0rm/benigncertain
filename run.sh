for i in {1..30}; do
    sudo python benign.py -n 20480 -o outfile -i intest 154.65.33.116
    echo "***RESPONSE***" && hexdump -C outfile
    echo "***REQUEST***" &&hexdump -C intest
done